---
title: Git Worktree Isolation
created: 2026-04-10
updated: '2026-06-08'
type: concept
tags:
- agent-system
- worktree
- isolation
- parallel
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Git Worktree Isolation

## Overview

Hermes supports using git worktrees to enable **multiple agents to operate on the same repository in parallel without conflicts** [1]. Each agent session works within an isolated worktree branch, ensuring file modifications do not interfere with each other [1].

## Usage

```bash
hermes -w              # Create isolated worktree on startup
hermes --worktree      # Same as above
```

Or enable globally in config.yaml:
```yaml
worktree: true         # Automatically create worktree every time started in a git repository
```

## How It Works

```text
hermes -w
    ↓
_setup_worktree()
    ↓
1. Check if current directory is inside a git repository (error out if not) [1]
2. Create new worktree under .worktrees/ (git worktree add) [1]
3. Create branch hermes/hermes-{8-char-random-ID}, based on HEAD [1]
4. Automatically add .worktrees/ to .gitignore [1]
5. Copy files listed in .worktreeinclude (gitignored but required by agent) [1]
6. Switch CWD to worktree directory [1]
    ↓
Agent works in isolated environment
    ↓
Session ends → _cleanup_worktree()
    ↓
Delete worktree directory + branch (git worktree remove + git branch -D) [1]
```

## .worktreeinclude File

Some files are ignored by `.gitignore` but required by the agent (e.g., `.env`, `node_modules`) [1]. Create a `.worktreeinclude` file in the project root:

```text
# One path per line, supports files and directories
.env
node_modules
```

- Files: Copied using `shutil.copy2` [1]
- Directories: Symlinks are created (saves disk space) [1]
- Path traversal attack protection: Both source and destination paths must reside within their respective root directories [1]

## Use Cases

- Multiple agents modifying different parts of the same repository simultaneously [1]
- Protecting the main branch from experimental changes [1]
- Combined with multiple Profiles (different Profile + different worktree = fully isolated parallel development) [1]

## Related Pages
- [[Security Defense System|security-defense-system]]
- [[Code Execution Sandbox|code-execution-sandbox]]

- [Configuration And Profiles](configuration-and-profiles.md) — Multi-Profile architecture
- [Multi Agent Architecture](multi-agent-architecture.md) — Multi-Agent collaboration

## Key Source Code

- `cli.py` — `_setup_worktree()` / `_cleanup_worktree()`
- `hermes_cli/main.py` — `-w`/`--worktree` argument parsing