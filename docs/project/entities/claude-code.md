---
title: "Claude Code"
created: 2026-06-05
updated: 2026-06-21
type: entity
tags: [ai-ml, agent-system, coding-tools]
sources:
  - type: web
    url: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works — Official Documentation"
    date: 2026-06-21
  - type: web
    url: "https://aiwiki.ai/wiki/claude_code"
    title: "Claude Code | AI Wiki"
    date: 2026-06-21
  - type: article
    url: "https://www.anthropic.com/research/claude-code-expertise"
    title: "Agentic coding and persistent returns to expertise — Anthropic Research"
    date: 2026-06-16
  - type: web
    url: "https://github.com/anthropics/claude-code"
    title: "Anthropic Claude Code GitHub Repository"
    date: 2026-06-21
  - type: analysis
    url: ""
    title: "Claude Code leaked source code analysis"
    date: 2026-06-05
confidence: high
contested: false
---

# Claude Code

Anthropic's agentic coding assistant — a terminal-native AI tool that reads files, edits code, runs commands, and autonomously works through development tasks [1][2]. First released as a beta research preview alongside Claude 3.7 Sonnet on February 24, 2025; made generally available May 22, 2025 [2]. Became Anthropic's fastest-growing product, reaching $1 billion annualized run rate in ~6 months and over $2.5 billion by February 2026 [2].

In a Pragmatic Engineer survey of 15,000 developers (January–February 2026), Claude Code earned a 46% "most loved" rating — highest of any AI coding tool, compared with 19% for Cursor and 9% for GitHub Copilot [2].

## Product Overview

### What It Is

Claude Code is an agentic coding system that operates across entire projects to understand codebases, execute multi-file changes, and complete development tasks autonomously [1][2]. Unlike code-completion assistants (GitHub Copilot inline suggestions) or IDE-integrated tools (Cursor), Claude Code runs primarily in the terminal as a REPL (Read-Eval-Print Loop) where developers describe tasks in plain English and Claude plans and executes the necessary steps [2].

### Key Differentiators

- **Terminal-native** — Runs in any terminal, composable with Unix philosophy, scriptable within existing workflows [2]
- **Full codebase understanding** — Reads entire project directories, understands cross-file dependencies without remote indexing servers [1][2]
- **Agentic autonomy** — Chains dozens of actions (read → edit → test → verify) autonomously while remaining interruptible by the user [1]
- **No setup overhead** — No additional servers, remote code indexing, or complex configuration required [2]

### Release Timeline

| Date | Version | Key Features |
|------|---------|--------------|
| 2025-02-24 | Beta (research preview) | Initial release with Claude 3.7 Sonnet [2] |
| 2025-05-22 | GA | General availability launch [2] |
| 2025-09-29 | v2.0 | Checkpoints for safe rollbacks, native VS Code extension, terminal v2.0 UX, Claude Agent SDK (formerly Claude Code SDK) [2] |
| 2025-Q4 | v2.1.0 | Hooks for agents and skills, hot reload for skills, session teleportation, language-specific output [2] |
| 2026-03 | — | Code Review (multi-agent PR analysis), Claude Code Security (vulnerability scanning), Channels (Telegram/Discord integration), voice mode, `/loop` recurring tasks, computer use on macOS, Enterprise Analytics API [2] |
| 2026-04 | — | Claude Opus 4.7 default model, native CLI binary, NO_FLICKER rendering engine, Focus View, `/ultraplan` cloud planning, vim visual modes, named themes, `/powerup` interactive learning [2] |
| 2026-05 | v2.1.139 | Agent View dashboard for managing background sessions, `/goal` command for outcome-based completion conditions, fast mode (`/fast`) with Opus 4.7 at ~2.5x speed [2] |
| 2026-05-28 | — | Claude Opus 4.8 default model — 4× less likely to let code flaws pass unremarked (3.7% vs 19.7% for Opus 4.7) [2] |

## Architecture

### The Agentic Loop

Claude Code's core architecture revolves around a three-phase agentic loop: **gather context → take action → verify results** [1]. These phases blend together — Claude uses tools throughout, whether searching files to understand code, editing to make changes, or running tests to check work [1].

The loop adapts to the task:
- A question about the codebase may only need context gathering
- A bug fix cycles through all three phases repeatedly
- A refactor involves extensive verification

Claude decides what each step requires based on what it learned from the previous step, chaining dozens of actions together and course-correcting along the way [1]. The user is part of this loop — interruptible at any point to steer Claude in a different direction [1].

### Models

Claude Code uses Claude models to understand code and reason about tasks. Multiple models available with different tradeoffs:
- **Sonnet** — Handles most coding tasks well, cost-effective for routine work
- **Opus** — Stronger reasoning for complex architectural decisions

As of May 2026, default model progression: Opus 4.6 → Opus 4.7 (April) → Opus 4.8 (May 28) [2]. Switch models with `/model` during a session or `claude --model <name>` at start [1].

Benchmark performance on agentic coding tasks:
- Opus 4.6: ~58% on CursorBench, baseline SWE-bench scores
- Opus 4.7: ~70% on CursorBench, 64.3% on SWE-bench Pro [2]
- Opus 4.8: 69.2% on SWE-bench Pro, 4× fewer unremarked code flaws vs predecessor [2]

### Tool System

Tools are what make Claude Code agentic — without them, Claude can only respond with text; with them, Claude acts [1]. Built-in tools fall into five categories:

| Category | Capabilities |
|----------|--------------|
| **File operations** | Read files, edit code, create new files, rename and reorganize [1] |
| **Search** | Find files by pattern, search content with regex, explore codebases [1] |
| **Execution** | Run shell commands, start servers, run tests, use git [1] |
| **Web** | Search the web, fetch documentation, look up error messages [1] |
| **Code intelligence** | See type errors/warnings after edits, jump to definitions, find references (requires code intelligence plugins) [1] |

Claude also has tools for spawning subagents, asking questions, and other orchestration tasks [1]. Claude chooses which tools to use based on the prompt and what it learns along the way — each tool use returns information that feeds back into the loop [1].

### Extensions Layer

Built-in tools form the foundation. Extensibility layer includes:
- **Skills** — Reusable workflow definitions for common patterns [1]
- **MCP (Model Context Protocol)** — Connect to external services and databases [1]
- **Hooks** — Automate workflows triggered by events [2]
- **Subagents** — Offload tasks to isolated agent sessions [1]

### Internal Architecture Patterns (from leaked source) [5]

Leaked source code revealed internal architecture patterns for memory management, subagent delegation, context compaction, and tool design [5]. See related pages: [Agent Memory Taxonomy](concepts/agent-memory-taxonomy.md), [Forked Agent Pattern](concepts/forked-agent-pattern.md), [Context Compaction Strategies](concepts/context-compaction-strategies.md), [Verification First Workflow](concepts/verification-first-workflow.md), [Output Filtering Strategies](concepts/output-filtering-strategies.md).

Key patterns identified:
- **Memory Management** — 4-type taxonomy (user/feedback/project/reference) with parallel extraction at session end [5]
- **Dream Pattern** — Background consolidation on time/session gate with orient → gather → consolidate → prune phases [5]
- **Forked Agent** — Subagents share parent's prompt cache but are isolated; parent trusts completion notifications without peeking [5]
- **Context Compaction** — Keeps system prompt, tools, recent messages, plan references; discards old tool results and intermediate steps [5]

## Core Features

### Codebase Understanding

When you run `claude` in a directory, Claude Code gains access to:
- **Your project** — Files in your directory and subdirectories, plus files elsewhere with permission [1]
- **Your terminal** — Any command you could run: build tools, git, package managers, system utilities [1]
- **Git state** — Current branch, uncommitted changes, recent commit history [1]
- **CLAUDE.md** — Project-specific instructions, conventions, and context loaded every session [1]
- **Auto memory (MEMORY.md)** — Learnings Claude saves automatically; first 200 lines or 25KB load at session start [1]

### Multi-file Operations

Claude can work across entire projects simultaneously:
- Read multiple files to understand cross-component dependencies
- Edit code in several files as part of a single task
- Run builds and tests to verify changes holistically
- Handle git workflows (commit, branch, merge) through natural language [2]

### Checkpoints

Introduced in v2.0 — safe rollback mechanism for experimental changes [2]. Allows developers to try risky modifications with confidence they can revert.

### Code Review

Launched March 2026 — multi-agent pull request analysis system [2]. Claude reviews PRs using multiple specialized agents that examine different aspects (security, style, correctness) in parallel.

### Security Scanning

Claude Code Security — vulnerability scanning integrated into the development workflow [2]. Identifies security issues and suggests fixes following codebase patterns.

### Channels Integration

Telegram and Discord integration allowing developers to interact with Claude Code through messaging platforms [2].

## Pricing and Access

### Subscription Plans (as of 2026)

| Plan | Price | Key Features |
|------|-------|--------------|
| **Free** | $0/mo | Limited access, no Claude Code [3] |
| **Pro** | $20/mo | Entry point for most developers; limited Claude Code access (historically included, now restricted) [4][5] |
| **Max** | $100–$200/mo | Full Claude Code access, Opus model usage, 20× message limits vs Pro [3][5] |

Claude Code used to be a feature of the $20/month Pro plan but is now exclusive to $100+/month plans following pricing changes in early 2026 [5]. Max subscribers have access to Opus models for complex tasks, while Sonnet 4.5 remains available on lower tiers [2].

### Usage Limits

- Message limits vary by plan (Max gets 20× Pro limits)
- Token-based billing for API usage
- Fast mode (`/fast`) delivers ~2.5x faster responses at higher per-token cost without changing model quality [2]

## Comparison with Alternatives

Claude Code competes in a crowded AI coding assistant market:

| Tool | Approach | Strengths | Weaknesses |
|------|----------|-----------|------------|
| **Claude Code** | Terminal-native agentic agent | Largest context window (1M tokens), highest SWE-bench scores (80.8% Verified), best for complex multi-file coding and large codebase understanding [6] | Slower than autocomplete tools, higher cost per session at volume [7] |
| **Cursor** | IDE-integrated agentic tooling | Best developer experience, pre-indexed semantic search on large monorepos, Supermaven autocomplete [6][8] | Stale index can be less accurate than live exploration for long sessions [9] |
| **GitHub Copilot** | Inline completion + chat | Lowest price for individuals, only genuinely useful free tier, established enterprise documentation (SOC 2, audit logs) [6][7] | Less autonomous; primarily autocomplete-focused rather than agentic |
| **Windsurf** | IDE with Cascade AI flows | Serious agentic IDE capability at lower cost [8] | Uncertain roadmap as of April 2026 [8] |
| **OpenAI Codex CLI** | Terminal agent (GPT-5.4/5.5) | Strong reasoning, OpenAI ecosystem integration | Newer product, less mature feature set |

Claude Code leads on benchmarks and autonomous multi-file operations; Cursor leads on developer experience and IDE integration [6][8]. GitHub Copilot wins on price for individuals [6]. For regulated industries, Copilot Enterprise has the most established compliance documentation [7].

## Security and Sandboxing

### Native Sandboxing

Introduced in v2.0 — OS-level enforcement that restricts filesystem and network access at the kernel level, not through permission prompts alone [10]. Provides a more secure environment for agent execution while reducing constant permission requests [11].

### Permission System

Three-tier model: **allow**, **ask**, and **deny** rules with project-level and managed settings [12]. Claude can request permissions to run commands, access files outside the project directory, or make network requests.

### Known Vulnerabilities

- **Sandbox bypass (2026)** — Critical security flaw allowed attackers to bypass network sandbox protections for an extended period, exposing developer credentials and source code [13][14]. Highlighted risks of integrating AI into core development workflows [14].
- **Windows WebDAV risk** — Anthropic recommends against enabling WebDAV or allowing Claude Code to access certain paths on Windows due to security implications [11]

### Enterprise Security

Enterprise Analytics API launched March 2026 provides usage monitoring and compliance reporting for organizations [2].

## Research Findings: Usage Patterns

Anthropic published a privacy-preserving analysis of ~400,000 Claude Code sessions from ~235,000 people between October 2025 and April 2026 [15]:

### Work Modes Distribution

Sessions classified into nine work modes:
- **Writing code**: 25% — Building something new
- **Fixing bugs**: 26% — Repairing broken functionality
- **Testing/Orchestrating**: 5% — Running tests, managing pipelines
- **Operating software**: 17% — Deploying, configuring, monitoring systems
- **Planning/Exploring**: 14% — Understanding existing systems, planning changes
- **Analysis/Prose**: 13% — Data analysis, documentation, presentations

### Key Findings

- Users spend an average of 20 hours per week using Claude Code [15]
- People make most planning decisions (what to do); Claude makes most execution decisions (how to do it) [15]
- Greater domain expertise → more work Claude does per instruction [15]
- Every major occupation succeeds at nearly the same rate as software engineers on coding tasks — success depends on problem understanding, not coding training [15]
- Debugging sessions fell by nearly half over 7 months; usage shifted toward end-to-end agentic use (deploying, analyzing data, writing documents) [15]
- Task value rose ~25% on average across all work types over the observation period [15]

### Implications

Domain expertise — not coding proficiency — amplifies effective tool use. The gap between intermediate and expert users is modest, suggesting domain proficiency alone enables nearly-expert-level agent direction [15]. This suggests agentic coding tools may absorb implementation-heavy work while rewarding workers with firm problem understanding [15].

## Limitations and Criticisms

### Performance Issues (March–April 2026)

Anthropic published a transparency postmortem on April 23, 2026 explaining three separate bugs that degraded Claude Code quality between March 4 and April 20, 2026 [2]. Usage limits were reset for all subscribers as remediation [2].

### Cost Concerns

- Higher per-session cost compared to autocomplete tools at volume [7]
- Pricing changes in early 2026 restricted Claude Code access from $20 Pro plan to $100+ plans, drawing criticism [5]
- Fast mode trades speed for higher per-token costs [2]

### Security Risks

- AI coding agents inherently execute commands on developer machines — sandbox bypass vulnerabilities demonstrate real credential exposure risks [13][14]
- Terminal access means Claude can run any command the user could run, including destructive operations if not properly constrained

### Context Window Limits

Despite 1M token context window, very large codebases may still exceed practical limits. Auto memory is capped at 200 lines or 25KB [1].

## Related Pages

- [Agent Memory Taxonomy](concepts/agent-memory-taxonomy.md) — 4-type classification system for agent memory management
- [Forked Agent Pattern](concepts/forked-agent-pattern.md) — Isolated subagent sessions sharing parent's prompt cache
- [Context Compaction Strategies](concepts/context-compaction-strategies.md) — Techniques for managing context window as scarce resource
- [Verification First Workflow](concepts/verification-first-workflow.md) — Run → Verify → Report evidence pattern
- [Output Filtering Strategies](concepts/output-filtering-strategies.md) — Reducing tool output before injecting into context
- [Agentic Llm](concepts/agentic-llm.md) — Broader discussion of agentic LLM systems
