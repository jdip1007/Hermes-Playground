---
title: NanoMP Dual-Process Nanopore Sequencing for Lower Respiratory Infections
created: "2026-06-15"
updated: "2026-06-15"
type: concept
tags: [nanopore, metagenomics, respiratory-infections, diagnostics, machine-learning, AMR]
sources:
  - Guo et al., The Lancet Microbe (2023), doi:10.1016/S2666-5247(23)00289-6
confidence: high
---

# NanoMP Dual-Process Nanopore Sequencing for Lower Respiratory Infections

## Overview

NanoMP (Nanopore Meta-Panel process) is a **dual-process sequencing approach** combining unbiased metagenomics with targeted enrichment on Oxford Nanopore platform, designed for comprehensive pathogen detection in lower respiratory tract infections (LRTIs) [1]. This represents one of the largest prospective clinical validations of Nanopore sequencing for simultaneous bacterial, fungal, and viral detection [1].

## Study Design

- **Cohort**: 450 specimens from 418 patients across 3 Beijing hospitals [1]
- **Sample types**: Bronchoalveolar lavage fluid (BALF, n=348) + sputum (n=102) [1]
- **Collection period**: January–June 2021 [1]
- **Reference standard**: Composite of culture, qPCR, pathology, imaging, and clinical adjudication [1]

## Methodology

### Dual-Process Architecture

| Process | Approach | Purpose |
|---------|----------|---------|
| **Meta process** | Unbiased metagenomics with saponin-based human DNA removal | Broad pathogen detection across all spectra |
| **Panel process** | Target amplification of specific pathogens (EBV, CMV, HSV1, Aspergillus fumigatus, Rhinovirus) | Enhanced sensitivity for clinically important but low-abundance organisms |

- **Dual-barcode system**: Custom design to demultiplex both processes on same flow cell [1]
- **Turnaround time**: ~6.5 hours total (2h extraction + 3.5–4h library prep + ~1h sequencing/analysis) [1]

### Machine Learning Filter System

- **Algorithm**: XGBoost classifier with ROC curve optimization [1]
- **Training data**: 21 species representing common LRTI pathogens validated against gold standard methods [1]
- **Quality control variables**: Multiple markers from sequencing process to distinguish true positives from contaminants [1]
- **Clinical interpretation categories**: Defined, Probable, Possible, Unlikely (based on literature and CAP-CHINA database) [1]

## Performance Results

### Overall Diagnostic Accuracy
- **Sensitivity**: 80.2% vs composite reference standard [1]
- **Specificity**: 98.8% [1]
- **Limitations**: Composite reference standard itself may miss pathogens detectable only by metagenomics [1]

### Pathogen-Specific Sensitivity (Meta Process)

| Pathogen Group | Sensitivity | Notes |
|----------------|-------------|-------|
| Bacteria | 82.9% | Good performance across Gram+ and Gram– |
| Fungi (non-Aspergillus) | 88.7% | Strong detection for Candida spp., etc. |
| Mycobacterium tuberculosis complex | 75.0% | Moderate; may benefit from targeted enrichment |
| Viruses | 39.4% | Low without enrichment — key limitation of unbiased approach |

### Panel Process Improvements (Target Enrichment)

| Pathogen | Meta Sensitivity | Panel Sensitivity | Improvement |
|----------|-----------------|-------------------|-------------|
| Viruses (overall) | 39.4% | >80.0% | **~2× improvement** |
| Aspergillus fumigatus | 42.3% | 81.8% | **~2× improvement** |

### AMR Gene Detection
- Successfully identified: blaKPC-2, blaOXA-23, mecA and subtypes [1]
- Long-read advantage: Can link AMR genes to parent organisms in mixed infections (critical for treatment decisions) [1]

## Critical Analysis

### Strengths ✅
✅ **Largest prospective clinical validation** of Nanopore sequencing for LRTIs to date [1]  
✅ **Dual-process design** addresses key limitation of metagenomics (low viral/fungal sensitivity) [1]  
✅ **Machine learning filtering** reduces false positives — critical for clinical adoption [1]  
✅ **AMR gene detection with organism linkage** via long reads — unique advantage over short-read platforms [1]  
✅ **Rapid turnaround** (~6.5 hours) enables same-day clinical decision-making [1]  

### Limitations ⚠️
⚠️ **Single-region study**: All samples from Beijing hospitals — generalizability to other populations/settings unclear [1]  
⚠️ **Composite reference standard limitations**: May underestimate true sensitivity if metagenomics detects pathogens missed by culture/qPCR [1]  
⚠️ **Panel limited to 5 targets**: Only EBV, CMV, HSV1, A. fumigatus, Rhinovirus — many clinically important viruses/fungi not covered [1]  
⚠️ **Human DNA removal may affect some pathogen detection**: Saponin lysis could bias against certain organisms [1]  
⚠️ **No health economic analysis**: Cost-effectiveness vs conventional diagnostics not evaluated [1]  

### Unanswered Questions ❓
❓ How does performance compare to Illumina-based metagenomics in same clinical setting?  
❓ Optimal panel composition for different clinical contexts (ICU vs outpatient, immunocompromised vs immunocompetent)?  
❓ Long-term impact on antimicrobial stewardship and patient outcomes?  
❓ Scalability to high-volume laboratories with automation?  

## Comparison to Alternative Approaches

### vs Illumina Metagenomics
| Feature | NanoMP (ONT) | Illumina mNGS |
|---------|--------------|---------------|
| Turnaround time | ~6.5 hours | 24–72+ hours (batching required) |
| Read length | Long reads (kb+) | Short reads (150–300bp) |
| AMR gene linkage | ✅ Direct via long reads | ❌ Requires assembly/inference |
| Sensitivity (viruses without enrichment) | Low (~40%) | Moderate-High |
| Cost per sample | Lower (no batching needed) | Higher when small batches |

### vs Conventional Diagnostics
- **Culture**: Gold standard but slow (2–7 days), misses fastidious organisms, ~50% of LRTIs remain undiagnosed [1]
- **Multiplex PCR panels**: Fast but limited to predefined targets; cannot detect novel/divergent pathogens [1]
- **NanoMP advantage**: Pathogen-agnostic + rapid + AMR detection in single test [1]

## Clinical Implications

1. **Same-day diagnosis** enables targeted antimicrobial therapy, reducing empirical broad-spectrum use [1]
2. **Comprehensive pathogen coverage** (bacteria + fungi + viruses) reduces need for multiple tests [1]
3. **AMR gene identification** guides antibiotic selection, particularly important for MDR organisms [1]
4. **Machine learning filtering** addresses key barrier to metagenomics adoption (false positive concern) [1]

## Future Directions

- Expand panel to include additional high-prevalence pathogens regionally
- Integrate host transcriptomic markers into ML filter system
- Validate in diverse geographic/clinical settings
- Health economic evaluation vs conventional diagnostic algorithms
- Automation for high-throughput laboratory deployment

## Cross-References

- [Clinical Metagenomics Viral Detection](clinical-metagenomics-viral-detection.md) — broader clinical metagenomics context  
- [Next Generation Sequencing](next-generation-sequencing.md) — sequencing technology comparison  
- [Metagenomics](metagenomics.md) — general metagenomic approaches  

## Confidence Assessment

**High confidence** in reported performance metrics based on:
- Lancet Microbe publication (high-impact journal) [1]
- Prospective multi-center design with 450 samples [1]
- Composite reference standard incorporating multiple diagnostic modalities [1]
- Transparent methodology and ML filter system description [1]

**Moderate confidence** in generalizability due to:
- Single-region (Beijing) cohort [1]
- Potential bias in composite reference standard [1]
- Limited panel composition may not reflect all clinical needs globally [1]
