# Dual Detection of *Legionella pneumophila* and *Legionella* Species by Real-Time PCR

> **Citation:** Yang G, Benson R, Pelish T, Brown E, Winchell JM, Fields B. "Dual detection of *Legionella pneumophila* and *Legionella* species by real-time PCR targeting the 23S-5S rRNA gene spacer region." *Clinical Microbiology and Infection* 16(3): 255-261 (2010). DOI: [10.1111/j.1469-0691.2009.02766.x](https://doi.org/10.1111/j.1469-0691.2009.02766.x)
> **Authors:** G. Yang, R. Benson, T. Pelish, E. Brown, J.M. Winchell, B. Fields (Respiratory Diseases Branch, Division of Bacterial Diseases, CDC, Atlanta, GA)
> **Published:** March 2010 | Online: April 28, 2009

## Overview

This study describes a dual-color real-time PCR assay targeting the 23S-5S rRNA intergenic spacer region for simultaneous detection of all *Legionella* species and specific discrimination of *L.* pneumophila from non-pneumophila species. Validated against 271 isolates representing 50 *Legionella* species and 149 clinical specimens (39 culture-positive, 110 culture-negative) collected over 17 years (1989–2006), the assay achieved **100% sensitivity** on culture-positive samples with a detection limit of **3 genome equivalents/reaction** or **7.5 CFU/mL**.

## Key Findings

### Assay Design
| Component | Target | Specificity | Fluorochrome |
|-----------|--------|-------------|--------------|
| Forward/Reverse primers | 23S-5S rRNA spacer (conserved across all *Legionella*) | Genus-wide | — |
| **Probe 1** (*L.* pneumophila-specific) | Species-specific sequence within amplicon | *L.* pneumophila only | CalOrange + BHQ |
| **Probe 2** (*Legionella* spp.) | Conserved sequence with LNA modifications | All *Legionella* species | FAM + BHQ (6 LNA bases) |

### Analytical Performance
- **Dynamic range**: 7-log (3 gEq to 3.0 × 10⁶ gEq per reaction)
- **Standard curve efficiency**: 100.7% (*L.* pneumophila probe), 102.6% (*Legionella* spp. probe); R² = 0.997–0.998
- **Limit of detection (LLOD)**: 3 genome equivalents/reaction or 7.5 CFU/mL for live *L.* pneumophila serogroup 1
- **Analytical specificity**: 100% — no cross-reactivity with 61 non-*Legionella* bacterial and viral strains tested

### Clinical Validation (n=149 specimens, 67 patients)
| Result Category | Count | Details |
|-----------------|-------|---------|
| Culture-positive, PCR-positive | **39/39 (100%)** | All culture-positive samples detected |
| Culture-negative, PCR-positive | **27/110 (24.5%)** | Further analyzed by DNA sequencing |
| Culture-negative, PCR-negative | 83/110 | No *Legionella* detected |

### Non-Pneumophila Species Identified in Clinical Specimens
Among the 27 culture-negative but PCR-positive samples:
- ***L.* longbeachae** — identified by sequencing (important non-pneumophila pathogen, particularly in Australia/New Zealand)
- ***L.* cincinnatiensis** — identified by sequencing
- ***L.* micdadei** (Pittsburgh pneumonia agent) — identified by sequencing; notably fastidious, requires amoebal co-culture for isolation

### Species Discrimination Logic
| *Legionella* spp. probe (FAM) | *L.* pneumophila probe (CalOrange) | Interpretation |
|-------------------------------|-------------------------------------|----------------|
| Positive | Positive | ***L.* pneumophila** |
| Positive | Negative | **Non-pneumophila *Legionella* spp.** |
| Negative | — | No *Legionella* detected |

### Cross-Reactivity Testing (61 strains)
No false positives with: *Bordetella* spp., *Corynebacterium diphtheriae*, *Chlamydia* spp. (*C.* pneumoniae, *C.* psittaci, *C.* trachomatis), *E.* coli, *Haemophilus influenzae*, *Mycoplasma* spp. (14 species), *Mycobacterium tuberculosis*, *Neisseria* spp., *Pseudomonas aeruginosa*, *Streptococcus* spp. (15 species), *Staphylococcus* spp., *Klebsiella pneumoniae*, influenza A/B, SARS-CoV, RSV, parainfluenza viruses, metapneumovirus, adenovirus

## Methodology

### Bacterial Strains
- 271 *Legionella* isolates representing **50 species** tested for analytical sensitivity/specificity
- Grown on BCYE agar at 35°C with 2.5% CO₂ for 48–72 hours
- Clinical specimen cultures incubated 7 days

### Primers and Probes
- Forward: 5′-GTA CTA ATT GGC TGA TTG TCT TGA CC-3′
- Reverse: 5′-CCT GGC GAT GAC CTA CTT TCG-3′
- *L.* pneumophila probe: CalOrange-labeled, BHQ quenched (species-specific)
- *Legionella* spp. probe: FAM-labeled with **6 LNA bases** (denoted by quotes in sequence), BHQ quenched

### Clinical Specimens
- 149 specimens from 67 patients across 11 sample types (sputum, BAL, bronchial aspirate, lung biopsy, post-mortem tissue, serum, urine, etc.)
- Collected over 17 years (1989–2006) at CDC
- Stored at −80°C; retrospective analysis performed

### Confirmation of PCR-Positive/Culture-Negative Samples
- DNA sequencing of the 23S-5S amplicon OR *mip* gene sequencing
- Sequences aligned with NCBI database or HPA Bioinformatics Tools *mip*-based identification tool

## Critical Analysis

### Strengths
1. **Dual-color, single-reaction design**: Simultaneous genus-wide detection and species discrimination in one tube — no post-PCR manipulation needed (eliminates contamination risk from gel electrophoresis)
2. **Comprehensive validation**: 50 *Legionella* species + 61 non-*Legionella* strains tested; clinical specimens spanning 17 years provide robust real-world performance data
3. **High sensitivity**: LLOD of 3 gEq/reaction enables detection even in low-burden clinical samples where culture fails
4. **Detects fastidious species**: Identified *L.* micdadei (requires amoebal co-culture) and *L.* longbeachae in clinical specimens — these would be missed by standard BCYE culture alone
5. **Addresses urine antigen test limitation**: UA detects only *L.* pneumophila serogroup 1; this PCR captures all species

### Limitations
1. **Doesn't identify non-pneumophila species**: Positive FAM/negative CalOrange indicates "non-pneumophila Legionella" but requires follow-up sequencing for species identification — delays definitive diagnosis
2. **No serogroup discrimination within *L.* pneumophila**: Cannot distinguish serogroup 1 (most common cause of LD) from other serogroups — clinically relevant since UA test specifically targets SG1
3. **Retrospective specimen analysis**: Archived samples stored at −80°C for years may have degraded DNA; sensitivity in fresh clinical specimens could differ
4. **Serum sensitivity <30%**: Confirms serum is suboptimal for *Legionella* PCR — limits applicability to easily obtainable sample types
5. **No comparison with commercial PCR platforms**: Assay designed for ABI 7900HT; performance on other real-time PCR instruments not validated

### Clinical/Public Health Relevance
- Addresses critical gap: urine antigen test (most widely used LD diagnostic) detects only *L.* pneumophila SG1 — this study shows non-pneumophila species cause clinically significant disease that would be missed
- Particularly important in regions where *L.* longbeachae is endemic (Australia/New Zealand) or where environmental exposures differ from typical water-based sources
- The 24.5% culture-negative/PCR-positive rate demonstrates substantial underdiagnosis by culture alone — PCR significantly increases detection rates
- Rapid turnaround (~3 hours) enables earlier targeted therapy and infection control measures

## Cross-References

See also: [Cap Ngs Clinical Test Standards](concepts/CAP-NGS-clinical-test-standards.md), [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md), [Antimicrobial Resistance](concepts/antimicrobial-resistance.md)
