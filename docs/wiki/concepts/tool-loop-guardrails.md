---
title: Tool call loop guardrail
created: 2026-05-04
updated: '2026-06-08'
type: concept
tags:
- agent-system
- tool-loop
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Tool Call Loop Guardrails

## Overview

`agent/tool_guardrails.py`(Line 455) Implement a **pure functional controller**, track the tool call mode of the agent in each round, and give a warning (default) or hard stop (opt-in) when a "loop" is found. Design principle: **warning-first** - By default, it only warns but does not block. Hard stop must be explicitly enabled.[1]

Source code:

```
agent/tool_guardrails.py:1-7
The controller in this module is intentionally side-effect free: it tracks
per-turn tool-call observations and returns decisions. Runtime code owns
whether those decisions become warning guidance, synthetic tool results, or
controlled turn halts.
```

## Three loop modes

### 1. Exact Failure Loop — Repeat failure with args

Signature =`(tool_name, sha256(canonical_json(args)))`. The cumulative number of failed calls with the same signature.[1]

| trigger | Default threshold | Behavior |
|------|---------|------|
| `exact_failure_warn_after` | 2 | warn |
| `exact_failure_block_after` | 5 | block (only hard_stop_enabled=true) |

### 2. Same Tool Failure Loop — the same tool fails with any args

according to`tool_name`Aggregate the failure count for this round.[1]

| trigger | Default threshold | Behavior |
|------|---------|------|
| `same_tool_failure_warn_after` | 3 | warn |
| `same_tool_failure_halt_after` | 8 | halt (only hard_stop_enabled=true) |

### 3. Idempotent No-Progress Loop — read-only tool with the same args and results

only right`IDEMPOTENT_TOOL_NAMES`(read_file/search_files/web_search/web_extract/session_search/browser_snapshot/mcp_filesystem_*) takes effect. The result is used`_result_hash()`Hash - first`safe_json_loads`Normalized to sha256.[1]

| trigger | Default threshold | Behavior |
|------|---------|------|
| `no_progress_warn_after` | 2 | warn |
| `no_progress_block_after` | 5 | block (only hard_stop_enabled=true) |

## Tool classification

`tool_guardrails.py:19-59`：

```python
IDEMPOTENT_TOOL_NAMES = frozenset({
    "read_file", "search_files",
    "web_search", "web_extract",
    "session_search",
    "browser_snapshot", "browser_console", "browser_get_images",
    "mcp_filesystem_read_file", "mcp_filesystem_read_text_file",
    "mcp_filesystem_read_multiple_files",
    "mcp_filesystem_list_directory", "mcp_filesystem_list_directory_with_sizes",
    "mcp_filesystem_directory_tree",
    "mcp_filesystem_get_file_info",
    "mcp_filesystem_search_files",
})

MUTATING_TOOL_NAMES = frozenset({
    "terminal", "execute_code", "write_file", "patch",
    "todo", "memory", "skill_manage",
    "browser_click", "browser_type", "browser_press",
    "browser_scroll", "browser_navigate",
    "send_message", "cronjob", "delegate_task", "process",
})
```

`_is_idempotent()`Double check: exclude mutating first, and then confirm it is in the idempotent set. Unlabeled tools (MCP/plug-ins) are not considered idempotent, and no-progress detection will not cause accidental damage.[1]

## decision-making structure

### `ToolGuardrailDecision`（`tool_guardrails.py:143-172`）

```python
@dataclass(frozen=True)
class ToolGuardrailDecision:
    action: str = "allow"  # allow | warn | block | halt
    code: str = "allow"
    message: str = ""
    tool_name: str = ""
    count: int = 0
    signature: ToolCallSignature | None = None

    @property
    def allows_execution(self) -> bool:
        return self.action in {"allow", "warn"}

    @property
    def should_halt(self) -> bool:
        return self.action in {"block", "halt"}
```

**Key Attributes**:`warn`Execution is still allowed (`allows_execution=True`), only runtime guidance is appended.`block`Intercept before calling,`halt`Stop the round after calling it.[1]

### `ToolCallSignature`（`tool_guardrails.py:126-141`）

```python
@dataclass(frozen=True)
class ToolCallSignature:
    tool_name: str
    args_hash: str   # sha256 of canonical_tool_args(args)
```

`canonical_tool_args`use`sort_keys=True, separators=(",", ":"), default=str`Serialization ensures args order is independent.`to_metadata()`Only expose hash, **do not expose raw args** to telemetry.[1]

## Workflow

`ToolCallGuardrailController`at the beginning of each round`reset_for_turn()`：[1]

```python
def reset_for_turn(self):
    self._exact_failure_counts: dict[ToolCallSignature, int] = {}
    self._same_tool_failure_counts: dict[str, int] = {}
    self._no_progress: dict[ToolCallSignature, tuple[str, int]] = {}
    self._halt_decision: ToolGuardrailDecision | None = None
```

### `before_call(tool_name, args)`

`tool_guardrails.py:238-280`. **Only if`hard_stop_enabled=True`** Just checked.[1]
- If the signature exact_failure_count ≥ block threshold → return`block`,Record`_halt_decision`。
- If it is idempotent and no_progress repeat_count ≥ block threshold → return`block`。
- otherwise`allow`。

### `after_call(tool_name, args, result, failed=None)`

`tool_guardrails.py:282-375`。[1]

**Failure path**:
1. The signature`_exact_failure_counts +1`
2. the tool`_same_tool_failure_counts +1`
3. Clear the no_progress record of the signature
4. Check same_tool halt → halt threshold →`halt`
5. Check exact warn threshold →`warn`
6. Check same_tool warn threshold →`warn`

**Success Path**:
1. Clear exact_failure / same_tool count
2. if not idempotent →`allow`
3. calculate`_result_hash(result)`, compared with the last record of this signature:
   - Same →`repeat_count +1`
   - different →`repeat_count = 1`
4. `repeat_count ≥ no_progress warn 阈值` → `warn`

## Failure detection

`classify_tool_failure()`（`tool_guardrails.py:188-218`) mirror`agent.display._detect_tool_failure`, **Guarantee guardrail judgment and visible to CLI users`[error]`Label consistent**. on the production path`run_agent.py`Always pass explicitly`failed=`;This function is the backbone of testing and tools.[1]

Special handling:
- `terminal`: Parse result as dict,`exit_code != 0`regarded as failure
- `memory`: `success: false` + `"exceed the limit"` → `[full]`
- General:`"error"` / `"failed"`/ by`Error`Beginning →`[error]`

## output

### `toolguard_synthetic_result(decision)`— synthesize tool results when block

```python
def toolguard_synthetic_result(decision):
    return json.dumps({
        "error": decision.message,
        "guardrail": decision.to_metadata(),
    }, ensure_ascii=False)
```

Replaces real tool calls, keeping the agent's tool result history intact.[1]

### `append_toolguard_guidance(result, decision)`— Attach runtime guidance when warning/halt

```
[Tool loop warning: repeated_exact_failure_warning; count=3; <message>]
```

or

```
[Tool loop hard stop: same_tool_failure_halt; count=8; <message>]
```

Attach it to the end of the original result so that the agent can see the self-reflection prompt in the next step of reasoning.[1]

## Configuration

```yaml
# config.yaml
tool_loop_guardrails:
  warnings_enabled: true       # 默认 true
  hard_stop_enabled: false     # 默认 false（opt-in）
  warn_after:
    exact_failure: 2
    same_tool_failure: 3
    idempotent_no_progress: 2
  hard_stop_after:
    exact_failure: 5
    same_tool_failure: 8
    idempotent_no_progress: 5
```

`ToolCallGuardrailConfig.from_mapping`（`tool_guardrails.py:82-123`) supports two-way compatibility between new nested keys and old flat keys.`_positive_int`Don't worry, illegal values ​​fall back to default.[1]

## design philosophy

> **warnings_enabled: true, hard_stop_enabled: false**
>
> Warnings are on by default, and hard stops are off by default, allowing interactive CLI/TUI sessions to receive gentle prompts unless the user explicitly turns on the circuit-breaker behavior in config.yaml.

——`tool_guardrails.py:71-72`

Reason: **hard stop will destroy the agent's exploration ability**. Loop detection may give false positives, and warning allows the model to decide whether to adjust the strategy on its own; only upgrade to hard stop in scenarios such as batch/cron/long tasks where no one is watching.[1]

## Verify PR

- `58b8996` `fix(agent): add tool-call loop guardrails`
- `0704589` `fix(agent): make tool loop guardrails warning-first`
- `8fa44b1` `fix(guardrails): preserve display _detect_tool_failure semantics`

## Related concepts

- [Tool Registry Architecture](tool-registry-architecture.md) — Central tool registry, guardrails intercepts at dispatch boundary
- [Interrupt And Fault Tolerance](interrupt-and-fault-tolerance.md) — Division of labor between error_classifier vs tool_guardrails: classifier handles **single error classification**, guardrails handles **multiple repeat patterns**
- [Parallel Tool Execution](parallel-tool-execution.md) — Parallel execution does not affect guardrails, per-turn controller is single-threaded aggregation

## Related Pages

- [[Agent Loop And Prompt Assembly|agent-loop-and-prompt-assembly]]
---
