---
title: "Pretraining Without Attention (BiGS) — Paper Analysis"
created: 2026-06-07
updated: 2026-06-07
type: concept
tags: [ai-ml, technique]
sources:
  - type: paper
    url: "https://arxiv.org/abs/2112.04484"
    title: "Pretraining Without Attention"
    date: 2021-12-09
confidence: high
contested: false
---

# Pretraining Without Attention (BiGS) — Paper Analysis

## Overview

**Paper:** Wang, Yan, Gu, Rush (Cornell/DeepMind), arXiv 2021.12 (published May 2022)
**Core Claim:** SSM-based routing + multiplicative gating can match BERT on GLUE without any attention layers.
**Key Finding:** First architecture to replicate BERT-level transfer learning results without attention.

## Architecture: BiGS (Bidirectional Gated SSM)

BiGS replaces self-attention with bidirectional SSM layers combined with a multiplicative gating mechanism. Two architectures tested:

### STACK/SSM (no gating)
- Replaces attention blocks with sequential forward + backward SSM layers
- Result: **77.2 avg GLUE** — catastrophic 6-point drop from BERT's 83.3
- Conclusion: Static SSM routing alone lacks sufficient interaction capacity

### GATED/SSM = BiGS (with gating)
- Bidirectional adaptation of gated unit (Hua et al., 2022)
- Three stages per layer: (1) gate computation via σ(W_v X), σ(W_f X), σ(W_b Flip(X)), (2) forward + backward SSM with multiplicative gate, (3) feed-forward with gating replacing traditional dense blocks
- Result: **83.3 avg GLUE** — matches BERT exactly at 11B tokens; improves to **85.8 avg** at full training (~97B tokens)

### Critical Insight
Multiplicative gating restores the interaction capacity that static SSM routing loses. The gate allows input-dependent modulation of SSM outputs, partially compensating for the absence of pairwise attention. [1]

## GLUE Results (Full Training ~97B tokens)

**BiGS GATED/SSM: 85.8 avg vs BERT's ~84-86 range** — same aggregate score but different per-task profile:

Where BiGS wins: RTE (79.4 vs 72), CoLA (64.4 vs 60.5) — syntactic reasoning and long-distance dependencies
Where BiGS loses: QQP (88.3 vs 92.7), MNLI (86.1 vs 86.7) — semantic similarity tasks

Same score, different inductive biases. [1]

## Long-Range Performance

BiGS extends to 4096 tokens natively since SSMs are O(L) not O(L²). No approximation needed.

**SCROLLS benchmark (encoder test):**
- BiGS 4096: QALT 32.8/31.7, CNLI 71.4 — competitive with LED and BART at same lengths
- Outperforms LED at all tested lengths on QALT task

**SQuAD 1.1 (adapted from 128→512 tokens):**
- BiGS: 89.5 F1 vs adapted BERT: 87.3 — outperforms when using same adaptation procedure
- Both underperform native 512-token BERT (90.9) [1]

## Syntactic Analysis — Different Inductive Biases

BiGS shows a more "stack-like" representation compared to BERT's global pairwise attention:

**Subject-verb agreement with attractors (Linzen et al., 2016):**
- BiGS consistently outperforms BERT as number of intervening attractors grows
- Sequential nature forces hierarchical processing rather than direct long-range matching

**CoLA syntactic categories:**
- BiGS outperforms BERT in 9/13 annotated syntactic phenomena categories
- Significantly better on two domains (subject-verb agreement, relative clauses)

**SSM kernel analysis reveals:**
- Early layers: local aggregation patterns (next word at layer 1, trigrams at layer 6)
- Deep layers: long-range future/past information (layers 14-17)
- Kernels adjust during fine-tuning — MNLI training causes long-distance kernels to expand scope outward [1]

## Gating Ablation — Why It Matters

**Adversarial QNLI test:** Distractor phrases inserted between hypothesis and premise to force models to skip irrelevant content.
- BiGS: 77.7% accuracy vs STACK/SSM: 69.7% — gating enables long-distance interaction generalization [1]

**Length-binned QNLI accuracy:**
- STACK/SSM degrades sharply as sequence length increases
- BiGS and BERT maintain stable performance across lengths
- Gating helps SSM generalize to variable-length textual input [1]

## FLOP Analysis

| Length | BiGS FLOPs | BERT FLOPs | Gap |
|--------|-----------|-----------|-----|
| 128 | 8.1E+10 | 7.9E+10 | Marginal advantage |
| 512 | 3.2E+11 | 3.4E+11 | Noticeable gap |
| 1024 | 6.5E+11 | 7.2E+11 | Widening |
| 4096 | 2.6E+12 | 4.1E+12 | 37% reduction |

Theoretical advantage grows nonlinearly with sequence length. Paper honestly notes: *"current implementations and hardware do not yet show this benefit."* [1]

## Limitations (from paper)

- Bidirectional pretraining only — no autoregressive language modeling tested
- English-only corpus, no multilingual evaluation
- No direct benefit on QA benchmarks (WikiQA, TriviaQA)
- Specialized loss functions may require additional adaptation for SSM training [1]

## How Claims Held Up (2024-2026 Retrospective)

**Validated:**
1. "SSMs need gating" — Confirmed by Mamba (selective SSMs), Jamba, and all subsequent SSM architectures incorporating input-dependent gating as their core innovation
2. "Different inductive biases" — Confirmed: SSM models excel at sequential/structural tasks; transformers dominate semantic similarity and multi-modal cross-attention
3. "Long-range without approximation" — Confirmed: SSM-based models genuinely handle long sequences more efficiently than attention
4. "FLOP advantage is real but unrealized in practice" — Confirmed: theoretical benefit exists, specialized kernels needed for practical speedup

**Partially validated:**
5. "SSMs can match transformers on NLP pretraining" — True for MLM/bidirectional tasks; autoregressive language modeling still favors transformers or hybrid architectures (Jamba)

**Not yet proven:**
6. "SSMs could be pretrained fully on much longer sequences" — Not demonstrated at scale beyond 4096 tokens in this work
7. Multilingual SSM pretraining — Still unexplored [1]

## Significance

BiGS proved the fundamental question: *"Is attention necessary for pretraining?"* Answer: No, but you need gating to compensate for what static routing loses. This opened architectural space beyond transformers and directly influenced the Mamba/Jamba lineage of selective SSM architectures.

See [State Space Models Ssm](concepts/state-space-models-ssm.md) for SSM background and technical details. [1]
