---
title: "High Output Long Read Sequencing from Human Blood"
summary: "Flow cell wash/reload method for increased long-read data from human blood with minimal cost, scaling to 48 genomes in 72 hours on PromethION 48"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [nanopore, human-blood, high-output, promethion]
sources:
  - type: protocol
    url: "https://nanoporetech.com/documents/protocols/high-output-extraction-method"
    title: "High output long read sequencing from human blood (en-2)"
    date: null
confidence: high
contested: false
---

## Overview

Method for obtaining increased long-read sequence data from human blood with minimal additional cost.[1] Scales to parallel processing — using all 48 positions on PromethION 48 generates 48 human genomes at 30× coverage with read N50 >20 kb every 72 hours.[1]

## Key Approach

- Start with 1 ml human blood (K₂-EDTA), extract with QIAGEN Puregene Blood Kit[1]
- Final library: 1–2 µg DNA split into 3 aliquots[1]
- Sequence each aliquot sequentially on one PromethION flow cell, washing between loads using Flow Cell Wash Kit (EXP-WSH004)[1]
- Internal testing yielded **extra 25% sequencing data** vs non-washed/re-loaded runs[1]

## Related Topics

[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Buffy Coat Dna Extraction](concepts/buffy-coat-dna-extraction.md)
[Dry Blood Spots Dna Extraction](concepts/dry-blood-spots-dna-extraction.md)

