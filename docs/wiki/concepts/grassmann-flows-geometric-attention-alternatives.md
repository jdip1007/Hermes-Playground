# Grassmann Flows & Geometric Attention Alternatives

**Date:** 2026-06-09
**Tags:** attention, geometry, manifold, transformer alternatives, sequence modeling

## Overview

The claim that "attention is not what you need" represents a growing research direction questioning whether explicit self-attention (Q×K^T softmax) is the fundamental ingredient for strong sequence models [8]. This deep dive covers the geometric/manifold-based alternative and related work.

---

## Core Paper: Attention Is Not What You Need (Zhang Chong, 2025) [1]

**arXiv:** 2512.19428
**Key Claim:** Self-attention is not fundamental — it's a special case of "tensor lifting" that can be replaced by Grassmann flows with linear scaling.

### Architecture: Causal Grassmann Mixing Layer [1]

Three key innovations:

1. **Dimensionality Reduction:** Token states reduced to low-dimensional space before interaction
2. **Subspace Encoding:** Local token pairs encoded as 2D subspaces on a Grassmann manifold (the set of all k-dimensional subspaces in R^n)
3. **Geometric Flow Dynamics:** Instead of computing an L×L attention weight matrix, the model evolves these subspaces through controlled geometric flows

### Key Insight: Attention as Tensor Lifting [1]

Zhang reinterprets self-attention as a particular instance of tensor lifting:
- Hidden vector mapped into high-dimensional space via outer products (Q⊗K)
- Softmax normalizes over this lifted representation
- This is NOT the only way to achieve pairwise token interaction

Grassmann flows achieve similar representational power by treating token pairs as subspaces rather than scalar weights, operating on a Riemannian manifold with O(n) complexity instead of O(n²).

### Results [1]

- **Wikitext:** Competitive perplexity with linear scaling
- **SNLI (NLI task):** Comparable accuracy to attention baselines
- Demonstrates that explicit L×L weight matrices are not necessary for strong performance

---

## Foundational Work on Grassmann Manifolds in Deep Learning

### Building Deep Networks on Grassmann Manifolds (Huang et al., 2016) [2]

**arXiv:** 1611.05742
**Authors:** Zhiwu Huang, Jiqing Wu, Luc Van Gool

First major attempt to generalize Euclidean deep learning to Grassmann manifolds:
- **Full-rank mapping layers:** Transform input Grassmannian data to more desirable representations
- **Re-orthogonalization layers:** Maintain manifold constraints during backpropagation
- Applied primarily to visual recognition tasks (subspace-based features)

**Connection to Zhang 2025:** Provides the mathematical toolkit for operating on Grassmann manifolds in neural networks — Zhang extends this from static feature representation to dynamic sequence modeling.

### Grassmannian Learning: Embedding Geometry Awareness (Zhang et al., 2018) [3]

**arXiv:** 1808.02229
**Authors:** Jiayao Zhang, Guangxu Zhu, Robert W. Heath, Kaibin Huang

Extended Grassmann manifold learning to both shallow and deep architectures:
- Subspace-structured features naturally expressed using Grassmann geometry
- Orthogonality constraints and low-rank objectives map cleanly to the manifold
- Demonstrated performance improvements in signal processing and NLP applications

**Key insight:** Many ML problems involve subspace distances, orthogonality constraints, or low-rank structures — all naturally expressed on Grassmann manifolds. This pre-dates Zhang 2025's application to attention replacement by several years.

---

## Related Geometric Attention Research

### Reorganizing Attention-Space Geometry (Gros, 2024) [4]

**arXiv:** 2407.18601
**Author:** Claudius Gros

Explores alternatives within the attention framework itself:
- Standard dot-product attention (DPA): Q^T K → large weights for parallel/antiparallel vectors
- **Expressive Attention (EA):** Uses (Q^T K)² — squared dot product
- Geometric interpretation: EA treats orthogonal queries and keys as equally relevant, breaking the parallelism bias of DPA

**Connection:** Shows that even within attention, the geometric choice of similarity metric matters. Zhang 2025 takes this further by abandoning scalar similarity entirely in favor of subspace geometry.

### Linear Attention with Global Context: Multipole Attention (Colagrande et al., 2025) [5]

**arXiv:** 2507.02748
**Authors:** Alex Colagrande, Paul Caillon, Eva Feillet, Alexandre Allauzen

Addresses O(n²) complexity while preserving global context:
- Multipole expansion technique from physics applied to attention
- Linear scaling with maintained long-range dependencies
- Applied to vision and physics simulation tasks

**Connection:** Another approach to escaping quadratic attention — uses physics-inspired approximations rather than manifold geometry.

### Native Hybrid Attention (Du et al., 2025) [6]

**arXiv:** 2510.07019
**Authors:** Jusen Du, Jiaxi Hu, Tao Zhang, Weigao Sun, Yu Cheng

Hybrid architecture combining linear and full attention:
- Long-term context maintained in key-value slots updated by linear RNN
- Short-term tokens augmented with full attention
- Unified layer design for intra & inter-layer hybridization

**Connection:** Pragmatic middle ground — keeps some attention while reducing quadratic cost. Contrasts with Zhang's complete elimination of explicit attention.

---

## The Broader Attention-Free Landscape

### SSM-Based Alternatives (for context) [7]

| Paper | Year | Approach | Complexity |
|-------|------|----------|------------|
| Mamba (Gu & Dao) | 2023 | Selective State Spaces | O(n) |
| RWKV | 2023 | Recurrent Transformer with KV cache | O(n) |
| BiGS (Wang et al.) | 2024 | SSM + Gating mechanism | O(n) |

These replace attention with recurrent state-space models. Zhang's Grassmann flows take a different path — geometric subspace dynamics rather than recurrence [1].

### Comprehensive Survey (Hays, 2026) [8]

**arXiv:** 2601.03329
Covers theoretical foundations, computational properties, and practical implementations of attention mechanisms across NLP, vision, and other domains. Useful for understanding the full landscape of attention variants.

---

## Why the Discrepancy? Synthesis

The "attention needed vs not needed" debate resolves when you recognize:

1. **Attention is a representation choice, not a necessity.** Zhang shows it's one instance of tensor lifting — subspace geometry on Grassmann manifolds achieves similar representational power differently.

2. **Scale matters.** Vaswani 2017 beat RNNs/LSTMs because those were weak baselines at the time. Modern SSMs with gating (Mamba, BiGS) and geometric approaches (Grassmann flows) are stronger competitors that didn't exist in 2017.

3. **Task dependency.** Attention excels at tasks requiring explicit token-to-token retrieval (QA, translation). Grassmann flows and SSMs compete on language modeling and classification but may lag on reasoning-heavy tasks where explicit attention patterns help interpretability.

4. **Complexity trade-off.** O(n²) attention → O(n) alternatives. The question is whether the linear approaches can match quality at scale (7B+ parameters), not just on small benchmarks like Wikitext or SNLI.

5. **Geometric unification.** Both attention and Grassmann flows operate in high-dimensional spaces — attention uses Euclidean dot products, Grassmann uses Riemannian manifold geometry. The latter may be more natural for certain data structures (subspace-structured features, hierarchical relationships).

---

## References

- Zhang Chong (2025). "Attention Is Not What You Need: Grassmann Flows as an Alternative to Self-Attention." arXiv:2512.19428
- Huang et al. (2016). "Building Deep Networks on Grassmann Manifolds." arXiv:1611.05742
- Zhang et al. (2018). "Grassmannian Learning: Embedding Geometry Awareness in Shallow and Deep Learning." arXiv:1808.02229
- Gros (2024). "Reorganizing attention-space geometry with expressive attention." arXiv:2407.18601
- Colagrande et al. (2025). "Linear Attention with Global Context: A Multipole Attention Mechanism for Vision and Physics." arXiv:2507.02748
- Du et al. (2025). "Native Hybrid Attention for Efficient Sequence Modeling." arXiv:2510.07019
- Gu & Dao (2023). "Mamba: Linear-Time Sequence Modeling with Selective State Spaces." arXiv:2312.00752
- Hays (2026). "Attention Mechanisms in Neural Networks." arXiv:2601.03329
