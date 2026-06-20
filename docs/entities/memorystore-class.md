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

## 位置

`tools/memory_tool.py` [1]

## 概述

MemoryStore 是记忆系统的核心类，管理 MEMORY.md 和 USER.md 的读写操作 [1]。

## 构造函数

```python
class MemoryStore:
    def __init__(self, memory_char_limit=2200, user_char_limit=1375):
        self.memory_entries: List[str] = []
        self.user_entries: List[str] = []
        self.memory_char_limit = memory_char_limit
        self.user_char_limit = user_char_limit
        self._system_prompt_snapshot: Dict[str, str] = {"memory": "", "user": ""}
```

## 核心方法

### `load_from_disk()`

从磁盘加载条目并捕获冻结快照 [1]。

### `add(target, content) -> Dict`

添加新条目，检查重复和字符限制 [1]。

### `replace(target, old_text, new_content) -> Dict`

使用短唯一子串匹配替换条目 [1]。

### `remove(target, old_text) -> Dict`

删除包含指定文本的条目 [1]。

### `format_for_system_prompt(target) -> Optional[str]`

返回冻结快照用于系统提示注入 [1]。

## 关键设计

- **冻结快照模式** — 系统提示在会话期间不变 [1]
- **原子写入** — 临时文件 + os.replace() 保证一致性 [1]
- **文件锁** — fcntl.flock() 用于并发安全 [1]
- **安全扫描** — 检测注入和泄露模式 [1]

## 相关页面

- [Memory System Architecture](../concepts/memory-system-architecture.md) — 记忆系统整体架构
- [Skills And Memory Interaction](../concepts/skills-and-memory-interaction.md) — 技能与记忆的交互设计
- [Security Defense System](../concepts/security-defense-system.md) — 记忆内容安全扫描

## 相关文件

- `tools/memory_tool.py` — 实现 [1]
- `agent/memory_manager.py` — 管理器 [1]
- `agent/prompt_builder.py` — 系统提示集成 [1]
