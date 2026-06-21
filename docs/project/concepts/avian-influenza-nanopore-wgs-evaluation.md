---
title: "Avian Influenza Whole-Genome Sequencing on Nanopore MinION"
created: "2026-06-08"
updated: "2026-06-08"
type: concept
tags: [nanopore, avian-influenza, HPAI, whole-genome-sequencing, library-prep, MinION]
sources:
  - type: paper
    url: "https://doi.org/10.3390/microorganisms11020529"
    title: "An Evaluation of Avian Influenza Virus Whole-Genome Sequencing Approaches Using Nanopore Technology"
    authors: "Ip HS, Uhm S, Killian ML, Torchetti MK"
    journal: "Microorganisms"
    date: "2023-02-19"
confidence: high
---

# Avian Influenza Whole-Genome Sequencing on Nanopore MinION

## Overview

This study from the USGS National Wildlife Health Center and USDA National Veterinary Services Laboratories systematically evaluates **five different library preparation kits** and **four primer sets** for whole-genome sequencing of avian influenza virus (AIV) on the Oxford Nanopore MinION platform. The goal was to identify optimal protocols for routine diagnostic laboratory use during HPAI outbreaks [1].

## Study Design

- **Samples**: 3 wild bird swab samples positive for HPAI H5N1 [1]
  - Sample 245467: Neotropical Cormorant, Arizona (Ct=25.18) [1]
  - Sample 245626: Eared Grebe, North Dakota (Ct=30.51 — lowest viral titer) [1]
  - Sample 246038: Canada Goose, California (Ct=16.44 — highest viral titer) [1]
- **Primer sets evaluated**: 4 sets for whole-genome RT-PCR amplification of all 8 influenza segments [1]
- **Library prep kits compared**: 5 ONT kits (Methods A, E, K, N, S) [1]

## Key Findings

### Primer Set Performance
| Primer Set | Source | cDNA Yield | Recommendation |
|------------|--------|------------|----------------|
| Set 1 (Zhou/Wentworth) | Original conserved primers | High | Good baseline |
| Set 2 (Modified Zhou) | This study | Moderate | Suboptimal |
| Set 3 (Mitchell B) | Mitchell et al. | Low | Not recommended |
| **Set 4 (Modified Mitchell)** | This study | **Highest** | **Best performer**, especially for low-titer samples |

### Library Kit Comparison
| Method | Kit | Complete Genomes/3 Samples | Total Reads | Accuracy vs MiSeq |
|--------|-----|---------------------------|-------------|-------------------|
| A (Native Barcoding) | SQK-LSK109 | 3/3 | 884,278 | 4 mutations total |
| E (Limited Amplification) | SQK-RBK004 | **0/3** | 10,759 | 190 mutations — worst |
| K (PCR Barcoding) | SQK-PBK004 | 3/3 | 1,870,741 | **2 mutations total — best accuracy** |
| N (Rapid Protocol) | SQK-LSK109 variant | 3/3 | 381,626 | 4+del7 mutations |
| S (Edited Primers) | SQK-PBK004 variant | **Partial only** | 3,653,632 | Uneven coverage |

### Best Overall Protocol: Method K (SQK-PBK004 + Set 4 primers)
- Generated complete genomes from all 3 samples including lowest-titer sample [1]
- Highest accuracy vs Illumina MiSeq reference (>99.985%) [1]
- Only 2 sequence differences in the most challenging sample [1]

### Key Technical Observations
- **Homopolymer errors**: Frameshifts common in PB1 and PA segments with automated assembly — manual curation needed [1]
- **Coverage threshold**: ≥60× coverage required for >99.95% accuracy on MinION [1]
- **Method E failure**: Least PCR amplification → most sequence variations (190 mutations) despite being marketed as "rapid" [1]

## Critical Analysis

### Strengths ✅
✅ **Systematic comparison** — rare head-to-head evaluation of 5 kits × 4 primer sets [1]  
✅ **Real diagnostic samples** — wild bird swabs representing typical surveillance specimens [1]  
✅ **Illumina MiSeq reference standard** for accuracy benchmarking [1]  
✅ **Practical guidance** — clear recommendations for diagnostic laboratories [1]  

### Limitations ⚠️
⚠️ **Only 3 samples** — insufficient to capture full diversity of circulating strains [1]  
⚠️ **All H5N1 clade 2.3.4.4b** — performance with other subtypes (H7, H9) unknown [1]  
⚠️ **Undersampled flow cell capacity** — only 3 samples on MinION; production runs would differ [1]  
⚠️ **No cost analysis** — per-sample costs not compared across methods [1]  
⚠️ **Primer-kit compatibility confounded** — not all primer sets compatible with all kits [1]  

### Unanswered Questions ❓
❓ How do these protocols perform with metagenomic (non-enriched) sequencing? [1]  
❓ Impact of newer R10 flow cells on homopolymer error rates? [1]  
❓ Performance with human clinical samples vs wild bird swabs? [1]  

## Clinical/Practical Implications

1. **Method K recommended** for routine AIV whole-genome sequencing on MinION [1]
2. **Set 4 primers** (modified Mitchell B) provide best amplification, especially for low-titer samples [1]
3. **Avoid Method E** despite "rapid" marketing — poor accuracy and incomplete genomes [1]
4. **Manual curation still needed** for homopolymer regions in PB1/PA segments [1]

## Cross-References

- [Ont R10 Avian Influenza Surveillance](concepts/ONT-R10-avian-influenza-surveillance.md) — R10 chemistry improvements for influenza sequencing (complementary study)
- [Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md) — MinION platform overview
- [Pandemic Influenza Emergence](concepts/pandemic-influenza-emergence.md) — influenza pandemic preparedness context
- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — broader NGS technology comparison

## Confidence Assessment

**High confidence** in protocol recommendations based on:
- Systematic experimental design with Illumina reference standard [1]
- Peer-reviewed publication (Microorganisms, MDPI 2023) [1]
- Authors from USGS and USDA — authoritative wildlife health institutions [1]

**Moderate confidence** in generalizability due to:
- Small sample size (n=3) [1]
- Single influenza clade tested [1]
- Flow cell capacity not fully utilized [1]
