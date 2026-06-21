---
title: "RTK (rtk-ai/rtk)"
created: 2026-06-05
updated: 2026-06-05
type: entity
tags: [agent-repo, ai-ml]
sources:
  - type: web
    url: "https://github.com/rtk-ai/rtk"
    title: "rtk-ai/rtk GitHub repository"
    date: 2026-06-05
confidence: medium
contested: false
---

# RTK (rtk-ai/rtk)

Open-source agent framework analyzed for cross-framework pattern extraction [1]. Contributed output filtering strategies and token budgeting patterns to the [Agent Architecture Patterns](../concepts/agent-architecture-patterns.md) knowledge base.

## Key Contributions

### Output Filtering Strategies

Applied before pasting tool output into context [1]:

1. **Stats Extraction** — Replace raw lists with counts/metrics (`git log` → "5 commits, +142/-89") [1]
2. **Failure Focus** — Lead with errors/failures, bury passing results [1]
3. **Deduplication** — Remove repeated patterns in logs, configs, or repetitive output blocks [1]
4. **Structure-Only JSON** — For large JSON/configs: strip values, keep schema/keys to save context tokens [1]
5. **Tree Compression** — Summarize directory structures with hierarchical counts rather than flat file listings [1]
6. **Fail-Safe Raw Output Preservation** — Save full terminal output to temp files before summarizing [1]

### Token Budgeting

Track tokens per session/task with alerts at 70%/90% thresholds [1]. Set per-task limits (search: 5K, code: 10K, generation: 20K) [1]. Suggest compression strategies when approaching limits [1].

## Related Pages

- [Output Filtering Strategies](../concepts/output-filtering-strategies.md)
- [Agent Architecture Patterns](../concepts/agent-architecture-patterns.md)
- [Claude Code](claude-code.md)
