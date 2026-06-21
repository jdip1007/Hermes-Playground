---
title: "Risk Ratios, Odds Ratios, and Hazard Ratios"
date: 2026-06-08
source: Email attachment (journal article)
authors: "Quentin F. Gronau, Garston Liang, Alexander Thorpe"
tags: [statistics, epidemiology, clinical-research]
---

## Risk Ratios, Odds Ratios, and Hazard Ratios

**Authors:** Quentin F. Gronau, Garston Liang, & Alexander Thorpe  
**Source:** Journal article (email attachment)

### Overview

Practical guide to interpreting three commonly reported measures in clinical studies: risk ratios (relative risk), odds ratios, and hazard ratios — with clear do's and don'ts for each.

### Key Measures

#### Risk Ratio (Relative Risk)
- **Definition:** Compares the probability of experiencing an event in two groups
- **Range:** 0 to infinity
- **Interpretation:** RR < 1 means exposure reduces risk; RR > 1 means exposure increases risk
- **Example:** In a lung cancer study, new drug group had 69.9% mortality vs 90.9% in standard treatment → RR = 0.77 (23% relative reduction)

#### Odds Ratio
- **Definition:** Compares the odds of experiencing vs not experiencing an event in two groups
- **Key limitation:** Overestimates risk ratio when outcome is common (>10%)
- **Rule:** Interpret OR as RR only when the risk of the event is low in both groups
- **Example:** Same study → OR = 0.23 (dramatically different from RR = 0.77)

#### Hazard Ratio
- **Definition:** Compares the instantaneous rate of experiencing an event in two groups at any point in time
- **Interpretation:** Treat as a risk ratio — HR < 1 means exposure group has lower hazard
- **Example:** Same study → HR = 0.5 (constant 2x reduction in death rate over time)

### Critical Distinctions

| Measure | What it compares | When to use |
|---------|------------------|-------------|
| Risk Ratio | Probability of event | Fixed follow-up, common outcomes |
| Odds Ratio | Odds of event vs non-event | Case-control studies, logistic regression output |
| Hazard Ratio | Instantaneous rate over time | Time-to-event data, varying follow-up durations |

### Common Misinterpretations

1. **Treating OR as RR when outcome is common** — leads to dramatic overestimation (0.23 vs 0.77 in the example)
2. **Confusing risk ratio with odds ratio** — they diverge significantly as event rates increase
3. **Ignoring time dimension of hazard ratios** — HR captures instantaneous rate, not cumulative probability

### Clinical Relevance

Essential reading for anyone interpreting clinical trial results or epidemiological studies. The paper uses a concrete lung cancer example to show how the same data produces three different numerical summaries depending on which measure is chosen. Understanding these distinctions prevents misinterpretation of treatment effect sizes in medical literature.

### Cross-References
[Sleep Regularity Mortality](concepts/sleep-regularity-mortality.md) — Uses hazard ratios for mortality prediction  
[Esbl Community Carriage Norway](concepts/esbl-community-carriage-norway.md) — Epidemiological study design  
[Enterobacter Spp Taxonomy Clinical Amr](concepts/enterobacter-spp-taxonomy-clinical-amr.md) — Clinical microbiology statistics
