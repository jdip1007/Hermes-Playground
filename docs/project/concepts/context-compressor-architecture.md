---
title: Context Compressor context compression architecture
created: 2026-04-08
updated: '2026-06-08'
type: concept
tags:
- agent-system
- agent-pattern
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Context Compressor — context compression architecture

## Overview

Context Compressor, located in `agent/context_compressor.py` (line 1699), is an **automatic context window compression** class [1]. When the conversation approaches model context limits, use an auxiliary LLM (cheap/fast model) for structured summarization of intermediate rounds while protecting head and tail context [1]. `ContextCompressor` The algorithm ontology is kept in this file [1].

**Layering Description**: The logic driving compression has been extracted from `run_agent.py` - `_compress_context` (`run_agent.py:3705`) is now just a forwarder, and the driver functions such as `compress_context`, `check_compression_model_feasibility`, `replay_compression_warning`, `try_shrink_image_parts_in_messages`, etc. have been extracted to `agent/conversation_compression.py` (line 556) [1]. `agent/context_compressor.py` still holds the `ContextCompressor` algorithm itself [1].

### Context Engine plug-in (2026-04-10)

Previously, there was only one way of context management - `ContextCompressor` (summary compression). If you want to change the strategy, you have to change the source code [1]. Now that `ContextEngine` ABC has been extracted, `ContextCompressor` has become an implementation of it. Third parties can write plug-ins to replace it without changing the Hermes source code [1].

**Essence: Change the decision "What to do when the context is almost full" from hard-coded to pluggable. **

```yaml
# config.yaml — 一行切换
context:
  engine: "compressor"   # 默认摘要压缩；设为插件名切换（如 "lcm"）
```

**Examples of possible alternative engines:**

| engine | Strategy | Applicable scenarios |
|------|------|---------|
| compressor (built-in) | LLM digest compression | General, default |
| lcm (assumed) | Store old conversations in a vector database for on-demand semantic retrieval | Very long sessions requiring precise recall |
| sliding-window (assumed) | Simple sliding window truncation, no summary | Low cost, no auxiliary model required |

**ContextEngine ABC requires the implementation of 3 core methods**:
- `name` — engine identification (property) [1]
- `should_compress(prompt_tokens)` — Whether compression is required [1]
- `compress(messages, current_tokens)` — performs compression and returns a list of new messages [1]

**Optional methods**: `on_session_start/end`, `get_tool_schemas` (the engine can expose tools to the agent, such as `lcm_grep`), `handle_tool_call`, `update_model` [1].

**Plug-in directory**: `plugins/context_engine/<name>/`, contains `plugin.yaml` + `__init__.py` (implement `register(ctx)` or expose `ContextEngine` subclass) [1].

**Only one engine is allowed to be active**, same as MemoryProvider's "at most one external" constraint [1].

Core idea: **Long conversations don’t need to throw away context – replace old rounds with structured summaries that retain key information. **

### Compression orchestration module (agent/conversation_compression.py)

The compressed orchestration logic has been extracted from `run_agent.py` to a separate module `agent/conversation_compression.py` [1]. This module is responsible for deciding when to trigger compression in the agent loop, calling `ContextCompressor`, handling compression aborts and cooldowns, and presenting warnings (such as `⚠ Compression aborted`) to the user [1].

## Architecture principles

### Compression algorithm

```text
算法流程（v3）:
  Phase 1: 廉价预处理（纯本地，不调 LLM，零 token 成本）
    ├── Pass 1: MD5 去重 — 同一文件读 5 次只留最新一份
    ├── Pass 2: Smart Collapse — 旧工具输出替换为信息化单行摘要
    └── Pass 3: tool_call 参数截断 — >500 字符截到 200
  Phase 2: 确定边界
    保护头部（系统提示 + protect_first_n 条非系统消息）+ 按 token 预算保护尾部
  Phase 3: LLM 结构化摘要（只处理 Phase 1 瘦身后的中间部分）
  Phase 4: 组装 + 清理孤立的 tool_call/tool_result 配对
```

#### Comparison of execution methods of old version (v2) vs new version (v3)

**The old version only has one step**: token reaches the threshold → hand the intermediate dialogue to LLM as it is for summary → replace. The problem is that the tool output is often several KB (`npm test` 200 lines, `read_file` reads the entire file), all of which are fed to LLM for summary. **The summary itself is very token**; the same file is read 5 times, and all 5 complete contents are there; when the compression effect is poor, it is triggered repeatedly, and LLM is adjusted to [1] every time.

**New version of three phases**: Phase 1 is a zero-cost local operation (string hashing, regular replacement, truncation), which can often cut off 30-50% of token [1]. The amount of data processed by Phase 3's LLM calls is therefore much smaller [1]. Coupled with the anti-shake mechanism (stop after 2 consecutive inefficiencies), the overall number of LLM calls and the amount of input per call are significantly reduced by [1].

### Evolution history

| improve | v1 | v2 | v3（2026-04-14+） |
|---|---|---|---|
| Summary template | No structure | Goal/Progress/Decisions/Files/Next Steps | **Numbered Completed Actions + Active State** (action-log style) |
| Summary update | Generate from scratch every time | iterative update | Iterative update (continue numbering) |
| tail protection | Fixed number of messages | Token budget (scaling) | Same as v2 |
| Tool output trim | none | Generic placeholder `_PRUNED_TOOL_PLACEHOLDER` | **Smart Collapse**: Generate informative one-line summaries by tool type |
| Remove duplicates | none | none | **MD5 deduplication**: Only the latest copy of the same tool result is retained |
| tool_call parameter | Leave it as is | Leave it as is | **>500 characters automatically truncated to 200 characters** |
| summary budget | fixed | Scale to compressed content | Same as v2, but `max_tokens` is reduced from 2× to **1.3×** (anti-expansion) |
| Anti-bounce | none | none | **Compression <10% for 2 consecutive times→skip** to avoid jitter loops |
| multimodal messaging | May crash | May crash | Skip list content on dedup/prune path |
| Compression note idempotent | Only first compressed append | Same as v1 | **Detect if it already exists** and do not add it again. |
| Failure cooldown | 10 minutes fixed | 10 minutes fixed | **10 minutes without provider, 60 seconds with transient errors** |
| Tool call integrity | may be lost | _sanitize_tool_pairs repair orphan pairs | Same as v2 |

## core components

### 1. Token budget management

```python
class ContextCompressor:
    def __init__(
        self,
        model,
        threshold_percent=0.50,
        protect_first_n=3,        # 头部保护：见下文
        protect_last_n=20,
        summary_target_ratio=0.20,
        ...
    ):
        self.protect_first_n = protect_first_n
        self.context_length = get_model_context_length(model)
        self.threshold_tokens = int(self.context_length * 0.50)  # 50% 触发
        self.tail_token_budget = int(self.threshold_tokens * 0.20)  # 尾部预算
        self.max_summary_tokens = min(int(self.context_length * 0.05), 12_000)  # 摘要上限
```

**Scale Design**: Both the tail budget and the summary cap are proportional to the model context window, with large window models getting richer summaries [1].

**`protect_first_n` (v2026.5.x configurable)**: `compression.protect_first_n` (default `3`, `ContextCompressor.__init__` parameters with the same name) - In addition to the permanently protected system prompts, the number of additional **verbatim reserved** non-system messages at the beginning; set to `0` to only nail the system prompt [1]. `ContextEngine` also exposes the field of the same name [1].

### 2. Tool output pruning (three-stage preprocessing)

`_prune_old_tool_results()` Now do three things, all without adjusting LLM [1]:

**Pass 1 — MD5 deduplication**: The same tool result (>200 chars, non-multimodal) is deduplicated by MD5 hash, only the latest copy is retained, and the old copy is replaced with:
```
[Duplicate tool output — same content as a more recent call]
```
Typical scenarios: Read the same file repeatedly, or search the same pattern [1] repeatedly.

**Pass 2 — Smart Collapse** (2026-04-14): Press `tool_call_id` to find out the tool name + parameters, and generate an **informational 1-line summary** to replace the original universal placeholder [1]. Different tools have different templates:

```text
[terminal] ran `npm test` -> exit 0, 47 lines output
[read_file] read config.py from line 1 (1,200 chars)
[search_files] content search for 'compress' in agent/ -> 12 matches
[patch] replace in config.py (1,500 chars result)
[web_search] query='cache control' (5,200 chars result)
[delegate_task] 'refactor auth module' (8,400 chars result)
[memory] save on long-term
```

Compared with the old `_PRUNED_TOOL_PLACEHOLDER`, the summary retains the **specific command/file path/result size**, and the model still knows "what has been done before" when looking at the history [1]. The built-in template covers terminal / read_file / write_file / search_files / patch / browser_* / web_search / web_extract / delegate_task / execute_code / skill_* / vision_analyze / memory / todo / clarify / text_to_speech / cronjob / process, and other tools use the common fallback [1].

**Pass 3 — tool_call parameter truncation**: If there is `tool_calls.function.arguments` length > 500 in the assistant message, it will be truncated to the first 200 characters + `...[truncated]` [1]. Fix scenario: `write_file(content=50KB)` This kind of call even if the tool result is pruned, the parameter itself still accounts for the context [1].

**Multimodal Protection**: All three Passes detect `isinstance(content, list)` and skip multimodal messages to avoid corrupting image/audio content [1].

#### Strip historical media (_strip_historical_media, #27189)

Added `_strip_historical_media()` (`context_compressor.py:275-329`) as the **last step** of `compress()` to execute [1]. It takes the latest user message with an image as the anchor and replaces the image part in all earlier messages with short placeholder text, so that multi-MB base64 image blobs do not have to be resent every round. If there is no user message with an image, or the only message with an image is the first message (there is no strippable content before it), [1] is returned unchanged. Only a shallow copy of the modified message is made, the input is never modified [1].

### 3. Summary budget calculation

```python
def _compute_summary_budget(turns_to_summarize):
    content_tokens = estimate_messages_tokens_rough(turns_to_summarize)
    budget = int(content_tokens * 0.20)  # 压缩到 20%
    return max(2000, min(budget, self.max_summary_tokens))
```

**Design**: The summary budget is proportional to the content to be compressed, but the upper and lower limits are controlled [1].

### 4. Serialize to summary text

```python
def _serialize_for_summary(turns):
    """
    将对话轮次序列化为带标签的文本:
    [TOOL RESULT xxx]: 内容 (截断为 3000 chars: 前2000 + ... + 后800)
    [ASSISTANT]: 内容 + [Tool calls: tool_name(args), ...]
    [USER]: 内容 (截断为 3000 chars)
    """
```

**Critical**: Contains the tool call name and parameters that enable the abstractor to preserve specific file paths, commands, and output [1].

### 5. Structured summary generation

#### First compression (v3 action-log template, 2026-04-14)

```text
## Goal
[用户要完成什么]

## Constraints & Preferences
[用户偏好、编码风格、约束、重要决策]

## Completed Actions
[编号动作列表,每条格式: N. ACTION target — outcome [tool: name]
例:
1. READ config.py:45 — found `==` should be `!=` [tool: read_file]
2. PATCH config.py:45 — changed `==` to `!=` [tool: patch]
3. TEST `pytest tests/` — 3/50 failed: test_parse, test_validate, test_edge [tool: terminal]
要求具体:文件路径、命令、行号、结果都必须保留]

## Active State
[当前工作状态:
- 工作目录和分支
- 已修改/创建的文件及简要说明
- 测试状态 (X/Y passing)
- 运行中的进程或服务器
- 关键环境信息]

## In Progress
[压缩触发时正在进行的工作]

## Blocked
[未解决的阻塞/错误,包含完整错误消息]

## Key Decisions
[重要技术决策及其 WHY]

## Resolved Questions
[用户问过且已回答的问题 — 包含答案,避免下一任 agent 重复回答]

## Pending User Asks
[用户问过但尚未回答的问题]

## Remaining Work
[未完成的任务]

## Relevant Files
[读取/修改/创建的文件]

## Critical Context
[具体值、错误消息、配置细节等不能丢失的信息]
```

#### v2 summary template (old version, for comparison reference)

```text
## Goal
[What the user is trying to accomplish]

## Constraints & Preferences
[User preferences, coding style, constraints, important decisions]

## Progress
### Done
[Completed work — include specific file paths, commands run, results obtained]
### In Progress
[Work currently underway]
### Blocked
[Any blockers or issues encountered]

## Key Decisions
[Important technical decisions and why they were made]

## Resolved Questions
[Questions the user asked that were ALREADY answered — include the answer]

## Pending User Asks
[Questions or requests from the user that have NOT yet been answered]

## Relevant Files
[Files read, modified, or created — with brief note on each]

## Remaining Work
[What remains to be done — framed as context, not instructions]

## Critical Context
[Any specific values, error messages, configuration details]

## Tools & Patterns
[Which tools were used, how they were used effectively, and any tool-specific discoveries]
```

#### v2 → v3 prompt word item-by-item difference

| paragraph | v2 | v3 | Reason for change |
|------|----|----|----------|
| Complete record | `## Progress > ### Done` free text | `## Completed Actions` forced number + fixed format `N. ACTION target — outcome [tool: name]` | Free text is prone to produce vague descriptions ("modified some files"), and the numbering format forces LLM to give specific paths, commands, and line numbers. |
| Format example | none | 3 examples given (READ/PATCH/TEST) | Few-shot guide LLM to adhere to the format |
| Current status | No independent paragraphs, information is scattered in Progress | Added `## Active State` (working directory, branch, modified files, test status, running process) | What is most needed to continue the agent is "where is it now and what is its status". The old version does not have a clear place to carry it. |
| tool mode | `## Tools & Patterns` independent paragraph | **Delete**, tool information is integrated into `[tool: name]` of Completed Actions | Tools and operations are bound to themselves, and separate columns are redundant and waste tokens. |
| Specificity requirements | "Be specific — include file paths, command outputs, error messages, and concrete values" | "Be CONCRETE — include file paths, command outputs, error messages, **line numbers**, and specific values. **Avoid vague descriptions like 'made some changes' — say exactly what changed.**" | Explicitly prohibit vague descriptions and add line numbers requirement |
| iterative update | "ADD new progress. Move from 'In Progress' to 'Done'" | "ADD new completed actions to numbered list **(continue numbering)**. Update 'Active State' to reflect current state. **Remove information only if it is clearly obsolete.**" | "continue numbering" prevents information loss caused by each compression number reset; "only if clearly obsolete" prevents excessive deletion |
| summary budget | `max_tokens = budget × 2` | `max_tokens = budget × 1.3` | 2× is too loose and causes summary bloat, 1.3× is more compact |

**Core design ideas**: The template of v2 leaves too many degrees of freedom for LLM, and the quality of the output is unstable; v3 changes "how to write an abstract" from open-ended to fill-in-the-blank through forced numbering, specific examples, and explicit prohibitions, making the compressed output more predictable and information dense [1].

#### Preamble (Character Settings) - Same as both versions

```text
You are a summarization agent creating a context checkpoint.
Your output will be injected as reference material for a DIFFERENT
assistant that continues the conversation.
Do NOT respond to any questions or requests in the conversation —
only output the structured summary.
Do NOT include any preamble, greeting, or prefix.
```

Source of inspiration: OpenCode's "do not respond to any questions" + Codex's "another language model" framework [1]. Unchanged in both editions [1].

#### iterative update

When there is an old digest, the prompt becomes:

```text
PREVIOUS SUMMARY: [旧摘要]
NEW TURNS TO INCORPORATE: [新轮次]

更新摘要,保留所有仍有用的旧信息。
ADD 新的 completed actions 到编号列表(继续编号)。
把 "In Progress" 移到 "Completed Actions"(完成时)。
把已答问题移到 "Resolved Questions"。
更新 "Active State" 反映当前状态。
仅在明显过时时才移除信息。
```

### 6. Adaptive failure cooling mechanism

```python
_SUMMARY_FAILURE_COOLDOWN_SECONDS = 600   # 10 分钟,用于无 provider
_TRANSIENT_COOLDOWN_SECONDS      = 60    # 1 分钟,用于瞬态错误

def _generate_summary(self, turns):
    if time.monotonic() < self._summary_failure_cooldown_until:
        return None  # 冷却期内跳过

    try:
        response = call_llm(task="compression", ...)
        self._summary_failure_cooldown_until = 0.0  # 成功则重置
    except RuntimeError:
        # 无 provider 配置 — 10 分钟内不会自己恢复
        self._summary_failure_cooldown_until = time.monotonic() + 600
    except Exception:
        # 瞬态错误(超时/限流/网络) — 短冷却快速重试
        self._summary_failure_cooldown_until = time.monotonic() + 60
```

**Design Considerations** (2026-04-14 Improvement): Distinguish between two types of failures. `RuntimeError` indicates configuration problems and will take a 10-minute long cooling. Other exceptions are transient problems and will take a 60-second short cooling by default, allowing compression to recover from short-term failures [1].

#### Abort compression on summary failure (abort-on-summary-failure, #28102/#28117)

`ContextCompressor` constructor adds `abort_on_summary_failure` flag (default `False`, `context_compressor.py:526`) [1]:

- **`True`** — When digest generation fails, compression is **generally aborted**: the original message is returned unchanged and `_last_compress_aborted=True` [1] is set. The conversation is **frozen** until the next `/compress` or `/new` [1].
- **`False` (legacy default)** — Insert a static "summary unavailable" placeholder and discard the intermediate window [1].

Configuration flags are `compression.abort_on_summary_failure` (default `False`) [1]. The caller `agent/conversation_compression.py` will present the `⚠ Compression aborted` warning; the `force` flag will clear the cooldown so that the user's `/compress` retry will take effect immediately after the automatic compression is aborted [1].

### 6b. Anti-Thrashing (Anti-Thrashing, 2026-04-14)

```python
def should_compress(self, prompt_tokens=None) -> bool:
    if tokens < self.threshold_tokens:
        return False
    # 连续 2 次压缩节省 <10%,跳过本次
    if self._ineffective_compression_count >= 2:
        logger.warning(
            "Compression skipped — last %d compressions saved <10%% each. "
            "Consider /new to start a fresh session, or /compress <topic> ..."
        )
        return False
    return True
```

Calculate the actual savings percentage based on `saved_estimate / display_tokens` after each compression:
- `>= 10%` → reset `_ineffective_compression_count = 0` [1]
- `< 10%`  → `_ineffective_compression_count += 1` [1]

**Solved Problem**: In some scenarios (the tail + head + summary itself is already large) compression can only squeeze out 1-2 messages, which is triggered in every round but is almost useless, forming a compression jitter cycle [1]. If it fails twice in a row, it will give up and prompt the user to `/new` or `/compress <topic>` to handle [1] manually.

### 7. Integrity protection of tool calls

```python
def _sanitize_tool_pairs(messages):
    """
    修复压缩后孤儿 tool_call / tool_result 对:
    
    故障模式 1: 工具结果引用的 call_id 对应的 assistant tool_call 被移除
    → API 报错 "No tool call found for function call output..."
    → 解决: 删除孤儿结果
    
    故障模式 2: assistant 有 tool_calls 但对应的结果被丢弃
    → API 报错 "every tool_call must be followed by a tool result..."
    → 解决: 插入存根结果 "[Result from earlier conversation]"
    """
```

**Importance**: Failure to fix will cause the API to reject the entire message list, failing compression with [1].

### 8. Boundary alignment

```python
def _align_boundary_forward(messages, idx):
    """如果边界落在 tool result 上，向前推到非工具消息"""

def _align_boundary_backward(messages, idx):
    """如果边界落在 tool call/result 组中间，向后拉回完整包含该组"""
```

**Prevent data loss**: Avoid splitting the assistant + tool_results group, otherwise `_sanitize_tool_pairs` will remove tail orphan results causing silent data loss [1].

**v0.10.0 Fix**: Added `_ensure_last_user_message_in_tail()` method, called at the end of `_find_tail_cut_by_tokens`, ensuring that **the last user message always remains at the end** [1]. Previously, in some scenarios, compression would push the user's active task instructions into the summary area, causing the agent to lose the current task context, stall or repeat completed work (#10896) [1].

### 9. Tail token budget protection

```python
def _find_tail_cut_by_tokens(messages, head_end, token_budget):
    # 硬底线：至少保护 3 条尾部消息
    min_tail = min(3, n - head_end - 1)
    
    # 软上限：允许预算 1.5 倍超额，避免在超大消息中间切割
    soft_ceiling = int(token_budget * 1.5)
    
    # 从末尾向前累加，直到超过 soft_ceiling 且已满足 min_tail
    # 如果预算不足以覆盖 min_tail → 回退到 n - min_tail（强制保护 3 条）
    # 如果预算覆盖全部 → 强制在 head 之后切割，确保压缩仍执行
```

Key change (2026-04-09): Changed from fixed message number protection to **token budget + hard bottom line min_tail=3**, which is more reasonable for both long and short messages [1].

**Header protection configurable**: The number of protected header messages `protect_first_n` is now configurable (default `3`), indicating the number of additional non-system messages protected in addition to system prompts, which can be adjusted through `compression.protect_first_n` of `config.yaml` [1].

**Historical media stripping**: After the compression is completed, `_strip_historical_media()` will be called to strip the historical multi-modal content (base64 images, etc.) outside the summary area to prevent old screenshots from continuing to occupy the context token [1].

### 10. Summary role selection

```python
# 摘要消息插入时，选择合适的 role 避免连续同角色
if last_head_role in ("assistant", "tool"):
    summary_role = "user"
else:
    summary_role = "assistant"

# 如果选择的角色与尾部冲突，尝试翻转
# 如果两种角色都会造成冲突 → 合并到第一条尾部消息中
```

## Context Management Panorama

### Infinite rounds of dialogue

Hermes **No limit on the number of dialogue turns** [1]. No `max_history`, no fixed round truncation [1]. The entire conversation history is kept in memory and maintained by compressor cycles:

```text
对话开始 → 消息累积 → 达到上下文窗口 50% → 自动压缩
                                              │
                                        修剪 + 摘要 + 重组
                                              │
                                        继续累积 → 再次达到 50% → 再次压缩 → ...
```

Theoretically unlimited conversations [1]. Each compaction generates an iteratively updated digest, rather than resummarizing [1] from scratch.

### Session split

The session is split during compression in order to retain the complete original message for later retrieval by `session_search` [1].

```text
压缩前:
  session "abc" (DB 中已有 msg 0-49 完整原始消息)
  内存中 msg 2-40 即将被压缩成摘要

压缩后:
  session "abc" (结束, reason="compression")
    → DB 中 msg 0-49 完整保留 ← session_search 可搜到原始内容

  session "abc-2" (新建, parent_session_id="abc")
    → 摘要 + 尾部消息 + 后续新消息
    → _last_flushed_db_idx 重置为 0

多次压缩形成链:
  abc → abc-2 → abc-3 → ...
  每一段都是完整的，通过 parent_session_id 链保持血缘
```

**Why not replace it in place? ** If the compressed message is overwritten back to the same session, the first half of the DB is the original message and the second half is the summary, and session_search finds inconsistent data [1]. Splitting ensures that the content of each session fragment is complete and consistent [1].

### Message persistence mechanism

Messages are not written to the DB one by one in real time, but are flushed in batches at the exit point:

```python
def _flush_messages_to_session_db(self, messages, conversation_history):
    # 增量写入：从上次水位线开始，只写新增消息
    flush_from = max(start_idx, self._last_flushed_db_idx)
    for msg in messages[flush_from:]:
        db.append_message(session_id, role, content, ...)
    self._last_flushed_db_idx = len(messages)  # 更新水位线
```

**Trigger timing** (20 call points in the code, covering all exit paths):

| scene | ensure |
|------|------|
| Conversation completed normally | ✅ Write [1] |
| API error max retry exhausted | ✅ Write [1] before giving up |
| User Interrupt (Ctrl+C) | ✅ Write [1] before interrupt |
| Rate limit was interrupted while waiting | ✅ Write [1] |
| 413/context overflow compression failed | ✅ Write [1] |
| Tool execution exception | ✅ Write [1] |
| Fallback provider all failed | ✅ Write [1] |

**Water level line anti-duplication**: `_last_flushed_db_idx` records the written position. Even if multiple exit paths call `_persist_session()` repeatedly, the same message is not written twice (fixes issue #860) [1].

```text
第一次 flush:  messages[0:15] → DB,  水位线 = 15
第二次 flush:  messages[15:23] → DB, 水位线 = 23
第三次 flush:  messages[23:23] → 跳过（无新消息）
```

## Design superiority

### Contrast discarding old messages

| Dimensions | discard old messages | Context Compressor |
|---|---|---|
| Information retention | Completely lost [1] | Structured snippets retain key information [1] |
| continuity | Agent forgot completed work [1] | Know progress and decisions [1] |
| Document tracking | Missing [1] | List related files [1] |
| iterative update | Not applicable [1] | Summary iterable update [1] |
| user experience | Agent repeats work [1] | Agent continues from summary [1] |

### Cost effective

Compression uses **auxiliary LLM** (a cheap model like Gemini 3 Flash) instead of the main conversational model [1]. Typical scenario:
- Auxiliary model cost: $0.01-0.05/compression [1]
- Avoided duplication of effort costs: far exceeds compression costs [1]
- Context savings: 30-70% [1]

## Configuration and operation

### Configuration parameters

```yaml
# config.yaml
compression:
  summary_provider: auto      # 或 openrouter, nous, custom
  summary_model: ""           # 空=自动选择
  threshold_percent: 0.50     # 50% 上下文使用时触发
  protect_first_n: 3          # 系统提示之外额外保护的非系统头部消息数；0=仅保护系统提示
```

> **Auxiliary compression model context length detection (fixed in 2026-05-13)**: When `auxiliary.compression.provider` is `auto`, the compression model reuses the main model's provider/base_url [1]. `_check_compression_model_feasibility` will now forward `custom_providers` to the `get_model_context_length()` call of the secondary compression model, so that per-model `context_length` overrides (such as 196608 of minimax-m2.7 on NVIDIA NIM) also take effect on the secondary model, no longer falling back to the value of models.dev (`fix(auxiliary): forward custom_providers ...`) [1].

### environment variables

```bash
# 为压缩任务设置特定模型
export AUXILIARY_COMPRESSION_MODEL=claude-haiku-4-5
export CONTEXT_COMPRESSION_PROVIDER=openrouter
```

### runtime status

```python
compressor.get_status()
# 返回: {
#   "last_prompt_tokens": 45000,
#   "threshold_tokens": 65536,
#   "context_length": 131072,
#   "usage_percent": 34,
#   "compression_count": 2
# }
```

## Comparison with OpenClaw (Claude Code) compression mechanism

OpenClaw's compression implementation is located in `src/agents/compaction.ts` and uses a **chunked digest** strategy, in sharp contrast to Hermes' **three-stage preprocessing + single digest** [1].

### Overall architectural differences

| Dimensions | Hermes v3 | OpenClaw |
|------|-----------|----------|
| overall strategy | Local preprocessing → Boundary demarcation → Single-shot LLM Summary [1] | Chunked + multiple LLM digests (two paths, see below) [1] |
| Number of LLM calls | **1 time** (only the middle part after weight loss)[1] | **Multiple times** (rolling N times, or parallel N+1 times) [1] |
| preprocessing | MD5 deduplication + Smart Collapse + parameter truncation (zero token)[1] | `stripToolResultDetails()` Remove tool details (lightweight) [1] |
| Chunking | Not divided into blocks, three sections: head, middle and tail [1] | Two chunking strategies (see below) [1] |

OpenClaw actually has two compression paths (`src/agents/compaction.ts`):

- **`summarizeChunks` (rolling)**: Cut into chunks according to the token upper limit, serial processing - chunk1 summary is passed in as `previousSummary` of chunk2, and gradually rolls [1]. LLM calls [1] N times.
- **`summarizeInStages` (parallel + merge)**: `splitMessagesByTokenShare()` is cut into N blocks (default `DEFAULT_PARTS=2`), each block is digested independently, and finally merged with [1] using `MERGE_SUMMARIES_INSTRUCTIONS`. LLM calls [1] N+1 times.

### Summary template comparison

**Hermes v3 (11 paragraphs):**

```
Goal / Constraints & Preferences / Completed Actions（编号+格式）/
Active State / In Progress / Blocked / Key Decisions /
Resolved Questions / Pending User Asks / Relevant Files /
Remaining Work / Critical Context
```

**OpenClaw (5 paragraphs):**

```
Decisions / Open TODOs / Constraints/Rules /
Pending user asks / Exact identifiers
```

The Hermes template is more detailed (11 paragraphs vs. 5 paragraphs), and the context obtained by the continuation agent is richer [1]. The OpenClaw template is more refined, but there is a `Exact identifiers` section that explicitly requires the retention of literal values ​​such as IDs/URLs/hashes/ports [1].

### Comparison one by one

| Dimensions | Hermes v3 | OpenClaw |
|------|-----------|----------|
| Operation record | `Completed Actions` Numbered list `N. ACTION target — outcome [tool: name]` [1] | No special paragraphs, integrated into Decisions [1] |
| runtime status | `Active State` (branch, test status, running process) [1] | None [1] |
| Exact value retained | `Critical Context` section [1] | `Exact identifiers` segment (IDs/URLs/hash/port) [1] |
| Unanswered question tracking | `Pending User Asks` + `Resolved Questions` (distinguish between answered/unanswered) [1] | `Pending user asks` (only tracking unanswered) [1] |
| Document tracking | `Relevant Files` Stand-alone paragraph [1] | None, preserve path by Exact identifiers [1] |
| Quality check | None (trust LLM output) [1] | `auditSummaryQuality()` Check 5 paragraphs, retry without passing, and generate the skeleton [1] |
| iterative update | "continue numbering" continues the old digest number [1] | `previousSummary` passes in the next block [1] |
| abstract cap | Compressed content × 0.2, upper limit 12K tokens [1] | Hard 16,000 characters [1] |
| Anti-shake | 2 consecutive times <10% → skip [1] | 6 skip reason categories (`already_compacted_recently`, etc.) [1] |
| Failure handling | RuntimeError 600s / transient 60s cooling [1] | 15 minute safety timeout + 3 retries + structured cover [1] |
| Tools for repair | `_sanitize_tool_pairs()` Complement orphan pair [1] | `repairToolUseResultPairing()` Delete orphans [1] |
| tail protection | token budget dynamics + hard bottom line 3 items [1] | `DEFAULT_RECENT_TURNS_PRESERVE=3` (maximum 12) [1] |
| multilingual | No special treatment [1] | "Write summary in the primary language" [1] |

### Each has his or her own strengths

**Hermes Advantages:**
- Local preprocessing (MD5 deduplication + Smart Collapse) cuts 30-50% tokens before LLM, OpenClaw does not have this layer [1]
- A single LLM call, no matter how long the conversation is, only calls [1] once
- The template is more detailed (11 paragraphs vs 5 paragraphs), and the context obtained by continuing the agent is richer [1]

**OpenClaw Advantages:**
- Quality verification closed loop (review → retry → backbone), Hermes does not have [1]
- The chunking strategy is naturally adapted to extremely long conversations (a single LLM input window is limited, and chunking avoids overflow) [1]
- `Exact identifiers` section explicitly reserved key literal [1]
- Skip reason classification is more detailed (6 reasons), helpful for debugging [1]

## Interaction with Prompt Caching

Anthropic's prompt caching works best with the system prompt prefix [1]. Compression strategy and cache coordination:

1. **Keep system prompts unchanged** — Maximize cache hits [1]
2. **Compress conversation history only** — Message part mutable [1]
3. **Using the same system prompt structure** — cache key stable [1]

## Triggers in the Agent loop

The agent loop logic that drives compression is now located in `agent/conversation_loop.py` (no longer in `run_agent.py`):

```python
while api_call_count < max_iterations and iteration_budget.remaining > 0:
    # 检查 token 预算
    if token_usage > threshold:
        compressed = compressor.compress(messages, current_tokens=token_usage)
        messages = [system_prompt] + [compressed] + recent_messages
```

## v2026.4.30+ Increased toughness

- **Unknown errors retry on main model first and then give up** (PR #16774) - aux compression does not fail immediately when an unknown error is reported, retry with the main model summary first and then decide whether to give the user a failure prompt [1]
- **Proactively notify the user when the Aux model fails** (PR #16775) - Even if the main fallback is rescued, the user will receive the surface of the aux failure (previously, the error was swallowed silently, resulting in the user not being able to see the aux configuration problem) [1]
- **Multimodal token estimation uses text-char sum instead** (PR #16369) - `_find_tail_cut_by_tokens` no longer attempts to decode image base64 to estimate tokens to avoid PIL memory explosion; images are estimated by their placeholder text character count [1]
- **Aux head budget reservation system + tools headroom** (PR #15631) - Leave space for system + tools when the aux model binding threshold is set to prevent the compression prompt from being too long and triggering aux's own ctx limit [1]
- **`/compress` is packaged in `_busy_command`** (PR #15388) - prevents the user from continuing to type during compression to avoid race condition [1]

## 2026-05-31 Increment — `/compress here [N]` Boundary Awareness + Compressor Quadruple Repair

### `/compress here [N]` — User-selected compression boundary (#35048, commit `bcc830100`)

Inspired by Claude Code Rewind "Summarize up to here" (v2.1.139, Week 20) ​​[1]. Added **User Selected Compression Boundary** subcommand to the existing `/compress` series:

- `/compress here [N]` - Digest all but the last `N` exchanges, the last `N` keep the original text (default `N=2`) [1]. Equivalent to `/compress --keep N` [1].
- Naked `/compress` (all-in pressure) and `/compress <focus>` (focus pressure) behave unchanged [1].

#### New module `hermes_cli/partial_compress.py` (line 235)

| function | Line number | Responsibilities |
|---|---|---|
| `parse_partial_compress_args(raw_args)` | `:55` | Parse `here [N]` / `--keep N` [1] |
| `_coerce_keep(value)` | `:111` | N → int [1] |
| `split_history_for_partial_compress(messages, keep_last)` | `:124` | Split head/tail by exchange boundary [1] |
| `rejoin_compressed_head_and_tail(summary_msg, tail)` | `:180` | **seam-alternation guard**: merge any illegal `user → user` / `assistant → assistant` adjacent [1] |

#### routing

- `cli.py:10006-10019` —— Give the `here [N]` path to the `partial_compress` module and reuse the existing `_compress_context` session-rotation / lock mechanism [1].
- `gateway/run.py` - Parallel registration of the same path [1].

**Why do you need seam guard? ** After the header summary becomes a single assistant message, the first message in the tail is still assistant (the continuation of a series of tool rounds), and illegal `assistant → assistant` [1] will appear at the splicing point. Guard inserts minimal placeholder user messages at the junction leaving role alternation unchanged [1].

Tested: 12 helper unit + 5 CLI integration + E2E (with interleaved tool-calls, degenerate seam, multimodal tail, real handler path) [1].

### Compressor four consecutive repairs (2026-05-29 ~ 30)

| commit | theme |
|---|---|
| `42bbd221e` (#35344) | **strip stale handoff prefix on resume** - `_strip_summary_prefix` only matches the two literals "current/legacy" SUMMARY_PREFIX, the earlier version of the prefix remains in the text after resume, and the old "resume exactly from Active Task" command hijacks the new round of reply [1]. Changed to support multi-version prefix history stripping, reconcile #26290 + #32787 double repair [1]. |
| `56b8dccf2` | **treat unanswered user questions as Active Task** - The template originally described Active Task as "task assignment / request", summary LLM writes `'None'` when seeing user **questions** (not explicit tasks), causing the next round to lose the sequel focus [1]. Change: Unanswered questions are also Active Task [1]. |
| `020601d41` | **drop conflicting 'resume Active Task' directive** - SUMMARY_PREFIX contains two mutually exclusive instructions at the same time ("As a background reference, do not respond" vs "Resume from Active Task"), delete the second [1]. |
| `e38b0b55d` + `9dbc3722a` | **avoid repeat preflight compaction from rough estimates** - preflight rough estimate triggers compaction [1] back and forth near the threshold boundary. Add monotonic clamping + StopIteration test fix [1]. |

### Status bar token sentinel clamp (`f2d4cf4f7`, #35858)

`fix(cli): clamp post-compression token sentinel in status bar`：

- Status bar reads `context_compressor.last_prompt_tokens`, originally only `or 0` protected 0/None [1].
- Sentinel may be negative (transient state) [1] at the moment compression is completed. `or 0` does not override [1]. Change `max(0, value or 0)` to [1].

### docs: Compression threshold sources (`860cf28da`, #35099)

`docs: clarify compression threshold is derived from the main model's context window`：

- The original document hints "you can adjust the compression threshold", but does not explain that the value is derived from [1] based on the **main model** context window.
- Add a note: Please check the main model context length before adjusting the threshold; switching to the main model will automatically recalculate [1].

---

## ABC compliance fix (2026-05-23 ~ 24, `8b2adea` + `dcbcdd6`)

- `agent/context_compressor.py:+7` - ABC compliance: `total_tokens` attributes are aligned with `api_mode` fields `ContextEngine` ABC [1].
- `agent/context_engine.py:+1` - ABC interface synchronization [1].
- `agent/conversation_loop.py` —— 4 places `update_model()` calls complement `api_mode` Parameters: long_context failover and probe stepping [1].
- `agent/agent_runtime_helpers.py` —— rollback restore path simultaneous interpretation `compressor_api_mode` [1].
- `agent/chat_completion_helpers.py` —— fallback activation path simultaneous interpretation [1].
- There are 31 root-logger calls (`logging.warning/error/info`) in 5 files instead of module logger (`logger.warning/error/info`), respecting the module-level log filtering [1].

Returns [1] with `tests/agent/test_last_total_tokens.py:+22` and `tests/run_agent/test_plugin_context_engine_init.py`.

## Relationships with other systems

- [Auxiliary Client Architecture](auxiliary-client-architecture.md) — compression called via `call_llm(task="compression")`
- [Smart Model Routing](smart-model-routing.md) — Get the context window using get_model_context_length()
- [Prompt Builder Architecture](prompt-builder-architecture.md) — The compressed message is passed to the prompt builder to rebuild the prompt
- [Prompt Caching Optimization](prompt-caching-optimization.md) — Compaction strategy coordinated with prompt caching
- [Large Tool Result Handling](large-tool-result-handling.md) — Tool output pruning is consistent with the concept of large result processing
- [Session Search And Sessiondb](session-search-and-sessiondb.md) — Original messages remain in DB for retrieval after Session split
- [Memory System Architecture](memory-system-architecture.md) — Pre-compression `on_pre_compress` notification (`flush_memories` tool removed in v2026.4.30)

## Related Pages

- [[Agent Loop And Prompt Assembly|agent-loop-and-prompt-assembly]]
---
