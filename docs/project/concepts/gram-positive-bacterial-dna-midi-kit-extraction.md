---
title: "Gram-Positive Bacterial DNA Extraction — QIAGEN Blood and Cell Culture DNA Midi Kit (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, microbiology, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/gram-positive-bacterial-dna-qiegen-blood-and-cell-culture-dna-midi-kit"
    title: "Gram-positive bacterial DNA – QIAGEN Blood and Cell Culture DNA Midi Kit Protocol"
    date: 2023-01-01
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated large-scale protocol for extracting genomic DNA from gram-positive bacteria using the QIAGEN Blood and Cell Culture DNA Midi Kit, optimized for downstream Nanopore long-read sequencing.[1] This protocol scales to 1 × 10¹¹ bacterial cells (~450 mg pellet), yielding 125–140 µg of HMW DNA — making it suitable for applications requiring substantial input material.[1]

## Materials

- **Input**: 1 × 10¹¹ bacterial cells (~450 mg cell pellet)[1]
- **Kit**: QIAGEN Blood and Cell Culture DNA Midi Kit[1]
- **Reagents**: RNase A, Lysozyme, isopropanol, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0)[1]
- **Consumables**: 50 ml Falcon tubes[1]
- **Equipment**: Centrifuge capable of taking 50 ml Falcon tubes, incubator/water bath[1]

## Protocol Steps

### Cell Lysis (Modified)

1. Lyse cells according to the standard QIAGEN protocol (steps 4–7, page 47), but **increase lysis time to 1 hour instead of 30 minutes for both steps 5 and 6** — this extended incubation is critical for breaking down gram-positive peptidoglycan cell walls[1]

### DNA Purification

2. Purify the lysate according to the standard protocol (steps 1–6, page 49)[1]

### DNA Recovery (Critical Step)

3. **Spool DNA instead of centrifuging** in steps 5A and 6A (page 51) — use one arm of disposable tweezers to spool[1]. Centrifugation at this stage risks shearing HMW DNA, so spooling is the recommended approach for preserving fragment length[1]

### Elution

4. Elute DNA overnight in 750 µl TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0) to maximize yield[1]

### Size Selection

5. Take ~20 µl eluate (corresponding to 3 µg DNA) and perform SPRI size selection[1]

## Results

| Metric | Value |
|--------|-------|
| Yield | 125–140 µg |
| OD 260/280 (post-SPRI) | 1.98 |
| OD 260/230 (post-SPRI) | 1.70 |

Fragment size assessed via Femto Pulse after SPRI size selection.[1] Libraries prepared using the Ligation Sequencing Kit with read length profiling reported.[1]

## Key Considerations

- **Extended lysis time** (1 hour vs standard 30 minutes for both steps) is essential for gram-positive organisms due to their thick peptidoglycan cell walls[1]
- **Spooling over centrifugation** during DNA recovery prevents mechanical shearing of HMW DNA — a critical step for preserving fragment length suitable for long-read sequencing[1]
- The OD 260/230 ratio (1.70) is slightly below the ideal ~2.0 range, suggesting possible residual contaminants from gram-positive cell wall components[1]

## Comparison with Other Gram-Positive Protocols

| Protocol | Input Scale | Yield | Kit |
|----------|-------------|-------|-----|
| This protocol (Midi Kit) | 1 × 10¹¹ cells (~450 mg) | 125–140 µg | QIAGEN Blood & Cell Culture DNA Midi Kit |
| Puregene Cell Kit protocol | 2 × 10⁹ cells (~3 mg) | 1–2 µg | QIAGEN Puregene Cell Kit + Lytic Enzyme Solution |

The Midi Kit protocol yields ~60× more DNA from ~150× more input cells, making it suitable for applications requiring bulk HMW DNA.[1]

## Related Topics

[Gram Positive Bacterial Dna Puregene Extraction](concepts/gram-positive-bacterial-dna-puregene-extraction.md) — Same sample type using QIAGEN Puregene Cell Kit (smaller scale)
[Human Cell Line Dna Genomic Tip Extraction](concepts/human-cell-line-dna-genomic-tip-extraction.md) — Similar large-scale approach for human cell lines
[Blood Culture Broth Dna Extraction](concepts/blood-culture-broth-dna-extraction.md) — Bacterial DNA extraction from blood culture broth
[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Next Generation Sequencing](concepts/next-generation-sequencing.md)
