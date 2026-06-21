---
title: "ECC (affaan-m/ECC)"
created: 2026-06-05
updated: 2026-06-05
type: entity
tags: [agent-repo, ai-ml]
sources:
  - type: web
    url: "https://github.com/affaan-m/ECC"
    title: "affaan-m/ECC GitHub repository"
    date: 2026-06-05
confidence: medium
contested: false
---

# ECC (affaan-m/ECC)

Open-source agent framework analyzed for cross-framework pattern extraction [1]. Contributed verification-first workflow, context budgeting, parallel execution matrices, cost-aware routing, and the regex > LLM rule to the [Agent Architecture Patterns](concepts/agent-architecture-patterns.md) knowledge base [1].

## Key Contributions

### Verification-First Workflow

Every task follows: **Run → Verify → Report evidence** [1]:
1. Execute the change/action
2. Run concrete verification (tests, checks, validation)
3. Report pass/fail with artifacts — not "I think it works"
4. Only declare success when evidence proves it

### Context Budgeting

Treat context window as a scarce resource [1]:
- Agent descriptions >30 words in frontmatter → trim to essentials
- Skill files >400 lines → split or lazy-load
- MCP servers wrapping CLI tools (`gh`, `git`) → remove, use native commands
- Combined rules files >300 lines → consolidate or reference externally

### Parallel Execution with Lane Matrices

Before parallel work, write a dependency graph mapping: lane name, parallel? flag, write surface, risk level, verification method [1]. Only parallelize when write surfaces don't collide. Batch reads/searches together, isolate writes by file/branch/service [1].

### Cost-Aware LLM Routing

Route model selection by task complexity [1]:
- Simple tasks (<10K chars, <30 items) → cheaper model (3-4x cost savings)
- Complex tasks → most capable model
- Track cumulative spend immutably with frozen dataclasses

### Regex > LLM Rule (95/5 rule)

Regex handles 95-98% of structured text → cheap, deterministic [1]. LLM only for <0.95 confidence edge cases → expensive fallback. Don't send structured parsing to an LLM when regex solves it deterministically at near-zero cost [1].

### Search-First Before Building

Decision matrix before writing custom code [1]:
- Exact match, well-maintained, MIT/Apache → **Adopt** as-is
- Partial match, good foundation → **Extend** with thin wrapper
- Multiple weak matches → **Compose** 2-3 small packages
- Nothing suitable → **Build** custom (informed by research)

### Agent Introspection Debugging (4-phase)

When stuck in loops or consuming tokens without progress [1]:
1. **Capture**: Record error, last tool calls, context pressure, environment assumptions
2. **Diagnose**: Match failure to known pattern before changing anything
3. **Recover**: Smallest reversible action that validates the diagnosis
4. **Report**: Structured debug report with evidence

### Content-Hash Caching

Cache expensive operations by SHA-256 content hash, not file path: survives file moves/renames (cache hit), auto-invalidates on content change (cache miss) [1]. Service layer separation keeps pure functions testable and caching transparent [1].

## Related Pages

- [Verification First Workflow](concepts/verification-first-workflow.md)
- [Context Compaction Strategies](concepts/context-compaction-strategies.md)
- [Agent Introspection Debugging](concepts/agent-introspection-debugging.md)
- [Agent Architecture Patterns](concepts/agent-architecture-patterns.md)
- [Claude Code](entities/claude-code.md)
