---
title: "Background Operations"
summary: "How the agent runs long-running tasks in the background while maintaining conversation — terminal processes, PTY sessions, checkpoint monitoring, and cron job patterns"
created: 2026-06-26
updated: 2026-06-26
type: concept
tags: [ai-ml, agent-system, agent-pattern]
sources:
  - type: web
    url: "https://hermes-agent.nousresearch.com/docs"
    title: "Hermes Agent Documentation"
    date: 2026-06-26
confidence: high
contested: false
---

## Overview

Background operations are how the agent runs long-running or reasoning-heavy tasks without blocking conversation. Unlike cron jobs (which fire independently and deliver results later), background processes stay tied to the current session — I can check progress, intervene mid-run, course-correct, and ask for decisions while you keep chatting about other things.[1]

## Three Patterns

### 1. Background Terminal + Process Polling

**For:** Mechanical long-running tasks with predictable output (data pipelines, bulk scraping, builds).

- Start: `terminal(background=True)` → returns a session ID
- Check progress: `process(action="poll")` for new output since last check
- Full history: `process(action="log", offset=N, limit=100)`
- Wait for completion: `process(action="wait", timeout=300)` blocks until done or timeout
- Stop: `process(action="kill")`

**Example workflow:**

```
User: "Run the news fetcher in background"
Agent: Starts terminal(background=True, command="python3 fetch_news.py")
       → Gets session_id: abc123
       → Tells user it's running, moves on to other topics
User (5 min later): "How's that going?"
Agent: process(action="poll", session_id="abc123")
       → Sees 47/100 articles fetched
       → Reports progress
```

**When to use:** The task is a single command or script, output flows linearly, no decisions needed mid-run.

### 2. PTY Background + Interactive Intervention

**For:** Tasks that require answering prompts, making choices, or navigating interactive CLIs.

- Same as pattern 1 but with `pty=True`
- Send input: `process(action="submit", data="y")` to answer yes/no prompts
- Send raw bytes (no newline): `process(action="write", data="\x03")` for Ctrl+C
- Close stdin: `process(action="close")` to signal EOF

**Example workflow:**

```
Agent: terminal(background=True, pty=True, command="pip install some-package")
       → Installer asks "Proceed? [Y/n]"
Agent: process(action="submit", data="y")
       → Installation continues
```

**Use cases:** Interactive installers, REPL sessions (Python, Node), step-by-step wizards, git rebase conflicts.

### 3. Checkpoint File + Periodic Polling

**For:** Reasoning-heavy multi-phase tasks where each phase needs evaluation before proceeding.

- Script writes progress markers to a file at each phase boundary
- Agent polls the checkpoint file between chatting with user
- If something fails or needs a decision, agent pauses and asks user
- Resume after user responds

**Example workflow (literature review pipeline):**

```
Phase 1: Search PubMed → write "phase1_complete: 23 papers found" to /tmp/checkpoint.json
Agent polls → sees phase 1 done → starts phase 2
Phase 2: Read abstracts → write "phase2_complete: 8 relevant" 
Agent polls → sees phase 2 done → asks user "8 papers look relevant, continue?"
User: "Yes"
Agent resumes → Phase 3: Full text analysis...
```

**When to use:** The task has multiple phases with decision points, or each phase produces output that needs human review before proceeding.

## Comparison with Cron Jobs

| Aspect | Background Process | Cron Job |
|--------|-------------------|----------|
| **Session context** | Tied to current conversation — I know what we're working on | Fresh session — no memory of current chat |
| **Intervention** | I can pause, ask questions, course-correct mid-run | Runs autonomously — no user present |
| **Progress checks** | User asks "how's that going?" anytime | Only delivers final result (or error) |
| **Duration** | Limited by session lifetime | Can run indefinitely across sessions |
| **Recurrence** | One-shot only | Supports schedules (daily, hourly, weekly) |

## Process Management Commands

### Starting a Background Process

```python
terminal(
    command="python3 long_script.py",
    background=True,           # Run in background
    timeout=600,               # Max seconds (foreground max: 600)
    workdir="/root/project",   # Working directory
    pty=False,                 # Interactive terminal?
    notify_on_complete=True,   # Auto-notify when done
)
```

### Checking Status

```python
# Quick progress check — returns new output since last poll
process(action="poll", session_id="abc123")

# Full log with pagination
process(action="log", session_id="abc123", offset=0, limit=200)

# Block until done (or timeout)
process(action="wait", session_id="abc123", timeout=300)

# List all background processes
process(action="list")
```

### Interactive Control

```python
# Answer a prompt (sends data + Enter)
process(action="submit", session_id="abc123", data="y")

# Send raw stdin without newline
process(action="write", session_id="abc123", data="\x03")  # Ctrl+C

# Close stdin / send EOF
process(action="close", session_id="abc123")

# Kill the process
process(action="kill", session_id="abc123")
```

## Pitfalls and Best Practices

### Watch Pattern Rate Limits

When using `watch_patterns` on background processes, there's a hard rate limit: **at most 1 notification per 15 seconds**. After 3 consecutive windows with dropped matches, watch patterns auto-disable. Use `notify_on_complete=True` instead for end-of-run markers like "DONE" or "PASS".[1]

### Cron Hallucination Prevention

The model (qwen3.6-27b-mtp) sometimes reports "ok" without actually executing scripts during cron jobs. Always add explicit file verification: `ls -la OUTPUT_FILE` or check line counts/timestamps before reporting success.[1]

### Session Lifetime

Background processes die when the session ends. For tasks that must outlive the current conversation, use cron jobs instead — they persist across sessions and can be scheduled to run at specific times.

### Parallel Background Processes

Multiple background processes can run simultaneously, each with its own session ID. Use `process(action="list")` to see all active processes and their states.

## When to Choose What

| Scenario | Pattern |
|----------|---------|
| 30-minute data pipeline | Background terminal + polling |
| Interactive installer | PTY background + submit |
| Multi-phase research with review points | Checkpoint file + periodic polling |
| Daily recurring task | Cron job |
| Task that must survive session end | Cron job |
| Quick script (< 1 minute) | Foreground terminal (no background needed) |

## Related Topics

[Agent Architecture Patterns](concepts/agent-architecture-patterns.md) — Agent Architecture Patterns: Pattern Categories
[Agentic Llm](concepts/agentic-llm.md) — Agentic LLM: AI agents operating in autonomous loops with tools
