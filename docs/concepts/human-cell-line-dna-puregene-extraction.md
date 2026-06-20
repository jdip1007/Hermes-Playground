---
title: "Human Cell Line DNA Extraction — QIAGEN Puregene Cell Kit (Oxford Nanopore Protocol)"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [bioinformatics, technique, sequencing]
sources:
  - type: manual
    url: "https://nanoporetech.com/documents/protocols/human-cell-line-dna-qiegen-puregene-cell-kit"
    title: "Human cell line DNA – QIAGEN Puregene Cell Kit Protocol v3"
    date: 2022-12-01
confidence: high
contested: false
---

## Overview

Oxford Nanopore Technologies published a validated protocol for extracting high-molecular-weight genomic DNA from human cell lines using the QIAGEN Puregene Cell Kit, optimized for downstream Nanopore long-read sequencing.[1] The protocol yields 20–30 µg of DNA with purity ratios suitable for library preparation (OD 260/280: 1.99, OD 260/230: 2.43).[1]

## Materials

- **Input**: 5 × 10⁶ cells[1]
- **Kit**: QIAGEN Puregene Cell Kit (formerly Gentra)[1]
- **Reagents**: 70% ethanol in nuclease-free water, TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0), 1× PBS, isopropanol[1]
- **Consumables**: 15 ml Falcon tubes, 1.5 ml Eppendorf DNA LoBind tubes, wide-bore pipette tips[1]
- **Equipment**: Centrifuge with 15 ml rotor, incubator/water bath (37°C and 50°C), vortex mixer, inoculation loop or disposable tweezers for spooling[1]

## Protocol Steps

### Cell Harvesting and Washing

1. Pellet 5 × 10⁶ cells by centrifugation at 300 × g for 3 minutes; aspirate supernatant completely[1]
2. Wash pellet with 200 µl 1× PBS, centrifuge at 300 × g for 3 minutes, discard supernatant[1]

### Lysis and Protein Precipitation

3. Resuspend pellet in 2 ml Cell Lysis Solution (wide-bore tip), transfer to 15 ml Falcon tube; gently invert if clumps remain[1]
4. Incubate at 37°C for 30 minutes[1]
5. Add 700 µl Protein Precipitation Solution, vortex in three 5-second pulses[1]
6. Centrifuge at 2000 × g for 5 minutes[1]

### DNA Precipitation and Spooling

7. Transfer supernatant to new tube; add 2.5 ml room-temperature isopropanol; discard pellet[1]
8. Mix by gently inverting tube 50 times[1]
9. Spool DNA using inoculation loop or disposable tweezers[1]
10. Dip spooled DNA into 70% cold ethanol (wash step)[1]
11. Remove from ethanol, air-dry for a few seconds[1]

### Resuspension and Size Selection

12. Transfer DNA to 1.5 ml LoBind tube with 250 µl TE buffer (1 mM EDTA, pH 8.0); allow gentle dislodging from loop/tweezers[1]
13. Incubate at 50°C for 2 hours with occasional gentle inversion; verify homogeneity before quantifying[1]
14. Take 3 µg eluate and perform SPRI size selection[1]

## Results

| Metric | Value |
|--------|-------|
| Yield | 20–30 µg |
| OD 260/280 | 1.99 |
| OD 260/230 | 2.43 |

Purity ratios indicate high-quality DNA suitable for library preparation.[1] Libraries were prepared using the Ligation Sequencing Kit.[1]

## Version History

- **v3** (December 2022): Updated step 1 to include centrifuge recommendations[1]
- **v2** (November 2022): Removed "Gentra" from QIAGEN Puregene kit name; updated link[1]
- **v1**: Initial publication[1]

## Related Topics

[Nanopore Sequencing Minion](nanopore-sequencing-minion.md)
[Blood Culture Broth Dna Extraction](blood-culture-broth-dna-extraction.md)
[Lysis Buffer Components](lysis-buffer-components.md)
[Next Generation Sequencing](next-generation-sequencing.md)
