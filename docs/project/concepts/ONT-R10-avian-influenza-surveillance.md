---
title: Oxford Nanopore R10 Chemistry for Avian Influenza Genomic Surveillance
created: "2026-06-15"
updated: "2026-06-15"
type: concept
tags: [nanopore, avian-influenza, HPAI, sequencing-chemistry, pandemic-preparedness, Cambodia]
sources:
  - Ratcliff et al., Microbiology Spectrum (2024), doi:10.1128/spectrum.01880-24
confidence: high
---

# Oxford Nanopore R10 Chemistry for Avian Influenza Genomic Surveillance

## Overview

This study provides a **head-to-head comparison** of Oxford Nanopore R9.4.1 vs R10.4.1 sequencing chemistries for influenza A virus characterization, with particular focus on resolving the biologically critical hemagglutinin (HA) multibasic cleavage site — a homopolymer region that distinguishes highly pathogenic avian influenza viruses (HPAIV) [1]. The work addresses a key limitation of earlier Nanopore chemistry and validates R10 for real-time HPAI surveillance in resource-limited settings [1].

## Study Design

- **Samples**: 45 influenza A virus isolates from Cambodia [1]
  - Human seasonal influenza (positive controls)
  - Avian influenza: low-pathogenic and highly pathogenic strains (H5Nx focus)
- **Collection sites**: Institut Pasteur du Cambodge, domestic bird surveillance + human ILI/SARI systems [1]
- **Sequencing platform**: GridION with both R9.4.1 and R10.4.1 flow cells/chemistries [1]
- **Reference standard**: Sanger sequencing of HA cleavage site for H5Nx samples (n=21) [1]

## Key Findings

### Overall Performance Metrics

| Metric | R9.4.1 | R10.4.1 | Improvement |
|--------|--------|---------|-------------|
| **Median read quality** | Lower | Significantly higher (P < 5e-324) [1] | ~1–1.5% absolute accuracy gain |
| **Read length** | Shorter | 27–34% longer reads [1] | Statistically significant (P < 5e-324) |
| **Data output at 140 fmol** | Baseline | +48% more Gbp vs R9 at same loading [1] | Substantial throughput gain |
| **Coding complete segments recovered** | Lower frequency | Higher across all samples [1] | Improved genome recovery |

### Critical Finding: Hemagglutinin Cleavage Site Resolution

The HA multibasic cleavage site is a **homopolymer of basic amino acids** (arginine/lysine) that distinguishes HPAIV from low-pathogenic strains. This region has been notoriously difficult to sequence accurately due to Nanopore's historical challenges with homopolymers [1].

| Chemistry | Correct Motif Resolution | Frameshift Errors |
|-----------|-------------------------|-------------------|
| **R9.4.1** | 60% of genomes (n=21) [1] | High — risk of misclassifying virulence |
| **R10.4.1** | **90%** of genomes [1] | Significantly reduced |

**Clinical significance**: Frameshift mutations in automated pipelines could incorrectly classify HPAIV as low-pathogenic, with severe consequences for outbreak response and public health interventions [1].

### Homopolymer Performance Analysis

- R10 showed **significantly lower minor population insertion/deletion frequencies**, driven by improved performance in low-complexity regions [1]
- Per-position indel rates correlated inversely with local sequence complexity (Shannon entropy) [1]
- Both chemistries still show elevated error rates at perfect homopolymers, but R10 substantially reduces this bias [1]

## Critical Analysis

### Strengths ✅
✅ **Direct head-to-head comparison** of R9 vs R10 on identical samples — rare in literature  
✅ **Focus on biologically critical region** (HA cleavage site) rather than just overall metrics  
✅ **Real-world surveillance samples** from active outbreak setting (Cambodia) [1]  
✅ **Sanger validation** for key clinical marker (cleavage site) [1]  
✅ **Open data**: 80 gene segments deposited at GISAID, raw data on NCBI  

### Limitations ⚠️
⚠️ **Small sample size** (n=45) — may not capture full diversity of circulating strains [1]  
⚠️ **Single geographic region** (Cambodia) — generalizability to other settings unclear  
⚠️ **Reference-based assembly only** (IRMA pipeline) — de novo performance not evaluated  
⚠️ **No cost comparison** between chemistries despite R10 being newer/potentially more expensive  
⚠️ **Limited subtype diversity** — focus on H5Nx; other subtypes (H7, H9, etc.) not well-represented  

### Unanswered Questions ❓
❓ How does R10 perform with metagenomic (non-enriched) sequencing vs targeted RT-PCR?  
❓ Impact on real-time outbreak decision-making in resource-limited settings?  
❓ Performance with newer basecalling models (Bonito, Dorado) beyond Guppy v6.4.6?  
❓ Long-term stability of R10 flow cells compared to R9?  

### Implications for Pandemic Preparedness

### 1. Real-Time Surveillance
- **Rapid HPAI detection** with accurate virulence classification enables timely culling, movement controls, and human prophylaxis [1]
- **Portable GridION/MinION** allows sequencing at point of surveillance (field labs in Cambodia) [1]
- **Reduced hand-curation** requirement — R10's improved accuracy decreases need for expert review [1]

### 2. One Health Integration
- Simultaneous monitoring of avian and human influenza strains supports zoonotic spillover detection [1]
- Critical for countries with high poultry density and limited diagnostic infrastructure

### 3. Technology Adoption
- Validates Nanopore as **complementary to Illumina** for influenza surveillance:
  - Nanopore advantage: Rapid, portable, long reads span homopolymers better
  - Illumina advantage: Higher accuracy per base, established pipelines
  
## Comparison to Alternative Approaches

### vs Illumina Sequencing
| Feature | ONT R10 | Illumina |
|---------|---------|----------|
| Turnaround time | Hours (real-time) [1] | Days (batching required) |
| Portability | ✅ GridION/MinION field-deployable [1] | ❌ Centralized instruments only |
| Homopolymer resolution | Good with R10 [1] | Excellent (short reads avoid issue) |
| Cost per genome | Lower for small batches | Economies of scale favor large runs |
| Established pipelines | Developing | Mature, widely validated |

### vs Sanger Sequencing
- **Nanopore advantage**: Whole genome coverage in single run vs targeted HA amplification only [1]
- **Sanger advantage**: Gold standard accuracy for short regions — still needed for validation

## Future Directions

1. **Integration with AI basecalling**: Newer models (Dorado) may further improve homopolymer resolution
2. **Metagenomic applications**: Extending R10 validation to untargeted respiratory pathogen detection
3. **Global surveillance networks**: Standardizing R10 protocols across GISAID-contributing laboratories [1]
4. **Cost-effectiveness studies**: Health economic evaluation vs conventional PCR + Sanger workflows

## Cross-References

- [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md) — broader clinical metagenomics context  
- [Pandemic Influenza Emergence](concepts/pandemic-influenza-emergence.md) — influenza pandemic preparedness framework  
- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — sequencing technology comparison  

## Confidence Assessment

**High confidence** in core findings based on:
- Direct head-to-head experimental design with identical samples [1]
- Sanger validation of critical clinical marker (HA cleavage site) [1]
- Publication in peer-reviewed journal (Microbiology Spectrum, ASM) [1]
- Open data deposition at GISAID and NCBI

**Moderate confidence** in generalizability due to:
- Limited sample size and geographic scope [1]
- Focus on H5Nx subtypes — other influenza lineages not well-represented [1]
- Reference-based assembly only — de novo performance unclear
