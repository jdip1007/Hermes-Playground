---
title: Context References (@ Reference System)
created: 2026-04-10
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
# Context References (@ Reference System)

## Overview

Hermes supports using the `@` prefix in user input to reference external content. The system automatically expands these references into actual content and injects them into the message before sending it to the LLM [1].

## Supported Reference Types

| Syntax | Function | Example |
|------|------|------|
| `@file:path` | Injects file content [1] | `@file:src/main.py` |
| `@file:path:line_number` | Injects specific lines of a file [1] | `@file:main.py:10-50` |
| `@folder:path` | Injects directory structure [1] | `@folder:src/` |
| `@diff` | Injects current git diff [1] | `Check what's wrong with @diff` |
| `@staged` | Injects git staged changes [1] | `Review the code in @staged` |
| `@url:address` | Fetches and injects webpage content [1] | `@url:https://example.com` |
| `@git:ref` | Injects git object content [1] | `@git:HEAD~1` |

## Processing Flow

```text
User input: "Help me check what's wrong with @file:main.py and @diff"
    ↓
parse_context_references() — Regex matches all @ references
    ↓
_expand_reference() — Expands each into actual content one by one
    ↓
Security checks:
  - Paths must be within cwd or allowed_root (prevents path escape) [1]
  - Rejects sensitive files (.ssh/*, .env, .netrc, etc.) [1]
  - Total injected content must not exceed 50% of context window (hard limit), warns if exceeding 25% [1]
    ↓
Injected into "--- Attached Context ---" block at end of message
    ↓
Sent to LLM (@ reference markers removed from original text)
```

## Security Mechanisms

**Sensitive File Interception**: The following paths are blocked from injection:
- `~/.ssh/*` (keys, config) [1]
- `~/.bashrc`, `~/.zshrc`, `~/.profile` (shell configs) [1]
- `~/.netrc`, `~/.pgpass`, `~/.npmrc`, `~/.pypirc` (credential files) [1]
- `skills/.hub/` (internal skill repository files) [1]

**Injection Volume Limits**:
- Hard limit: Injected content must not exceed **50%** of the model's context window [1]
- Soft limit: A warning is printed when exceeding **25%** [1]
- If the hard limit is exceeded, the entire reference operation is rejected (`blocked=True`) [1]

**Path Safety**: Reference paths are resolved to absolute paths and must fall within `cwd` or `allowed_root`, preventing path traversal attacks like `@file:../../etc/passwd` [1].

## Differences from Context Files

| | Context References (@ References) | Context Files (AGENTS.md, etc.) |
|---|---|---|
| Trigger Method | User explicitly writes `@` in input [1] | System auto-loads [1] |
| Injection Location | End of user message [1] | System prompt [1] |
| Content Source | Files/diffs/URLs/git objects [1] | Fixed filenames [1] |
| Lifecycle | Single turn [1] | Entire session [1] |

## Key Source Code

| File | Responsibility |
|------|------|
| `agent/context_references.py` | Reference parsing, expansion, security checks [1] |
| `cli.py` | Entry point calling `preprocess_context_references()` [1] |

## Related Pages
- [[Prompt Caching Optimization|prompt-caching-optimization]]
- [[Agent Loop And Prompt Assembly|agent-loop-and-prompt-assembly]]

- [Prompt Builder Architecture](prompt-builder-architecture.md) — Loading mechanism for Context Files (AGENTS.md, etc.)
- [Security Defense System](security-defense-system.md) — Security check framework