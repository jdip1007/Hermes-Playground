---
title: "State-Space Models (SSMs) for Deep Learning"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [ai-ml, technique]
sources:
  - type: paper
    url: "https://arxiv.org/abs/2112.04484"
    title: "Pretraining Without Attention (BiGS)"
    date: 2021-12-09
  - type: paper
    url: "https://arxiv.org/abs/2111.00396"
    title: "S4: Efficiently Modeling Long Sequences with Structured State Spaces"
    date: 2021-11-01
  - type: paper
    url: "https://arxiv.org/abs/2206.11893"
    title: "On the Parameterization and Initialization of Diagonal State Space Models (S4D)"
    date: 2022-06-23
confidence: high
contested: false
---

# State-Space Models (SSMs) for Deep Learning

## Definition

State-space models are a class of sequence modeling architectures that describe the relationship between a continuous-time scalar input `u(t)` and output `y(t)` through differential equations:

```
x'(t) = Ax(t) + Bu(t),  y(t) = Cx(t) + Du(t)
```

Where `x(t)` is an N-dimensional hidden state, parameterized by matrices A ∈ R^(N×N), B ∈ R^(N×1), C ∈ R^(1×N), D ∈ R^(1×1). [1]

When discretized for sequence processing, this becomes a recurrence:
```
x_k = Ā x_(k-1) + B̄ u_k,  y_k = C x_k + D u_k
```

Critically, the linearity of this recursion allows outputs to be computed as a **convolution** with a precomputed kernel K ∈ R^L:
```
K = (CB, CAB, ..., CA^(L-1)B),  y = K * u
```

This means SSMs can be trained via backpropagation through the convolution without the serial bottleneck of RNNs and without the quadratic cost of attention. [1]

## Key Architectures

### HiPPO (Recurrent Memory with Optimal Polynomial Projections)

The foundational parameterization of matrix A that yields stable training. Gu et al. (2020) proposed a specific structure for A based on orthogonal polynomial projections, enabling the model to compress long input histories into fixed-size states. [1]

### S4 (Structured State Space)

Gu et al. (2021) demonstrated an effective approach for using SSMs in neural networks with HiPPO parameterization. S4 retains the ability to model long-term sequences while being more efficient than RNNs to train. Achieved strong results on speech generation and Long Range Arena benchmark, outperforming standard transformer architectures. [1]

### S4D (Diagonal State Space)

Simplified diagonalized version of S4 proposed by Gu et al. (2022) and Gupta (2022). Uses a simpler approximation of the original parameterization that achieves comparable results with reduced complexity. BiGS experiments found several S4 parameterizations performed similarly, settling on S4D for simplicity. [1]

## Computational Properties

**Complexity:** O(L) per token vs O(L²) for attention — linear scaling with sequence length. Each layer has only 2L static kernel values (forward + backward). [1]

**FLOP advantage grows nonlinearly with length:** At 128 tokens, BiGS shows slightly lower FLOPs than BERT. At 512 tokens, the gap widens noticeably. At 4096 tokens: BiGS 2.6E+12 vs BERT 4.1E+12 (37% reduction). [1]

**Practical speedup not yet realized:** Current implementations and hardware do not show theoretical benefits without specialized kernels. Related work by Dao et al. (2022, Mamba) considers specialized kernels for SSM computation. [1]

## Limitations Identified in BiGS Paper

- **SSMs alone underperform on NLP pretraining** — STACK/SSM scored 77.2 avg GLUE vs BERT's 83.3 (6 point gap). Static routing lacks the interaction capacity of attention.
- **Gating is essential** — Multiplicative gating restores representational capacity. GATED/SSM (BiGS) matched BERT at 83.3 avg. [1]
- **Bidirectional pretraining only** — Not tested on autoregressive language modeling. Some SSM benefits (RNN-based generation) less apparent in bidirectional settings.
- **No clear benefit on QA tasks** — WikiQA, TriviaQA showed no direct improvement over baselines. Specialized loss functions may require additional adaptation. [1]

## Relationship to Other Architectures

SSMs combine RNN-like long-range dependency modeling with CNN-like training speed. They differ from:

- **RNNs:** SSMs use linear recursion enabling parallel convolution computation; RNNs are inherently sequential
- **CNNs:** SSMs have global receptive fields through the state vector; CNNs require many layers for long-range dependencies
- **Transformers:** SSMs use static routing (input-independent kernel); attention uses dynamic pairwise interactions

See [Pretraining Without Attention Bigs](concepts/pretraining-without-attention-bigs.md) for the BiGS architecture that proved SSMs + gating can match BERT. [1]

## Current Status (2024-2026)

The core insight from BiGS — that SSMs need multiplicative gating to compensate for static routing — became foundational for subsequent architectures:

- **Mamba (Dao et al., 2023/2024):** Selective SSMs with input-dependent gating achieved competitive autoregressive language modeling
- **Jamba (AI21 Labs, 2024):** Hybrid transformer + Mamba architecture — validates BiGS finding that SSMs work best combined with other components
- **RWKV:** Linear-time attention mechanism achieving competitive results without quadratic complexity

Transformers remain dominant due to ecosystem maturity and multi-modal cross-attention patterns. However, as context windows grow beyond 100K tokens, O(L²) attention becomes structurally unsustainable even with flash attention optimizations — giving SSMs a long-term advantage for very-long-sequence applications.
