---
title: MemoryStore Class
created: 2026-04-07
updated: '2026-06-08'
type: entity
tags:
- agent-system
- memory
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# MemoryStore Class

## Location

`tools/memory_tool.py` [1]

## Overview

MemoryStore is the core class of the memory system, managing read/write operations for MEMORY.md and USER.md [1].

## Constructor

```python
class MemoryStore:
    def __init__(self, memory_char_limit=2200, user_char_limit=1375):
        self.memory_entries: List[str] = []
        self.user_entries: List[str] = []
        self.memory_char_limit = memory_char_limit
        self.user_char_limit = user_char_limit
        self._system_prompt_snapshot: Dict[str, str] = {"memory": "", "user": ""}
```

## Core Methods

### `load_from_disk()`

Loads entries from disk and captures a frozen snapshot [1].

### `add(target, content) -> Dict`

Adds a new entry, checking for duplicates and character limits [1].

### `replace(target, old_text, new_content) -> Dict`

Replaces an entry using short unique substring matching [1].

### `remove(target, old_text) -> Dict`

Removes entries containing the specified text [1].

### `format_for_system_prompt(target) -> Optional[str]`

Returns a frozen snapshot for system prompt injection [1].

## Key Design Features

- **Frozen Snapshot Pattern** — System prompts remain unchanged during a session [1]
- **Atomic Writes** — Temporary files + os.replace() ensure consistency [1]
- **File Locking** — fcntl.flock() used for concurrency safety [1]
- **Security Scanning** — Detects injection and leakage patterns [1]

## Related Pages

- [Memory System Architecture](../concepts/memory-system-architecture.md) — Overall memory system architecture
- [Skills And Memory Interaction](../concepts/skills-and-memory-interaction.md) — Skill and memory interaction design
- [Security Defense System](../concepts/security-defense-system.md) — Security scanning for memory content

## Related Files

- `tools/memory_tool.py` — Implementation [1]
- `agent/memory_manager.py` — Manager [1]
- `agent/prompt_builder.py` — System prompt integration [1]