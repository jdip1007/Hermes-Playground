# Phylogenetic Tree Statistics: The `treestats` R Package

> **Source:** Janzen T, Etienne RS (2024). "Phylogenetic tree statistics: A systematic overview using the new R package 'treestats'." *Molecular Phylogenetics and Evolution* 200:108168. DOI: [10.1016/j.ympev.2024.108168](https://doi.org/10.1016/j.ympev.2024.108168)
> **Tags:** phylogenetics, tree statistics, R package, diversification, balance metrics

## Overview

Janzen & Etienne (2024) introduce `treestats`, an R package providing fast C++-based implementations of 70 phylogenetic summary statistics [1]. The study systematically evaluates correlations between these statistics across both empirical trees (221 family-level phylogenies spanning birds, mammals, fish, amphibians, ferns, and flowering plants) and simulated trees under four diversification models. Key findings reveal that most statistics are highly correlated with tree size, three major clusters of correlated statistics exist, and balance is a multidimensional rather than one-dimensional property of phylogenetic trees [1].

## The 70 Summary Statistics

Statistics are classified by information source:

### Node Statistics (1–20)
Measure properties at branching nodes (L = left daughter tips, R = right daughter tips) [1]:
- **Colless index** (abs(L−R)), corrected Colless, quadratic Colless — imbalance measures [1, 2]
- **Blum statistic**, Rogers J index, equal weights Colless
- **Cherries** (L+R=2), pitchforks (L+R=3), double cherries, fourprong — shape metrics
- **Stairs/stairs2 measures**, ILnumber, Rquartet index, I statistic, J1, Beta distribution
- **Average/maximum ladder measures** — caterpillar-like topology detection

### Depth Statistics (21–33)
Based on node/tip depth from root [1]:
- Maximum depth, Sackin index, average leaf depth, total path length
- Variance of leaves' depth, B1/B2 statistics, symmetry nodes index
- Width-based: maximum width, max difference in widths, Mw/Md ratio

### Distance Matrix (34–40)
Pairwise distances between tips [1]:
- Total cophenetic index, area per pair index
- Mean pairwise distance (MPD), variance in pairwise distance
- J statistic, mean nearest taxon distance, phylogenetic species variability (PSV)

### Eigen Decompositions (41–48)
Spectral properties of tree matrices [1]:
- Distance Laplacian spectrum: principal eigenvalue, eigen gap, asymmetry, peakedness
- Raw Laplacian matrix: min/max eigenvalues
- Adjacency matrix: min/max eigenvalues

### Network Science (49–55)
Graph-theoretic measures on unrooted trees [1, 3]:
- Wiener index, diameter, maximum betweenness/closeness/eigencentrality
- Weighted variants using branch lengths

### Branching Times (56–60)
Temporal information from ultrametric trees [1]:
- Crown age, tree height, Pybus & Harvey's gamma statistic
- Pigot's rho (diversification slope), nLTT (lineage-through-time alignment)

### Branch Lengths (61–68)
Distribution of branch lengths ignoring topology [1]:
- Phylogenetic diversity, mean/variance of branch lengths
- External vs. internal branch length statistics
- Treeness statistic (internal/external ratio)

### New Statistic: Imbalance Steps (70) [1]
Number of steps to transform a tree from fully balanced to fully imbalanced by re-attaching branches to one crown lineage. Normalized as N − log₂(N) − 1 for tree size correction.

## Key Findings

### Three Major Clusters of Correlated Statistics [1]

Across both empirical and simulated trees, statistics group into three large clusters:

1. **Balance cluster**: Colless, Sackin, J1, depth-related statistics
2. **Shape cluster**: Cherries, pitchforks, ladders, stairs metrics, beta, Rogers statistic
3. **Branch length/timing cluster**: Mean branch length, gamma, mean pairwise distance, nLTT

Three outlier statistics resist clear clustering: Laplacian spectrum eigen gap, minimum adjacency matrix eigenvalue, and weighted eigencentrality — suggesting they capture unique information not shared by other metrics.

### Tree Size Problem [1]

**Almost all summary statistics correlate with tree size**, even after normalization:
- Only cherries, pitchforks, and rquartet adequately correct for tree size across all models
- Colless, Sackin, total cophenetic index correct only under Yule model assumptions
- **Recommendation**: Use tree size as a covariate rather than relying on self-normalization

### Balance Is Multidimensional [1]

Using five imbalancing algorithms (A-R, A-O, T-R, T-Y, T-O) to generate trees of intermediate balance:

- Almost all statistics vary **non-linearly** with balance
- Nine statistics show **non-monotonic** relationships: avg_ladder, double cherries, ew_colless, four_prong, max_betweenness, pitchforks, rogers, stairs, symmetry nodes
- Only diameter and max_depth show linear relationships with intermediate balance
- Different imbalancing algorithms produce different trajectories — balance is not one-dimensional

### Numerical Balance Verification [1]

Using the imbalancing algorithm as a test:
- **Balance statistics** (increase with balance): imbalance steps, J1, J statistic, mean internal branch length, mean pairwise distance, PSV, treeness
- **Imbalance statistics** (decrease with balance): mean external branch length, mean nearest taxon distance, variance in branch length

### Information Content Analysis [1]

Statistics with lowest average correlation (most unique information):
- Empirical trees: weighted eigencentrality, Pigot's rho, Laplacian spectrum components
- Simulated trees: gamma, nLTT, four prong

## Methodology

### Implementation [1]
- C++ implementations via Rcpp for speed optimization (orders of magnitude faster than existing packages)
- 98% code coverage through test-driven development
- Minimal dependencies: ape, Rcpp, nloptR only
- Available on CRAN, GitHub, and Zenodo

### Empirical Data [1]
221 family-level phylogenies from seven taxonomic groups (birds: 122 trees, amphibians: 45, ray-finned fish: 42, mammals: 24, cartilaginous fish: 5, ferns: 7, flowering plants: 7). Trees selected with ≥80% species coverage and ≥10 tips.

### Simulated Data [1]
300,000 trees per model (1.2M total) under four diversification models:
- Constant-rate birth-death (BD)
- Diversity-dependent diversification (DDD)
- Protracted birth-death (PBD)
- Binary state-dependent diversification (SSE/BiSSE)

All simulated conditional on 300 extant tips and crown age of 10 My.

## Critical Analysis

### Strengths

1. **Comprehensive benchmark**: First systematic comparison of 70 statistics across both empirical and simulated data
2. **Computational efficiency**: C++ implementations make large-scale analysis feasible; critical for applications in [[selection-signatures-viral-phylogeny-shape]] where tree shape metrics must be computed rapidly on many trees
3. **Practical recommendations**: Clear guidance on statistic selection to minimize intercorrelation
4. **New methodology**: Imbalance steps statistic and imbalancing algorithms provide tools for studying intermediate balance

### Limitations

1. **Ultrametric/binary restriction**: Statistics apply only to ultrametric, time-calibrated, strictly bifurcating trees — excludes many viral phylogenies which are non-ultrametric due to serial sampling
2. **No within-virus application tested**: Empirical data from macroevolutionary (species-level) trees; applicability to intrahost viral phylogenies not directly validated
3. **Correlation ≠ causation**: Cluster structure reveals information overlap but does not identify which statistics best discriminate specific evolutionary processes

### Practical Recommendations from Authors

- Pick statistics from different clusters: e.g., Colless + cherries + phylogenetic diversity
- Include at least one low-correlation statistic (weighted eigencentrality, Pigot's rho)
- For balance assessment: use max_depth (linear with intermediate balance)
- Use tree size as covariate rather than relying on normalization

## Connections to Other Work

- [[selection-signatures-viral-phylogeny-shape]] — Barzilai & Schrago (2023) apply 15 of these metrics to distinguish selection regimes in viral phylogenies; principal eigenvalue and cherries were most informative
- [Rna Virus Macroevolution](concepts/rna-virus-macroevolution.md) — Kitchen et al. (2010) family-level phylogeny analysis could benefit from treestats balance metrics to quantify tree shape patterns
- [Phylogenetics Phylodynamics](concepts/phylogenetics-phylodynamics.md) — Gamma statistic (Pybus & Harvey, 2000) included in treestats; used for detecting population growth/decline in pathogen phylogenies

## References

1. Janzen T, Etienne RS (2024). Phylogenetic tree statistics: A systematic overview using the new R package 'treestats'. *Mol Phylogenet Evol* 200:108168. DOI: 10.1016/j.ympev.2024.108168
2. Fischer M, et al. (2023). Tree Balance Indices: A Comprehensive Survey. Springer Nature
3. Chindelevitch L, et al. (2021). Network science inspires novel tree shape statistics. *PLoS ONE* 16:e0259877
