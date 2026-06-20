---
title: "Rabbit Skin DNA Extraction — QIAGEN Genomic-tip (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/rabbit-skin-dna-qiegen-genomic-tip"
    title: "Rabbit skin DNA – QIAGEN Genomic-tip Protocol v2"
    date: 2023-08-14
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated protocol for extracting high-molecular-weight genomic DNA from rabbit skin tissue using the QIAGEN Blood and Cell Culture DNA Midi Kit with Genomic-tip columns, optimized for downstream Nanopore long-read sequencing.[1] Skin tissue presents unique challenges due to its dense keratin structure and connective tissue composition — this protocol addresses those with extended overnight Proteinase K digestion at 50°C and a critical homogeneity check before column loading.[1]

## Materials

- **Input**: Up to 100 mg rabbit skin tissue[1]
- **Kit**: QIAGEN Blood and Cell Culture DNA Midi Kit[1]
- **Reagents**: QIAGEN Proteinase K, RNase A (100 mg/ml), G2 buffer, 70% ethanol in nuclease-free water, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0), isopropanol[1]
- **Consumables**: 15 ml Falcon tubes, 1.5 ml Eppendorf DNA LoBind tubes[1]
- **Equipment**: Centrifuge with 15 ml rotor, incubator/water bath (50°C), tweezers and scalpel[1]

## Protocol Steps

### Lysis Buffer Preparation

1. Add 19 µl RNase A (100 mg/ml) to a 15 ml Falcon tube, then add 9.5 ml G2 buffer[1]

### Tissue Homogenization

2. Grind up to 100 mg skin tissue using tweezers and scalpel; transfer resulting pulp to the Falcon tube containing ATL buffer[1]. Alternative homogenization methods (liquid nitrogen/mortar & pestle, TissueRuptor) are mentioned but **not validated** by Oxford Nanopore for this tissue type[1]

### Proteinase K Digestion

3. Add 250 µl Proteinase K; vortex thoroughly — efficient mixing is critical for complete lysis[1]
4. Incubate overnight at 50°C[1]

### Homogeneity Check (Critical Step)

5. If lysate is not homogenous or tissue pieces remain visible: centrifuge at 2000 × g for 10 minutes at 4°C; discard pellet and retain supernatant[1]. **Non-homogeneous lysate will block the Genomic-tip column** — this step must be performed before proceeding[1]

### DNA Purification

6. Purify lysate according to QIAGEN Genomic-tip protocol (steps 1–6, pages 49–52)[1]

### Elution (Critical Step)

7. Elute for 2 hours at 50°C using 150 µl TE buffer (1 mM EDTA, pH 8.0), occasionally mixing by gentle inversion to maximize yield[1]

### Size Selection

8. Take 3 µg eluate and perform SPRI size selection[1]

## Results

| Metric | Value | Notes |
|--------|-------|-------|
| Yield | 30–60 µg | Higher than muscle tissue protocols |
| OD 260/280 | 1.95 | Within acceptable range |
| OD 260/230 | 3.99 | **Not representative of good quality** — likely reagent carry-over from extraction or SPRI purification step |

Purity ratios indicate generally suitable DNA for library preparation, though the elevated OD 260/230 ratio suggests potential contamination.[1] Libraries prepared using the Ligation Sequencing Kit with read length profiling reported.[1] Flow cell output can be increased by performing a flow cell wash step when data acquisition rate deteriorates due to pore accumulation in "unavailable" or "recovering" state, then adding new library.[1]

## Key Considerations

- **Manual homogenization** (tweezers + scalpel) is the validated method — alternative approaches like liquid nitrogen grinding or TissueRuptor are not validated for rabbit skin by Oxford Nanopore[1]
- **Overnight Proteinase K digestion at 50°C** is essential for breaking down dense keratin and connective tissue structure in skin samples[1]
- **Homogeneity check before column loading** prevents Genomic-tip blockage — a critical quality control step specific to this protocol[1]
- **2-hour elution at 50°C** maximizes DNA recovery from the Genomic-tip matrix[1]
- The unexpectedly high OD 260/230 ratio (3.99 vs expected ~2.0) indicates potential reagent carry-over — consider additional wash steps if purity is critical for downstream applications[1]

## Comparison with Other Rabbit Tissue Protocols

| Parameter | Skin (G2 Buffer) | Muscle (G2 Buffer) | Muscle (ATL Buffer) |
|-----------|------------------|-------------------|---------------------|
| Yield | 30–60 µg | 30–50 µg | 10–20 µg |
| OD 260/280 | 1.95 | 2.06 | 1.99 |
| OD 260/230 | 3.99* | 2.68 | 2.96 |
| Proteinase K | Single overnight | Single overnight | Two-stage (overnight + 30 min) |

*Note: Skin protocol shows elevated OD 260/230 ratio, likely due to reagent carry-over rather than true DNA purity.[1]

## Version History

- **v2** (August 14, 2023): Updated URL link[1]
- **v1** (February 11, 2019): Initial protocol publication[1]

## Related Topics

[Rabbit Muscle Dna Genomic Tip Extraction](rabbit-muscle-dna-genomic-tip-extraction.md) — Same approach for rabbit muscle tissue using G2 buffer
[Rabbit Muscle Dna Atl Buffer Extraction](rabbit-muscle-dna-atl-buffer-extraction.md) — Rabbit muscle extraction using ATL buffer with two-stage digestion
[Human Cell Line Dna Genomic Tip Extraction](human-cell-line-dna-genomic-tip-extraction.md) — Similar Genomic-tip approach for human cell lines
[Nanopore Sequencing Minion](nanopore-sequencing-minion.md)
[Next Generation Sequencing](next-generation-sequencing.md)
