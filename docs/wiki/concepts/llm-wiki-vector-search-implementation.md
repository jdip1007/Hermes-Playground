---
title: "LLM Wiki Vector Search Implementation"
created: 2026-06-20
updated: 2026-06-20
type: concept
tags: [ai-ml, agent-system, technique]
sources:
  - type: paper
    url: "https://arxiv.org/abs/2005.11401"
    title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    date: 2020-05-22
  - type: paper
    url: "https://arxiv.org/abs/2310.11511"
    title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
    date: 2023-10-17
  - type: web
    url: "https://huggingface.co/BAAI/bge-small-en-v1.5"
    title: "BAAI/bge-small-en-v1.5 — Hugging Face Model Card"
    date: 2024-03-01
  - type: paper
    url: "https://arxiv.org/abs/2212.10496"
    title: "Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)"
    date: 2022-12-19
  - type: web
    url: "https://github.com/microsoft/GraphRAG"
    title: "From Local to Global: A Graph RAG Approach to Querying Summarized Knowledge"
    date: 2024-03-01
confidence: high
contested: false
---

## Overview

The LLM wiki at `/root/wiki/` uses a vector index for semantic search across its knowledge base of ~216 concept, entity, comparison, and query pages. The system embeds each page into 384-dimensional vectors using BAAI/bge-small-en-v1.5 (via fastembed/ONNX), then performs cosine similarity search at query time to find semantically relevant pages regardless of exact keyword matches.[1][2]

This implementation follows the RAG (Retrieval-Augmented Generation) pattern — offline embedding, online retrieval, grounded generation — adapted for a local wiki corpus with no external database dependencies. The vector index is maintained as a lightweight numpy array (~320 KB) alongside JSON metadata.

## RAG Technical Background

### Core Architecture

RAG augments an LLM's generation step with externally retrieved context rather than relying solely on parametric (pre-trained) knowledge.[1] Three stages:

**① Indexing (offline):** Documents are chunked (typically 500-2000 tokens per chunk, 10-20% overlap), each chunk embedded into a dense vector using an embedding model, and vectors + metadata stored in a vector database.

**② Retrieval (online):** User query is embedded using the same model as indexing. Similarity search finds top-K nearest neighbors via cosine similarity or inner product. Retrieved chunks are concatenated into context.

**③ Generation:** LLM receives `system prompt + retrieved context + user question` and generates an answer grounded in retrieved content, not just parametric memory.

### Embedding Models — The Critical Component

Retrieval quality depends almost entirely on the embedding model. Key properties:

- **bge-small-en-v1.5:** 384 dims, 512 max tokens, ONNX-compatible, strong MTEB score for size
- **text-embedding-3-small (OpenAI):** 1536 dims, 8191 max tokens, API-only, good general-purpose
- **E5-mistral-7b-instruct:** 4096 dims, 8192 max tokens, state-of-the-art on MTEB, requires GPU

Critical: the embedding model must use the same prompt template for queries and documents. BGE uses `"Represent this sentence for searching relevant passages: {query}"` for queries but just `"{document}"` for docs — mixing these up degrades retrieval by 15-30%.[2]

### Cosine Similarity Math

```
similarity(q, d) = (q · d) / (||q|| × ||d||)
```

Normalizes for magnitude — only direction matters. Most embedding models produce unit-normalized vectors anyway, so it reduces to a dot product. Scores above 0.75 typically indicate strong semantic matches; below 0.5 often means noise. Distribution depends on corpus domain and chunk size.

### Chunking Strategies

- **Naive fixed-size:** Split by N tokens with overlap. Simple but breaks at paragraph/topic boundaries
- **Semantic chunking:** Use sentence embeddings to detect topic shifts — split where cosine similarity between consecutive sentences drops below a threshold. More expensive, preserves coherence
- **Recursive character splitting (LangChain default):** Try paragraphs → sentences → words as fallback splitters

### Advanced RAG Patterns

**HyDE (Hypothetical Document Embeddings):** Generate a fake answer first, embed THAT instead of the query, retrieve against it.[3] Works because hypothetical answers use vocabulary closer to source documents than user questions. Improves retrieval by 10-20% on complex queries.

**Self-RAG:** The LLM generates "critique tokens" — special tokens deciding whether to retrieve, whether retrieved content is relevant, and whether the final answer is supported.[4] Adds a reflection loop but significantly reduces hallucination.

**Multi-query RAG:** Generate 3-5 paraphrased versions of the user query, retrieve for each, merge results. Catches vocabulary mismatches where different sources use different terms for the same concept.

**Reranking (two-stage retrieval):** Retrieve top-100 with fast embeddings, then rerank with a cross-encoder model (e.g., bge-reranker-large) that scores query-document pairs jointly. Cross-encoders are slower but 2-3× more accurate than bi-encoder similarity because they attend to both texts simultaneously.

**Graph RAG:** Build a knowledge graph from documents, retrieve subgraphs instead of flat chunks. Preserves entity relationships and enables multi-hop reasoning across sources.[5] Microsoft's implementation showed strong results on summarization tasks requiring synthesis across many documents.

### Failure Modes

- **Hallucination despite retrieval:** LLM ignores retrieved context → fix with stronger system prompt ("Answer ONLY using provided sources"), lower temperature
- **Retrieval misses relevant docs:** Embedding model doesn't capture domain vocabulary → fix with hybrid dense+sparse (BM25) search or domain-specific embedding fine-tuning
- **Context window overflow:** Too many chunks exceed LLM context limit → fix with aggressive reranking to top-3-5, or summarization before injection
- **Chunk boundary loss:** Key information split across two chunks → fix with larger chunk size + more overlap, or hierarchical retrieval

### Token Economics

Typical RAG pipeline costs: embedding query (~10 tokens input, negligible) + vector DB lookup (~$0.0001/query at scale) + LLM generation (retrieved context ~2-4K tokens + question ~50 tokens → answer). Retrieved context dominates token costs — a 3K-token context at $10/M input tokens = $0.03/query vs $0.006 without RAG. Tradeoff: accuracy improves by reducing hallucination ~40-70% on knowledge-intensive tasks.[1]

## Implementation Architecture

### Three-Phase Pipeline (This System)

**Indexing (offline):** Raw wiki pages embedded as `{title}\nTags: {tags}\n{body[:2048]}` — combining frontmatter metadata with the first 2048 characters of body text to capture both structural signals and content semantics while truncating long pages that would dilute signal.[3]

**Retrieval (online):** User queries embedded using the same model, cosine similarity computed against all stored vectors. Results above configurable threshold (default 0.65) returned ranked by score. Search runs in ~2 seconds including model load time on local hardware.

**Generation:** Retrieved pages read and synthesized into answers, either directly or via delegated subagents for token-efficient workflows.

### Embedding Model

- **Model:** BAAI/bge-small-en-v1.5
- **Dimensions:** 384
- **Runtime:** ONNX (via fastembed) — no PyTorch or GPU required
- **Max tokens:** 512
- **Memory:** Under 200 MB during inference

Chosen for strong MTEB performance relative to size and fully local execution.[3]

### Storage Format

Two files at `/root/wiki/`:

- `.vectors.npy` — numpy float32 array of shape (N × 384), where N is indexed page count (~320 KB for 216 pages)
- `.vector_meta.json` — JSON mapping each vector index position to file path, title, and metadata (model name, dimensions, build timestamp)

### Scripts

- **`.wiki_vectors.py`** — Build/update vector index. `python .wiki_vectors.py build` (full rebuild), `update <path>` (incremental). Processes pages in batches of 64 with progress reporting
- **`.wiki_search.py`** — Query the index. `python .wiki_search.py "query" --top 8 --threshold 0.65`. Outputs human-readable results and JSON for programmatic consumption

Both scripts use PEP 723 inline dependencies, runnable via `uv run` or direct Python execution.

## Performance Characteristics

### Indexing Speed

- Full rebuild (216 pages): ~30 seconds
- Single page update: <1 second per page
- Incremental updates preferred after individual changes; full rebuilds recommended after bulk operations (10+ pages)

### Query Latency

- First query in session: ~2 seconds (includes model load and cache warmup)
- Subsequent queries: ~0.5 seconds (model cached in memory)
- Cosine similarity over 216 vectors is negligible (<1ms); bottleneck is embedding the query text

### Token Savings via Delegation

When wiki searches are delegated to subagents, the main conversation context avoids loading index.md (~4K tokens), grep results, and intermediate page reads (~8-12K total). The subagent performs all file I/O in its isolated session and returns only a synthesized summary (~300-500 tokens) — saving approximately 60-80% of context tokens per wiki query.

## Threshold Guidance

| Threshold | Use Case | Expected Results |
|-----------|----------|------------------|
| 0.0 (default) | Broad exploration, no filtering | All pages ranked by similarity |
| 0.5 | General queries | Reasonable matches only |
| 0.65 | Default for wiki queries | Good precision/recall balance |
| 0.75+ | Specific technical questions | High confidence, fewer results |

Higher thresholds reduce noise but risk missing relevant pages with slightly different vocabulary. Lower thresholds increase recall at the cost of requiring more manual filtering.

## Integration with Wiki Workflow

### During Ingest

After creating or updating any wiki page, the vector index is updated via `python /root/wiki/.wiki_vectors.py update <path>`. Keeps semantic search results current without full rebuild. The llm-wiki skill documents this as step 7 in the ingest workflow.

### During Query

Recommended query flow combines both approaches:
1. Run vector search for semantic matches (catches paraphrases, related concepts)
2. Run grep (`search_files`) for exact keyword matches (catches specific terms, acronyms)
3. Merge results, deduplicate by path
4. Read top 5-8 combined results

### Skill Updates

The `llm-wiki` skill was updated to include vector index awareness: ingest step 7 runs the update command after page changes, query step 3 offers semantic search as a complement to grep, and a dedicated "Vector Index" section documents the system. A pitfall warning reminds agents to keep the index in sync with wiki changes.

## Limitations

### Embedding Granularity

Current approach embeds `title + tags + body[:2048]`. Works well for most pages (median ~100 lines) but truncates longer pages (>500 lines). The largest page (`messaging-gateway-architecture.md` at 1,087 lines) loses detail from its lower sections. Semantic chunking or section-level embeddings could improve coverage for long documents but add complexity.

### Vocabulary Mismatch on Domain-Specific Terms

The embedding model (bge-small-en-v1.5) is trained on general English corpora and may not capture domain-specific terminology well in bioinformatics, microbiology, or agent architecture contexts. Hybrid search combining dense vectors with sparse BM25 keyword matching would mitigate this but was not implemented to keep the system lightweight.

### No ANN Indexing

With only ~216 pages, brute-force cosine similarity is fast enough (~1ms). For larger wikis (10K+ pages), an approximate nearest neighbor index (HNSW, IVF-PQ) would be necessary for acceptable query latency.[1]

## Related Topics

[[llm-wiki]]
[[retrieval-augmented-generation]]
[[embedding-models]]
