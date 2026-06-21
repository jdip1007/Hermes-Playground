---
title: "Human Cell Line DNA Extraction — QIAGEN Genomic-tip (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/human-cell-line-dna-qiegen-genomic-tip"
    title: "Human cell line DNA – QIAGEN Genomic-tip Protocol v3"
    date: 2023-08-01
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated protocol for extracting high-molecular-weight genomic DNA from human cell lines using the QIAGEN Blood and Cell Culture DNA Maxi Kit with Genomic-tip columns, optimized for downstream Nanopore long-read sequencing.[1] This protocol scales to larger inputs (1 × 10⁸ cells) compared to the Puregene Cell Kit approach, yielding concentrated DNA at 400–450 ng/µl.[1]

## Materials

- **Input**: Cell culture (1 × 10⁸ cells)[1]
- **Kit**: QIAGEN Blood and Cell Culture DNA Maxi Kit[1]
- **Reagents**: 70% ethanol in nuclease-free water, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0), buffer QF[1]
- **Consumables**: 50 ml Falcon tubes[1]
- **Equipment**: Shaker for Eppendorf tubes, microfuge[1]

## Protocol Steps

### Cell Lysis

1. Harvest 1 × 10⁸ cells and lyse according to the QIAGEN Genomic DNA Handbook — "Preparation of cell culture" section (page 25)[1]

### DNA Isolation

2. Follow the QIAGEN Genomic-tip handbook starting at the "Isolation of genomic DNA from blood, cultured cells, tissue, yeast, or bacteria using genomic-tips" section (page 49)[1]

### Optional Concentration Step

3. At elution stage: use buffer QF warmed to 50°C; spin down precipitated DNA at 4300 × g for 15 minutes at 4°C[1]
4. Wash pellet with cold 70% ethanol; spin down at 4400 × g for 10 minutes at 4°C[1]

### Resuspension

5. Resuspend pellet in 1 ml sterile TE (10 mM Tris-HCl, 1 mM EDTA, pH 8.0) on a platform shaker overnight at room temperature[1]

## Results

| Metric | Value |
|--------|-------|
| Yield | 400–450 ng/µl |
| OD 260/280 | 1.9 |
| OD 260/230 | 2.4 |

Fragment size assessed via Femto Pulse.[1] Libraries prepared using the Ligation Sequencing Kit with read length profiling reported both with and without g-TUBE fragmentation.[1]

## Version History

- **v3** (August 2023): Updated materials required; updated QIAGEN protocol name[1]
- **v2** (June 2023): Removed reference to specific kit codes[1]
- **v1** (January 2022): Initial protocol release[1]

## Related Topics

[Human Cell Line Dna Puregene Extraction](concepts/human-cell-line-dna-puregene-extraction.md) — Alternative Oxford Nanopore protocol using QIAGEN Puregene Cell Kit (smaller scale, 5 × 10⁶ cells)
[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Blood Culture Broth Dna Extraction](concepts/blood-culture-broth-dna-extraction.md)
[Next Generation Sequencing](concepts/next-generation-sequencing.md)
