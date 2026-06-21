---
title: "Universal SARS-CoV-2 Tiled Amplicon Sequencing on Nanopore"
created: "2026-06-08"
updated: "2026-06-08"
type: concept
tags: [nanopore, SARS-CoV-2, tiled-amplicons, ARTIC, whole-genome-sequencing, Kazakhstan]
sources:
  - type: paper
    url: "https://doi.org/10.1038/s41598-023-37588-x"
    title: "Universal whole-genome Oxford nanopore sequencing of SARS-CoV-2 using tiled amplicons"
    authors: "Kalendar R, Kairov U, Karabayev D, Aitkulova A, Tynyshtykbayeva N, Daniyarov A, Otarbay Z, Rakhimova S, Akilzhanova A, Sarbassov D"
    journal: "Scientific Reports (Nature)"
    date: "2023-06-14"
confidence: high
---

# Universal SARS-CoV-2 Tiled Amplicon Sequencing on Nanopore

## Overview

This study from Nazarbayev University (Kazakhstan) and University of Helsinki develops an optimized protocol for universal SARS-CoV-2 whole-genome sequencing using **tiled amplicons up to 4.8 kb** on Oxford Nanopore MinION [1]. The key innovation is a comprehensive multiplexed primer set with two pools (A/B, 48 primer pairs total) that can be flexibly configured for amplicon sizes from 1.2 kb to 4.8 kb or longer — addressing the ARTIC Midnight protocol's limitation of systematic dropout regions [1].

## Key Innovations

### Primer Design
- **Two overlapping pools** (A and B): 24 primer pairs each, covering entire ~30 kb SARS-CoV-2 genome [1]
- **~700 bp overlap** between adjacent amplicons in each pool [1]
- **Flexible configuration**: Primers from different pools can be combined for any target size (1.2–4.8+ kb) [1]
- Designed using FastPCR software with thermodynamic optimization (-tiling[-700], -tm55-58, -3tm23-32) [1]

### cDNA Synthesis Improvement
| Protocol | Reverse Transcriptase | Primers | Performance |
|----------|----------------------|---------|-------------|
| **This study** | Maxima H Minus (Thermo Fisher) | SARS-CoV-2 specific primers (10–20 nM) | **Superior**: 2+ PCR cycles lower Ct, works on degraded RNA |
| ARTIC Midnight | LunaScript RT Supermix | Random primers | Systematic dropouts, fails on low-titer/degraded samples |

### Performance on Degraded Samples
- Successfully amplified long fragments (up to 4.8 kb) from samples stored ~1 year at −20°C with multiple freeze-thaw cycles [1]
- **Genome integrity assessment**: Paired amplification of A05-A08 (2400 bp, 5' end) and B48-A45 (3041 bp, near poly-A site) enables degradation detection [1]
- Most common pattern: Reduced 3' amplicon intensity indicating distal genome degradation [1]

### Validation Results
- **341 sequences** deposited in GISAID across multiple SARS-CoV-2 variants [1]
- All samples passed quality control and were assigned correct Pango lineages [1]
- Lineage assignments matched between this protocol and ARTIC Midnight for overlapping samples — confirming accuracy regardless of methodology [1]

## Critical Analysis

### Strengths ✅
✅ **Handles degraded RNA** — critical for retrospective surveillance and poorly stored specimens [1]  
✅ **Flexible amplicon sizing** — adaptable to different sequencing platforms and sample quality [1]  
✅ **Improved cDNA synthesis** — specific primers + Maxima H Minus outperforms ARTIC Midnight [1]  
✅ **Validated across variants** — 341 sequences spanning multiple Pango lineages [1]  
✅ **Open protocol** — primer sets and methods fully described for reproducibility [1]  

### Limitations ⚠️
⚠️ **No head-to-head quantitative comparison** with ARTIC on same samples (only lineage matching) [1]  
⚠️ **Single-country cohort** (Kazakhstan) — limited geographic diversity of variants tested [1]  
⚠️ **Ct <32 selection bias** — only moderate-high viral load samples included; performance at Ct >32 unknown [1]  
⚠️ **No cost analysis** vs ARTIC or Illumina-based approaches [1]  

### Unanswered Questions ❓
❓ Performance with Omicron subvariants and future divergent lineages?  
❓ Comparison to ARTIC v4/v5 protocols (released after this study)?  
❓ Applicability to other RNA viruses beyond SARS-CoV-2?  

## Clinical/Practical Implications

1. **Retrospective surveillance**: Enables sequencing of archived/degraded samples that would fail with standard ARTIC [1]
2. **Resource-limited settings**: Simplified protocol reduces dependency on specific commercial kits [1]
3. **Variant monitoring**: Flexible primer design can be adapted for emerging variants with mutations in primer binding sites [1]
4. **Cost reduction**: Fewer PCR cycles and simpler workflow compared to Midnight two-round multiplex [1]

## Cross-References

- [Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md) — MinION platform overview
- [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md) — broader clinical metagenomics context for SARS-CoV-2 surveillance
- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — sequencing technology comparison
- [Pandemic Influenza Emergence](concepts/pandemic-influenza-emergence.md) — parallels in pandemic pathogen genomic surveillance

## Confidence Assessment

**High confidence** in protocol performance based on:
- 341 validated sequences deposited in GISAID [1]
- Published in Scientific Reports (Nature portfolio, 2023) [1]
- Lineage assignments consistent with established methods [1]

**Moderate confidence** in superiority claims due to:
- Lack of direct quantitative comparison metrics vs ARTIC Midnight [1]
- Limited variant diversity tested during study period [1]
