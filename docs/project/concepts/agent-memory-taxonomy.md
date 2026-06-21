---
title: "Agent Memory Taxonomy"
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

# Agent Memory Taxonomy

A 4-type classification system for agent memory management, derived from [Claude Code](entities/claude-code.md) architecture [1]. All stored information uses one of four types to ensure semantic organization and prevent duplication [1].

## The Four Types

### user
User profile, role, preferences, responsibilities, knowledge. Helps tailor behavior. Examples: communication style, technical expertise level, timezone, project conventions [1].

### feedback
Corrections and confirmations about approach. What to avoid, what to keep doing. Must include WHY (reasoning) and HOW TO APPLY (actionable guidance). Example: "User prefers concise responses because verbose output wastes tokens" [1].

### project
Ongoing work, goals, initiatives, bugs, incidents. Not derivable from code/git history. Convert relative dates to absolute. Examples: active feature branches, known bugs, deployment schedules [1].

### reference
Pointers to external systems and resources. Where to find up-to-date information. Examples: API documentation URLs, database schemas, service endpoints [1].

## Extraction Pattern

- Runs as a forked subagent at session end [1]
- Uses parallel reads then parallel writes (turn 1: read all files, turn 2: write all updates) [1]
- Checks existing memories before creating duplicates [1]
- Organizes semantically by topic, not chronologically [1]
- Maintains an index file with one-line pointers, not full content [1]

## Consolidation Pattern

4-phase background consolidation on time/session gate [1]:
1. **Orient** — Read index, skim existing memories [1]
2. **Gather** — Look for new signals (daily logs, drifted facts, transcript search) [1]
3. **Consolidate** — Merge new signal into existing files, convert relative dates, delete contradicted facts [1]
4. **Prune** — Update index, remove stale entries, resolve contradictions [1]

## Pitfalls

- Don't save memories about things derivable from current state (code patterns, architecture, git history, file structure) [1]
- Don't interleave reads and writes across multiple turns — batch them [1]
- Don't fabricate or predict results before verification arrives [1]

## Related Pages

- [Claude Code](entities/claude-code.md)
- [Forked Agent Pattern](concepts/forked-agent-pattern.md)
- [Context Compaction Strategies](concepts/context-compaction-strategies.md)
