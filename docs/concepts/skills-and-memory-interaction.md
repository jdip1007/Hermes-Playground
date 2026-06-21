---
title: Skills and Memory Interaction
created: 2026-04-07
updated: '2026-06-08'
type: concept
tags:
- agent-system
- agent-pattern
- skill
- memory
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Skills and Memory Interaction

## Design Philosophy

Skills and Memory are two **different types of persistence mechanisms** for the Hermes Agent; they complement rather than compete with each other[1]:

| Dimension | Memory | Skills |
|------|--------|--------|
| **Stored Content** | Facts, preferences, lessons learned | Procedural knowledge, workflows |
| **Capacity** | MEMORY.md: 2200 characters<br>USER.md: 1375 characters[1] | No hard limit[1] |
| **Format** | Item list (§ separated) | Markdown documents + file structure[1] |
| **Purpose** | Quick reference for stable facts | Complete guides for complex tasks[1] |
| **Loading Method** | Injected into system prompt[1] | Progressive disclosure (metadata → full content)[1] |
| **When to Use** | User preferences, environmental facts, tool quirks | Complex workflows with 5+ tool calls[1] |

## Decision Tree

```text
After completing a task, ask:

Is this knowledge...
├─ A simple, stable fact? → Save to Memory
│   (e.g., "User prefers Chinese", "Server is at /root")
│
└─ A complex procedural workflow? → Create as a Skill
    (e.g., "Steps to deploy an ML model", "Process for debugging issue X")
```

## Behavioral Guidelines

### Memory Guidelines (Injected into System Prompt)[1]

```text
You have persistent memory across sessions. Save durable facts using the memory tool:
user preferences, environment details, tool quirks, and stable conventions.
Memory is injected into every turn, so keep it compact and focused on facts
that will still matter later.

Prioritize what reduces future user steering — the most valuable memory is one
that prevents the user from having to correct or remind you again.

Do NOT save task progress, session outcomes, completed-work logs, or temporary
TODO state to memory; use session_search to recall those from past transcripts.[1]
```

### Skills Guidelines (Injected into System Prompt)[1]

```text
After completing a complex task (5+ tool calls), fixing a tricky error,
or discovering a non-trivial workflow, save the approach as a skill
with skill_manage so you can reuse it next time.

When using a skill and finding it outdated, incomplete, or wrong,
patch it immediately with skill_manage(action='patch') — don't wait to be asked.
Skills that aren't maintained become liabilities.[1]
```

## Skill Self-Improvement Loop[1]

```text
1. Agent executes a complex task (5+ tool calls)
   ↓
2. Detects a new pattern or workflow
   ↓
3. Creates a skill using skill_manage(action='create')
   ↓
4. Next time a similar task is encountered → skills_list discovers the skill
   ↓
5. skill_view loads full instructions
   ↓
6. Issues found during execution → Fix with skill_manage(action='patch')
   ↓
7. Skill continuously improves[1]
```

## Role of Session Search[1]

`session_search` is the third persistence mechanism, used to recall **past conversations**[1]:

```text
When the user references something from a past conversation or you suspect
relevant cross-session context exists, use session_search to recall it before
asking them to repeat themselves.[1]
```

Comparison of the Three Mechanisms[1]:

| Mechanism | Content | Retrieval Method |
|------|------|----------|
| **Memory** | Stable facts | Automatically injected into system prompt every turn[1] |
| **Skills** | Procedural knowledge | Loaded on demand (progressive disclosure)[1] |
| **Session Search** | Past conversation records | FTS5 full-text search + LLM summarization[1] |

## Practical Examples[1]

### Saving to Memory[1]

```python
# User correction
memory(action='add', target='user', content='User prefers communicating in Chinese')

# Environmental fact
memory(action='add', target='memory', content='Server is Ubuntu 22.04, Python 3.11')

# Tool quirk
memory(action='add', target='memory', content='patch tool uses fuzzy matching; minor whitespace differences will not break it')[1]
```

### Creating as a Skill[1]

```python
# Complex workflow
skill_manage(
    action='create',
    name='deploy-ml-model',
    content='---\nname: deploy-ml-model\n...'
)[1]
```

## Maintenance Priority[1]

```text
Memory > Skills > Session Search[1]
```

- **Memory** is most important — injected every turn, directly influences behavior[1]
- **Skills** are next — loaded on demand, but affect the quality of complex tasks[1]
- **Session Search** is last — used for recalling context, not core behavior[1]

## Related Pages
- [[Agent Loop And Prompt Assembly|agent-loop-and-prompt-assembly]]

- [Skills System Architecture](skills-system-architecture.md) — Progressive disclosure architecture for the skills system
- [Memory System Architecture](memory-system-architecture.md) — Frozen snapshots and atomic writes for the memory system
- [Session Search And Sessiondb](session-search-and-sessiondb.md) — Session search as the third persistence mechanism

## Related Files

- `agent/prompt_builder.py` — Guideline text definitions
- `tools/memory_tool.py` — Memory implementation
- `tools/skills_tool.py` — Skills implementation
- `tools/session_search_tool.py` — Session Search implementation
- `hermes_state.py` — SessionDB (FTS5 search)