---
title: "LLM Wiki Pattern"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [ai-ml, agent-system]
sources:
  - type: web
    url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
    title: "LLM Wiki — Karpathy's gist"
    date: 2026-04-02
confidence: high
contested: false
---

# LLM Wiki Pattern

A pattern for building personal knowledge bases using LLMs, proposed by Andrej Karpathy. The core insight: instead of RAG (retrieving raw chunks on every query), the LLM incrementally builds and maintains a persistent, interlinked wiki that compounds over time.

## Core Idea

Most LLM-document systems use **RAG**: upload files, retrieve relevant chunks at query time, generate an answer. The problem: the LLM rediscover knowledge from scratch each time. No accumulation. Synthesizing five documents means finding and piecing together fragments every single query. NotebookLM, ChatGPT file uploads, and most RAG systems work this way [1].

The LLM Wiki pattern flips this: the LLM **compiles knowledge once** into a structured wiki of markdown files, then keeps it current as new sources arrive. Cross-references are pre-built. Contradictions are already flagged. Synthesis reflects everything ingested [1].

## Three-Layer Architecture

1. **Raw sources** — Immutable collection of source documents (articles, papers, images). The LLM reads but never modifies these. Source of truth [1].
2. **The wiki** — Directory of LLM-generated markdown files: summaries, entity pages, concept pages, comparisons. The LLM owns this layer entirely [1].
3. **The schema** — Configuration document (e.g., `CLAUDE.md`, `AGENTS.md`) that defines structure, conventions, and workflows. Co-evolved by human + LLM over time [1].

## Three Operations

### Ingest

Drop a new source into raw collection → LLM reads it, discusses takeaways, writes/updates wiki pages, updates index, appends to log. A single source may touch 10–15 wiki pages [1]. Can be done one-at-a-time with human involvement or batched with less supervision.

### Query

Ask questions against the compiled wiki. LLM searches relevant pages, reads them, synthesizes answers with citations. Key insight: **good answers can be filed back into the wiki as new pages** — comparisons, analyses, discovered connections compound in the knowledge base instead of disappearing into chat history [1].

### Lint

Periodic health-checks: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, important concepts lacking their own page, missing cross-references, data gaps fillable via web search [1]. See [Llm Wiki Lint Workflow](concepts/llm-wiki-lint-workflow.md) for a specific implementation.

## Indexing and Logging

- **index.md** — Content-oriented catalog: every page listed with link + one-line summary, organized by category. Updated on every ingest. Works at moderate scale (~100 sources, hundreds of pages) without embedding-based RAG infrastructure [1].
- **log.md** — Chronological append-only record of ingests, queries, lint passes. Consistent prefix format (`## [YYYY-MM-DD] action | Subject`) makes it parseable with unix tools [1].

## Why It Works

The maintenance burden of knowledge bases grows faster than their value for humans — updating cross-references, keeping summaries current, tracking contradictions across dozens of pages causes abandonment. LLMs don't get bored, don't forget cross-references, and can touch 15 files in one pass [1]. Maintenance cost approaches zero.

**Division of labor:** Human curates sources, directs analysis, asks good questions. LLM handles all bookkeeping — summarizing, cross-referencing, filing [1].

## Historical Context

Related to Vannevar Bush's **Memex** (1945): a personal, curated knowledge store with associative trails between documents. Bush's vision was private and actively curated, with connections as valuable as the documents themselves. The unsolved part was who does the maintenance — the LLM fills that gap [1].

## Tools and Ecosystem

- **Obsidian** — IDE for browsing the wiki (graph view, wikilinks, Dataview plugin) [1]
- **qmd** ([tobi/qmd](https://github.com/tobi/qmd)) — Local search engine for markdown with hybrid BM25/vector search + LLM re-ranking. CLI and MCP server [1]
- **Obsidian Web Clipper** — Browser extension converting web articles to markdown [1]
- **Marp** — Markdown-based slide deck format, usable directly from wiki content [1]
- **llm-wiki-compiler** ([atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler)) — Node.js CLI that compiles sources into concept wikis with the same Karpathy inspiration. Obsidian-compatible. Replaces agent judgment on page creation; tuned for small corpora [1]

## Use Cases

Personal knowledge management, research deep-dives, book companion wikis (like Tolkien Gateway), business/team internal wikis fed by Slack/meeting transcripts, competitive analysis, due diligence, course notes, hobby deep-dives — anything involving accumulating knowledge over time [1].

## Related Pages

- [Agent Architecture Patterns](concepts/agent-architecture-patterns.md)
- [Llm Wiki Lint Workflow](concepts/llm-wiki-lint-workflow.md)
