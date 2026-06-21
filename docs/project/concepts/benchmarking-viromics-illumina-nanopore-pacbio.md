---
title: "Benchmarking Viromics: Illumina vs Nanopore vs PacBio"
created: "2026-06-08"
updated: "2026-06-08"
type: concept
tags: [viromics, benchmarking, Illumina, nanopore, PacBio, bacteriophage, metagenomics, assembly]
sources:
  - type: paper
    url: "https://doi.org/10.1099/mgen.0.001198"
    title: "The long and short of it: benchmarking viromics using Illumina, Nanopore and PacBio sequencing technologies"
    authors: "Cook R, Brown N, Rihtman B, Michniewski S, Redgwell T, Clokie M, Stekel DJ, Chen Y, Scanlan DJ, Hobman JL, Nelson A, Jones MA, Smith D, Millard A"
    journal: "Microbial Genomics"
    date: "2024-02-20"
confidence: high
---

# Benchmarking Viromics: Illumina vs Nanopore vs PacBio

## Overview

This is the **first comprehensive head-to-head benchmark** comparing Illumina, Oxford Nanopore (ONT), and PacBio sequencing technologies for viral metagenomics (viromics). Using a mock bacteriophage community of 15 previously sequenced phage genomes, the study evaluates genome recovery rates, error profiles, assembly algorithms, and downstream impacts on diversity estimation [1].

## Study Design

- **Mock community**: 15 bacteriophage genomes spanning 44–320 kb, GC content 38–61% [1]
- **Abundance range**: 169,000 to 684 million genome copies (deliberate diversity) [1]
- **Sequencing platforms**: Illumina MiSeq (2×250 bp), ONT MinION (R9.4.1), PacBio Sequel I [1]
- **Assembly algorithms tested**: SPAdes (Illumina), Flye, Unicycler, Canu, wtdbg2 (long-read) [1]
- **Viral prediction tools**: VIBRANT and DeepVirFinder [1]

## Key Findings

### Genome Recovery by Platform
| Approach | Complete Genomes Recovered | SNP Error Rate vs Illumina | INDEL Error Rate vs Illumina |
|----------|---------------------------|---------------------------|------------------------------|
| **Illumina only (SPAdes)** | Best recovery | Baseline (lowest) | Baseline (lowest) |
| ONT only (Flye, best) | Max 1 complete genome | **+41% higher** | **+157% higher** |
| PacBio only (Flye, best) | Max 1 complete genome | +12% higher | +78% higher |
| **ONT+Illumina hybrid (Unicycler)** | Most genomes recovered | Comparable to Illumina-only | Comparable to Illumina-only |
| PacBio+Illumina hybrid | Improved but less than ONT+Illumina | Reduced errors | Reduced errors |

### Critical Technical Findings
1. **High coverage hurts long-read assembly**: Very high read depth of specific genomes was detrimental — subsampling reads (50–100×) produced longest contigs [1]
2. **Polishing reduces errors to Illumina levels**: Adding Illumina short-reads to polish ONT/PacBio assemblies reduced SNPs and INDELs to comparable levels with Illumina-only [1]
3. **Assembler matters significantly for long-reads**: Flye outperformed wtdbg2 and Unicycler for ONT data; PacBio could not be assembled by Unicycler at all [1]
4. **ssDNA phage bias from MDA**: PhiX174 (ssDNA) undetectable in any long-read sample — consistent with known MDA amplification biases [1]

### Impact on Diversity Estimation
- Illumina and hybrid approaches generally **underestimated** diversity but were closer to true values than long-read-only [1]
- ONT+Unicycler gave closest estimate of true mock community diversity among long-read-only methods [1]
- Choice of sequencing technology had downstream impacts on gene prediction, viral prediction, and alpha diversity metrics (Shannon/Simpson indices) [1]

## Critical Analysis

### Strengths ✅
✅ **First comprehensive viromics benchmark** — fills critical gap in literature [1]  
✅ **Mock community design** — known ground truth enables rigorous evaluation [1]  
✅ **Multiple assemblers tested** — practical guidance for algorithm selection [1]  
✅ **Downstream impact analysis** — connects technical metrics to biological interpretation [1]  
✅ **Open data**: All reads deposited at ENA (PRJEB56639), assemblies on FigShare [1]  

### Limitations ⚠️
⚠️ **Bacteriophage-only mock community** — results may not generalize to eukaryotic viruses [1]  
⚠️ **R9.4.1 flow cells used for ONT** — newer R10 chemistry would likely improve error rates [1]  
⚠️ **MDA amplification bias** — required for long-read input but distorts abundance estimates [1]  
⚠️ **PacBio yield lower than ONT** — may have unfairly disadvantaged PacBio comparison [1]  
⚠️ **No clinical/environmental samples tested** — mock community lacks complexity of real viromes [1]  

### Unanswered Questions ❓
❓ How do these findings translate to eukaryotic viral metagenomics? [1]  
❓ Impact of R10 flow cells and newer basecallers on ONT performance? [1]  
❓ Performance with PacBio HiFi reads (not available at time of study)? [1]  
❓ Optimal digital normalization strategies for virome assembly? [1]  

## Recommendations from Authors

1. **Single platform**: Use Illumina — best genome recovery, lowest error rates [1]
2. **Hybrid approach**: ONT+Illumina with Unicycler — best overall assemblies [1]
3. **Polishing essential**: Always polish long-read assemblies with short reads [1]
4. **Downsample long reads**: 50–100× coverage optimal for phage assembly [1]
5. **Match assembler to platform**: Flye for ONT, avoid Unicycler for PacBio [1]

## Cross-References

- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — broader NGS technology comparison
- [Metagenomics](concepts/metagenomics.md) — general metagenomic approaches and workflows
- [Nanopore Sequencing Minion](concepts/nanopore-sequencing-minion.md) — MinION platform overview
- [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md) — clinical viromics applications

## Confidence Assessment

**High confidence** in core benchmarking results based on:
- Rigorous mock community design with known ground truth [1]
- Comprehensive comparison across 3 platforms and 5 assemblers [1]
- Peer-reviewed publication (Microbial Genomics, Microbiology Society 2024) [1]
- Open data deposition at ENA [1]

**Moderate confidence** in generalizability due to:
- Bacteriophage-only focus — eukaryotic viruses may behave differently [1]
- R9.4.1 ONT chemistry — newer platforms would improve results [1]
- MDA amplification bias — real viromes without MDA may differ [1]
