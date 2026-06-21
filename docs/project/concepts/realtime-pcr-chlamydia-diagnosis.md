# Real-Time PCR Diagnosis of *Chlamydia pneumoniae*, *C.* psittaci, and *C.* abortus on Opened Molecular Platforms

> **Citation:** Opota O, Brouillet R, Greub G, Jaton K. "Methods for Real-Time PCR-Based Diagnosis of *Chlamydia pneumoniae*, *Chlamydia psittaci*, and *Chlamydia abortus* Infections in an Opened Molecular Diagnostic Platform." In: Bishop-Lilly KA (ed.), *Diagnostic Bacteriology: Methods and Protocols*. Methods in Molecular Biology, vol. 1616. Springer, 2017. DOI: [10.1007/978-1-4939-7037-7_11](https://doi.org/10.1007/978-1-4939-7037-7_11)
> **Authors:** Onya Opota, René Brouillet, Gilbert Greub, Katia Jaton (Institute of Microbiology, Lausanne University Hospital, Switzerland)
> **Published:** 2017

## Overview

This methods chapter details a standardized real-time PCR platform for detecting three clinically important *Chlamydia* species — *C.* pneumoniae (human respiratory pathogen), *C.* psittaci (zoonotic respiratory pathogen from birds), and *C.* abortus (zoonotic pathogen causing abortion in livestock with human spillover). The assays use TaqMan probe technology on an opened molecular diagnostic platform capable of running up to 91 different PCR reactions (69 pathogens/resistance genes) simultaneously on a single microplate.

## Key Findings / Assay Design

### Two-PCR Strategy for Species Discrimination
| PCR | Target Gene | Detects | Probe Fluorochrome | Amplicon Length |
|-----|-------------|---------|-------------------|-----------------|
| **C.* pneumoniae** (single) | *pst1* gene | *C.* pneumoniae only | VIC (3′), TAMRA (5′) | 82 bp |
| **PCR1** (*C.* psittaci/*abortus*) | 16S–23S rRNA operon | Both *C.* psittaci AND *C.* abortus | FAM + DQ (dark quencher), MGB probe | 133 bp |
| **PCR2** (*C.* psittaci specific) | CDS CPSIT_0607 | *C.* psittaci only | VIC + DQ, MGB probe | 118 bp |

### Interpretation Logic for *C.* psittaci vs. *C.* abortus
| PCR1 (16S-23S) | PCR2 (CPSIT_0607) | Respiratory Sample | Genital/Abortion Sample |
|-----------------|-------------------|--------------------|------------------------|
| Positive | Positive | ***C.* psittaci** | ***C.* psittaci** |
| Positive | Negative | *C.* psittaci OR *C.* abortus (ambiguous) | ***C.* abortus** |
| Negative | — | Neither species detected | Neither species detected |

### Key Technical Features
- **LNA-modified probes**: Locked nucleic acids in reverse primers and MGB (minor groove binder) probes increase specificity and Tm without extending probe length
- **Standardized parameters**: All amplicons, primer/probe Tm values harmonized across the platform — enables multiplexing of up to 91 reactions per plate
- **Synthetic plasmid controls**: Positive controls consist of synthetic plasmids containing exact PCR amplicon sequences (not whole genomes)
- **Inhibition control**: Each sample includes an internal control with 200 copies of positive control plasmid — detects PCR inhibition from sample matrix

### Sample Processing
- **DNA extraction**: MagNA Pure 96® (Roche) — magnetic glass particle technology, automated
- **Liquid handling**: STARlet® (Hamilton®) for high-throughput distribution with barcode recognition
- **Sample types**: Sputum, BAL, nasopharyngeal swabs, genital specimens, abortion tissues
- **N-acetyl cysteine**: Used for sputum lysis before extraction

### Cycling Conditions (ABI 7900)
1. 2 min at 50°C (UNG activation for contamination control)
2. 10 min at 95°C (polymerase activation)
3. 45 cycles: 15 s at 95°C + 60 s at 60°C

## Critical Analysis

### Strengths
1. **Platform standardization**: Harmonized Tm and amplicon lengths allow integration into a high-throughput multiplex platform — significant operational efficiency for reference laboratories
2. **Species discrimination strategy**: Duplex PCR approach (PCR1 + PCR2) elegantly distinguishes *C.* psittaci from closely related *C.* abortus using a species-specific gene (CPSIT_0607)
3. **Comprehensive controls**: Inhibition control, extraction negative control, PCR negative control — robust quality assurance framework
4. **Sample type flexibility**: Same assay applicable to respiratory and genital specimens with interpretation adjusted by sample type

### Limitations
1. **Cannot detect avian *C.* abortus specifically**: The CPSIT_0607 gene is specific to *C.* psittaci; avian *C.* abortus (newly classified 2021) would test PCR1+/PCR2− — indistinguishable from mammalian *C.* abortus. This gap was highlighted by the Netherlands outbreak (Raven et al. 2025) where initial PCR detected "C. psittaci" but genotyping revealed avian *C.* abortus
2. **Respiratory sample ambiguity**: For respiratory specimens, PCR1+/PCR2− is ambiguous (*C.* psittaci OR *C.* abortus possible) — requires follow-up genotyping for definitive identification
3. **Opened platform limitations**: Requires dedicated pre- and post-amplification laboratories with strict contamination control — not feasible in all clinical settings
4. **No quantitative standardization across species**: Each PCR has its own regression curve; cross-assay quantitation comparison not validated
5. **Doesn't detect *C.* trachomatis or other zoonotic *Chlamydia* spp (*C.* caviae, *C.* felis) — separate assays needed

### Clinical Relevance
- Essential for diagnosing atypical pneumonia etiologies where standard bacterial cultures are negative
- Critical for occupational health: farmers, veterinarians, poultry workers, and bird owners at risk for zoonotic *Chlamydia* infection
- The Netherlands avian *C.* abortus outbreak (2025) revealed a diagnostic gap — this platform's PCR1+/PCR2− result would have been reported as "ambiguous" rather than specifically identifying the novel pathogen
- Treatment implications: All three species respond to tetracyclines (doxycycline first-line), but accurate species identification guides public health response (contact tracing, animal source investigation)

## Cross-References

See also: [Avian Chlamydia Abortus Netherlands](concepts/avian-chlamydia-abortus-netherlands.md), [Cap Ngs Clinical Test Standards](concepts/CAP-NGS-clinical-test-standards.md), [Clinical Metagenomics Viral Detection](concepts/clinical-metagenomics-viral-detection.md)
