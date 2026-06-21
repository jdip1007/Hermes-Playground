---
title: "CRISPR-Cas9 Genome Editing"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [bioinformatics, technique, microbiology]
sources:
  - type: paper
    url: "PubMed"
    title: "Genome modification by CRISPR/Cas9"
    date: "2014-12"
  - type: paper
    url: "PubMed"
    title: "CRISPR-Based Gene Therapies: From Preclinical to Clinical Treatments"
    date: "2024-05"
  - type: paper
    url: "PubMed"
    title: "CRISPR/Cas9 Immune System as a Tool for Genome Engineering"
    date: "2017-06"
confidence: high
contested: false
---

# CRISPR-Cas9 Genome Editing

## Overview

CRISPR-Cas9 is a revolutionary genome editing tool adapted from bacterial adaptive immune systems [1][3]. It enables precise, programmable DNA modifications using a guide RNA (gRNA) and the Cas9 nuclease [1].

## Mechanism

1. **gRNA design** — 20nt sequence complementary to target DNA [1]
2. **Cas9 binding** — Cas9-gRNA complex scans DNA for PAM site (NGG for SpCas9) [1][3]
3. **DNA cleavage** — Double-strand break ~3bp upstream of PAM [1]
4. **Repair** — Non-homologous end joining (NHEJ, causes indels) or homology-directed repair (HDR, enables precise edits) [1]

## Key Variants

- **SpCas9** — Original Streptococcus pyogenes variant, most widely used [3]
- **SaCas9** — Smaller (Staphylococcus aureus), fits in AAV vectors [3]
- **Base editors** — C→T or A→G without double-strand breaks [1]
- **Prime editors** — Search-and-replace editing, broader edit types [1]
- **CRISPRi/a** — Repression/activation without cutting DNA [1]

## Applications

- **Functional genomics** — Gene knockouts, pooled screens [1]
- **Therapeutics** — Sickle cell disease (Casgevy approval 2023), beta-thalassemia [2]
- **Agriculture** — Disease resistance, yield improvement [1]
- **Microbiology** — Pathogen attenuation, antimicrobial resistance studies [1]
- **Diagnostics** — CRISPR-based detection (SHERLOCK, DETECTR) [1]

## Clinical Status

As of 2024, CRISPR-based therapies have received regulatory approval for sickle cell disease and beta-thalassemia [2]. Over 100 clinical trials are ongoing across oncology, genetics, and infectious disease [2].

## Challenges

- Off-target effects remain a concern [1][3]
- Delivery methods (viral vs. non-viral) [2]
- Immune responses to Cas proteins [2]
- Ethical considerations (germline editing) [2]

## Related

[Next Generation Sequencing](concepts/next-generation-sequencing.md), [Single Cell Sequencing](concepts/single-cell-sequencing.md), [Bioinformatics](concepts/bioinformatics.md)
