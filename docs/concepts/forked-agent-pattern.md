---
title: "Forked Agent Pattern"
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

# Forked Agent Pattern

A pattern for spawning isolated subagent sessions that share the parent's prompt cache while keeping intermediate output hidden from the parent [1]. Derived from [Claude Code](../entities/claude-code.md) architecture [1].

## Cache-Safe Forking

Forks share the parent's prompt cache (system prompt, tools, model, messages prefix, thinking config) [1]. This means:
- The fork inherits all context up to the fork point [1]
- Token costs for shared prefix are cached (no re-processing) [1]
- Forks are isolated — parent doesn't see intermediate tool noise [1]

## When to Fork

- **Research**: Fork open-ended questions that require exploration [1]
- **Implementation**: Fork work requiring more than a couple edits [1]
- **Parallel forks** for independent research questions in one message [1]

## Fork Prompt Design

Fork inherits parent context, so the prompt is a **directive** (what to do), not background explanation [1]. Be specific about scope: what's in, what's out, what another agent handles. Don't re-explain background the fork already knows [1].

## Parent Behavior

- Trust completion notifications — don't peek at intermediate output [1]
- Don't fabricate or predict fork results before notification arrives [1]
- Use parallel forks for independent tasks to save wall-clock time [1]

## Related Pages

- [Claude Code](../entities/claude-code.md)
- [Agent Memory Taxonomy](agent-memory-taxonomy.md)
- [[parallel-execution-matrices]]
