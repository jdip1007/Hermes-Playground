---
title: "DeepSeek-V4"
created: 2026-06-04
updated: 2026-06-04
type: entity
tags: [ai, llm, moe, deepseek]
sources:
  - type: paper
    url: "https://www.alphaxiv.org/abs/deepseek-v4"
    title: "DeepSeek-V4 Technical Report"
    authors: ["DeepSeek-AI"]
    date: "April 2026"
---

# DeepSeek-V4

## Overview

**DeepSeek-V4** is a family of Mixture-of-Experts (MoE) large language models released by DeepSeek-AI in April 2026 [1]. It introduces two variants — **V4-Pro** and **V4-Flash** — both featuring million-token context windows, hybrid attention mechanisms, and novel architectural innovations including Compressed Sparse Attention (CSA), Heavily Compressed Attention (HCA), and Manifold-Constrained Hyper-Connections (mHC) [1].

## Model Variants [1]

### DeepSeek-V4-Pro
- **Total parameters**: 1.6 trillion
- **Activated parameters per token**: ~49 billion
- **Context length**: 1 million tokens
- **Training tokens**: >32 trillion
- **Position**: Flagship model, competitive with top-tier proprietary LLMs

### DeepSeek-V4-Flash
- **Total parameters**: 284 billion
- **Activated parameters per token**: ~13 billion
- **Context length**: 1 million tokens
- **Training tokens**: >32 trillion
- **Position**: Cost-efficient variant for high-throughput inference

## Key Architectural Innovations [1]

### Compressed Sparse Attention (CSA) + HCA Hybrid
Combines two attention mechanisms:
- **CSA**: Selectively activates attention heads based on token importance, reducing computation while preserving long-range dependencies
- **HCA (Heavily Compressed Attention)**: Aggressively compresses attention for less critical tokens

### Manifold-Constrained Hyper-Connections (mHC)
A novel inter-layer connectivity pattern that constrains information flow along learned manifolds, improving gradient propagation and representation quality across the deep network [1].

### Muon Optimizer
A new optimizer designed for large-scale MoE training, featuring:
- Adaptive momentum correction tailored for sparse activation patterns
- Improved convergence stability on trillion-parameter models
- Reduced memory footprint compared to AdamW

## Training Details [1]

- **Training corpus**: >32 trillion tokens (multilingual)
- **Training framework**: Custom distributed training system optimized for MoE architectures
- **Expert routing**: Learned gating mechanism with load balancing regularization

## Performance Highlights [1]

Based on benchmark results reported in the technical paper, V4-Pro achieves competitive performance across:
- Standard LLM benchmarks (MMLU, GSM8K, HumanEval)
- Long-context understanding tasks (million-token range)
- Multilingual capabilities
- Code generation and reasoning

V4-Flash offers a favorable cost-performance tradeoff for production deployment [1].

## Related Concepts

- [[DeepSeek-V4-Pro]] — Flagship variant
- [[DeepSeek-V4-Flash]] — Cost-efficient variant
- [[Compressed Sparse Attention (CSA)]] — Hybrid attention mechanism
- [[Manifold-Constrained Hyper-Connections (mHC)]] — Inter-layer connectivity innovation
- Mixture-of-Experts (MoE) architecture
