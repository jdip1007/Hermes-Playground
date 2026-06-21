# Ridom spa Sequencing Protocol — Standardized Method for S. aureus Typing

## Overview

The official **Ridom GmbH** protocol (Document version 1.1, June 2004) for DNA sequencing of the *spa* gene in *Staphylococcus aureus*. This standardized workflow covers DNA preparation from bacterial cultures, PCR amplification of the spa repeat region, Sanger sequencing using ABI BigDye chemistry, and analysis with Ridom StaphType™ software. The protocol established the gold-standard methodology for spa typing used worldwide in clinical microbiology laboratories.

## Citation

> Ridom GmbH. (2004). "DNA Sequencing of the spa Gene." Document version 1.1, June 2004.
> Ridom GmbH, Sedanstr. 27, D-97082 Würzburg, Germany. Email: info@ridom.de

## Protocol Summary

### DNA Preparation (Two Methods)

#### Method A: InstaGene Boiling Lysis (Rapid)
1. Wash loopful of *S. aureus* cells with distilled water
2. Incubate in 200 µl **6% InstaGene matrix** (BIO-RAD) for 20 min at 56°C
3. Vortex, heat 8 min at 100°C
4. Centrifuge 8,000 × g for 2–3 min
5. Use **20 µl supernatant** for PCR

#### Method B: Mechanical Lysis + Qiagen Cleanup (Higher Quality)
1. Wash several loops of cells with distilled water
2. Incubate in 500 µl TE buffer (Tris-HCl 10 mM, EDTA 0.1 mM, pH 7.5) for 10 min at 100°C
3. Add 150 µl acid-washed glass beads (#G4649, Sigma)
4. Mechanical lysis: **Mixer Mill MM 200** (Retsch), maximum speed, 7 min
5. Centrifuge 12,000 × g for 10 min
6. Clean with **QIAamp DNA Blood Mini Kit** (Qiagen) — Blood and Body Fluid Spin Protocol
7. Use **5 µl supernatant** for PCR; store at -20°C

### PCR Amplification of spa Repeat Region

#### Reaction Mix (50 µl total)
- Cleaned template DNA
- 200 µM dNTPs (dATP, dCTP, dGTP, dTTP)
- **10 pmol each primer** (HPLC-cleaned):
  - Forward: `spa-1113f` — 5'-TAA AGA CGA TCC TTC GGT GAG C-3' [positions 1092–1113]
  - Reverse: `spa-1514r` — 5'-CAG CAG TAG TGC CGT TTG CTT-3' [positions 1534–1514]
- 5 µl 10× PCR Buffer II (Applied Biosystems)
- MgCl₂: **1.5 mM**
- AmpliTaq DNA polymerase: **1.25 U** (Applied Biosystems)

#### Thermal Cycling Conditions
| Step | Temperature | Duration | Cycles |
|---|---|---|---|
| Initial denaturation | 80°C | 5 min | 1 |
| Denaturation | 94°C | 45 s | 35 |
| Annealing | 60°C | 45 s | 35 |
| Extension | 72°C | 90 s | 35 |
| Final extension | 72°C | 10 min | 1 |

### PCR Product Purification (ExoSAP)
1. Incubate **5 µl PCR product** with:
   - Exonuclease I (New England Biolabs): **1 U** at 37°C for 30 min
   - Shrimp alkaline phosphatase (Amersham Pharmacia Biotech): **1 U** at 37°C for 30 min
2. Inactivate enzymes: 80°C for 15 min
3. Store purified products at 4°C

### Sanger Sequencing (ABI BigDye v3.0)

#### Sequencing Reaction Mix (10 µl total)
- ABI Prism BigDye Terminator v3.0 Ready Reaction Cycle Sequencing Kit premix: **1.0 µl**
- Tris-HCl/MgCl₂ buffer (400 mM Tris-HCl, 10 mM MgCl₂): **1.5 µl**
- Sequencing primer (same as PCR primers): **10 pmol**
- Cleaned PCR product: **2 µl**

#### Thermal Cycling for Sequencing
| Step | Temperature | Duration | Cycles |
|---|---|---|---|
| Denaturation | 96°C | 10 s | 25 |
| Annealing/Extension | 60°C | 4 min | 25 |

### Sequencing Product Purification (Two Methods)

#### Method A: Centri-Sep Spin Columns (Princeton Separations)
- Individual samples, per manufacturer instructions

#### Method B: MultiScreen HV Plates + Sephadex G50 (Millipore/Amersham)
- Batch processing with 150 µl pre-rinse step (required for capillary sequencers)
- Per Millipore Tech Note TN053

### Sequencing Platform
**ABI 3100 Avant Genetic Analyzer** (Applied Biosystems), per manufacturer instructions.

### Sequence Analysis
Analyzed using **Ridom StaphType™** software (Ridom GmbH, Würzburg, Germany).

## Technical Notes

### Primer Design Rationale
- Primers flank the variable X region of the *spa* gene containing 24 bp tandem repeats
- Numbered from 3' end on forward strand relative to GenBank accession **J01786**
- Forward primer at positions 1092–1113, reverse at 1514–1534

### Expected Product Size
Variable depending on number of repeat units: typically ~1,150–1,500 bp (as noted in Mohammed et al. 2021 application).

## Critical Analysis

### Strengths
- **Standardized and reproducible**: Same protocol used globally enables cross-laboratory comparison
- **Two DNA prep options**: Rapid method for high-throughput screening, thorough method for difficult isolates
- **Well-established chemistry**: ABI BigDye v3.0 provides reliable Sanger sequencing quality
- **Commercial software support**: Ridom StaphType™ automates repeat identification and typing

### Limitations
- **Sanger sequencing only**: Cannot detect mixed populations or heterogeneity within a single isolate
- **spa gene alone**: Limited discriminatory power compared to MLST or whole-genome sequencing (WGS)
- **2004 protocol**: ABI 3100 Avant is legacy hardware; modern labs use ABI 3500/3730xl or Illumina platforms
- **No quality metrics specified**: No mention of minimum base call quality scores or coverage requirements

### Modern Alternatives
- **WGS-based spa typing**: Can be extracted computationally from whole-genome assemblies (e.g., using Ridom SeqSphere+, Enterobase)
- **Nanopore sequencing**: Real-time spa typing directly from long reads
- **Multiplex PCR panels**: Combine spa with mecA, PVL, SCCmec typing in single reaction

## Cross-References

[Spa Typing Staph Aureus Iraq](concepts/spa-typing-staph-aureus-iraq.md) — Application of this protocol in Iraqi clinical isolates (Mohammed et al. 2021)
[Antimicrobial Resistance](concepts/antimicrobial-resistance.md) — spa typing as epidemiological tool for tracking MRSA clones
[Genome Based Salmonella Serotyping](concepts/genome-based-salmonella-serotyping.md) — Similar molecular typing paradigm applied to Salmonella
[Ont R10 Avian Influenza Surveillance](concepts/ONT-R10-avian-influenza-surveillance.md) — Nanopore sequencing as modern alternative to Sanger-based typing
