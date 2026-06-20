---
title: "Context Compaction Strategies"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: analysis
    url: ""
    title: "Claude Code leaked source code analysis"
    date: 2026-06-05
confidence: high
contested: false
---

# Context Compaction Strategies

Techniques for managing context window as a scarce resource, derived from Claude Code's leaked source code analysis [1]. Derived from [Claude Code](../entities/claude-code.md) and [Ecc Repo](../entities/ecc-repo.md).

## What to Keep vs Discard

### Keep
- System prompt and tool definitions [1]
- Recent messages [1]
- Plan references [1]
- Memory files [1]

### Discard
- Old tool results [1]
- Intermediate steps [1]
- Raw data that's been processed into summaries [1]

## Compaction Strategy

Use compact boundary messages to separate old/new context. Be aggressive about discarding intermediate data. Keep only essential context when sessions get long [1].

## Context Budgeting Thresholds (ECC)

| Component | Flag Threshold | Action |
|-----------|---------------|--------|
| Agent descriptions | >30 words in frontmatter | Trim to essentials [1] |
| Skill files | >400 lines | Split or lazy-load [1] |
| MCP servers wrapping CLI tools (`gh`, `git`) | Any | Remove — use native commands [1] |
| Combined rules/configs | >300 lines | Consolidate or reference externally [1] |

## Token Budgeting (RTK)

Track tokens per session/task with alerts at 70%/90% thresholds. Set per-task limits:
- Search tasks: ~5K tokens [1]
- Code tasks: ~10K tokens [1]
- Generation tasks: ~20K tokens [1]

Suggest compression strategies when approaching limits [1].

## Lazy Loading

Load skill/content only when triggered, not all at once. Saves context tokens significantly. Classification model: Always needed / Sometimes needed / Rarely needed [1].

## Related Pages

- [Claude Code](../entities/claude-code.md)
- [Ecc Repo](../entities/ecc-repo.md)
- [Rtk Repo](../entities/rtk-repo.md)
- [Output Filtering Strategies](output-filtering-strategies.md)
