---
title: "Compressed Sparse Attention (CSA)"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [ai, llm, attention-mechanism]
sources:
  - type: paper
    url: "https://www.alphaxiv.org/abs/deepseek-v4"
    title: "DeepSeek-V4 Technical Report"
    authors: ["DeepSeek-AI"]
    date: "April 2026"
---

# Compressed Sparse Attention (CSA)

## Overview

**Compressed Sparse Attention (CSA)** is a hybrid attention mechanism introduced in DeepSeek-V4 that selectively activates attention heads based on token importance, reducing computational cost while preserving long-range dependency modeling [1]. It works alongside **Heavily Compressed Attention (HCA)** to form a tiered attention system [1].

## Mechanism

### CSA + HCA Hybrid Architecture
The hybrid combines two complementary approaches:

1. **CSA (Compressed Sparse Attention)**: Activates a subset of attention heads for each token based on learned importance scores, maintaining high-fidelity attention for critical tokens while compressing less important ones [1].

2. **HCA (Heavily Compressed Attention)**: Applies aggressive compression to attention computation for tokens deemed less critical, using low-rank approximations and token pooling strategies [1].

### Key Design Principles
- **Selective activation**: Not all attention heads process every token equally — importance gating determines which heads engage fully vs. compressed mode [1]
- **Long-range preservation**: Critical long-distance dependencies are maintained even under compression [1]
- **Computational efficiency**: Reduces FLOPs significantly compared to dense attention, especially at million-token context lengths [1]

## Benefits

- Enables million-token context windows without quadratic attention cost explosion [1]
- Maintains competitive benchmark performance despite reduced computation [1]
- Complements MoE architecture by providing another layer of sparsity [1]

## Related Concepts

- [[DeepSeek-V4]] — Model family using CSA+HCA hybrid
- Mixture-of-Experts (MoE) architecture
- Sparse attention mechanisms in transformers
