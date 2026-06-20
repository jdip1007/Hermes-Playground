---
title: "PromethION 24-Hour Genome End-to-End Workflow"
summary: "PromethION 24-hour genome protocol enables ultra-rapid whole-genome sequencing from blood to variant calls in ~24 hours on P24/P48 platform, targeting ≥30x coverage with ~30 kb read N50"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [nanopore, promethion, whole-genome-sequencing, human-variation, rapid-diagnosis]
sources:
  - type: protocol
    url: "https://nanoporetech.com/documents/protocols/24-hour-genome-end-to-end-workflow-from-blood-to-analysis"
    title: "PromethION: 24-hour genome end-to-end workflow from blood to analysis (v114 revB, Dec 2025)"
    date: 2025-12-08
confidence: high
contested: false
---

## Overview

Oxford Nanopore's PromethION 24-hour genome protocol enables ultra-rapid whole-genome sequencing from blood to variant calls in approximately 24 hours.[1] Designed for the PromethION 24/48 platform, this workflow targets ≥30x coverage with ~30 kb read N50, supporting robust calling of small and large variants plus methylation detection and phasing information.

## Workflow Summary

### Sample Preparation (~150 minutes)

- **DNA extraction**: HMW gDNA from 500 µl whole blood using Qiagen Puregene Blood Kit (cat. 158023/158026)[1]
- **Fragmentation**: Megaruptor 3 (Diagenode, E07010003) shearing to target ~30 kb N50[1]
- **QC**: Qubit dsDNA Broad Range quantification (expected 50–150 ng/µl), Femto Pulse gDNA 165 kb Analysis Kit for length verification[1]

### Library Preparation (~85 minutes + overnight)

- **Input**: ~2.7 µg fragmented gDNA per sample[1]
- **Repair & end-prep**: NEBNext FFPE DNA Repair Mix (M6630), FFPE Repair v2 Module (E7360), Ultra II End Repair/dA-Tailing Module (E7546)[1]
- **Adapter ligation**: Ligation Sequencing Kit V14 (SQK-LSK114) with Salt-T4 DNA Ligase (NEB, M0467)[1]
- **Clean-up**: AMPure XP beads (AXP from SQK-LSK114), elution in 97 µl[1]

### Sequencing (13–16 hours)

- **Flow cells**: 3× PromethION Flow Cell R10.4.1 (FLO-PRO114M) per sample on P24/P48 device[1]
- **Minimum active pores**: 5,000 per flow cell (warranty); representative results use 7,000-pore cells achieving 30x in 12.9 hours[1]
- **Basecalling**: HAC model with 5mC/5hmC modified base detection in CpG context, aligned to hg38[1]

### Data Analysis

Secondary analysis via `wf-human-variation` EPI2ME workflow produces per-sample VCF files using:[1]

| Variant Type | Tool |
|---|---|
| SNVs & small indels | Clair3 |
| Structural variants (SVs) | Sniffles2 |
| Copy number variants (CNVs) | Spectre |
| Short tandem repeats (STRs) | Straglr |
| DNA methylation | modkit |

Tertiary interpretation via Fabric or Geneyx platforms.[1]

## Key Specifications

- **Total time**: ~24 hours from blood draw to variant calls[1]
- **Coverage target**: ≥30x human genome[1]
- **Read N50**: ~30 kb (Gaussian profile characteristic of Megaruptor shearing)[1]
- **Kit compatibility**: SQK-LSK114 (prepares 2 samples), EXP-AUX003 auxiliary vials for 2 additional samples[1]
- **Library storage**: 4°C short-term, -80°C long-term (>3 months)[1]

## Stopping Points

Extracted or fragmented gDNA can be stored at −20°C for later use.[1] Library can be stored at 4°C (short-term/repeated flow cell loading) or -80°C (long-term).[1]

## Related Topics

[Nanopore Sequencing Minion](nanopore-sequencing-minion.md)
[Next Generation Sequencing](next-generation-sequencing.md)
[Megaruptor 3 Extraction Method](megaruptor-3-extraction-method.md)
[Blood Culture Broth Dna Extraction](blood-culture-broth-dna-extraction.md)
