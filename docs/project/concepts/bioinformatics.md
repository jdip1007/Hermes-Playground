---
title: "Bioinformatics"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [bioinformatics, technique]
sources:
  - type: paper
    url: "PubMed"
    title: "Introduction to bioinformatics"
    date: "2006-07"
  - type: paper
    url: "PubMed"
    title: "Bioinformatics in Clinical Genomic Sequencing"
    date: "2020-06"
  - type: paper
    url: "PubMed"
    title: "Bioinformatics for Cancer Immunotherapy"
    date: "2020"
confidence: high
contested: false
---

# Bioinformatics

## Overview

Bioinformatics is the application of computational tools to manage, analyze, and interpret biological data [1]. It sits at the intersection of biology, computer science, statistics, and information engineering [1].

## Core Areas

- **Sequence analysis** — Alignment (BLAST, Bowtie, BWA), assembly (SPAdes, Canu), variant calling (GATK, FreeBayes) [1]
- **Structural bioinformatics** — Protein structure prediction (AlphaFold, RoseTTAFold), molecular docking [1]
- **Genomics** — Genome annotation, comparative genomics, population genetics [2]
- **Transcriptomics** — Differential expression (DESeq2, edgeR), RNA-seq pipelines [2]
- **Proteomics** — Mass spectrometry data analysis, protein-protein interaction networks [1]
- **Metabolomics** — Metabolic pathway analysis, flux balance analysis [1]

## Key Databases

- **NCBI** — GenBank, PubMed, SRA, RefSeq [1]
- **EMBL-EBI** — ENA, UniProt, ArrayExpress [1]
- **DDBJ** — DNA Data Bank of Japan [1]
- **Specialized**: KEGG (pathways), Pfam (protein families), GTDB (microbial taxonomy) [2]

## Computational Infrastructure

- **Workflow managers**: Nextflow, Snakemake, CWL [2]
- **Cloud platforms**: AWS, GCP, Terra, AnVIL [2]
- **HPC**: SLURM, PBS clusters [1]
- **Containers**: Docker, Singularity/Apptainer [2]

## Challenges

- Data volume and storage (petabyte-scale for large cohorts) [2]
- Reproducibility and standardization [2]
- Integration of multi-omics data [3]
- Interpretation and clinical translation [2][3]

## Related

[Next Generation Sequencing](concepts/next-generation-sequencing.md), [Metagenomics](concepts/metagenomics.md), [Single Cell Sequencing](concepts/single-cell-sequencing.md)
