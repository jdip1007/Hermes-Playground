# Signatures of Natural Selection in Viral Phylogeny Tree Topology Shape

> **Citation:** Barzilai LP, Schrago CG. "Signatures of natural selection in tree topology shape of serially sampled viral phylogenies." *Molecular Phylogenetics and Evolution* 183 (2023): 107776. DOI: [10.1016/j.ympev.2023.107776](https://doi.org/10.1016/j.ympev.2023.107776)
> **Authors:** Lucia P. Barzilai, Carlos G. Schrago (Federal University of Rio de Janeiro, Brazil)
> **Published:** March 27, 2023 | **Received:** Nov 10, 2022 → Accepted: Mar 24, 2023

## Overview

This study investigates whether tree topology shape metrics can distinguish between different evolutionary regimes (neutral evolution, negative selection, positive selection, frequency-dependent selection) in serially sampled viral phylogenies. Using forward-time individual-based simulations and empirical HIV intrahost datasets, the authors demonstrate that tree shape metrics — particularly those derived from Laplacian spectral density analysis — are powerful, computationally efficient tools for inferring selection regimes from viral phylogenetic trees.

## Key Findings

### Four Evolutionary Regimes Successfully Distinguished
- **15 tree shape metrics** evaluated across 3 categories: (i) small configuration/asymmetry, (ii) network science-based, (iii) distance Laplacian spectral properties
- **4 evolutionary scenarios** tested: neutral (N), purifying negative selection (NS), positive selection (PS), frequency-dependent selection (FD)
- Classification error rates: 0.2% (clonal founder), 1.5% (non-clonal founder), 0.55% combined — misclassifications only between N and FD

### Most Informative Metrics
| Rank | Metric | Category | Key Discrimination |
|------|--------|----------|-------------------|
| 1 | Principal eigenvalue | Laplacian spectral | Best single metric; distinguishes all 4 regimes alone |
| 2 | Number of cherries | Small configuration | PS vs. others (PS has fewer cherries) |
| 3 | Peakedness | Laplacian spectral | N vs. FD differentiation |

### Positive Selection Signature
- Trees under PS show: **fewer** cherries, pitchforks, maximum width, eigenvector centrality, closeness centrality; **greater** Colless/Sackin indexes, maximum height, stairs, betweenness centrality, diameter
- Intuitively: positive selection creates more asymmetric, elongated trees (selective sweeps prune diversity)

### Empirical HIV Analysis
- 48% classified as frequency-dependent selection, 28% neutral, 16% negative selection, only 8% positive selection
- **88% of empirical datasets** classified as clonal founder populations — indicating very low initial genetic diversity in HIV transmission events
- Suggests most intrahost HIV evolution is driven by immune-mediated frequency-dependent dynamics or drift

### Founder Population Diversity Matters
- Two simulation approaches: **clonal** (all founders identical) vs. **non-clonal** (diverse founder pool from coalescent process)
- NS vs. neutral distinction most affected by founder diversity
- Clonal simulations more easily classified overall

## Methodology

### Simulation Framework
- **SANTA-SIM**: Individual-based, discrete-generation forward-time simulator for haploid organisms
- Population: N=1,000 individuals, 9 kb genome, μ = 2×10⁻⁵ substitutions/site/generation (empirical HIV rate)
- 500 replicates × 4 scenarios × 2 founder types = **4,000 total datasets**
- Serial sampling: 100 sequences every 10th generation over 1,000 generations

### Phylogenetic Inference
- Trees reconstructed with **IQ-TREE** using best-fit model + 1,000 ultrafast bootstrap replicates
- Incorporates phylogenetic inference error into metric evaluation (realistic approach)

### Classification Approach
- **RandomForest bagging** (randomForest R package) for multi-metric classification
- Decision trees (tree R package) for interpretable cut-off rules
- Feature importance measured by mean decrease in Gini index

## Critical Analysis

### Strengths
1. **Computationally efficient**: Tree shape metrics require minimal computation vs. intensive statistical methods — important for big data era and reducing environmental impact of bioinformatics
2. **Handles non-ultrametric trees**: Laplacian spectral methods work with serially sampled (non-ultrametric) phylogenies, unlike many traditional approaches
3. **Incorporates inference error**: Using IQ-TREE reconstructed trees rather than true simulation trees makes findings more applicable to real data
4. **Empirical validation**: HIV intrahost datasets from Los Alamos database provide ground-truth comparison

### Limitations
1. **Simulation-only framework for selection regimes**: The four fitness functions in SANTA-SIM are simplified models; real viral evolution involves complex, dynamic landscapes not captured by static fitness assignments
2. **Single virus system (HIV)**: Empirical validation limited to HIV subtype B env sequences from untreated patients — generalizability to other viruses untested
3. **No interhost data**: Study focuses exclusively on intrahost diversity; the authors note that interhost phylogenies tend to be more symmetric and carry different information (phylogeography vs. selection)
4. **Founder population unknown in practice**: While 88% of HIV datasets classified as clonal, this is an inference from tree shape — actual founder bottleneck sizes are rarely known
5. **N vs. FD ambiguity**: The hardest distinction (0.55% error rate concentrated here) suggests these regimes produce nearly indistinguishable tree shapes in some parameter ranges

### Clinical/Research Relevance
- Provides a fast, low-compute alternative to intensive phylodynamic models for initial screening of selection regime hypotheses
- Particularly useful for large-scale surveillance where computational resources are limited
- Complements rather than replaces traditional neutrality tests (Tajima's D, Fu and Li's D) which rely on sequence alignments/branch lengths and make unrealistic assumptions about RNA virus generation times

## Cross-References

See also: [Phylogenetics Phylodynamics](phylogenetics-phylodynamics.md), [Phylogenetic Tree Statistics Treestats](phylogenetic-tree-statistics-treestats.md), [Emerging Rna Viruses Genomic Adaptation](emerging-rna-viruses-genomic-adaptation.md)
