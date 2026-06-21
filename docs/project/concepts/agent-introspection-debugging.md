---
title: "Agent Introspection Debugging"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: web
    url: "https://github.com/affaan-m/ECC"
    title: "ECC introspection debugging pattern"
    date: 2026-06-05
confidence: high
contested: false
---

# Agent Introspection Debugging

A 4-phase approach for when agents are stuck in loops or consuming tokens without progress. Derived from [Ecc Repo](../entities/ecc-repo.md).[1]

## Four Phases[1]

### 1. Capture
Record error, last tool calls, context pressure, environment assumptions. Take a snapshot of the current state before making any changes.[1]

### 2. Diagnose
Match failure to known pattern before changing anything. Don't start guessing — identify which category of problem this is (auth failure, rate limit, malformed input, infinite loop).[1]

### 3. Recover
Smallest reversible action that validates the diagnosis. Make one change at a time and verify it addresses the root cause.[1]

### 4. Report
Structured debug report with evidence. Include: what was observed, what pattern matched, what action was taken, what result followed.[1]

## Core Principle[1]

Stop retrying blindly. Capture state → diagnose pattern → minimal recovery action → verify. Each blind retry wastes tokens and may mask the real issue.[1]

## Related Pages

- [Ecc Repo](../entities/ecc-repo.md)
- [Verification First Workflow](verification-first-workflow.md)
- [Agent Memory Taxonomy](agent-memory-taxonomy.md)
