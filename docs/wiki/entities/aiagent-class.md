---
title: AIAgent Class
created: 2026-04-07
updated: '2026-06-08'
type: entity
tags:
- agent-system
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# AIAgent Class

## Location

`run_agent.py:326` (class definition)[1]

## Overview

The AIAgent is the core conversation loop class of Hermes Agent, responsible for managing LLM interactions, tool calls, and session state [1]. Starting from v0.14.0, `run_agent.py` underwent a major refactoring: the class **remains in `run_agent.py`**, but core implementations such as `__init__`, `run_conversation`, `_build_system_prompt`, tool execution, Codex runtime, etc., have been extracted to the `agent/` submodules. The class now only retains **thin forwarder methods**[1].

After refactoring `run_agent.py`: approximately 12 helper modules were extracted into the `agent/` package. Many methods on AIAgent are now just thin forwarders, with the actual implementations residing in modules under `agent/`[1].

## Constructor

The `__init__` (`run_agent.py:349`) itself is a forwarder, passing all parameters as-is to `init_agent()` in `agent/agent_init.py`[1].

```python
class AIAgent:
    def __init__(self,
        base_url: str = None,
        api_key: str = None,
        provider: str = None,
        api_mode: str = None,           # e.g., "codex_app_server"
        model: str = "",                # defaults to empty string, resolved at runtime to "anthropic/claude-opus-4.6"
        max_iterations: int = 90,
        tool_delay: float = 1.0,
        enabled_toolsets: list = None,
        disabled_toolsets: list = None,
        quiet_mode: bool = False,
        save_trajectories: bool = False,
        platform: str = None,           # "cli", "telegram", etc.
        session_id: str = None,
        skip_context_files: bool = False,
        load_soul_identity: bool = False,
        skip_memory: bool = False,
        iteration_budget: "IterationBudget" = None,
        fallback_model: dict = None,
        credential_pool=None,
        checkpoints_enabled: bool = False,
        pass_session_id: bool = False,
        # ... total of 60+ parameters: routing params, dozens of callbacks, etc.
    ):
        """Forwarder — see agent.agent_init.init_agent"""
        from agent.agent_init import init_agent
        init_agent(self, ...)
```

## Core Methods

Most methods within the class are forwarders, delegating implementation to submodules in `agent/`[1]:

| Method | Location | Forwarding Target |
|--------|----------|-------------------|
| `chat(message, stream_callback=None) -> str` | `run_agent.py:3880` | Internally calls `run_conversation`, returns `final_response` |
| `run_conversation(...)` | `run_agent.py:3867` | `agent/conversation_loop.py:187` `run_conversation()` |
| `_build_system_prompt(...)` | `run_agent.py:2164` | `agent/system_prompt.py` `build_system_prompt()` |
| `_build_system_prompt_parts(...)` | `run_agent.py:2159` | `agent/system_prompt.py` `build_system_prompt_parts()` |
| `_run_codex_app_server_turn(...)` | `run_agent.py:3894` | `agent/codex_runtime.py` `run_codex_app_server_turn()` |
| `_execute_tool_calls(...)` | `run_agent.py` | `agent/tool_executor.py` `execute_tool_calls_sequential/concurrent` |
| `_sanitize_api_messages(...)` | `run_agent.py:2196` | `agent/agent_runtime_helpers.py` `sanitize_api_messages()` |

### `chat(self, message: str, stream_callback: Optional[callable] = None) -> str`

Simple interface that returns the final response string [1].

### `run_conversation(self, user_message: str, system_message: str = None, conversation_history: List[Dict] = None, task_id: str = None, stream_callback: Optional[callable] = None, persist_user_message: Optional[str] = None) -> Dict[str, Any]`

Full interface that returns a `{final_response, messages}` dictionary [1]. The actual loop logic resides in `agent/conversation_loop.py`[1].

`AIAgent.run_conversation` itself is just a forwarder at `run_agent.py:3859`; the actual implementation is `run_conversation` at `agent/conversation_loop.py:187` (with a leading `agent` parameter)[1]. `_build_system_prompt` (`run_agent.py:2156`) is similarly a forwarder → `build_system_prompt` in `agent/system_prompt.py`[1].

## Conversation Loop

Implementation is located at `agent/conversation_loop.py:187`[1]:

```python
agent.iteration_budget = IterationBudget(agent.max_iterations)
api_call_count = 0

# Optional codex_app_server runtime: delegates the entire turn to the codex app-server subprocess
if agent.api_mode == "codex_app_server":
    return agent._run_codex_app_server_turn(...)

while (api_call_count < agent.max_iterations
       and agent.iteration_budget.remaining > 0) or agent._budget_grace_call:
    api_call_count += 1
    # ... initiates API call
    if assistant_message.tool_calls:
        agent._execute_tool_calls(assistant_message, messages,
                                  effective_task_id, api_call_count)  # → agent/tool_executor.py
    else:
        return final_response
```

## Key Features [1]

- **Fully synchronous** — does not use asyncio
- **Forwarder architecture** — lean class body, implementations distributed across `agent/` submodules
- **Tool loop** — supports multi-turn tool calls with sequential/concurrent execution paths
- **Iteration budget** — `IterationBudget` controls the maximum number of API calls
- **Platform-aware** — injects different prompts based on the platform
- **Memory integration** — automatically loads and injects memory
- **Skill integration** — builds skill index (with two-level caching)
- **Context compression** — automatically manages context length
- **Codex runtime** — supports `codex_app_server` / `codex_responses` api_mode
- **System prompt persistence** — system prompts are stored in SessionDB; the Gateway reads them back when creating a new AIAgent each turn to reuse prefix caching

## Related Pages

- [Agent Loop And Prompt Assembly](../concepts/agent-loop-and-prompt-assembly.md) — Core agent loop and system prompt assembly
- [Multi Agent Architecture](../concepts/multi-agent-architecture.md) — Sub-agent delegation and iteration budget system
- [Prompt Builder Architecture](../concepts/prompt-builder-architecture.md) — System prompt builder architecture

## Related Files [1]

- `run_agent.py` — `AIAgent` class definition and forwarder methods (4123 lines)
- `agent/agent_init.py` — `init_agent()`, constructor implementation (1504 lines)
- `agent/conversation_loop.py` — `run_conversation()`, conversation loop (4099 lines)
- `agent/system_prompt.py` — Three-layer system prompt assembly (346 lines)
- `agent/tool_executor.py` — Tool call execution (910 lines)
- `agent/codex_runtime.py` — Codex app-server / Responses runtime (448 lines)
- `agent/agent_runtime_helpers.py` — Runtime helpers such as message sanitization (2158 lines)
- `agent/prompt_builder.py` — System prompt text constants and context file loading (1465 lines)
- `model_tools.py` — Tool orchestration