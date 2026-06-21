---
title: "Oxford Nanopore Adaptive Sampling"
summary: "Real-time read selection technology enabling targeted sequencing by accepting or rejecting DNA strands at the pore via MinKNOW software using FASTA reference and .bed file defining regions of interest"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [nanopore, adaptive-sampling, targeted-sequencing, enrichment, depletion]
sources:
  - type: protocol
    url: "https://nanoporetech.com/documents/protocols/adaptive-sampling"
    title: "Adaptive Sampling Protocol (ADS_S1016_v1_revN, Sep 2025)"
    date: 2025-09-05
confidence: high
contested: false
---

## Overview

Adaptive sampling is Oxford Nanopore's real-time read selection technology that enables targeted sequencing by accepting or rejecting DNA strands as they enter the pore.[1] Unlike amplicon-based or pull-down enrichment, it requires no upfront sample manipulation — target selection occurs during sequencing itself via MinKNOW software using a FASTA reference and .bed file defining regions of interest (ROI).[1]

## How It Works

As each strand enters a nanopore, the first ~400 bases (the "AS chunk", acquired over 1 second at 400 b/s) are basecalled and aligned to the provided reference.[1] The alignment location is checked against the .bed file: if it maps to an ROI, sequencing proceeds; if off-target, MinKNOW reverses the applied potential, ejecting the strand back to the cis side of the membrane where it can be recaptured.[1]

## Two Modes

### Enrichment Mode

- Sequences in the .bed are **accepted**; everything else is rejected[1]
- Logic: aligns in .bed → accept; outside .bed → reject; no alignment → reject[1]
- Best for targeting known genomic regions comprising <10% of total sample[1]

### Depletion Mode

- Sequences in the .bed are **rejected**; everything else is accepted[1]
- Logic: aligns in .bed → reject; outside .bed → accept; no alignment → accept[1]
- Best for enriching unknown/rare genomes by depleting known ones (e.g., host DNA in microbiome samples)[1]
- Requires targeting 95–99% of sample for rejection to achieve meaningful enrichment[1]

## Performance

- **Enrichment factor**: ~5–10× when targeting <10% of total genome[1]
- **Mean depth on MinION**: >20–40× ROI achievable with optimal settings[1]
- Targeting >10% reduces enrichment significantly due to pores spending too much time on off-target reads[1]

## Key Optimization Factors

### Library Fragmentation

Shorter fragments are strongly recommended for adaptive sampling:[1]

- **Pore blocking**: Strand rejection increases pore attrition; shorter fragments reduce blocking and extend flow cell longevity[1]
- **Efficiency**: If ROIs average 2–5 kb, a 30 kb N50 library wastes ~25–28 kb per accepted read sequencing off-target flanking sequence[1]
- **Sampling rate**: Shorter fragments allow more decision cycles per unit time — each rejection "samples" only the fragment length rather than an entire long molecule[1]

Example: For 3 kb ROIs with a 30 kb library, each accepted read takes ~75 seconds (at 400 b/s) yielding only 3 kb useful data — equivalent to ~38 missed sampling opportunities (decision time ~2 s).[1]

### Molarity-Based Loading

Load by molarity rather than mass:[1]

- **Ideal load**: 50–65 fmol per flow cell[1]
- Calculation: fragment length × 660 g/mol/bp → convert to ng for target femtomoles[1]
- Example: 6.5 kb N50 library at 50 fmol ≈ 214.5 ng[1]
- Higher DNA input (up to 600 ng with V14 chemistry) does not negatively affect runs and is advised if ligation efficiency is suboptimal[1]

### Buffer Regions

Buffer regions flank each ROI to compensate for the fact that only the first AS chunk determines acceptance:[1]

- **Recommended buffer**: ~N25 to N10 of read length distribution per side[1]
- For an 8 kb N50 library, aim for ~20 kb total buffer[1]
- Side-specific buffering (using .bed column 6 for strand direction) halves added sequence vs indiscriminate bilateral buffering[1]
- Overlapping buffers from adjacent targets are treated as a single region — no issues[1]

### Reference FASTA

Must represent the complete sample to prevent force-alignment artifacts:[1]

- Using only one chromosome causes repetitive sequences from other chromosomes to misalign, degrading enrichment[1]
- For metagenomic depletion, include all known genomes in reference[1]

## .bed File Setup

Two separate .bed files can be loaded in MinKNOW:[1]

| Location | Purpose | Content |
|---|---|---|
| Run Options → Adaptive Sampling | Controls accept/reject decisions | ROI + buffer |
| Analysis → Alignment | Real-time coverage tracking only (does not affect run) | ROI only (unbuffered) |

Validate .bed files with Bed Bugs tool before use.[1]

## Device Specifications

Adaptive sampling is computationally intensive — MinKNOW must basecall, align, and decide in real time for every captured strand.[1] Live basecalling should be disabled when running adaptive sampling on multiple flow cells to avoid decision latency affecting enrichment.[1]

## Troubleshooting Notes

- **Low enrichment**: Check total target fraction (<10% ideal), buffer size appropriateness, reference completeness[1]
- **High pore blocking**: Reduce library fragment length; perform more frequent flow cell washes[1]
- **Edge coverage drop-off**: Increase buffer size to improve minimum intra-ROI coverage at expense of average coverage[1]

## Related Topics

[Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md)
[Promethion 24Hr Genome Workflow](concepts/promethion-24hr-genome-workflow.md)
[Next Generation Sequencing](concepts/next-generation-sequencing.md)
