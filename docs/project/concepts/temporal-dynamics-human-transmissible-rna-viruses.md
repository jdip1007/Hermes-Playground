# Temporal Dynamics, Discovery, and Emergence of Human-Transmissible RNA Viruses

> **Citation:** Lu L, Zhang F, Brierley L, Robertson G, Chase-Topping M, Lycett S, Woolhouse M. "Temporal Dynamics, Discovery, and Emergence of Human-Transmissible RNA Viruses." *Molecular Biology and Evolution* 41(1): msad272 (2024). DOI: [10.1093/molbev/msad272](https://doi.org/10.1093/molbev/msad272)
> **Authors:** Lu Lu*, Feifei Zhang, Liam Brierley, Gail Robertson, Margo Chase-Topping, Samantha Lycett, Mark Woolhouse (University of Edinburgh, Peking University, University of Liverpool, Biomathematics and Statistics Scotland)
> **Published:** January 18, 2024 | Open Access

## Overview

This study uses phylogenetic analysis of 1,408 genome sequences from 743 distinct RNA virus species/types across 59 genera to investigate how temporal changes in virus discovery — particularly the accelerating discovery of nonhuman viruses — have reshaped our understanding of human infectivity and transmissibility evolution. By censoring datasets by virus discovery date in 10-year steps back to the early 20th century, the authors reveal three major trends: (1) increasing proportion of genera with nonhuman-infective ancestral states, (2) growing fraction of purely human-transmissible or strictly zoonotic lineages vs. mixed lineages, and (3) more human viruses now having nearest relatives that do not infect humans.

## Key Findings

### Dataset Composition
- **1,408 representative genome sequences** from 743 distinct RNA virus species/types in 59 genera across 24 families
- **260 species/types (35%)** can infect humans:
  - **162 strictly zoonotic (L2)** — infect humans but don't spread within human populations; 281 sequences (87 from humans, 194 nonhuman)
  - **98 human-transmissible (L34)** — can spread within human populations; 314 sequences (167 from humans, 147 nonhuman)
  - Remaining 813 sequences are L1 viruses (nonhuman only)

### Discovery Rate Trends
- L2 and L34 species/types accumulated at average rates of **1.9/yr** and **1.2/yr** since 1938
- Nonhuman L1 virus discovery has accelerated dramatically in the past 2 decades
- **Slowdown in higher-level taxonomic diversity**: 50% of genera/families containing L2/L34 viruses were known by 1976–1994 — suggesting most extant human RNA viruses may already be discovered

### Phylogenetic Ancestral State Analysis
- Most likely ancestral state is **L1 (nonhuman) for 85% of genera** (expected value: 70%)
- Both absolute number and proportion of genera with L1 ancestral states have **increased markedly over time** as more nonhuman viruses were discovered
- Over the last 20 years, the absolute number of genera with most likely L2 or L34 ancestral states has **declined**

### Lineage Classification (n=149 distinct human virus lineages)
| Type | Count | Description |
|------|-------|-------------|
| Strictly zoonotic only | 79 (53%) | Contain only L2 species/types |
| Human-transmissible only | 58 (39%) | Contain only L34 species/types |
| Mixed (L2 + L34) | 12 (8%) | Contain both L2 and L34 |

- **74% of lineages** contain just a single human virus species/type
- Human transmissibility has independently evolved on at least **70 occasions** across diverse taxa
- In at least **15 genera and 14 families**, human transmissibility evolved more than once
- Mixed lineages: 92% enveloped, 33% vector-borne

### Temporal Shift in Nearest Relatives
- At discovery time, L34 viruses were **3.9× more likely** to have an L34 nearest relative than L2; L2 viruses were **3.0× more likely** to have L2 nearest relative (P < 0.001) — strong phylogenetic clustering
- However, since discovery: **61% of L34 viruses** and **37% of L2 viruses** now have different IT-level nearest relatives due to new nonhuman virus discoveries
- Most human viruses originally without congeneric relatives (26–30/47) are now most closely related to L1 viruses

### Genome Type Patterns
- **(−)ssRNA viruses** disproportionately strictly zoonotic; rarely specialist human viruses (only 2 Rubulavirus species infect only humans vs. 20 (+)ssRNA species from multiple genera)
- **Vector-borne viruses**: significantly underrepresented among human-transmissible lineages relative to strictly zoonotic — likely because arthropod transmission bypasses respiratory barriers needed for human-to-human spread

## Methodology

### Infection/Transmission (IT) Level Classification
Based on Woolhouse et al. 2013 framework:
- **L1**: Not known to infect humans
- **L2**: Infect humans from nonhuman reservoir but don't spread within human populations (strictly zoonotic)
- **L34**: Can spread within human populations — L3 = self-limiting outbreaks, L4 = epidemic potential

### Phylogenetic Analysis
- Bayesian maximum clade credibility trees for 52 genera (>1 species/type each); polymerase protein sequences used
- Ancestral state reconstruction mapped IT levels onto phylogenies
- **Temporal censoring**: Analysis repeated with datasets censored by virus discovery year in 10-year steps back to early 20th century

### Lineage Definition
- Strictly zoonotic lineages: contain only L2 species/types
- Human-transmissible lineages: contain only L34 species/types
- Mixed lineages: contain both L2 and L34 species/types

## Critical Analysis

### Strengths
1. **Novel temporal approach**: Censoring by discovery date is a creative way to address ascertainment bias — the "discovery curve" method extended beyond simple species counts
2. **Comprehensive dataset**: 743 species across 59 genera represents one of the most complete RNA virus phylogenetic analyses for emergence risk assessment
3. **Directly addresses Global Virome Project debate**: Provides evidence-based framework for prioritizing surveillance — shows that discovery of nonhuman viruses is reshaping our understanding faster than human virus discovery
4. **Phylogenetic clustering quantified**: Demonstrates that IT level is phylogenetically informative but the signal changes as more data becomes available

### Limitations
1. **Ascertainment bias persists despite temporal correction**: The censoring approach mitigates but doesn't eliminate bias — early discoveries were heavily human-focused, and this historical imbalance affects baseline estimates
2. **L34 grouping conflates outbreak vs. epidemic potential**: L3 (self-limiting) and L4 (epidemic-capable) are combined, which may obscure important differences in evolutionary trajectories
3. **Single representative sequence per species/type**: May miss within-species diversity relevant to host range evolution
4. **No mechanistic insight**: The study identifies patterns but doesn't explain *why* certain genome types or transmission modes correlate with transmissibility — receptor usage hypothesis is mentioned but not tested
5. **Limited to RNA viruses**: DNA virus emergence dynamics may differ substantially

### Clinical/Public Health Relevance
- Supports the hypothesis that human-transmissible viruses commonly emerge from nonhuman reservoirs, particularly in lineages already containing human-infective members
- Suggests surveillance should focus on genera with existing human-infective viruses rather than purely nonhuman genera
- The declining proportion of mixed lineages implies that strictly zoonotic (L2) viruses rarely evolve into human-transmissible forms — consistent with epidemiological experience showing no clear examples of L2→L34 transitions
- Informs risk assessment frameworks like the Spillover project by providing phylogenetic context for emergence probability

## Cross-References

See also: [Emerging Rna Viruses Genomic Adaptation](concepts/emerging-rna-viruses-genomic-adaptation.md), [Rna Virus Macroevolution](concepts/rna-virus-macroevolution.md), [Phylogenetics Phylodynamics](concepts/phylogenetics-phylodynamics.md), [Pandemic Influenza Emergence](concepts/pandemic-influenza-emergence.md)
