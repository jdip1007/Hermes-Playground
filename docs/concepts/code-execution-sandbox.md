---
title: Code Execution Sandbox (execute_code)
created: 2026-04-10
updated: '2026-06-08'
type: concept
tags:
- agent-system
- sandbox
- code-execution
- tools
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Code Execution Sandbox

## Overview

The `execute_code` tool allows the LLM to write a Python script that is executed in an isolated subprocess [1]. The script can call back into a limited set of Hermes tools via RPC, compressing multi-step tool chains into a single inference step, reducing token consumption and latency [1].

## Core Value

```text
Traditional method: 10 rounds of tool calls = 10 LLM inferences + 10 context expansions
execute_code: 1 LLM script write + 1 execution, intermediate results do not enter context
```

## Sandbox Restrictions

### Allowed Tools (Only 7) [1]

```python
SANDBOX_ALLOWED_TOOLS = [
    "web_search",      # Search
    "web_extract",     # Web extraction
    "read_file",       # Read file
    "write_file",      # Write file
    "search_files",    # Search files
    "patch",           # Patch/Modify file
    "terminal",        # Terminal command
]
```

### Resource Limits [1]

```python
DEFAULT_TIMEOUT = 300         # 5 minute timeout
DEFAULT_MAX_TOOL_CALLS = 50   # Max 50 tool calls
MAX_STDOUT_BYTES = 50_000     # Output limit 50KB
MAX_STDERR_BYTES = 10_000     # Error output limit 10KB
```

Can be overridden via `code_execution.*` in config.yaml [1].

## Two Communication Modes [1]

| Mode | Applicable Backend | Communication Method |
|------|---------|---------|
| **UDS (Unix Domain Socket)** | local | Parent process opens an RPC listener; child process calls tools via socket |
| **File-based RPC** | Docker / SSH / Modal / Daytona | Child process writes request file → Parent polls → Writes response file |

### Flow [1]

```text
1. Parent process generates hermes_tools.py stub (contains RPC functions)
2. Parent process starts RPC listener (UDS socket or file polling thread)
3. Child process executes script written by LLM
4. Script calls hermes_tools.web_search(...) etc.
   → Sent back to parent process via RPC → Parent process calls actual tools → Returns results
5. Only final stdout is returned to LLM, intermediate results do not enter context
```

## Relationship with Terminal Backends [1]

Scripts from `execute_code` **run within the current terminal backend**. If the backend is Docker, the script runs inside Docker and callbacks to local tools via file-based RPC [1].

## Post-Write Validation Chain: Delta Lint → LSP Diagnostics → File-Mutation Footer [1]

Hermes strengthened the "agent immediately knows if a file write failed" workflow in three steps from v0.13.0 to v0.14.0 [1]:

### 1. Delta Lint (v0.13.0+) [1]

`tools/file_tools.py:1045,1061,1171`: Automatically runs Python / JSON / YAML / TOML syntax checks after `write_file` + `patch`. **Only reports newly introduced errors** to the agent (existing errors are ignored) [1].

### 2. LSP Semantic Diagnostics (v0.14.0+) [1]

`agent/lsp/` (11 modules, ~4400 lines: `cli.py / protocol.py / client.py:930 / manager.py:644 / eventlog.py / install.py / servers.py:1040 / range_shift.py / workspace.py / reporter.py`) [1]:

Runs a **real language server** for **semantic analysis** after writing—type errors, undefined symbols, missing imports, unreachable code—and immediately surfaces them to the agent [1]. LSP servers are installed on-demand by `agent/lsp/install.py`, and `agent/lsp/servers.py` maintains a registry of servers for Python/TypeScript/Go/Rust, etc. [1].

A significant upgrade over basic syntax checking [1].

### 3. File-Mutation Verifier Footer (v0.14.0+) [1]

`tools/file_state.py` + `agent/file_safety.py`: If files are written or modified in a turn, **appends a footer to the agent** summarizing exactly what changed on disk (paths, line counts, deltas) [1]. The agent immediately detects failures like "I thought it was saved but it wasn't," preventing false success reports [1].

## Related Pages
- [[Tool Registry Architecture|tool-registry-architecture]]
- [[Security Defense System|security-defense-system]]

- [Terminal Backends](terminal-backends.md) — Which backend executes the script
- [Large Tool Result Handling](large-tool-result-handling.md) — Overflow protection for tool results

## Key Source Code [1]

- `tools/code_execution_tool.py` (1347 lines) — Complete sandbox implementation
- `tools/file_tools.py:1045,1061,1171` — Delta lint (v0.13.0+)
- `agent/lsp/` — LSP semantic diagnostics (v0.14.0+, 11 modules)
- `tools/file_state.py` + `agent/file_safety.py` — File-mutation footer (v0.14.0+)