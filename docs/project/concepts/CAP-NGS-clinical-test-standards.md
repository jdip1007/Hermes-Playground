---
title: "CAP Laboratory Standards for NGS Clinical Tests"
created: "2026-06-08"
updated: "2026-06-08"
type: concept
tags: [NGS, clinical-laboratory, accreditation, CAP, quality-assurance, regulatory, bioinformatics]
sources:
  - type: paper
    url: "https://doi.org/10.5858/arpa.2014-0250-CP"
    title: "College of American Pathologists' Laboratory Standards for Next-Generation Sequencing Clinical Tests"
    authors: "Aziz N, Zhao Q, Bry L, Driscoll DK, Funke B, Gibson JS, Grody WW, Hegde MR, Hoeltge GA, Leonard DGB, Merker JD, Nagarajan R, Palicki LA, Robetorye RS, Schrijver I, Weck KE, Voelkerding KV"
    journal: "Archives of Pathology & Laboratory Medicine"
    date: "2015-04"
confidence: high
---

# CAP Laboratory Standards for NGS Clinical Tests

## Overview

The College of American Pathologists (CAP) developed the **first regulatory framework** specifically for clinical next-generation sequencing (NGS) testing [1]. Published in 2015, this landmark document established 18 laboratory accreditation checklist requirements covering both wet bench (analytic) and dry bench (bioinformatics) processes — addressing a critical gap as NGS adoption outpaced existing CLIA regulations designed for Sanger sequencing [1].

## Key Standards Framework

### Wet Bench Process Requirements
1. **Documentation**: Written SOPs for all NGS procedures from sample receipt through reporting [1]
2. **Validation**: Analytic sensitivity, specificity, precision (inter/intra-run), limit of detection [1]
3. **Quality Management Program**: Integrated QA covering pre-analytic, analytic, and post-analytic phases [1]
4. **Confirmatory Testing**: Documented policy for when/how to confirm NGS variants (Sanger or orthogonal method) [1]

### Bioinformatics/Dry Bench Requirements
5. **Pipeline Documentation**: Version-controlled bioinformatics workflows with traceability [1]
6. **Database Management**: Curated variant databases with update procedures and version tracking [1]
7. **Variant Interpretation**: Standardized classification system (e.g., ACMG guidelines for germline variants) [1]
8. **Incidental Findings**: Policy for reporting secondary findings beyond primary test indication [1]
9. **Data Storage & Transfer**: Secure storage, backup protocols, confidentiality during data transfer [1]

### Validation-Specific Requirements
- **Analytic Sensitivity**: Must demonstrate detection of known pathogenic variants (e.g., p.F508del in CFTR) [1]
- **Analytic Specificity**: False-positive rate calculation across assayed regions — traditional "negative sample" approach inadequate for NGS [1]
- **Limit of Detection**: Critical for heterogeneous samples (tumor specimens, NIPT, mosaic cases); requires dilution/mixing experiments since Sanger gold standard is less sensitive than NGS [1]
- **Precision**: Minimum 3 samples; barcoded replicates for single-lane sequencers [1]
- **Homologous Sequence Interference**: Upfront bioinformatics analysis required to identify pseudogene interference [1]

### Change Management
| Change Type | Revalidation Required | Example |
|-------------|----------------------|---------|
| Minor change | Confirmation only | New lot of validated capture reagent [1] |
| Major change | Full revalidation | New sequencing platform, different target enrichment method [1] |

## Critical Analysis

### Strengths ✅
✅ **First NGS-specific regulatory framework** — filled critical gap in CLIA/CAP standards [1]  
✅ **Comprehensive scope** — covers wet bench + bioinformatics (unique to NGS complexity) [1]  
✅ **Practical flexibility** — allows laboratories discretion in confirmatory testing policies based on validation data [1]  
✅ **Expert consensus** — 17 authors from major US academic medical centers (Harvard, Stanford, Mayo Clinic, Cleveland Clinic, etc.) [1]  

### Limitations ⚠️
⚠️ **2015 publication date** — predates many current NGS applications (liquid biopsy, single-cell, long-read sequencing)  
⚠️ **Short-read focused** — written primarily for Illumina-style platforms; less applicable to Nanopore/PacBio [1]  
⚠️ **No specific bioinformatics standards** — general requirements without detailed pipeline specifications [1]  
⚠️ **Resource-intensive compliance** — small laboratories may struggle with validation requirements  

### Unanswered Questions ❓
❓ How do these standards apply to AI/ML-based variant interpretation?  
❓ Standards for metagenomic NGS (pathogen detection) vs targeted panels?  
❓ Regulatory framework for direct-to-consumer NGS testing?  

## Clinical/Practical Implications

1. **Accreditation prerequisite**: CAP-accredited laboratories must comply with these 18 checklist items [1]
2. **Validation burden**: Comprehensive validation required before clinical implementation — typically 6–12 months [1]
3. **Bioinformatics accountability**: First regulatory recognition that bioinformatics pipelines are part of the "analytic" process requiring validation [1]
4. **Ongoing monitoring**: Laboratories must document compliance and maintain benchmarks achieved during validation [1]

## Cross-References

- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — broader NGS technology overview
- [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md) — clinical metagenomics applications (regulatory context)
- [[nanopore-TB-identification-genotyping-drug-resistance]] — WHO-approved tNGS test (complementary regulatory framework)

## Confidence Assessment

**High confidence** in standards content based on:
- CAP is the primary US laboratory accreditation body for pathology [1]
- 17 expert authors from leading academic medical centers [1]
- Published in Archives of Pathology & Laboratory Medicine (CAP journal) [1]
- Standards have been adopted and updated since initial publication

**Moderate confidence** in current applicability due to:
- Rapid evolution of NGS technology since 2015
- Newer platforms (Nanopore, PacBio HiFi) not specifically addressed [1]
- AI/ML integration in variant calling post-dates this framework
