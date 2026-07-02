---
title: "Single-Stranded DNA Binding Protein (SSB)"
summary: "Class of proteins binding ssDNA/ssRNA; E. coli SSB tetramer used as fluorescent biosensor for mRNA quantification in vitro transcription assays"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [biochemistry, protein, ssDNA, biosensor, transcription, E. coli, RNA polymerase]
sources:
  - type: paper
    url: "https://doi.org/10.1016/j.bbrc.2018.01.147"
    title: "Application of the SSB biosensor to study in vitro transcription"
    authors: "Cook, Hari-Gupta, Toseland"
    date: 2018-01-31
  - type: web
    url: "https://en.wikipedia.org/wiki/Single-stranded_binding_protein"
    title: "Single-stranded binding protein — Wikipedia"
    date: 2026-07-02
  - type: web
    url: "https://en.wikipedia.org/wiki/Replication_protein_A"
    title: "Replication protein A — Wikipedia"
    date: 2026-07-02
confidence: medium
contested: false
---

## Overview

Single-stranded binding proteins (SSBs) are a class of proteins found across all domains of life — from bacteria to humans, including viruses.[2] Their primary function is binding to single-stranded nucleic acids (ssDNA or ssRNA), preventing secondary structure formation and protecting the strand from nuclease degradation during replication, repair, and recombination.[3][2]

The best-characterized member is *E. coli* SSB, a homotetramer of ~19 kDa subunits that binds ssDNA with low nanomolar affinity (Kd ~low nM).[3] Recent work has repurposed fluorescently labeled SSB as a biosensor for direct mRNA quantification in vitro transcription assays, eliminating the need for RNA purification or radioactive labeling.[2]

## Structure and Classification

### Bacterial SSB (*E. coli*)

- **Quaternary structure:** Homotetramer of 175-amino-acid subunits (~19 kDa each)[2][1]
- **Domain architecture:** Three beta-strands forming a single six-stranded beta-sheet per monomer; dimers form the functional tetramer[3]
- **Binding mode:** Wraps around ssDNA via tryptophan-rich binding clefts (Trp54 and Phe60 directly involved in nucleic acid contact)[1]
- **Mutation G26C:** Engineered cysteine at position 26 for site-specific fluorophore labeling; does not affect DNA binding or tetramer formation[1]

### Eukaryotic equivalents

No sequence homology exists between bacterial SSB and eukaryotic nuclear ssDNA-binding proteins, but functional parallels are clear:

- **Replication Protein A (RPA):** Heterotrimer (RPA70/RPA32/RPA14) with six OB-folds; binds ssDNA during replication, recombination, and nucleotide excision repair[3]
- **Mitochondrial SSB (mtSSB/SSBP1 in humans, RIM1 in yeast):** Tetrameric structure with sequence similarity to bacterial SSB; binds single-stranded mitochondrial DNA[3]

### Viral SSB

Herpes simplex virus ICP8 is a 128 kDa zinc metalloprotein with distinct head-neck-shoulder architecture; required for viral DNA replication during lytic infection.[3]

## Mechanism of Action

SSB proteins coat exposed ssDNA at replication forks, preventing:
- Self-annealing (re-hybridization) of complementary strands[3]
- Secondary structure formation (hairpins, G-quadruplexes)[3]
- Nuclease attack on unprotected single-stranded regions[3]

This creates a nucleoprotein filament that serves as a platform for recruiting downstream factors — helicases, polymerases, and recombinases like Rad51.[3]

## SSB as mRNA Biosensor (MDCC-SSB)

### Principle

The *E. coli* SSB G26C mutant labeled with the environmentally sensitive fluorophore MDCC (N-[2-(1-maleimidyl)ethyl]-7-diethylaminocoumarin-3-carboxamide) exhibits fluorescence enhancement upon binding ssRNA, enabling direct mRNA quantification without purification.[1]

### Key findings from Cook et al. (2018)[1]

**Binding characterization:**
- SSB binds ssRNA70 with kinetics indistinguishable from ssDNA70 in EMSA assays[1]
- Tryptophan fluorescence quenching: 50% quench for ssDNA; similar response for ssRNA but weaker apparent affinity (Kd ~200 nM vs. low nM for ssDNA)[1]
- SSB prefers ssDNA over ssRNA, consistent with prior reports[1]

**Fluorescence biosensor:**
- MDCC-SSB shows 1.9-fold fluorescence increase with excess ssDNA70 and 2.1-fold with ssRNA70[1]
- Linear response between fluorescence intensity and mRNA concentration over two orders of magnitude[1]
- Calibration against known ssRNA70 concentrations allows conversion to SSB binding sites (65-base units)[1]

**Advantages over conventional methods:**
| Method | Limitation | MDCC-SSB advantage |
|--------|-----------|-------------------|
| Gel electrophoresis | Qualitative only, requires high yield | Quantitative, works at low yields |
| UV spectroscopy | Requires purification to remove protein/DNA contamination | Direct addition to crude reaction mix |
| RT-qPCR | Multi-step, amplification bias, product loss during isolation | Single-step, no amplification needed |
| Radioactive labeling | Safety concerns, disposal costs | Non-radioactive fluorophore |
| Qubit/fluorescent dyes | Expensive reagents, dedicated instruments | Low-cost protein-based sensor |

**Application — Myosin VI and transcription:**
- Antibody depletion of myosin VI from HeLaScribe extracts: 60% decrease in MDCC-SSB fluorescence (matching RT-qPCR results)[1]
- Small molecule inhibitor TIP (25 mM): 70% decrease in transcription, consistent with prior findings[1][1]
- In vivo validation: MCF-7 cells treated with TIP showed decreased expression of ESR1, ACTB, PS2, and GREB1 genes — more dramatic than myosin VI knockdown alone (suggesting compensatory rescue by other proteins like myosin IC)[1][1]

## Applications

### Current uses
- **In vitro transcription quantification:** Direct mRNA measurement without purification[1]
- **Helicase activity assays:** Real-time fluorescence monitoring of DNA unwinding (Dillingham et al. 2008)[1]
- **Single-molecule studies:** Visualizing helicase processivity at the single-molecule level[1][1]

### Potential extensions
- RNA helicase activity assays[1]
- Other RNA processing enzyme characterization[1]
- Comparative transcription factor screening[1]

## Caveats and Limitations

- **Substrate preference:** SSB binds ssDNA with higher affinity than ssRNA (Kd ~200 nM for RNA vs. low nM for DNA)[1][1]
- **Stoichiometry ambiguity:** Saturation concentration differs between ssDNA and ssRNA — may reflect different binding modes (e.g., 35-base vs. 65-binding site) or affinity differences; not fully resolved[1]
- **Calibration required for quantification:** Qualitative comparisons work without calibration, but absolute mRNA concentrations require standard curves with known ssRNA amounts[1]
- **Not suitable for double-stranded RNA or DNA:** SSB specifically binds single-stranded nucleic acids

## Related Topics

*Replication Protein A (RPA) — Eukaryotic nuclear equivalent of bacterial SSB*
*DNA replication — Process where SSB plays a critical role at the replication fork*
*RNA polymerase II — Transcription enzyme studied using MDCC-SSB biosensor*
*Myosin VI — Nuclear motor protein that enhances RNAPII transcription*
