---
title: "AI Agent Runaway Incidents and Failure Modes"
created: 2026-06-12
updated: 2026-06-12
type: concept
tags: [ai-ml, agent-system, agent-pattern]
sources:
  - type: web
    url: "https://github.com/dipampaul17/AgentGuard"
    title: "AgentGuard – Auto-kill AI agents before they burn through your budget"
    date: 2025-07-31
  - type: web
    url: "https://inkog.io/report"
    title: "Scanned 500 AI agent repos for bugs, nobody thinks of infinite loops"
    date: 2026-04-04
  - type: web
    url: "https://github.com/converra/agent-triage"
    title: "Agent-triage – diagnosis of agent failures from production traces"
    date: 2026-03-11
  - type: web
    url: "https://nailinstitute.org"
    title: "AVE Database – Open taxonomy of 50 failure modes in multi-agent AI systems"
    date: 2026-03-25
  - type: web
    url: "https://github.com/tansive/tansive"
    title: "Tansive – AI Agents that won't accidentally restart your prod database"
    date: 2025-07-08
  - type: web
    url: "https://www.spendsafe.ai/"
    title: "Spendsafe.ai – Ship AI agents that can't drain your wallet"
    date: 2025-11-17
  - type: article
    url: "/root/bug_reports/cron-dedup-bug-2026-06-12.md"
    title: "Cron Dedup Bug Report – Hermes Agent Incident"
    date: 2026-06-12
confidence: high
contested: false
---

# AI Agent Runaway Incidents and Failure Modes

## Overview

AI agents, particularly autonomous LLM-based systems, are prone to several classes of failure modes that can lead to resource exhaustion [1], financial damage [6], or system lockout [7]. This page documents known incidents, patterns, and mitigation strategies for runaway agent behavior.

**Key insight:** The combination of *autonomous decision-making* + *unbounded resource access* + *lack of circuit breakers* creates a dangerous failure mode where agents can consume excessive resources before human intervention is possible — a pattern observed across multiple platforms [1][2][6][7].

---

## Incident Classification

### 1. Infinite Loop Failures

Agents that enter recursive loops, repeatedly executing the same task or generating new tasks without termination conditions. This is a widespread problem: an analysis of 500+ AI agent repositories found that "nobody thinks of infinite loops" as a common oversight in agent design [2]. Many implementations lack proper loop detection mechanisms entirely [1].

**Known cases:**
- **AgentGuard discovery (2025):** Analysis revealed that many AI agent implementations lack proper loop detection, leading to infinite task generation [1]
- **Inkog report (2026):** Scanned 500+ AI agent repositories and found that "nobody thinks of infinite loops" as a common oversight in agent design [2]

**Pattern:** Agent generates subtask → subtask fails or produces no result → agent retries with same approach → loop continues until resource exhaustion [1][2]

### 2. Resource Exhaustion Failures

Agents that consume excessive compute, API credits, or cloud resources due to unbounded operations. This has become significant enough that dedicated tools like Spendsafe.ai were created specifically because AI agents were draining user wallets through uncontrolled API calls [6]. Similarly, Tansive was built after incidents where AI agents accidentally restarted production databases, causing cascading failures [5].

**Known cases:**
- **Spendsafe.ai (2025):** Created specifically because AI agents were draining user wallets through uncontrolled API calls [6]
- **Tansive project (2025):** Built after incidents where AI agents accidentally restarted production databases, causing cascading failures [5]

**Pattern:** Agent has access to expensive resources → no budget limits or rate limiting → agent makes repeated costly operations → financial damage [5][6]

### 3. Cascading Multi-Agent Failures

When multiple agents interact and create feedback loops that amplify errors or resource consumption. The AVE Database documents 50 distinct failure modes in multi-agent AI systems, including cascading failures where one agent's error triggers others [4]. The growing number of diagnostic tools like Agent-triage indicates these are becoming real-world incidents requiring production-level monitoring [3].

**Known cases:**
- **AVE Database (2026):** Open taxonomy documenting 50 distinct failure modes in multi-agent AI systems, including cascading failures where one agent's error triggers others [4]
- **Agent-triage project (2026):** Built to diagnose agent failures from production traces, indicating growing real-world incidents [3]

**Pattern:** Agent A fails → generates error response → Agent B interprets error as new task → creates more work → system amplifies the initial failure [3][4]

### 4. User Lockout Failures

When runaway agents consume all available resources, preventing human intervention through normal channels. The Hermes Agent cron incident exemplifies this: 75+ duplicate cron jobs created through a platform bug consumed LM Studio backend capacity, making the system unresponsive to user commands [7]. This creates a chicken-and-egg problem where the system is too overloaded to let you fix what's overloading it [7].

**Known cases:**
- **Hermes Agent cron incident (2026):** 75+ duplicate cron jobs created through platform bug consumed LM Studio backend capacity, making the system unresponsive to user commands [7]

**Pattern:** Agent creates excessive parallel tasks → model overloaded → gateway can't respond → user cannot send stop commands → requires external kill switch [7]

---

## Root Cause Analysis

### Common Failure Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Missing termination conditions** | No loop detection or max iteration limits [1][2] | Infinite task generation [1] |
| **Unbounded resource access** | No budget caps, rate limits, or concurrency controls [6] | API cost explosion [5][6] |
| **Lack of priority system** | All tasks compete equally for resources [7] | User lockout during cron flood [7] |
| **No circuit breakers** | System doesn't auto-pause when detecting anomalies [1] | Cascading failures continue unchecked [3][4] |
| **Idempotency gaps** | Operations create duplicates instead of updating [7] | Cron job accumulation bug [7] |

### Why These Failures Are Dangerous

1. **Speed:** AI agents can make decisions and execute actions faster than human response times [1][6]
2. **Scale:** Cloud resources allow agents to scale operations exponentially before detection [5][6]
3. **Opacity:** Agent reasoning is often opaque, making it hard to diagnose failures in real-time — hence tools like Agent-triage that analyze production traces post-incident [3]
4. **Feedback loops:** Multi-agent systems can amplify errors through inter-agent communication, with 50 documented failure modes showing how cascading effects propagate [4]

---

## Mitigation Strategies

### 1. Circuit Breaker Patterns

**Concept:** Auto-pause agent operations when detecting anomalous behavior (high error rates, excessive resource usage, timeout thresholds). This is the core mechanism behind AgentGuard's approach to auto-killing agents before they burn through budgets [1].

**Implementation examples:**
- Budget limits per session/agent [6]
- Rate limiting on API calls [5][6]
- Concurrency caps (max parallel tasks) — addresses the root cause of user lockout incidents [7]
- Timeout-based auto-termination [1]

### 2. Priority Queuing

**Concept:** User requests always get priority over automated/background tasks. This directly addresses the Hermes Agent incident where cron jobs overwhelmed interactive sessions [7].

**Implementation:**
- Interactive sessions > scheduled tasks > health checks [7]
- When model is overloaded, queue lower-priority tasks instead of executing them [1][6]
- Force kill command that bypasses normal channels (`/stop-all-cron`) — prevents user lockout [7]

### 3. Idempotent Operations

**Concept:** Ensure repeated operations produce the same result without creating duplicates. The Hermes Agent cron bug demonstrated how non-idempotent create operations led to 75+ duplicate jobs accumulating across sessions [7].

**Implementation:**
- Check for existing resources before creating new ones — "list before create" pattern [7]
- Use update semantics instead of create when possible [7]
- Unique identifiers for deduplication [2][7]

### 4. Resource Budgeting

**Concept:** Hard limits on compute, API costs, and execution time per agent session. Tools like AgentGuard [1] and Spendsafe.ai [6] implement this by setting spending caps that auto-terminate agents when exceeded.

**Tools:**
- **AgentGuard** — Auto-kills AI agents before they burn through budgets via eBPF-based runtime monitoring [1]
- **Spendsafe.ai** — Prevents wallet drainage through API call budgeting [6]
- **Tansive** — Sandboxes agent actions to prevent accidental production database restarts [5]

---

## Related Concepts

- [Agent Architecture Patterns](agent-architecture-patterns.md) — Architectural patterns for AI agents
- [Multi Agent Architecture](multi-agent-architecture.md) — Multi-agent system design in Hermes
- [Cron Scheduling](cron-scheduling.md) — Cron scheduling and automation workflows
- [Tool Loop Guardrails](tool-loop-guardrails.md) — Tool call loop guardrails
- [Interrupt And Fault Tolerance](interrupt-and-fault-tolerance.md) — Interrupt propagation and fault tolerance

---

## Open Research Questions

1. How to detect infinite loops in agent behavior without false positives? [2]
2. What are optimal circuit breaker thresholds for different agent types? [1][6]
3. Can we formalize safety guarantees for multi-agent systems? [4]
4. How to balance autonomy with resource constraints? [5][6]
5. What monitoring metrics best predict runaway behavior before it occurs? [3]

---

## References

[1] AgentGuard – Auto-kill AI agents before they burn through your budget (HN, 2025-07-31)  
[2] Inkog Report: Scanned 500 AI agent repos for bugs (HN, 2026-04-04)  
[3] Agent-triage – diagnosis of agent failures from production traces (HN, 2026-03-11)  
[4] AVE Database – Open taxonomy of 50 failure modes in multi-agent AI systems (HN, 2026-03-25)  
[5] Tansive – AI Agents that won't accidentally restart your prod database (HN, 2025-07-08)  
[6] Spendsafe.ai – Ship AI agents that can't drain your wallet (HN, 2025-11-17)  
[7] Cron Dedup Bug Report – Hermes Agent Incident (Internal, 2026-06-12)
