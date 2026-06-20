---
title: "Muon Optimizer"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [ai, optimization, deep-learning]
sources:
  - type: paper
    url: "https://www.alphaxiv.org/abs/deepseek-v4"
    title: "DeepSeek-V4 Technical Report"
    authors: ["DeepSeek-AI"]
    date: "April 2026"
---

# Muon Optimizer

## Overview

**Muon** is a custom optimizer developed by DeepSeek-AI for training large-scale Mixture-of-Experts (MoE) models [1]. It was used to train the DeepSeek-V4 series on >32 trillion tokens, achieving stable convergence on trillion-parameter architectures [1].

## Key Features

### Adaptive Momentum Correction
Tailored momentum updates that account for sparse activation patterns in MoE models — different experts receive gradient updates at different frequencies, requiring specialized momentum handling compared to dense optimizers like AdamW [1].

### Convergence Stability
Designed to maintain training stability on extremely large parameter counts (V4-Pro: 1.6T total parameters) [1]. Addresses common issues with optimizer divergence in sparse architectures where only a fraction of parameters are active per forward pass [1].

### Memory Efficiency
Reduced memory footprint compared to standard AdamW, important for distributed training at trillion-parameter scale [1].

## Related Concepts

- [[DeepSeek-V4]] — Model family trained with Muon
- Mixture-of-Experts (MoE) training challenges
- Optimizer design for sparse neural networks
