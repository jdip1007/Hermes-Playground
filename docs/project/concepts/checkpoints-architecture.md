---
title: Checkpoint Manager v2 — Transparent Filesystem Snapshots
created: 2026-05-14
updated: '2026-06-08'
type: concept
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
# Checkpoint Manager v2 — Transparent Filesystem Snapshots

## Overview

`tools/checkpoint_manager.py` (1638 lines) automatically creates a shadow-git snapshot **every turn** before `write_file` / `patch` / `terminal --dangerous`, allowing users to roll back to the state prior to any turn [1]. v0.13.0 is a major rewrite (**v2**), changing the *per-project* shadow repo to a *single shared bare-ish store*, with object deduplication + true pruning [1].

> Key positioning: **This is NOT a tool** — the LLM never sees the checkpoint manager in the schema [1]. It is transparent infrastructure, controlled by the `checkpoints` config flag or the `--checkpoints` CLI flag [1].

## v1 → v2 Changes

### Issues with v1 (comments at ``tools/checkpoint_manager.py:24-30``) [1]

- One complete shadow git repo per working directory [1]
- Objects are not deduplicated across projects [1]
- Disk usage skyrockets for multi-project users [1]
- Pruning is practically ineffective [1]

### v2 Design: Single Shared Store

```
~/.hermes/checkpoints/
    store/                           ← single bare-ish git repo
        HEAD, config, objects/       ← git internals (shared across projects)
        refs/hermes/<hash16>         ← per-project branch tip
        indexes/<hash16>             ← per-project git index
        projects/<hash16>.json       ← {workdir, created_at, last_touch}
        info/exclude                 ← shared default exclusion rules
    .last_prune                      ← auto-prune idempotency marker
    legacy-<timestamp>/              ← pre-v2 per-project shadow repos automatically migrated here
```

`hash16` is the first 16 characters of the SHA hash of the working directory, used as a namespace [1].

## Automatic Migration

`migrate_legacy_shadows()` (``tools/checkpoint_manager.py:340``) [1]:

- Scans `CHECKPOINT_BASE` on first v2 init [1]
- Moves *any pre-v2 shadow repo* (directories containing a `HEAD` file at the top level) + scattered directories into a `legacy-<timestamp>/` subdirectory [1]
- Skips v2 reserved top-level entries (`store/`, `.last_prune`, `legacy-*`) [1]
- v2 starts from a clean state; old data can be manually restored or cleaned up along with legacy files according to retention policies [1]

## Implementation Details

### Complete Git State Isolation

The three environment variables ``GIT_DIR`` + ``GIT_WORK_TREE`` + ``GIT_INDEX_FILE`` all point to the shared store —— **do not** pollute the user project directory's `.git/` [1]:

```python
env = {
    "GIT_DIR":        store_dir,
    "GIT_WORK_TREE":  workdir,
    "GIT_INDEX_FILE": store_dir / "indexes" / hash16,
}
```

Each commit uses a namespaced branch `refs/hermes/<hash16>`, with object deduplication [1].

### ``DEFAULT_EXCLUDES`` (line 78-117)

Predefined global ignores, overriding [1]:

- Dependencies / build outputs: `node_modules/`, `dist/`, `build/`, `target/`, `.next/`, `.nuxt/`
- Caches: `__pycache__`, `*.pyc`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `coverage/`
- Virtual environments: `.venv/`, `venv/`, `env/`
- VCS: `.git/`, `.hg/`, `.svn/`
- Hermes conventions: `.worktrees/` (avoids recursively snapshotting sibling worktrees) [1]
- Compiled/Binary: `*.so`, `*.dylib`, `*.dll`, `*.o`, `*.a`, `*.jar`, `*.class`

### Prune (``prune_checkpoints`` line 1223)

```python
def prune_checkpoints(
    retention_days: int = 7,
    *,
    max_total_size_mb: int = 0,
) -> dict:
```

Three steps [1]:

1. **Orphan**: refs where the `workdir` field no longer exists (project deleted) → delete [1]
2. **Stale**: `last_touch` older than `now - retention_days * 86400` → delete [1]
3. **Size cap**: When `max_total_size_mb > 0`, delete per project starting from the oldest checkpoint until total size falls below the threshold [1]

Finally, ``git gc --prune=now`` reclaims unreferenced objects [1]. `legacy-*` directories are also automatically cleaned up according to retention policies [1].

The `.last_prune` file provides idempotency protection, preventing consecutive prune runs across multiple Hermes starts [1].

## Trigger Conditions

``maybe_checkpoint_before_tool()`` (constructor line 601) —— *at most once per turn* [1]:

- Tool name belongs to `write_file` / `patch` / `terminal` with a destructive flag → captures snapshot **before** tool execution [1]
- Multiple writes in the same turn only trigger one snapshot on the first write —— fully preserving all uncommitted changes up to the next turn [1]

## User Interface

```
hermes checkpoints list                    # snapshots for current project
hermes checkpoints show <id>               # view diff
hermes checkpoints rollback <id>           # roll back to a specific snapshot
hermes checkpoints prune                   # execute prune immediately
hermes checkpoints config                  # view retention/cap configuration
```

``hermes_cli/checkpoints.py`` exposes the CLI; the slash command `/checkpoints` shares the same argparse surface [1].

## Configuration (``config.yaml``)

```yaml
checkpoints:
  enabled: true
retention_days: 7         # Expires after 7 days
max_total_size_mb: 500    # Maximum total size limit; 0 = unlimited
```

## Verification Summary

| Claim | Verification |
|------|------|
| Single shared store | ``tools/checkpoint_manager.py:71`` `_STORE_DIRNAME = "store"` |
| Cross-project object deduplication | Only one `objects/` directory + namespace refs `refs/hermes/<hash16>` |
| Per-project namespace | Via `hash16` SHA prefix |
| Automatic pre-v2 migration | ``migrate_legacy_shadows()`` line 340 |
| True pruning | ``prune_checkpoints`` line 1223, includes ``git gc --prune=now`` |
| Size cap | ``max_total_size_mb`` line 589 + ``_enforce_size_cap()`` line 1087 |
| Does not pollute user `.git/` | ``GIT_DIR`` + ``GIT_WORK_TREE`` + ``GIT_INDEX_FILE`` all point to shared store |
| Invisible to LLM | ``tools/checkpoint_manager.py:12`` —— "This is NOT a tool" |

## Related Pages
- [[Session Search And Sessiondb|session-search-and-sessiondb]]
- [[Interrupt And Fault Tolerance|interrupt-and-fault-tolerance]]

- [Worktree Isolation](worktree-isolation.md) — `.worktrees/` sibling directories are actively excluded by checkpoints
- [Security Defense System](security-defense-system.md) — `terminal` dangerous command mode + checkpoint serves as rollback insurance
- [Cli Architecture](cli-architecture.md) — `/checkpoints` slash command

## Related Files

- ``tools/checkpoint_manager.py`` — Main implementation (1638 lines)
- ``hermes_cli/checkpoints.py`` — ``hermes checkpoints`` CLI