---
title: "Gram-Positive Bacterial DNA Extraction — QIAGEN Puregene Cell Kit (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, microbiology, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/gram-positive-bacterial-dna-qiegen-puregene-cell-kit"
    title: "Gram-positive bacterial DNA – QIAGEN Puregene Cell Kit Protocol v2"
    date: 2023-01-01
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated protocol for extracting genomic DNA from gram-positive bacteria using the QIAGEN Puregene Cell Kit supplemented with Lytic Enzyme Solution, optimized for downstream Nanopore long-read sequencing.[1] Gram-positive bacteria require enzymatic cell wall digestion due to their thick peptidoglycan layer — this protocol addresses that challenge with a dedicated lysozyme-based lysis step.[1]

## Materials

- **Input**: 2 × 10⁹ bacterial cells (~3 mg cell pellet)[1]
- **Kit**: QIAGEN Puregene Cell Kit[1]
- **Reagents**: QIAGEN Lytic Enzyme Solution, RNase A Solution, Cell Lysis Solution, Protein Precipitation Solution, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0), 70% ethanol, isopropanol, nuclease-free water[1]
- **Consumables**: 2 ml Eppendorf tubes, 1.5 ml Eppendorf tubes[1]
- **Equipment**: Microfuge, shaker, magnetic rack, incubator/water bath (37°C, 80°C)[1]

## Protocol Steps

### Cell Wall Digestion and Lysis

The protocol follows the QIAGEN Puregene Handbook (steps 1–19, pages 62–63) with modifications for gram-positive organisms:[1]

1. Transfer 500 µl cell culture to a 2 ml Eppendorf tube on ice[1]
2. Centrifuge at 13,000–16,000 × g for 5 seconds; discard supernatant[1]
3. Resuspend pellet in 300 µl TE buffer by pipetting[1]
4. Add 1.5 µl Lytic Enzyme Solution; mix by inverting 25 times; incubate at 37°C for 30 minutes[1]
5. Centrifuge at 13,000–16,000 × g for 1 minute; discard supernatant[1]
6. Add 300 µl Cell Lysis Solution; mix by pipetting — **optional**: incubate at 80°C for 5 minutes for recalcitrant species[1]
7. Add 1.5 µl RNase A Solution; invert 25 times; incubate at 37°C for 1 hour[1]

### Protein Precipitation and DNA Recovery

8. Incubate on ice for 1 minute to cool rapidly[1]
9. Add 100 µl Protein Precipitation Solution; vortex vigorously for 20 seconds at high speed — **for high-polysaccharide species**: incubate on ice for 15–60 minutes before proceeding[1]
10. Centrifuge at 13,000–16,000 × g for 3 minutes; protein pellet should be tight (if not, repeat after 5 min on ice)[1]
11. Pipette 300 µl isopropanol into a clean 1.5 ml tube; carefully pour supernatant from previous step into it — avoid dislodging the protein pellet[1]
12. Mix by inverting gently 50 times[1]
13. Centrifuge at 13,000–16,000 × g for 1 minute; DNA visible as small white pellet[1]
14. Discard supernatant; drain tube on absorbent paper (pellet may be loose — handle carefully)[1]
15. Wash pellet with 300 µl 70% ethanol; invert several times[1]
16. Centrifuge at 13,000–16,000 × g for 1 minute; discard supernatant and drain on absorbent paper[1]
17. Air-dry for 5 minutes — **avoid over-drying** as DNA becomes difficult to dissolve[1]

### Elution and Size Selection

18. Elute overnight in 200 µl TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0)[1]
19. Take ~150 µl eluate (pooled from several replicates, corresponding to 3 µg DNA) and perform SPRI size selection[1]

## Results

| Metric | Value | Notes |
|--------|-------|-------|
| Yield | 1–2 µg | Per replicate; pool multiple for library prep |
| OD 260/280 (post-SPRI) | 2.15 | Within expected range |
| OD 260/230 (post-SPRI) | 7.01 | Unexpectedly high — expected ~2.0–2.2 for pure DNA; may indicate polysaccharide interference with absorbance reading |

Fragment size assessed via Femto Pulse after SPRI size selection.[1] Libraries prepared using the Ligation Sequencing Kit with read length profiling reported.[1]

## Key Considerations

- **Lytic Enzyme Solution** is essential for breaking down gram-positive peptidoglycan cell walls — this distinguishes the protocol from human cell line or gram-negative bacterial extraction workflows[1]
- **High-polysaccharide species** require extended ice incubation (15–60 minutes) after protein precipitation to prevent polysaccharide co-precipitation with DNA[1]
- **Recalcitrant species** may need 80°C heat lysis step for 5 minutes[1]
- The unexpectedly high OD 260/230 ratio (7.01 vs expected ~2.0–2.2) suggests polysaccharide contamination affecting absorbance measurements — a known challenge with gram-positive bacterial DNA extraction[1]

## Version History

- **v2** (January 2023): Updated protocol to align with QIAGEN handbook update; updated recommended Puregene extraction kit[1]
- **v1**: Initial publication[1]

## Related Topics

[Human Cell Line Dna Puregene Extraction](concepts/human-cell-line-dna-puregene-extraction.md) — Same kit used for human cell lines (no Lytic Enzyme needed)
[Blood Culture Broth Dna Extraction](concepts/blood-culture-broth-dna-extraction.md) — Bacterial DNA extraction from blood culture broth
[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Next Generation Sequencing](concepts/next-generation-sequencing.md)
