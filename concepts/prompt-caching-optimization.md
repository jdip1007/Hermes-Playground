---
title: Prompt Caching 优化架构
created: 2026-04-07
updated: 2026-05-12
type: concept
tags: [architecture, module, performance, cost-optimization, anthropic, openrouter, nous-portal]
sources: [agent/prompt_caching.py, run_agent.py]
---

# Prompt Caching — Anthropic 缓存优化架构

## 概述

Prompt Caching 位于 `agent/prompt_caching.py`（201 行纯函数，无类状态），实现 Anthropic 风格的多层 cache_control 断点策略。在多轮对话中可以减少约 **75% 输入 token 成本**，对启用了长前缀缓存的 Claude 路径还能在**跨会话**第一轮就命中缓存。

两种核心策略：

| 策略 | 函数 | TTL 布局 | 适用路径 |
|------|------|----------|----------|
| **`system_and_3`** | `apply_anthropic_cache_control` | 4 断点全部同 TTL（5m 或 1h） | 默认路径（非长前缀） |
| **`prefix_and_2`** | `apply_anthropic_cache_control_long_lived` | 1h 稳定前缀 + 5m 滚动尾 | Claude on Anthropic / OpenRouter / Nous Portal（v2026.5.x+） |

可配置项：`prompt_caching.cache_ttl`（5m 默认，1h 可选；v0.12.0 起从硬编码改成 config）。

## system_and_3：原始策略

Anthropic 允许在消息中标记 `cache_control` 断点；断点前的内容会缓存，命中时只收 cache_read 费用（约正常费用的 10%）。Anthropic 限制**最多 4 个断点**。

| 断点 | 位置 | 缓存内容 | 稳定性 |
|---|---|---|---|
| 1 | 系统提示 | 身份 + 平台提示 + 技能索引 | 最高（轮内不变） |
| 2 | 倒数第 3 条非系统消息 | 早期对话 | 高 |
| 3 | 倒数第 2 条非系统消息 | 中期对话 | 中 |
| 4 | 倒数第 1 条非系统消息 | 最近对话 | 低（每轮滚动） |

四个断点全部使用同一个 TTL（5m 或 1h），由 `cache_ttl` 参数决定（源码 `agent/prompt_caching.py:59-89`）。

### 滚动窗口

```
轮次 1: [系统提示★] [用户1★] [助手1★] [助手2★]
轮次 2: [系统提示★] [用户1] [助手1] [用户2★] [助手2★] [用户3★]
                                       ↑断点向后滚动
```

★ = cache_control 标记。每个新请求新断点位置后移。

## prefix_and_2：跨会话长前缀策略（v2026.5.x+ 新增）

**触发条件**：Claude 模型且 provider 为 Anthropic、OpenRouter、Nous Portal（含 Portal-Claude 路径，v0.11+ 起 Portal Qwen 也走此路径）。`run_agent.py:12472` 处分支。

**核心思想**：把 4 个断点拆分成两层 TTL：

| 断点 | 位置 | TTL | 目的 |
|---|---|---|---|
| 1 | `tools[-1]` 数组末尾 | **1h** | tools array 整体缓存（Anthropic 缓存顺序 tools → system → messages） |
| 2 | 系统消息 `content[0]`（稳定前缀块） | **1h** | 跨会话稳定前缀（身份 + 工具描述 + 标准指导） |
| 3 | 倒数第 2 条非系统消息 | **5m** | 滚动窗口 |
| 4 | 倒数第 1 条非系统消息 | **5m** | 滚动窗口 |

**关键不变量**：
- 系统消息必须被**预先切分**成有序 content blocks，`block[0]` 是字节级稳定的跨会话前缀，后续块带上下文文件 / 易变后缀。若未切分则整段标 1h（fallback 路径，仍正确但 hit rate 降低）。
- 滚动窗口从 3 收缩到 2，腾出第 4 个断点给 tools。
- 标记 tools 最后一个 dict 缓存整个 tools 数组（Anthropic 文档：marker 放在你想包进缓存前缀的最后一块上）。OpenAI-wire 边界上，marker 在 OpenRouter/Nous Portal 转发到 Anthropic 时保留。

为什么用 OpenAI-wire 也能用？因为 marker 字段直接出现在 tool / message dict 上，OpenRouter 和 Nous Portal 透传该字段；最终由 Anthropic 后端读取生效。原生 Anthropic 路径由 `convert_tools_to_anthropic` 显式转换 marker（`mark_tools_for_long_lived_cache`，行 178-200）。

### 收益

第一次会话：tools + system prefix 写入 1h 缓存。第二次会话**冷启动**：系统提示和 tools 数组直接 cache_read 命中（不再付正常 token 费用），即使消息历史完全不同也能省下大头开销。Hermes 在 `prompt_builder` 中保证系统消息的 prefix block 字节稳定（同一 user config 下，第 0 块永远一样的 byte stream）。

## 核心组件

### `_apply_cache_marker`

```python
def _apply_cache_marker(msg, cache_marker, native_anthropic=False):
    # tool 角色：只在 native_anthropic 模式下标记
    # 空内容：在消息级别标记
    # 字符串内容：转换为 [{"type": "text", "text": ..., "cache_control": ...}]
    # 列表内容：在最后一个元素添加 cache_control
```

统一处理 Anthropic API 的多种消息格式变体（字符串、对象列表、tool result）。

### `_build_marker`

```python
def _build_marker(ttl: str) -> Dict[str, str]:
    marker = {"type": "ephemeral"}
    if ttl == "1h":
        marker["ttl"] = "1h"
    return marker
```

5m 是 Anthropic 默认 ephemeral TTL，所以不需要显式写 `"ttl"`。1h 需要显式声明。

### `_mark_system_stable_block`

只标记系统消息 `content[0]`（稳定前缀块）。如果系统消息还是单段字符串（未切分），降级把整段包成单 block 标记——仍然正确，只是失去 prefix vs suffix 分离的 hit rate 收益。

## 配置入口

```yaml
# config.yaml
prompt_caching:
  cache_ttl: "5m"   # 或 "1h"
```

或环境变量：`HERMES_PROMPT_CACHE_TTL=1h`。

之前（v0.11 及更早）TTL 是硬编码的，v0.12.0 起改成可配置（PR #15065，salvage of #12659）。1h TTL 对**间歇性突发**会话特别有用（用户离开 30 分钟后回来，缓存未过期）。

## 成本对比（示意）

假设系统提示 + tools 共 8000 tokens，每轮消息平均 2000 tokens：

| 场景 | 无缓存 | system_and_3（5m） | prefix_and_2（1h prefix） |
|---|---|---|---|
| 单一会话 10 轮 | 100K tokens | ~30K tokens（命中） | ~28K tokens |
| 30 分钟后冷启动 1 轮 | 10K tokens | 10K（缓存过期） | **1K cache_read + 2K** |

prefix_and_2 的真正价值在**冷启动**：会话切换、`/new`、新进程，第一轮就能复用上一次会话留下的 1h 前缀缓存。

## 设计原则

- **纯函数**：无类状态、无 AIAgent 依赖。每个函数 deep-copy 输入返回新列表，调用方可任意组合。
- **共享 marker 构造**：所有 TTL 通过 `_build_marker` 走同一逻辑，避免散落的 `{"type": "ephemeral"}` 字面量。
- **多 provider 透传**：相同 marker 字段在 Anthropic 原生 / OpenRouter / Nous Portal 三条路径都成立，由后端 Anthropic API 读取。

## 集成点

| 调用点 | 路径 |
|--------|------|
| `run_agent.py:1446`（`system_and_3` 文档注释） | 标准路径 |
| `run_agent.py:12472-12483`（`prefix_and_2`） | Claude on Anthropic/OpenRouter/Nous Portal |
| `run_agent.py:3607` | 其他端点的 `system_and_3` 注释 |

## 与其他系统的关系

- [[prompt-builder-architecture]] — 必须保证系统消息 `content[0]` 字节稳定，否则 1h 前缀缓存命中率会大幅下降
- [[provider-transport-architecture]] — `AnthropicTransport` / `ChatCompletionsTransport` 在 build_kwargs 阶段透传 marker
- [[auxiliary-client-architecture]] — 辅助模型不使用 prompt caching（避免污染主会话 prefix cache，且辅助任务通常一次性）
- [[context-compressor-architecture]] — 压缩会冻结快照保留 prefix cache，详见 prefix-cache 友好的 OpenClaw 对比段
- [[smart-model-routing]] — 缓存价格信息来自 models.dev
