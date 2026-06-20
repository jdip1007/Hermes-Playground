---
title: "Verification-First Workflow"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: web
    url: "https://github.com/affaan-m/ECC"
    title: "ECC verification-first pattern"
    date: 2026-06-05
confidence: high
contested: false
---

# Verification-First Workflow

Every task follows: **Run → Verify → Report evidence** [1]. Derived from [Ecc Repo](../entities/ecc-repo.md).

## Four Steps

1. **Execute** the change/action [1]
2. **Verify** with concrete checks (tests, validation, health checks) [1]
3. **Report** pass/fail with artifacts — not "I think it works" [1]
4. Only declare success when evidence proves it [1]

## Key Principle

Verify before acting saves more tokens than any optimization [1]. Hash critical configs, maintain baselines, detect regressions proactively [1].

## Schema Validation

Validate all skill inputs/outputs against JSON schemas [1]. Prevent malformed skills from loading. Check required fields: `name`, `description`, `triggers`, `steps` [1].

## Crypto Signatures (ruflo pattern)

Hash fixes and critical changes for integrity verification [1]. Detect unauthorized modifications to production configs [1].

## Related Pages

- [Ecc Repo](../entities/ecc-repo.md)
- [Agent Introspection Debugging](agent-introspection-debugging.md)
- [Context Compaction Strategies](context-compaction-strategies.md)
