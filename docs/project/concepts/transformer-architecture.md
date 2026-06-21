---
title: "Attention Is All You Need — The Transformer Architecture"
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [ai-ml, architecture, attention, deep-learning]
sources:
  - type: paper
    url: "https://arxiv.org/abs/1706.03762"
    title: "Attention Is All You Need"
    authors: "Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin"
    venue: "NIPS 2017 (Advances in Neural Information Processing Systems)"
    date: 2017-06-12
confidence: high
contested: false
---

# Attention Is All You Need — The Transformer Architecture

## Overview

The seminal paper that introduced the **Transformer** architecture — the first sequence transduction model based entirely on attention mechanisms, dispensing with recurrence and convolutions[1]. Published at NIPS 2017 by eight researchers from Google Brain/Google Research[1]. This architecture became the foundation for all subsequent large language models (GPT, BERT, T5, etc.)[1].

## Key Innovation

Prior sequence transduction models relied on RNNs/LSTMs or CNNs with an encoder-decoder structure, optionally augmented with attention[1]. The Transformer replaces recurrence entirely with **multi-head self-attention**, enabling:

- **Full parallelization** within training examples (no sequential bottleneck)[1]
- **Constant path length** between any two positions (O(1) vs O(n) for RNNs)[1]
- **Significantly faster training** — 12 hours on 8 GPUs vs weeks for competitive models[1]

## Architecture Details

### Overall Structure

Encoder-decoder architecture, each composed of a stack of N = 6 identical layers[1].

**Encoder layer** (2 sub-layers)[1]:
1. Multi-head self-attention
2. Position-wise feed-forward network

**Decoder layer** (3 sub-layers)[1]:
1. Masked multi-head self-attention (prevents attending to future positions)
2. Multi-head encoder-decoder attention (queries from decoder, keys/values from encoder output)
3. Position-wise feed-forward network

Each sub-layer has a **residual connection** followed by **layer normalization**: `LayerNorm(x + Sublayer(x))`[1]. All sub-layers produce outputs of dimension d_model = 512[1].

### Scaled Dot-Product Attention

The core attention operation:

`Attention(Q, K, V) = softmax(QK^T / √d_k) V`

Where Q (queries), K (keys), V (values) are matrices[1]. The scaling factor `1/√d_k` prevents dot products from growing large in magnitude and pushing softmax into regions with vanishingly small gradients[1]. Under the assumption that query/key components are independent random variables with mean 0 and variance 1, their dot product has **mean 0 and variance d_k** — scaling maintains unit variance regardless of dimension[1].

### Multi-Head Attention

Instead of a single attention function with d_model-dimensional keys/values/queries, linearly project Q/K/V h times with different learned projections to dimensions d_k, d_k, d_v:

`MultiHead(Q,K,V) = Concat(head_1,...,head_h) W^O`

where `head_i = Attention(QW^Q_i, KW^K_i, VW^V_i)`[1]

In the base model: h = 8 heads, d_k = d_v = d_model / h = 64[1]. Total computational cost similar to single-head attention with full dimensionality[1]. Multi-head attention allows the model to **jointly attend to information from different representation subspaces at different positions** — something a single head would average away[1].

### Position-wise Feed-Forward Networks

Applied to each position separately and identically:

`FFN(x) = max(0, xW_1 + b_1)W_2 + b_2`

Two linear transformations with ReLU activation[1]. Input/output dimensionality d_model = 512, inner-layer d_ff = 2048[1]. Equivalent to two convolutions with kernel size 1[1].

### Positional Encoding

Since the model contains no recurrence or convolution, positional information must be injected explicitly[1]. The paper uses **sinusoidal encodings**:

`PE(pos, 2i) = sin(pos / 10000^(2i/d_model))`
`PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))`[1]

Wavelengths form a geometric progression from 2π to 10000·2π[1]. Key property: for any fixed offset k, PE_(pos+k) can be represented as a **linear function of PE_pos**, enabling the model to easily learn relative positions[1]. The authors experimented with learned positional embeddings and found nearly identical results, but chose sinusoidal because it may allow extrapolation to sequence lengths longer than those seen during training[1].

### Embeddings and Weight Sharing

Input/output tokens converted to vectors of dimension d_model via learned embeddings[1]. Same weight matrix shared between both embedding layers and the pre-softmax linear transformation (following Press & Wolf, 2016)[1]. Embedding weights multiplied by √d_model[1].

## Training Details

**Optimizer**: Adam with β₁=0.9, β₂=0.98, ε=10⁻⁹[1]

**Learning rate schedule**: Linear warmup for first 4000 steps, then decay proportional to inverse square root of step number:
`lr = d_model^(-0.5) · min(step_num^(-0.5), step_num · warmup_steps^(-1.5))`[1]

**Regularization**: Three types — residual dropout (0.1 for base model), label smoothing (ε_ls = 0.1), and embedding dropout[1].

**Hardware**: 8 NVIDIA P100 GPUs[1]. Base model: 100K steps / 12 hours[1]. Big model: 300K steps / 3.5 days[1].

## Results

| Model | EN-DE BLEU | EN-FR BLEU | Training Cost (FLOPs) |
|-------|-----------|-----------|----------------------|
| Transformer (base) | 27.3 [1] | 38.1 [1] | 3.3 × 10¹⁸ [1] |
| Transformer (big) | 28.4 [1] | 41.0 [1] | 2.3 × 10¹⁹ [1] |

The big model outperformed the best previously reported models **including ensembles** by over 2 BLEU on EN-DE, and established a new single-model state-of-the-art of 41.0 BLEU on EN-FR — at less than 1/4 the training cost of previous SOTA[1].

## Model Variations (Ablation Study)

Key findings from varying base model components:
- Reducing attention heads from 8 to 4 or increasing to 16/32 slightly hurts performance[1]
- Reducing d_k (attention key size) hurts quality — suggests dot product may not be the optimal compatibility function[1]
- Bigger models are better; dropout is very helpful in avoiding overfitting[1]
- Learned positional embeddings produce nearly identical results to sinusoidal[1]

## Complexity Comparison

| Layer Type | Complexity per Layer | Sequential Ops | Max Path Length |
|-----------|---------------------|----------------|----------------|
| Self-Attention | O(n²·d) [1] | O(1) — fully parallelizable [1] | O(1) — direct connections [1] |
| Recurrent (RNN/LSTM) | O(n·d²) [1] | O(n) — sequential bottleneck [1] | O(n) — must traverse intermediates [1] |
| Convolutional | O(k·n·d²) [1] | O(1) — parallelizable [1] | O(log_k(n)) — logarithmic depth [1] |

The O(1) path length of self-attention is crucial for learning long-range dependencies[1].

## Historical Significance

This paper introduced the architecture that became the universal backbone for:
- **GPT series** (autoregressive language models)[1]
- **BERT** (bidirectional encoders)[1]
- **T5, BART** (sequence-to-sequence models)[1]
- **Vision Transformers** (ViT — applying Transformer to images)[1]
- **Multimodal models** (CLIP, DALL-E)[1]
- Essentially every modern LLM[1]

The paper's title was initially seen as provocative — attention had been used alongside RNNs for years[1]. The claim that recurrence could be entirely eliminated was radical at the time[1]. The results proved it correct[1].

## Citation

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems 30 (NIPS 2017)*. arXiv:1706.03762[1].

## See Also

- [Attention Mechanisms Nn](concepts/attention-mechanisms-nn.md) — Comprehensive mathematical treatment of attention mechanisms
- [Compressed Sparse Attention Csa](concepts/compressed-sparse-attention-csa.md) — Sparse attention patterns reducing O(n²) complexity
- [Mixture Of Experts Moe](concepts/mixture-of-experts-moe.md) — MoE architecture for scaling models efficiently
- [State Space Models Ssm](concepts/state-space-models-ssm.md) — SSMs as an alternative to attention (Mamba, etc.)
- [Pretraining Without Attention Bigs](concepts/pretraining-without-attention-bigs.md) — BiGS: pretraining without attention
