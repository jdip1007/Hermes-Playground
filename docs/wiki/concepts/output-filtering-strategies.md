---
title: "Output Filtering Strategies"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: web
    url: "https://github.com/rtk-ai/rtk"
    title: "rtk-ai/rtk output filtering patterns"
    date: 2026-06-05
confidence: high
contested: false
---

# Output Filtering Strategies

Techniques for reducing tool output before pasting into context. Applied before injecting terminal/command results into the agent's context window. Derived from [Rtk Repo](../entities/rtk-repo.md) [1].

## Six Strategies

### 1. Stats Extraction
Replace raw lists with counts/metrics. Example: `git log` → "5 commits, +142/-89"; `find . -name "*.py"` → "47 Python files across 12 directories" [1].

### 2. Failure Focus
Lead with errors/failures, bury passing results unless explicitly requested. Test suites: failures first. Build logs: surface compiler errors immediately [1].

### 3. Deduplication
Remove repeated patterns in logs, configs, or repetitive output blocks. Collapse identical log lines into counts [1].

### 4. Structure-Only JSON
For large JSON/configs: strip values, keep schema/keys to save context tokens. Useful for understanding structure without drowning in data [1].

### 5. Tree Compression
Summarize directory structures with hierarchical counts rather than flat file listings. Example: "src/ (12 files) → api/ (4), components/ (8)" [1].

### 6. Fail-Safe Raw Output Preservation
Save full terminal output to temp files before summarizing. Never discard raw data permanently without a reference path for later inspection [1].

## When to Apply

- Tool outputs exceed ~50 lines [1]
- Context pressure is building [1]
- Repeated patterns are visible in output [1]
- The user hasn't explicitly requested full output [1]

## Related Pages

- [Rtk Repo](../entities/rtk-repo.md)
- [Context Compaction Strategies](context-compaction-strategies.md)
- [Agent Architecture Patterns](agent-architecture-patterns.md)
