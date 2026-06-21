---
title: "LLM Wiki Lint Workflow (brtrx)"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [ai-ml, agent-pattern]
sources:
  - type: web
    url: "https://gist.github.com/brtrx/ba595fd01e344d797cb66d34d982ecad"
    title: "CLAUDE.md — Lint Workflow Block"
    date: 2026-06-07
confidence: high
contested: false
---

# LLM Wiki Lint Workflow (brtrx)

A specific implementation of the lint operation for [Llm Wiki Pattern](concepts/llm-wiki-pattern.md), designed as a drop-in block for `CLAUDE.md`. Created by brtrx.

## Design Principle

Lint runs in **batches of 5 sources per session** to protect context window. Order is randomised (seed 42) — not alphabetical or ingestion-order — to counteract topic clustering and reveal cross-cutting connections that order-biased passes miss [1].

## State Files

- **`wiki/lint-status.md`** — Tracks which sources have been linted (`[ ]` unchecked, `[x]` checked). Randomised order stored here; must not be re-shuffled between sessions [1].
- **`wiki/lint-scratch.md`** — Accumulates findings from previous batches. Used to detect unresolved patterns across batches [1].

## Process (8 Steps)

1. Read `lint-status.md` → find next 5 unchecked sources (`[ ]`) [1]
2. Read `lint-scratch.md` → load prior batch findings, check for unresolved patterns [1]
3. For each source: read the source page, then read every entity/concept page it links to [1]
4. Append findings to `lint-scratch.md` under a new batch header [1]
5. After all 5 sources: re-read scratch entries, note **cross-cutting patterns** (e.g., same broken link in multiple sources = higher priority) [1]
6. Execute all fixes for the batch [1]
7. Mark 5 sources `[x]` in `lint-status.md`. Hub pages touched get `[~]` if not all contributing sources linted yet; promote to `[x]` only when complete [1]
8. Append one summary entry to `log.md` [1]

## Finding Categories

Seven categories used as headings in `lint-scratch.md`:

- **Broken wikilinks** — link target doesn't match any slug in the index [1]
- **Missing pages** — entity/concept linked inline but no page exists [1]
- **Stale sources lists** — concept/entity page's `sources:` frontmatter missing a source that links to it [1]
- **Stubs** — pages with thin content warranting expansion [1]
- **Contradictions** — claims conflicting across pages [1]
- **Stale claims** — things newer sources may have superseded [1]
- **Format issues** — frontmatter missing required fields, wrong link syntax [1]

## Key Differences from Standard Lint

Compared to the general lint approach described in [Llm Wiki Pattern](concepts/llm-wiki-pattern.md), this implementation adds:

- **Batched processing** (5 sources/session) instead of full-wiki scans
- **Randomised order** with persistent seed to avoid topic clustering bias
- **Two state files** (`lint-status.md`, `lint-scratch.md`) for tracking progress across sessions
- **Cross-cutting pattern detection** — explicitly looking for issues appearing in multiple sources as a priority signal
- **Hub page tracking** — `[~]` marker for pages touched but not fully linted

## Related Pages

- [Llm Wiki Pattern](concepts/llm-wiki-pattern.md)
