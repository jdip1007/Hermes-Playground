---
title: "Metagenomics"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [bioinformatics, metagenomics, microbiology, sequencing]
sources:
  - type: paper
    url: "PubMed"
    title: "What Is Metagenomics Teaching Us, and What Is Missed?"
    date: "2020-09"
  - type: paper
    url: "PubMed"
    title: "Genome-resolved metagenomics using environmental and clinical samples"
    date: "2021-09"
  - type: paper
    url: "PubMed"
    title: "Metagenomic tools in microbial ecology research"
    date: "2021-02"
confidence: high
contested: false
---

# Metagenomics

## Overview

Metagenomics is the study of genetic material recovered directly from environmental or clinical samples, bypassing the need for culturing individual organisms [1]. It enables comprehensive analysis of microbial communities [2].

## Workflow

1. **Sample collection** — Environmental (soil, water) or clinical (stool, sputum, blood) [2]
2. **DNA extraction** — Often the most variable step; kit choice significantly impacts results [3]
3. **Sequencing** — Typically shotgun NGS (Illumina), increasingly long-read (Nanopore, PacBio) [2]
4. **Bioinformatics analysis** — Quality control, assembly, binning, annotation [3]
5. **Interpretation** — Taxonomic profiling, functional annotation, comparative analysis [1]

## Key Approaches

- **Shotgun metagenomics** — Random sequencing of all DNA; provides taxonomic + functional data [2]
- **16S/ITS amplicon sequencing** — Targeted marker gene sequencing; cheaper but limited resolution [3]
- **Metatranscriptomics** — RNA-based; reveals active functions rather than potential [1]
- **Metaproteomics** — Protein-level analysis of communities [2]
- **Metabolomics** — Metabolite profiling of communities [1]

## Analysis Tools

- **Assembly**: MEGAHIT, metaSPAdes [3]
- **Binning**: MetaBAT2, MaxBin2, CONCOCT [2]
- **Taxonomic profiling**: Kraken2, MetaPhlAn, Centrifuge [3]
- **Functional annotation**: HUMAnN, eggNOG-mapper [3]
- **Quality assessment**: CheckM, BUSCO [2]

## Clinical Applications

- Pathogen detection in culture-negative infections [2]
- Microbiome-associated disease biomarkers [1]
- Antimicrobial resistance gene surveillance [2]
- Hospital outbreak investigation [1]

## Challenges

- Reference database incompleteness (especially for non-model organisms) [1]
- Host DNA contamination in clinical samples [2]
- Strain-level resolution limitations with short reads [2]
- Distinguishing pathogens from colonizers [1]

## Related

[Next Generation Sequencing](concepts/next-generation-sequencing.md), [Antimicrobial Resistance](concepts/antimicrobial-resistance.md), [Microbiome](concepts/microbiome.md)
