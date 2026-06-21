---
title: "Agentic Search — Retrieval Strategies in LLM Agent Systems"
created: 2026-06-09
updated: 2026-06-09
type: concept
tags: [ai-ml, agent-system]
sources:
  - type: paper
    url: "https://arxiv.org/abs/2605.15184"
    title: "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"
    date: 2026-05-14
confidence: high
contested: false
---

# Agentic Search — Retrieval Strategies in LLM Agent Systems

## Overview

Agentic search refers to the process by which an LLM agent identifies, executes, and consumes search operations over a corpus to answer user queries. Unlike standalone retrieval pipelines (fixed query → top-k results → prompt), agentic retrieval is **iterative and agent-directed**: the model decides what to search for, how many queries to issue, and whether retrieved results are sufficient or require refinement [1].

## Two Design Dimensions

End-to-end effectiveness is jointly determined by:

### 1. Retrieval Strategy

Three broad categories [1]:

- **Lexical Search** — Exact or pattern-based matching over raw text (grep, BM25, regex). No embedding model needed; negligible computational cost beyond the scan. BM25 remains competitive on BEIR benchmarks, often outperforming early dense retrieval in zero-shot settings [1]. SPLADE extends lexical matching with learned vocabulary expansion [1].
- **Semantic (Dense) Search** — Encodes queries and documents as dense vectors in a shared embedding space; retrieves nearest neighbors via ANN search. Established by Dense Passage Retrieval (DPR). Excels at paraphrase handling but depends on embedding model quality, vector index infrastructure, and indexing latency [1].
- **Hybrid Approaches** — Combine lexical and semantic signals. Reciprocal Rank Fusion (RRF) merges ranked lists without score calibration. ColBERT computes token-level similarity between query and document representations. Lexical and semantic methods often retrieve different relevant documents, making their combination more effective than either alone [1].

### 2. Agent Harness

Two classes of harnesses differ in control over the tool-calling loop [1]:

- **Custom Harnesses** — Built using agent frameworks or SDKs (e.g., LangChain). Fine-grained control over system prompt, tool definitions, context construction, result formatting, and iteration termination. Enable domain-specific optimizations like dynamic prompting and result truncation policies. Tradeoff: significant engineering overhead [1].
- **Provider-Native CLI Harnesses** — Embed tool calling into a shell-based interface (Claude Code, Codex, Gemini CLI). Model has direct access to system utilities (grep, find, cat) as native tool actions. Minimal setup cost; provider-managed context engineering. Sacrifice fine-grained control [1].

### 3. Tool-Calling Architecture

Orthogonal to harness choice — governs how retrieval results are delivered to the model [1]:

- **Standard (Inline)** — Results returned directly as tool response messages appended to conversation context. Simple; no intermediate step between fetching and generation. Large result sets compete for context window space, creating "context rot" that degrades long-horizon performance [1].
- **Programmatic (File-Based)** — Results written to disk; model receives a file path or summary pointer. Agent must explicitly read/search the file. Decouples retrieval size from context pressure; enables progressive disclosure and agent-driven post-retrieval filtering. Tradeoff: additional tool call adds latency; requires model to understand file-based workflow [1].

## Key Empirical Findings (Sen et al., 2026)

Evaluated on LongMemEval-S (116 questions, 6 categories) across Chronos (custom harness), Claude Code, Codex CLI, and Gemini CLI with five models: Claude Opus 4.6, Claude Haiku 4.5, GPT-5.4, Gemini 3.1 Pro, Gemini 3.1 Flash-Lite [1].

### Experiment 1: Retrieval Mode × Harness × Tool Calling

**Inline delivery**: Lexical search (grep) uniformly outperformed dense retrieval for every harness-model pair. Largest margin: Chronos + Gemini Flash-Lite (86.2% vs 62.9%). Narrowest: Claude Code + Opus 4.6 (76.7% vs 75.0%) [1].

**Programmatic delivery**: Reordered the comparison — vector exceeded grep on 5 of 10 harness-model pairs. Sharpest regression: Codex/GPT-5.4 dropped from 93.1% (inline grep) to 55.2% (programmatic grep) [1].

### Experiment 2: Scaling with Increasing Noise

Progressively mixed in unrelated conversation history (s5 → s10 → s20 → s30 → full, where full = 39-66 sessions per item). Key findings [1]:

- Grep accuracy is **not monotone** — Chronos Opus rises to 90.5% at s20, dips to 85.3% at s30, reaches 89.7% at full
- Vector often stronger at low session counts; crossover depends on harness and backbone, not corpus size alone
- Dense retrieval tends to explore embedding space neighborhoods (recovers indirect mentions but admits topical false friends as sessions accumulate)
- Lexical retrieval exploits surface cues — brittle to phrasing but ruthlessly precise when the agent discovers a discriminative pattern

## Interpretation

1. **LongMemEval rewards literal witness recovery** — exact dates, counts, preferences that remain stable under tokenization. Grep surfaces these without an embedding bottleneck [1].
2. **"Retrieval" is really retrieval-plus-orchestration** — the harness shapes system prompts, tool descriptions, and how hits are rendered back into chat. Moving Claude Opus 4.6 between Chronos (93.1%) and Claude Code (76.7%) shifts accuracy as much as swapping retrievers [1].
3. **Programmatic delivery is a tool-use stress test** — changes the task from "read the tool message" to "locate, open, and integrate an artifact." When that second stage is brittle, accuracy collapses independently of retrieval quality [1].
4. **Weaker models suffer more with dense retrieval** — Claude Haiku 4.5 on Claude Code showed especially large grep-vector gaps (55.2% vs 44.0% inline), plausibly because weaker models are less consistent at iterative query refinement and reranker-aware reading [1].

## Limitations

Conclusions tied to long-memory conversational QA grounded in multi-session chat, explicit time expressions, and personal/user facts. In domains where evidence is rarely literal (scientific synthesis over paraphrased abstracts, visual-heavy documents, code semantics), dense retrieval and hybrid routing may perform differently [1].

## Related Concepts

- [Agent Architecture Patterns](concepts/agent-architecture-patterns.md) — Broader patterns for agent system design
- [Context Compaction Strategies](concepts/context-compaction-strategies.md) — Managing context window pressure in long-horizon tasks
- [Llm Wiki Pattern](concepts/llm-wiki-pattern.md) — Knowledge base pattern that uses retrieval as a core mechanism
