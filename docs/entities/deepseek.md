---
title: "DeepSeek"
created: 2026-06-04
updated: 2026-06-04
type: entity
tags: [ai, llm, company]
sources:
  - type: paper
    url: "https://www.alphaxiv.org/abs/deepseek-v4"
    title: "DeepSeek-V4 Technical Report"
    authors: ["DeepSeek-AI"]
    date: "April 2026"
---

# DeepSeek (DeepSeek-AI)

## Overview

**DeepSeek** is an AI research company known for developing open-weight large language models[1]. The organization has released multiple model families including the DeepSeek-V4 series (April 2026), featuring Mixture-of-Experts architectures with novel attention mechanisms and training optimizations[1].

## Model Family

### DeepSeek-V4 Series (April 2026)
- **DeepSeek-V4-Pro**: 1.6T total / 49B activated parameters, million-token context[1]
- **DeepSeek-V4-Flash**: 284B total / 13B activated parameters, million-token context[1]

Key innovations in V4:
- Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) hybrid[1]
- Manifold-Constrained Hyper-Connections (mHC)[1]
- Muon optimizer for large-scale MoE training[1]
- Trained on >32 trillion tokens[1]

## Related Concepts

- [[DeepSeek-V4]] — V4 model family overview
- [[Compressed Sparse Attention (CSA)]] — Hybrid attention mechanism
- [[Manifold-Constrained Hyper-Connections (mHC)]] — Inter-layer connectivity innovation
