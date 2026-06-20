---
title: "Andrej Karpathy"
created: 2026-06-07
updated: 2026-06-07
type: entity
tags: [person, ai-ml]
sources:
  - type: web
    url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
    title: "LLM Wiki — Karpathy's gist"
    date: 2026-04-02
confidence: high
contested: false
---

# Andrej Karpathy

AI researcher and engineer. Former Director of AI at Tesla (autonomous driving). Known for contributions to computer vision, neural network visualization, and LLM education.

## Key Contributions

- **LLM Wiki pattern** — Proposed the persistent compounding knowledge base approach using LLMs as wiki maintainers instead of RAG systems [1]. The pattern defines three layers (raw sources, wiki, schema) and three operations (ingest, query, lint).
- **Computer vision at Tesla** — Led Tesla's autonomous driving vision team. Pioneered end-to-end neural network approaches for self-driving perception and planning.
- **Neural network visualization** — Created widely-used tools for understanding deep learning models internally.

## LLM Wiki Pattern

Karpathy's 2026 gist describes the core idea: instead of RAG (retrieving raw chunks on every query), have the LLM incrementally build and maintain a persistent wiki of interlinked markdown files. The knowledge compiles once and stays current, with cross-references pre-built and contradictions flagged [1].

See [Llm Wiki Pattern](../concepts/llm-wiki-pattern.md) for full details.

## Related Pages

- [Llm Wiki Pattern](../concepts/llm-wiki-pattern.md)
- [Agent Architecture Patterns](../concepts/agent-architecture-patterns.md)
