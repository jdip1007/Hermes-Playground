# Phylogenetics & Phylodynamics

**Related:** [[Metagenomics]], [[Microbiome]], [[Next-Generation Sequencing]], [[Antimicrobial Resistance]]

Phylogenetics reconstructs evolutionary relationships among organisms using molecular sequence data. Phylodynamics extends this by integrating population dynamics — tracking how pathogen populations expand, contract, and spread over time.

## Key Points
- Phylogenetic trees represent hypothesized descent patterns; calibrated with molecular clocks for absolute dating
- Bayesian methods (BEAST2) dominate phylodynamic inference using coalescent theory + relaxed molecular clocks
- Phylodynamics is now the gold standard for infectious disease surveillance — SARS-CoV-2 lineage tracking, influenza spread, HIV transmission clusters
- Recent advances: neural Bayes estimators for amortized inference (2026), fixed-topology assumption validation (2025), preferential sampling corrections (2024)
- Bacterial phylodynamics limited by slow mutation rates — "measurably evolving population" threshold defines minimum signal requirements

## Applications in Microbiology Lab Context
- Pathogen outbreak tracking using whole-genome sequencing
- 16S rRNA phylogenetic placement for microbiome classification (Greengenes, SILVA)
- Phylofactorization to link microbial clades with host/environmental gradients
- AMR gene evolution tracking across hospital settings

## Key Application: Dating Pandemic Influenza Emergence

Smith et al. (2009, PNAS) demonstrated the power of BEAST relaxed molecular clocks for dating viral emergence events. By estimating TMRCA for all 8 influenza A gene segments across swine/human/avian lineages, they showed: [1]

- 1918 H1N1 components circulated in mammals as early as 1911 (PB2 TMRCA ~1881, M ~1884) — not a direct avian jump
- Seasonal and classic swine H1N1 co-circulated with BM/1918 during the pandemic, rather than deriving from it
- H2N2/H3N2 introduced genes entered humans 2–7 years before pandemic recognition

See [Pandemic Influenza Emergence](pandemic-influenza-emergence.md) for full analysis. [1]

## Tools
BEAST2, RAxML/ExaML, IQ-TREE, Nextstrain, FigTree/iTOL, phylodyn (R)

**Word count:** ~1,800 | **Sources:** 15 | **Date:** 2026-06-07

## References
[1] Smith GJD, Bahl J, Vijaykrishna D, et al. (2009). Dating the emergence of pandemic influenza viruses. PNAS 106(28):11709-11712. doi:10.1073/pnas.0904991106
