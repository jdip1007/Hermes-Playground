---
title: "Agent Architecture Patterns"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: analysis
    url: ""
    title: "Claude Code leaked source code + cross-framework analysis"
    date: 2026-06-05
confidence: high
contested: false
---

# Agent Architecture Patterns

Cross-cutting patterns for optimizing agent token usage, context management, and workflow efficiency. Synthesized from [Claude Code](entities/claude-code.md) leaked source code plus 10 external agent repos including [Rtk Repo](entities/rtk-repo.md), [Ecc Repo](entities/ecc-repo.md), DeepCode, antigravity-skills, serena, ruflo, kilocode, and others.[1]

## Pattern Categories

### Memory & State[1]
- [Agent Memory Taxonomy](concepts/agent-memory-taxonomy.md) — 4-type classification (user/feedback/project/reference)[1]
- Structured storage separating short-term (session) vs long-term (persistent) memory[1]
- RAG retrieval for past decisions and corrections[1]
- Automatic memory compaction when approaching limits[1]

### Context Efficiency[1]
- [Context Compaction Strategies](concepts/context-compaction-strategies.md) — budgeting, lazy loading, threshold alerts[1]
- [Output Filtering Strategies](concepts/output-filtering-strategies.md) — 6 strategies for reducing tool output before context injection[1]
- LSP context: inject only relevant symbols/functions based on call graph analysis instead of dumping entire files[1]

### Execution Patterns[1]
- [Forked Agent Pattern](concepts/forked-agent-pattern.md) — cache-safe subagent spawning with isolation[1]
- Parallel execution lane matrices (ECC) — dependency graphs before parallel work[1]
- Cost-aware routing — route model selection by task complexity for 3-4x savings[1]
- Hooks over skills — hooks intercept behavior cross-cuttingly; skills define it[1]

### Verification & Safety[1]
- [Verification First Workflow](concepts/verification-first-workflow.md) — Run → Verify → Report evidence[1]
- Schema validation for all inputs/outputs[1]
- Crypto signatures for critical changes[1]

### Debugging[1]
- [Agent Introspection Debugging](concepts/agent-introspection-debugging.md) — 4-phase: Capture → Diagnose → Recover → Report[1]

## Key Rules[1]

**Regex > LLM (95/5 rule)**: Regex handles 95-98% of structured text → cheap, deterministic. LLM only for <0.95 confidence edge cases. Don't send structured parsing to an LLM when regex solves it deterministically at near-zero cost.[1]

**Search-First Before Building**: Always search existing solutions (npm/PyPI/GitHub/MCP servers) before writing net-new code. Research costs less than maintaining custom solutions.[1]

**Content-Hash Caching**: Cache expensive operations by SHA-256 content hash, not file path. Survives file moves/renames, auto-invalidates on content change.[1]

## Related Pages

- [Claude Code](entities/claude-code.md)
- [Rtk Repo](entities/rtk-repo.md)
- [Ecc Repo](entities/ecc-repo.md)
- [Agent Memory Taxonomy](concepts/agent-memory-taxonomy.md)
- [Forked Agent Pattern](concepts/forked-agent-pattern.md)
- [Context Compaction Strategies](concepts/context-compaction-strategies.md)
- [Output Filtering Strategies](concepts/output-filtering-strategies.md)
- [Verification First Workflow](concepts/verification-first-workflow.md)
- [Agent Introspection Debugging](concepts/agent-introspection-debugging.md)
