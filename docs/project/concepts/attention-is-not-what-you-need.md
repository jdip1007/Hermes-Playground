---
title: "Attention Is Not What You Need — Paper Analysis"
created: 2026-06-09
updated: 2026-06-09
type: concept
tags: [ai-ml, architecture, attention-free]
sources:
  - type: paper
    url: "https://arxiv.org/abs/2512.19428"
    title: "Attention Is Not What You Need"
    authors: "Zhang Chong"
    date: 2025-12-22
confidence: high
contested: false
---

# Attention Is Not What You Need — Paper Analysis

## Overview

**Paper:** Zhang Chong, arXiv Dec 2025 (updated Jun 2026)
**Core Claim:** Explicit self-attention is not necessary for strong performance and reasoning. Proposes Grassmann flows as an attention-free alternative.
**Key Finding:** Purely Grassmann-based models achieve perplexities within 10-15% of size-matched Transformers on Wikitext-2.

## Architecture: Causal Grassmann Layer

Instead of forming an L×L attention matrix, the architecture uses geometric operations on manifolds:

### Three-stage process per layer:
1. **Linear reduction** — token states are linearly reduced to lower dimensionality
2. **Grassmann encoding** — local token pairs encoded as 2D subspaces on Grassmann manifold via Plücker coordinates
3. **Gated mixing** — geometric features fused back into hidden states through gated mixing

### Key insight:
Information propagates by controlled deformations of low-rank subspaces over multi-scale local windows. Core computation lives on a finite-dimensional manifold rather than in an unstructured tensor space. [1]

## Results

### Wikitext-2 language modeling:
- Grassmann models (13-18M params): validation perplexity within 10-15% of size-matched Transformers
- Competitive performance without any attention mechanism [1]

### SNLI natural language inference:
- Grassmann-Plücker head on DistilBERT: **0.8550 val / 0.8538 test accuracy**
- Transformer head baseline: **0.8545 val / 0.8511 test accuracy**
- Slight outperformance on inference task [1]

## Theoretical Framework

### Attention as tensor lifting:
Paper argues standard multi-head attention is best seen as tensor lifting — hidden vectors mapped into high-dimensional space of pairwise interactions, learning proceeds by constraining this lifted tensor through gradient descent. Extremely expressive but mathematically opaque after many layers. [1]

### Grassmann advantage:
- Linear scaling in sequence length for fixed rank (vs O(L²) for attention)
- More structured route toward geometric and invariant-based interpretations of neural reasoning
- Computation on finite-dimensional manifold vs unstructured tensor space [1]

## Complexity Comparison

| Aspect | Transformer Attention | Causal Grassmann |
|--------|----------------------|------------------|
| Sequence scaling | O(L²) | O(L) for fixed rank |
| Computation space | Unstructured tensor | Finite-dimensional manifold |
| Interpretability | Low (opaque after many layers) | Higher (geometric invariants) |

## Limitations

- Only tested on small benchmarks (Wikitext-2, SNLI) — not evaluated at scale
- 10-15% perplexity gap remains vs Transformers
- No evaluation on autoregressive generation beyond language modeling
- Not compared to other attention-free architectures (Mamba, RWKV, BiGS) [1]

## Relationship to Other Attention-Free Work

This paper joins a growing lineage questioning attention's necessity:

- **BiGS (Wang et al., 2021):** SSM + gating matches BERT on GLUE without attention
- **Mamba (Gu & Dao, 2023):** Selective SSMs for autoregressive LM
- **RWKV:** Linear-time recurrent architecture
- **This paper (Zhang, 2025):** Grassmann manifold-based approach

Different approaches, same conclusion: attention is not strictly necessary. [1]

## Significance

Directly challenges the foundational assumption of "Attention Is All You Need" (Vaswani et al., 2017). Provides theoretical framework for why attention works (tensor lifting) and proposes geometric alternative with better interpretability properties. Small-scale results promising but need large-scale validation. [1]

## See Also

- [Transformer Architecture](concepts/transformer-architecture.md) — Original "Attention Is All You Need" paper
- [Pretraining Without Attention Bigs](concepts/pretraining-without-attention-bigs.md) — BiGS: SSM-based attention-free pretraining
- [State Space Models Ssm](concepts/state-space-models-ssm.md) — SSM architectures (Mamba, etc.)
