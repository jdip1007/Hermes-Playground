---
title: "Next-Generation Sequencing (NGS)"
created: 2026-05-28
updated: 2026-06-08
type: concept
tags: [bioinformatics, sequencing, technique]
sources:
  - type: paper
    url: "PubMed"
    title: "Bioinformatics in Clinical Genomic Sequencing"
    date: "2020-06"
  - type: paper
    url: "PubMed"
    title: "DNA sequencing: the key to unveiling genome"
    date: "2020-10"
  - type: paper
    url: "PubMed"
    title: "Nanopore DNA sequencing technologies and their applications"
    date: "2024-03"
  - type: paper
    url: "https://wwwnc.cdc.gov/EID/article/22/2/15-1796.pdf"
    title: "Nanopore Sequencing as a Rapidly Deployable Ebola Outbreak Tool"
    date: "2016-02"
confidence: high
contested: false
---

# Next-Generation Sequencing (NGS)

## Overview

NGS refers to high-throughput parallel DNA sequencing technologies that replaced Sanger sequencing as the dominant method for genomic analysis [2]. Key platforms include Illumina (short-read), PacBio and Oxford Nanopore (long-read) [2,3].

## Major Platforms

- **Illumina** — Short-read (150-300bp), highest accuracy (~99.9%), dominant in clinical settings [2]
- **PacBio (HiFi)** — Long-read (15-25kb), high accuracy (~99.9%), good for structural variants [2]
- **Oxford Nanopore** — Ultra-long reads (100kb+), portable (MinION), real-time analysis, slightly lower raw accuracy [3]

## Applications

- Whole-genome sequencing (WGS) and whole-exome sequencing (WES) [2]
- RNA-seq for transcriptomics and gene expression profiling [2]
- Metagenomic sequencing for microbial community analysis [3]
- Clinical diagnostics and pathogen identification [1,3]
- Epigenetics (ChIP-seq, ATAC-seq, bisulfite sequencing) [2]

## Clinical Considerations

NGS in clinical settings requires rigorous bioinformatics pipelines for variant calling, quality control, and interpretation [1]. Key challenges include distinguishing pathogenic variants from benign polymorphisms and managing the volume of incidental findings [1].

## Field Deployment (Portable Sequencing)

The [Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md) platform enables sequencing in resource-limited or remote outbreak settings [4]:
- Pocket-sized device (~75 g), no calibration required, operational immediately upon arrival [4]
- Successfully deployed during 2014–2015 Ebola outbreak in Liberia (CDC/NIH field lab) — produced 4 full-length EBOV genomes/day with one operator and two devices [4]
- Illumina MiSeq also deployed to West Africa (Feb 2015) but requires ~40–100 kg equipment, field engineer calibration, and more infrastructure [4]

## Related

[Single Cell Sequencing](concepts/single-cell-sequencing.md), [Metagenomics](concepts/metagenomics.md), [Crispr Cas9](concepts/crispr-cas9.md), [Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
