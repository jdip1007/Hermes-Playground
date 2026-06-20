---
title: "Single-Cell Sequencing"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [bioinformatics, sequencing, technique, single-cell]
sources:
  - type: paper
    url: "PubMed"
    title: "Applications of Single-Cell DNA Sequencing"
    date: "2021-08"
  - type: paper
    url: "PubMed"
    title: "Single-Cell RNA Sequencing Technology Landscape in 2023"
    date: "2024-01"
  - type: paper
    url: "PubMed"
    title: "From bulk, single-cell to spatial RNA sequencing"
    date: "2021-11"
confidence: high
contested: false
---

# Single-Cell Sequencing

## Overview

Single-cell sequencing technologies enable genomic, transcriptomic, and epigenomic analysis at the resolution of individual cells, revealing cellular heterogeneity that bulk sequencing masks [1][2][3].

## Key Technologies

- **scRNA-seq** — Single-cell RNA sequencing (10x Genomics, Drop-seq, Smart-seq2) [2]
- **scATAC-seq** — Chromatin accessibility at single-cell resolution [1]
- **CITE-seq** — Simultaneous protein and RNA measurement [2]
- **Spatial transcriptomics** — Gene expression with spatial context (Visium, MERFISH) [3]

## Major Platforms

- **10x Genomics Chromium** — Droplet-based, high throughput (10,000+ cells), 3' or 5' counting [2]
- **Smart-seq2** — Full-length transcript coverage, lower throughput, higher sensitivity [2]
- **Drop-seq** — Open-source droplet platform, cost-effective [2]

## Applications

- Cell type identification and classification in complex tissues [2][3]
- Developmental biology and lineage tracing [2]
- Cancer heterogeneity and tumor microenvironment characterization [1]
- Immunology and immune cell profiling [2]
- Microbial single-cell genomics [1]

## Challenges

- Ambient RNA contamination (addressed by tools like SoupX) [2]
- Dropout events (genes not detected despite expression) [2]
- Computational complexity of data analysis [2]
- Cost per cell remains higher than bulk methods [2][3]

## Related

[Next Generation Sequencing](next-generation-sequencing.md), [Metagenomics](metagenomics.md), [Bioinformatics](bioinformatics.md)
