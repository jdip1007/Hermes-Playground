---
title: "Multiplex Nanopore Sequencing for Arboviral Detection (Ampli-FlaCk)"
created: "2026-06-08"
updated: "2026-06-08"
type: concept
tags: [nanopore, arbovirus, dengue, zika, chikungunya, multiplex-PCR, diagnostics, Brazil]
sources:
  - type: paper
    url: "https://doi.org/10.3390/v16010023"
    title: "A Multiplex Nanopore Sequencing Approach for the Detection of Multiple Arboviral Species"
    authors: "Xavier J, Fonseca V, Adelino T, et al."
    journal: "Viruses"
    date: "2024-01-22"
confidence: high
---

# Multiplex Nanopore Sequencing for Arboviral Detection (Ampli-FlaCk)

## Overview

The **Ampli-FlaCk** protocol is a multiplex RT-PCR + Oxford Nanopore sequencing approach designed to simultaneously detect and genotype multiple arboviral species in a single reaction [1]. Developed by a large Brazilian consortium including Fiocruz, PAHO/WHO, and multiple state public health laboratories (LACENs), this method targets Chikungunya virus (CHIKV) and orthoflaviviruses (dengue DENV-1–4, Zika ZIKV, yellow fever YFV, West Nile WNV) [1].

## Key Findings

### Protocol Design
- **Multiplex RT-PCR**: Combines primers for CHIKV envelope gene (~1050 bp) and orthoflavivirus NS5 gene (~1000 bp) in a single reaction [1]
- **OneStep RT-PCR Kit**: Simultaneous reverse transcription + PCR amplification [1]
- **MinION sequencing**: Up to 96 samples per experiment using Rapid Barcoding Kit [1]
- **Degenerate primers**: Cover nucleotide diversity of NS5 gene across orthoflavivirus species [1]

### Performance on Clinical Samples (n=49)
|| Virus | Samples | Median Ct | Detection Rate | Lineage Identified |
||-------|---------|-----------|----------------|-------------------|
|| DENV-1 | 14 | 19.49 | High | Genotype V |
|| DENV-2 | 13 | 27.10 | Moderate | Genotype III |
|| CHIKV | 14 | 26.20 | High | ECSA lineage |
|| YFV | 7 | 16.80 | Very high | South America I |
|| ZIKV | 1 | ND | Single sample | Asian lineage |

- **Overall identification rate**: 83.67% (41/49 clinical samples) [1]
- **Median mapped reads/sample**: 10,229 [1]
- **Long read recovery**: ~1000 bp in 89.80% of samples [1]
- **Limit of detection**: DENV Ct values 30–37; CHIKV up to Ct 40 [1]

### Phylogenetic Validation
- Successfully reconstructed phylogenetic trees for DENV-2 and CHIKV from clinical samples [1]
- Correctly placed sequences within known clades (DENV-2 genotype II cosmopolitan, CHIKV ECSA lineage) [1]
- Validated in field surveillance activities across Brazil (2021–2022) and Uruguay (early 2023) [1]

## Critical Analysis

### Strengths ✅
✅ **Multiplex design** — single reaction for multiple arboviruses reduces cost/time [1]  
✅ **Long reads (~1000 bp)** enable lineage assignment, not just species detection [1]  
✅ **Field-deployable** — MinION portability enables sequencing at point of surveillance [1]  
✅ **Validated across Brazil and Uruguay** — multi-country consortium with 25+ institutions [1]  
✅ **Handles degraded RNA** — works on samples stored under suboptimal conditions [1]  
✅ **Overcomes serological cross-reactivity** — molecular detection avoids flavivirus antibody cross-reaction [1]  

### Limitations ⚠️
⚠️ **Sensitivity drops at high Ct values (>30)** — only 16.33% of low-viral-load samples yielded reliable results [1]  
⚠️ **Small validation cohort** (n=49) — limited assessment of detection limits [1]  
⚠️ **Targeted approach** — cannot detect novel/unexpected arboviruses outside primer coverage [1]  
⚠️ **No comparison to gold-standard RT-qPCR** — performance benchmarked against itself rather than reference method [1]  
⚠️ **Single gene region (NS5/envelope)** — limited genomic context for recombination detection [1]  

### Unanswered Questions ❓
❓ How does Ampli-FlaCk compare to Illumina-based arboviral panels?  
❓ Performance with co-infections (DENV+ZIKV, DENV+CHIKV)?  
❓ Scalability to additional arboviruses (Mayaro, Oropouche, etc.)?

## Clinical/Practical Implications

1. **Rapid outbreak response** — enables same-day genotyping during arboviral epidemics in the Americas [1]
2. **Surveillance integration** — can be deployed at LACEN-level public health laboratories across Brazil [1]
3. **Lineage tracking** — long reads provide phylogenetic markers for transmission chain reconstruction [1]
4. **Cost-effective multiplexing** — 96 samples per flow cell reduces per-sample cost vs individual assays [1]

## Cross-References

- [Nanopore Sequencing Minion](nanopore-sequencing-minion.md) — MinION platform overview and field deployment history
- [Clinical Metagenomics Viral Detection](clinical-metagenomics-viral-detection.md) — broader clinical metagenomics context for viral diagnostics
- [Next Generation Sequencing](next-generation-sequencing.md) — sequencing technology comparison
- [Pandemic Influenza Emergence](pandemic-influenza-emergence.md) — arboviral emergence parallels influenza pandemic preparedness

## Confidence Assessment

**High confidence** in core protocol performance based on:
- Multi-center validation across Brazil and Uruguay [1]
- Peer-reviewed publication in Viruses (MDPI, 2024) [1]
- Open access with supplementary data available [1]

**Moderate confidence** in generalizability due to:
- Limited sample size for sensitivity assessment at low viral loads [1]
- Primarily tested on known-positive samples rather than clinical screening cohort [1]
- No head-to-head comparison with established RT-qPCR diagnostics [1]
