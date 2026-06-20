---
title: "Claude Code"
created: 2026-06-05
updated: 2026-06-05
type: entity
tags: [ai-ml, agent-system]
sources:
  - type: analysis
    url: ""
    title: "Claude Code leaked source code analysis"
    date: 2026-06-05
confidence: high
contested: false
---

# Claude Code

Anthropic's agentic coding assistant [1]. Leaked source code revealed internal architecture patterns for memory management, subagent delegation, context compaction, and tool design [1].

## Architecture Patterns (from leaked source) [1]

### Memory Management System

4-type taxonomy for all stored information [1]:

1. **user** — User profile, role, preferences, responsibilities, knowledge
2. **feedback** — Corrections and confirmations about approach with WHY and HOW TO APPLY
3. **project** — Ongoing work, goals, initiatives, bugs, incidents (not derivable from code/git)
4. **reference** — Pointers to external systems and resources

Memory extraction runs as a forked subagent at session end using parallel reads then parallel writes [1]. Organizes semantically by topic, not chronologically [1]. Maintains an index file with one-line pointers [1].

### Memory Consolidation (Dream Pattern)

4-phase background consolidation on time/session gate [1]:
1. **Orient** — Read index, skim existing memories
2. **Gather** — Look for new signals (daily logs, drifted facts, transcript search)
3. **Consolidate** — Merge new signal into existing files, convert relative dates, delete contradicted facts
4. **Prune** — Update index, remove stale entries, resolve contradictions

### Forked Agent Pattern

Forks share parent's prompt cache (system prompt, tools, model, messages prefix) [1]. Forks are isolated — parent doesn't see intermediate tool noise [1]. Parent trusts completion notifications without peeking at intermediate output [1].

### Context Compaction

Keeps: system prompt, tool definitions, recent messages, plan references, memory files [1]. Discards: old tool results, intermediate steps, raw data that's been processed [1]. Uses compact boundary messages to separate old/new context [1].

## Related Pages

- [Agent Memory Taxonomy](../concepts/agent-memory-taxonomy.md)
- [Forked Agent Pattern](../concepts/forked-agent-pattern.md)
- [Context Compaction Strategies](../concepts/context-compaction-strategies.md)
- [Verification First Workflow](../concepts/verification-first-workflow.md)
- [Output Filtering Strategies](../concepts/output-filtering-strategies.md)
