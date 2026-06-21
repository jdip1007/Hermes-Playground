---
title: "Rabbit Lung DNA Extraction — QIAGEN Genomic-tip with G2 Buffer (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/rabbit-lung-dna-qiegen-genomic-tip"
    title: "Rabbit lung DNA – QIAGEN Genomic-tip Protocol v2"
    date: 2023-08-14
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated protocol for extracting high-molecular-weight genomic DNA from rabbit lung tissue using the QIAGEN Blood and Cell Culture DNA Midi Kit with Genomic-tip columns, utilizing G2 buffer as the primary lysis reagent.[1] This protocol uses a single overnight Proteinase K digestion approach optimized for lung tissue structure.[1]

## Materials

- **Input**: Up to 100 mg rabbit lung tissue[1]
- **Kit**: QIAGEN Blood and Cell Culture DNA Midi Kit[1]
- **Reagents**: QIAGEN Proteinase K, RNase A (100 mg/ml), G2 buffer, 70% ethanol in nuclease-free water, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0), isopropanol[1]
- **Consumables**: 15 ml Falcon tubes, 1.5 ml Eppendorf DNA LoBind tubes[1]
- **Equipment**: Centrifuge with 15 ml rotor, incubator/water bath (50°C), tweezers and scalpel[1]

## Protocol Steps

### Lysis Buffer Preparation

1. Add 19 µl RNase A (100 mg/ml) to a 15 ml Falcon tube, then add 9.5 ml G2 buffer[1]

### Tissue Homogenization

2. Grind up to 100 mg lung tissue using tweezers and scalpel; transfer resulting pulp to the Falcon tube containing ATL buffer[1]. Alternative homogenization methods (liquid nitrogen/mortar & pestle, TissueRuptor) are mentioned but **not validated** by Oxford Nanopore for this tissue type[1]

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

| Metric | Value |
|--------|-------|
| Yield | ~50 µg |
| OD 260/280 | 1.91 |
| OD 260/230 | 2.43 |

Purity ratios indicate high-quality DNA suitable for library preparation.[1] Libraries prepared using the Ligation Sequencing Kit with read length profiling reported.[1] Flow cell output can be increased by performing a flow cell wash step when data acquisition rate deteriorates due to pore accumulation in "unavailable" or "recovering" state, then adding new library.[1]

## Key Considerations

- **Single overnight Proteinase K digestion** with G2 buffer provides efficient tissue breakdown for lung samples[1]
- **Manual homogenization** (tweezers + scalpel) is the validated method — alternative approaches like liquid nitrogen grinding or TissueRuptor are not validated for rabbit lung by Oxford Nanopore[1]
- **Homogeneity check before column loading** prevents Genomic-tip blockage — a critical quality control step specific to this protocol[1]
- **2-hour elution at 50°C** maximizes DNA recovery from the Genomic-tip matrix[1]

## Comparison with ATL Buffer Protocol

| Parameter | G2 Buffer Protocol | ATL Buffer Protocol |
|-----------|-------------------|---------------------|
| Yield | ~50 µg | ~50 µg |
| OD 260/280 | 1.91 | 1.94 |
| OD 260/230 | 2.43 | 2.55 |
| Proteinase K | Single overnight incubation (250 µl) | Two-stage: overnight + 30 min secondary (50 µl each stage) |
| Lysis Buffer Volume | 9.5 ml single addition | 1 ml initial + 9 ml secondary |

Both protocols yield similar amounts of DNA from rabbit lung tissue, with the G2 buffer protocol being simpler (single incubation step) while the ATL buffer protocol uses a two-stage digestion approach.[1]

## Version History

- **v2** (August 14, 2023): Updated URL link[1]
- **v1** (February 11, 2019): Initial protocol publication[1]

## Related Topics

[Rabbit Lung Dna Atl Buffer Extraction](concepts/rabbit-lung-dna-atl-buffer-extraction.md) — Same sample type using ATL buffer with two-stage digestion
[Rabbit Muscle Dna Genomic Tip Extraction](concepts/rabbit-muscle-dna-genomic-tip-extraction.md) — Rabbit muscle extraction using G2 buffer
[Rabbit Skin Dna Genomic Tip Extraction](concepts/rabbit-skin-dna-genomic-tip-extraction.md) — Rabbit skin extraction using G2 buffer
[Human Cell Line Dna Genomic Tip Extraction](concepts/human-cell-line-dna-genomic-tip-extraction.md) — Similar Genomic-tip approach for human cell lines
[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Next Generation Sequencing](concepts/next-generation-sequencing.md)
