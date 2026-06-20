---
title: "Mixture-of-Experts (MoE)"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [ai, llm, neural-network-architecture]
sources:
  - type: paper
    url: "https://www.alphaxiv.org/abs/deepseek-v4"
    title: "DeepSeek-V4 Technical Report"
    authors: ["DeepSeek-AI"]
    date: "April 2026"
---

# Mixture-of-Experts (MoE) Architecture

## Overview

**Mixture-of-Experts (MoE)** is a neural network architecture pattern where the model contains multiple specialized sub-networks ("experts"), and a gating mechanism routes each input to a subset of experts [1]. This enables scaling total parameter count while keeping per-token computation constant [1].

## Key Characteristics

### Sparse Activation
Only a fraction of total parameters are activated for each token:
- **DeepSeek-V4-Pro**: 1.6T total / 49B activated (~3% activation ratio) [1]
- **DeepSeek-V4-Flash**: 284B total / 13B activated (~4.6% activation ratio) [1]

### Benefits
- **Scalability**: Total model capacity grows without proportional compute cost increase [1]
- **Specialization**: Different experts learn to handle different types of inputs or tasks [1]
- **Cost efficiency**: Inference cost determined by activated parameters, not total count [1]

### Challenges
- **Load balancing**: Ensuring experts are utilized evenly during training [1]
- **Communication overhead**: Distributed training requires expert routing across devices [1]
- **Optimizer adaptation**: Standard optimizers (AdamW) struggle with sparse update patterns — specialized optimizers like [[Muon Optimizer]] address this [1]

## Related Concepts

- [[DeepSeek-V4]] — Uses MoE architecture
- [[Compressed Sparse Attention (CSA)]] — Complementary sparsity mechanism
- [[Muon Optimizer]] — Optimizer designed for MoE training
