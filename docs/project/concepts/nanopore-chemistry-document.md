---
title: "Oxford Nanopore Chemistry Technical Document"
created: 2026-07-01
source: Oxford Nanopore Technologies | V CHTD_500_v1_revAU_26May2026
source_url: https://nanoporetech.com
tags: [nanopore, ONT, sequencing, chemistry, library-prep]
---

# Oxford Nanopore Chemistry Technical Document

**Version:** V CHTD_500_v1_revAU (26 May 2026) | **Pages:** 96 | **Full text:** [[nanopore-chemistry-full-text]]

## Overview

Comprehensive reference for all Oxford Nanopore library preparation chemistries, kits, barcodes, adapters, and reagents. FOR RESEARCH USE ONLY.

## Document Structure (16 Sections)

### Introduction
1. **Library Preparation Chemistry** — Conversion of DNA/RNA to nanopore-sequencing format. Flow cells contain ion-permeable nanopores in electrically-resistant membrane; ionic current disruption identifies bases.
2. **Store Terminology** — Product phase definitions, ordering guidance

### Available Kits (Current)
3. **Ligation-based Sequencing Kits** — Adapter attachment via ligation enzymes during library prep
4. **Rapid-based Sequencing Kits** — Faster workflow, includes 10x Genomics single-cell/spatial transcriptomics compatibility (SQK-LSK114 + EXP-PCA001)
5. **RNA and cDNA Sequencing Kits** — Direct RNA sequencing (native base modifications) and cDNA intermediates
6. **Barcoding Kits** — Pooling multiple samples per flow cell. RT, strand switching, UMI incorporation, full-length RNA cDNA-RT adapter ligation
7. **Expansion Packs** — Extra reagents/barcodes for efficient kit use

### Sample Input & Optimization
8. **Sample Input Recommendations** — Good quality library = molecules with sequencing adapters on both ends. Fragmenting DNA boosts output but may prevent ultra-long reads. Relationship between input and output varies by sheared vs unsheared gDNA
9. **Making the Most of Your Flow Cell** — Blocking mitigation: fragment starting DNA, flow cell washing (nuclease digests sample remnants). Wash kit removes 99% library; recommend barcoding when reusing

### Legacy Kits
10. **Legacy Ligation-based Kits** — Previously available kits
11. **Legacy Rapid-based Kits** — Including rapid sequencing adapters with PCR adapter ligation workflow (~100 min)
12. **Legacy RNA/cDNA Kits** — Reverse transcription, strand switching, primer annealing (~80-90 min workflows)
13. **Legacy Barcoding Kits** — Native Barcoding Expansions 1-12, 13-24, and 96

### Sequences & Reagents
14. **Barcode Sequences** — Full list of native barcodes NB01-NB96. First 24 in SQK-NBD114.24, all 96 in SQK-NBD114.96
15. **Adapter Sequences** — Current kit adapter sequences (RNA21-RNA24 listed)
16. **Kit Reagents** — Complete reagent inventory

## Key Kit Codes Referenced

| Code | Description |
|------|-------------|
| SQK-LSK114 | Ligation sequencing kit V14 |
| SQK-RBK114.24 | Rapid Barcoding Kit 24 V14 |
| SQK-NBD114.24 | Native Barcoding Kit 24 V14 |
| SQK-NBD114.96 | Native Barcoding Kit 96 V14 |
| EXP-PCA001 | 10x Genomics expansion pack |

## Related Pages

- [Dna Extraction Kits Comparison](concepts/dna-extraction-kits-comparison.md) — Extraction kit comparison
- [[nanopore-protocols]] — Sequencing protocols reference
