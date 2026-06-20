---
title: "DNA Extraction Kits and Protocols — Comprehensive Comparison"
summary: "Detailed analysis of all DNA extraction kits, reagents, buffers, and shearing methods used in Oxford Nanopore sequencing protocols documented in the LLM Wiki. Includes comparison table, protocol details, reagent compositions, yields, and usage recommendations."
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [dna-extraction, kits-comparison, nanopore, protocols, reagents]
sources: []
confidence: high
contested: false
---

# DNA Extraction Kits and Protocols — Comprehensive Comparison

## Overview

This document provides a detailed analysis of all DNA extraction kits, reagents, buffers, lysis methods, and shearing/fragmentation tools used across the Oxford Nanopore sequencing protocols documented in our LLM Wiki. The information is compiled from 34 wiki concept pages created on 2026-06-19, each derived from validated Oxford Nanopore protocol documents or peer-reviewed literature.

**Scope:** DNA extraction kits (QIAGEN, Zymo Research, Thermo Fisher), lysis buffers (ATL, AL, G2), shearing instruments (Covaris g-TUBE, Diagenode Megaruptor 3, FastPrep-96), size selection reagents (AMPure XP SPRI beads), and specialized methods (phenol-chloroform agarose plugs, FTA cards + EZ2 Connect automation).

---

## 1. DNA Extraction Kits — Detailed Profiles

### 1.1 QIAGEN MagAttract HMW DNA Kit

**Catalog:** 67270 | **Manufacturer:** QIAGEN (Hilden, Germany)
**Type:** Magnetic bead-based, automatable

**Description:**
The MagAttract HMW DNA Kit uses paramagnetic beads coated with a proprietary binding matrix to capture high-molecular-weight genomic DNA from chaotropic lysis buffers. Designed for automation on KingFisher Flex or Duo Prime systems, it eliminates spin-column shear forces that fragment long DNA molecules — making it ideal for long-read sequencing applications.

**Key Reagents/Components:**
- MagAttract HMW DNA paramagnetic particles (proprietary surface chemistry)
- Lysis buffer with guanidinium salts and detergent
- Wash buffers (ethanol-based)
- Elution buffer or nuclease-free water compatible

**Protocol Overview:**
1. Lyse sample in chaotropic lysis buffer + Proteinase K
2. Incubate at 50–56°C for protein digestion
3. Bind DNA to paramagnetic beads
4. Wash beads on magnetic rack (automated)
5. Elute HMW DNA in low-salt buffer

**Sample Types Validated:**
- Human brain tissue (25 mg → 8–15 µg yield)
- Rabbit buffy coat (via Ficoll-Paque isolation first)
- Atlantic salmon blood (stored in 90% ethanol at −80°C — highest output)
- Atlantic salmon tissue (brain, heart, liver, spleen, fin; ~25 mg → lower output than blood)
- Green anole lizard tail (ethanol-preserved or fresh, 100 mg)

**Typical Yield:** 8–15 µg from 25 mg tissue; varies by sample type
**Purity:** OD 260/280 ~1.9–2.0; OD 260/230 >2.0
**Special Features:** Fully automatable, no spin columns (reduced shear), optimized for HMW DNA preservation

---

### 1.2 QIAGEN Puregene Cell Kit

**Catalog:** D-5943 | **Manufacturer:** QIAGEN (formerly Gentra Systems)
**Type:** Semi-selective precipitation (no column)

**Description:**
The Puregene Cell Kit uses a unique semi-selective precipitation method that avoids silica columns entirely. DNA is precipitated with isopropanol while proteins and contaminants remain soluble, then spooled or pelleted by centrifugation. This approach preserves extremely long DNA molecules (>100 kb) because there are no column-binding shear forces.

**Key Reagents/Components:**
- Cell Lysis Solution (detergent-based, chaotropic salts)
- Protein Precipitation Solution (high-salt solution that precipitates proteins selectively)
- Isopropanol for DNA precipitation
- 70% ethanol wash
- TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0) for elution

**Protocol Overview:**
1. Harvest cells/pellet (5 × 10⁶ cells or equivalent biomass)
2. Lyse in Cell Lysis Solution at 37°C for 30 min
3. Add Protein Precipitation Solution → vortex → centrifuge
4. Transfer supernatant, add isopropanol → invert 50× to precipitate DNA
5. Spool DNA with inoculation loop or pelleted by centrifugation
6. Wash with 70% ethanol, air-dry briefly
7. Resuspend in TE buffer at 50°C for 2 hours

**Sample Types Validated:**
- Human cell lines (5 × 10⁶ cells → 20–30 µg yield)
- C. elegans strain SX3254 (with semi-selective precipitation size selection using PVP 360,000 + NaCl)
- Gram-positive bacteria (2 × 10⁹ cells / ~3 mg pellet → 1–2 µg per replicate; requires Lytic Enzyme Solution pre-treatment)

**Typical Yield:** 20–30 µg from human cell lines; 1–2 µg from gram-positive bacteria
**Purity:** OD 260/280 = 1.99; OD 260/230 = 2.43 (human cell line)
**Special Features:** No column shear forces → longest DNA fragments preserved; spooling option for visual confirmation of HMW DNA

---

### 1.3 QIAGEN Blood and Cell Culture DNA Midi Kit

**Catalog:** 13362 | **Manufacturer:** QIAGEN
**Type:** Genomic-tip gravity-flow column + semi-selective precipitation

**Description:**
The Blood and Cell Culture DNA Midi Kit uses large-capacity Genomic-tip columns (gravity-flow, not spin) combined with semi-selective precipitation. This hybrid approach provides high yields from mid-scale inputs while preserving HMW DNA integrity through gentle elution and optional spooling.

**Key Reagents/Components:**
- G2 buffer (guanidinium-based lysis buffer for tissue)
- ATL buffer alternative (for certain protocols)
- RNase A Solution (100 mg/ml)
- Proteinase K (20 mg/ml)
- Genomic-tip 500/G columns (gravity-flow, high-capacity)
- Buffer QF (elution buffer with salt for precipitation)
- TE buffer (10 mM Tris-HCl, 1 mM EDTA, pH 8.0)

**Protocol Overview:**
1. Homogenize tissue in G2 buffer + RNase A (or ATL buffer variant)
2. Add Proteinase K → incubate overnight at 50°C (tissue) or shorter for cells
3. Load lysate onto Genomic-tip column (gravity flow)
4. Wash columns with kit buffers
5. Elute in Buffer QF warmed to 50°C
6. Optional: precipitate DNA from eluate, wash with cold 70% ethanol
7. Resuspend pellet in TE buffer overnight at room temperature on shaker

**Sample Types Validated:**
- Human cell lines (1 × 10⁸ cells → 400–450 ng/µl concentrated)
- Western clawed frog (*Xenopus tropicalis*) muscle (100 mg frozen, homogenized with TissueRuptor II; semi-selective precipitation size selection)
- Green anole lizard tail (100 mg ethanol-preserved or fresh tissue)
- Human saliva pooled from multiple individuals (stored in Isohelix GeneFiX device)
- Rabbit liver tissue (up to 80 mg ground with tweezers/scalpel; G2 buffer lysis overnight at 50°C)

**Typical Yield:** 400–450 ng/µl from human cell lines; varies by sample type for tissues
**Purity:** OD 260/280 = 1.9; OD 260/230 = 2.4 (human cell line)
**Special Features:** Gravity-flow columns minimize shear; semi-selective precipitation preserves HMW DNA; scalable from cells to tissue

---

### 1.4 QIAamp MinElute ccfDNA Midi Kit

**Catalog:** 55134 | **Manufacturer:** QIAGEN
**Type:** Silica-membrane spin column, optimized for cell-free DNA

**Description:**
The QIAamp MinElute ccfDNA Midi Kit is specifically designed to isolate cell-free DNA (cfDNA) and circulating cell-free DNA (ccfDNA) from plasma or serum. The MinElute columns have a small elution volume (~50 µl), concentrating the typically low-abundance cfDNA into a manageable volume for downstream applications.

**Key Reagents/Components:**
- Lysis buffer optimized for plasma/serum
- Silica-membrane MinElute spin columns (small elution volume)
- Wash buffers (ethanol-based)
- Elution buffer or nuclease-free water

**Protocol Overview:**
1. Start with 1–5 ml serum/plasma from EDTA K₂ blood tubes
2. Process while fresh to minimize gDNA contamination from cell lysis during storage
3. Lyse and bind cfDNA to silica membrane
4. Wash columns
5. Elute in small volume (~50 µl) for concentration

**Sample Types Validated:**
- Human blood plasma/serum (EDTA K₂ tubes, 12 samples multiplexed with unique barcodes)

**Typical Yield:** Variable — depends on input plasma volume and cfDNA concentration; ≥6 ng per barcode recommended for optimal flow cell performance
**Special Features:** Optimized for short DNA fragments (cfDNA typically 150–200 bp); small elution volume concentrates dilute samples; validated for multiplex sequencing workflows

---

### 1.5 QIAGEN DNeasy Blood & Tissue Kit

**Catalog:** 69504 | **Manufacturer:** QIAGEN
**Type:** Silica-membrane spin column, general-purpose genomic DNA

**Description:**
The DNeasy Blood & Tissue Kit is one of the most widely used DNA extraction kits globally. It uses ATL/AL buffer chemistry with Proteinase K digestion followed by silica-column purification. The kit is versatile across sample types but requires protocol modifications for challenging matrices (blood culture broth, stool).

**Key Reagents/Components:**
- ATL Buffer (~4 M guanidine HCl + Triton X-100 + Tris-HCl pH 8.0) — cell lysis
- AL Buffer (~5 M guanidine isothiocyanate + detergent) — equalizes chaotropic conditions for silica binding
- Proteinase K (20 mg/ml, supplied or purchased separately)
- RNase A Solution (optional, included in some versions)
- AW1 and AW2 wash buffers (ethanol-based)
- AE elution buffer (10 mM Tris-HCl, pH 8.5) or nuclease-free water
- DNeasy spin columns (silica membrane)

**Protocol Overview:**
1. Lyse sample in ATL buffer + Proteinase K → incubate at 56°C for 30 min
2. Add AL buffer to equalize chaotropic salt concentration
3. Load onto DNeasy spin column → centrifuge
4. Wash with AW1 and AW2 buffers
5. Elute in AE buffer or water

**Sample Types Validated:**
- Rat stool pellets (with custom lysis buffer: 100 mM Tris-HCl, 100 mM EDTA, 10 mM NaCl, 1% N-lauroyl-sarcosine, pH 7.5 per Maudet et al.)
- Blood culture broth (after SPS removal via centrifugation + ethanol wash) — standard protocol without SPS removal gives ZERO PCR amplification

**Typical Yield:** Variable by sample type; ~µg range from blood/tissue
**Purity:** OD 260/280 ~1.7–1.9; OD 260/230 >2.0
**Special Features:** Most versatile kit in the QIAGEN lineup; requires SPS removal for blood culture samples; custom lysis buffer needed for stool

---

### 1.6 QIAGEN DNeasy PowerMax Soil Kit

**Catalog:** MAX96 | **Manufacturer:** QIAGEN (formerly MO BIO)
**Type:** Silica-membrane column with bead-beating mechanical lysis

**Description:**
The DNeasy PowerMax Soil Kit (formerly MO BIO PowerMax) is designed for extracting microbial community DNA from soil and other environmental samples. It includes a bead-beating step to mechanically disrupt tough cell walls of bacteria, fungi, and archaea that chemical lysis alone cannot penetrate.

**Key Reagents/Components:**
- Bead-beating tubes with glass beads (mechanical lysis)
- C1/C2/C3 lysis buffers (guanidinium-based + detergents)
- RNase A Solution
- Protein precipitation buffer
- Silica-membrane columns (high-capacity for soil extracts)
- Wash and elution buffers

**Protocol Overview:**
1. Start with ~8 g soil sample (do not exceed 10 g kit capacity to avoid membrane blockage)
2. Add lysis buffers + glass beads → bead-beat on vortex mixer
3. Centrifuge to pellet debris
4. Transfer supernatant through silica-membrane columns
5. Wash and elute

**Sample Types Validated:**
- Soil (8 g starting material; tested modifications at 65°C or overnight RT showed no improvement vs standard protocol)

**Typical Yield:** Variable by soil type; optimized for microbial community representation
**Special Features:** Bead-beating essential for tough environmental samples; do not exceed 10 g input; formerly MO BIO PowerMax Soil Kit

---

### 1.7 QIAGEN Plasmid Plus Midi Kit

**Catalog:** 12363 | **Manufacturer:** QIAGEN
**Type:** Alkaline lysis + silica-membrane column, plasmid-specific

**Description:**
The Plasmid Plus Midi Kit uses alkaline lysis to selectively isolate supercoiled plasmid DNA from bacterial cultures while precipitating chromosomal DNA and proteins. The "Plus" variant includes enhanced purification steps for higher purity compared to standard miniprep kits.

**Key Reagents/Components:**
- Buffer P1 (resuspension buffer with RNase A)
- Buffer P2 (alkaline lysis: NaOH + SDS)
- Buffer P3 (neutralization: potassium acetate, pH 5.5 — precipitates chromosomal DNA and SDS-protein complexes)
- PE wash buffer (ethanol-supplemented)
- EB elution buffer (10 mM Tris-HCl, pH 8.5) or nuclease-free water
- QIAGEN spin columns

**Protocol Overview:**
1. Harvest 50–150 ml overnight bacterial culture by centrifugation (6000 × g, 10 min, 4°C)
2. Resuspend pellet in 250 µl Buffer P1 (+ RNase A)
3. Add 250 µl Buffer P2 → invert 10× for complete lysis
4. Add 350 µl Buffer P3 → invert 10× to precipitate salts and chromosomal DNA
5. Centrifuge 10 min at 20,000 × g → transfer supernatant to column
6. Wash with 750 µl PE buffer
7. Elute in 100–150 µl Buffer EB or water

**Sample Types Validated:**
- Bacterial cultures (E. coli and other standard hosts) — Oxford Nanopore's recommended method for plasmid DNA extraction

**Typical Yield:** 20–30 µg total plasmid DNA from 50–150 ml culture (varies by plasmid size and copy number)
**Purity:** A260/280 ratio 1.7–1.9; A260/230 ratio >2.0
**Plasmid Size Range:** Optimized for standard plasmids (2–15 kb); larger constructs may require modified protocols or agarose plug methods

---

### 1.8 ZymoBIOMICS DNA Miniprep Kit

**Catalog:** D4302 | **Manufacturer:** Zymo Research (Irvine, CA)
**Type:** Silica-membrane column with bead-beating lysis

**Description:**
The ZymoBIOMICS DNA Miniprep Kit is designed for extracting genomic DNA from microbial communities. It uses a combination of chemical and mechanical lysis to recover DNA from diverse organisms including Gram-positive bacteria, Gram-negative bacteria, fungi, and spores. Validated against the ZymoBIOMICS Microbial Community Standard (a defined mixture of 18 species).

**Key Reagents/Components:**
- C1/C2/C3 lysis buffers (guanidinium-based + detergents)
- Bead-beating tubes with zirconia/silica beads
- RNase A Solution
- Silica-membrane spin columns
- Wash and elution buffers

**Protocol Overview:**
1. Resuspend microbial sample in lysis buffer
2. Add glass/zirconia beads → bead-beat on vortex mixer
3. Centrifuge to pellet debris
4. Transfer supernatant through silica-membrane columns
5. Wash and elute

**Sample Types Validated:**
- Environmental water (eDNA) — outperformed Quick-DNA HMW MagBead, QIAGEN MagAttract, Puregene, and PowerWater kits in community representation accuracy against the ZymoBIOMICS Microbial Community Standard control

**Typical Yield:** Variable by sample type; optimized for community representation rather than maximum yield
**Special Features:** Best community representation among tested kits for eDNA; validated against defined microbial standards

---

### 1.9 Oxford Nanopore Rapid PCR Barcoding Kit (SQK-RBK114)

**Catalog:** SQK-RBK114.24 / SQK-RBK114.96 | **Manufacturer:** Oxford Nanopore Technologies
**Type:** Transposase-based library preparation with PCR amplification and barcoding

**Description:**
The Rapid PCR Barcoding Kit enables rapid (≈10 min hands-on) library preparation from bacterial colonies or small DNA inputs using Tn5 transposase tagmentation. Includes 96 unique barcodes for multiplexing. Designed for quick turnaround applications like colony identification or outbreak investigation.

**Key Reagents/Components:**
- Tn5 transposase loaded with adapter sequences
- PCR master mix (polymerase, primers, dNTPs)
- 96 unique barcode primers (for multiplexing)
- SFB Expansion Module (SQK-EXP114.96) for scaling from 24 to 96 barcodes
- AMPure XP beads for cleanup

**Protocol Overview:**
1. Pick bacterial colony or add template DNA
2. Optional: treat with thermolabile Proteinase K
3. Tagmentation with Tn5 transposase (5 min at room temperature)
4. PCR amplification with barcode primers
5. AMPure XP bead cleanup (0.6× ratio)
6. Elute in 17 µl elution buffer

**Sample Types Validated:**
- Bacterial colonies (E. coli — Gram-negative; whole genome colony PCR)
- Environmental water eDNA (PCR-amplified approach, compared with non-amplified Ligation Sequencing Kit)

**Typical Input:** 50–200 ng plasmid DNA or bacterial colony
**Special Features:** Fastest library prep method (~10 min hands-on); PCR amplification enables low-input samples; 96-plex multiplexing; transposase-based (no fragmentation step needed)

---

### 1.10 Thermo Fisher PrepMan Ultra Reagent

**Catalog:** A47506 | **Manufacturer:** Thermo Fisher Scientific / Applied Biosystems
**Type:** Chemical lysis reagent for difficult-to-lyse organisms

**Description:**
PrepMan Ultra is a proprietary chemical lysis reagent designed to rapidly inactivate pathogens and release nucleic acids from difficult-to-lyse organisms including mycobacteria, spores, and viruses. It contains chaotropic salts and detergents that denature proteins and disrupt cell walls without requiring hazardous phenol-chloroform as the primary lysis step (though phenol-chloroform may still be used for downstream purification).

**Key Reagents/Components:**
- PrepMan Ultra reagent (proprietary formulation: chaotropic salts + detergents)
- Glass beads for mechanical disruption (used in conjunction)
- AMPure XP beads for downstream cleanup

**Protocol Overview (M. tuberculosis from Löwenstein-Jensen culture):**
1. Dispense 700 µl PrepMan Ultra into tube with glass beads (beads ≤50% liquid level)
2. Add one loop-full of culture, twirl loop to remove
3. Heat at 95°C for 15 minutes
4. Shear in BioSpec BeadBeater: 3 pulses × 40 seconds at 6.0 m/s
5. Centrifuge 10 min at 13,000 rpm → transfer 450 µl supernatant
6. AMPure XP bead cleanup

**Sample Types Validated:**
- *Mycobacterium tuberculosis* from Löwenstein-Jensen solid culture (community-contributed protocol based on Bainomugisa et al., 2018 — complete nanopore-only assembly of XDR M. tuberculosis Beijing lineage)

**Special Features:** Rapid pathogen inactivation (biosafety); effective against mycobacterial cell walls; heat step at 95°C enhances lysis; validated for nanopore sequencing of clinically relevant pathogens

---

## 2. Lysis Buffers — Detailed Profiles

### 2.1 ATL Buffer (QIAGEN)

**Composition:**
- Guanidine hydrochloride (~4 M) — chaotropic salt for protein denaturation and nuclease inactivation
- Triton X-100 (non-ionic detergent, CMC ~0.24 mM) — membrane disruption via micelle formation
- Tris-HCl buffer — maintains pH ~8.0, optimal for Proteinase K activity

**Mechanism:** Guanidinium ions compete with intramolecular hydrogen bonds in proteins, causing irreversible unfolding at concentrations >2 M. Triton X-100 solubilizes lipid bilayers by incorporating into membranes above its CMC, forming mixed micelles that dissolve membrane structure. Together they lyse cells and denature all proteins including DNases/RNases.

**Efficacy:** Gram-negative bacteria (thin peptidoglycan) are readily lysed by ATL alone. Gram-positive organisms (thick peptidoglycan, up to 80 nm) often require extended Proteinase K incubation or lysozyme pre-treatment because the detergent cannot penetrate dense cell walls on its own.

**Used in:** DNeasy Blood & Tissue Kit; rabbit lung/muscle/skin DNA extraction protocols (Genomic-tip with ATL variant)

---

### 2.2 AL Buffer (QIAGEN)

**Composition:**
- Guanidine isothiocyanate (~5 M) — stronger chaotrope than guanidine HCl (chaotropicity: SCN⁻ > ClO₄⁻ > I⁻ > NO₃⁻ > Br⁻ > Cl⁻)
- Additional proprietary detergent components

**Mechanism:** The isothiocyanate group (-N=C=S) carbamoylates protein amino groups, providing additional irreversible denaturation beyond chaotropic effects. Raises total chaotropic salt concentration to the level required for DNA-silica binding (>5 M guanidinium equivalent). Silica-binding requires high-salt conditions where chaotropic ions displace water molecules from both DNA phosphate backbone and silica surface, enabling direct phosphodiester-silica interactions.

**Why Two Buffers (ATL + AL)?** ATL provides the initial lysis environment — Triton X-100 is gentler than GITC and works well with Proteinase K at 56°C for cell disruption. AL raises chaotropic concentration to silica-binding levels after digestion is complete, avoiding potential interference between GITC's isothiocyanate group and Proteinase K's active site during the digestion step.

**Used in:** DNeasy Blood & Tissue Kit; blood culture broth extraction (after SPS removal)

---

### 2.3 G2 Buffer (QIAGEN)

**Composition:** Guanidinium-based lysis buffer optimized for tissue samples, used with RNase A and Proteinase K.

**Mechanism:** Similar to ATL but formulated for efficient tissue homogenization and overnight digestion at 50°C. Used in the Blood and Cell Culture DNA Midi Kit protocol for animal tissues.

**Used in:** Rabbit liver DNA extraction (up to 80 mg ground tissue + G2 buffer + RNase A + Proteinase K, incubated overnight at 50°C); rabbit lung/skin/muscle DNA extraction protocols (Genomic-tip with G2 variant)

---

### 2.4 Lytic Enzyme Solution (QIAGEN)

**Composition:** Lysozyme-based enzymatic solution for digesting peptidoglycan cell walls of Gram-positive bacteria.

**Mechanism:** Lysozyme cleaves β-(1,4)-glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine in peptidoglycan, weakening the thick cell wall that prevents chemical lysis buffer penetration. Essential for extracting DNA from Gram-positive organisms (Staphylococcus, Streptococcus, Bacillus, etc.).

**Protocol:** Add 1.5 µl Lytic Enzyme Solution to bacterial pellet resuspended in TE buffer → incubate at 37°C for 30 minutes → proceed with standard Puregene Cell Kit protocol. For recalcitrant species: optional 80°C heat lysis step for 5 minutes after adding Cell Lysis Solution.

**Used in:** Gram-positive bacterial DNA extraction with QIAGEN Puregene Cell Kit (Oxford Nanopore Protocol v2)

---

## 3. Shearing and Fragmentation Methods

### 3.1 Covaris g-TUBE

**Manufacturer:** Covaris (Woburn, MA) | **Type:** Centrifugal force shearing

**Mechanism:** DNA solution is loaded into a specialized tube with an internal constriction. During centrifugation at high speed, the DNA molecules are forced through the narrow gap between the tube wall and inner structure, generating shear forces that fragment DNA to predictable sizes without acoustic energy or beads.

**Key Parameters (Oxford Nanopore validated):**
- Microfuge: Eppendorf 5424 at 6000 rpm → ~8 kb average Lambda DNA fragments
- Input: >4 µg standard; Oxford Nanopore validated 100–1000 ng in 49 µl equivalently
- No beads required — purely centrifugal force shearing

**Advantages:** Reproducible fragment sizes; no heat generation (unlike acoustic shearing); works with low-input samples (100–500 ng) where fragmentation increases molecule count and throughput. Different centrifuges/samples require speed optimization.

**Used in:** Human cell line DNA extraction (Genomic-tip protocol — optional g-TUBE fragmentation before library prep); salmon blood/tissue DNA extraction (optional shearing to increase output at expense of read N50)

---

### 3.2 Diagenode Megaruptor 3

**Catalog:** E07010003 (Shearing Kit) | **Manufacturer:** Diagenode (Belgium)
**Type:** Acoustic shearing with focused ultrasonication

**Mechanism:** Uses focused acoustic energy to create cavitation bubbles in the DNA solution. Bubble collapse generates localized shear forces that fragment DNA. The Megaruptor 3 Shearing Kit includes specialized tubes and buffers optimized for reproducible fragmentation.

**Key Parameters (Oxford Nanopore validated):**
- Input: 2000 ng gDNA in 100 µl nuclease-free water
- QC with Agilent FEMTO Pulse or equivalent after shearing

**Advantages:** Reduced library input requirements; increased read length N50; reduced pore blocking compared to unsheared HMW DNA. Optional size selection before shearing helps remove shortest fragments.

**Used in:** PromethION 24-hour genome workflow (Megaruptor 3 shearing → Ligation Sequencing Kit); salmon blood/tissue DNA extraction (optional)

---

### 3.3 FastPrep-96 High Throughput Bead Beating Grinder

**Manufacturer:** MP Biomedicals / Teknor | **Type:** Mechanical bead-beating, high throughput

**Mechanism:** Samples in microtubes with beads are agitated at high speed on a specialized platform. The beads collide with DNA molecules and sample debris, generating mechanical shear forces that fragment DNA to target sizes.

**Key Parameters (Oxford Nanopore validated):**
- Capacity: Up to 192 samples simultaneously
- Speed: 1600 SPM for 5 minutes → N50 distributions of 10–30 kb (depending on settings)
- Concentration: 30 ng/µl in 120 µl volume (recommended)
- No beads required for DNA processing — purely mechanical shearing

**Advantages:** Highest throughput shearing method; generates reproducible N50 distributions of 10, 12.5, 15, and 20 kb depending on settings. Further optimization may be needed based on sample quality and desired fragment size.

**Used in:** Brain tissue DNA extraction (optional FastPrep-96 shearing for higher throughput at expense of read length); high-throughput genomic DNA shearing protocol

---

## 4. Size Selection Methods

### 4.1 SPRI Bead Size Selection (AMPure XP)

**Catalog:** A63881 | **Manufacturer:** Beckman Coulter / Agencourt
**Type:** Solid-phase reversible immobilization using paramagnetic PEG/NaCl beads

**Mechanism:** AMPure XP beads contain carboxyl-coated magnetic particles that bind DNA in the presence of polyethylene glycol (PEG) and sodium chloride. The binding is size-dependent — shorter fragments require higher bead-to-sample ratios to bind, while longer fragments bind at lower ratios. By adjusting the bead ratio, specific size ranges can be enriched or depleted.

**Custom Buffer Preparation (>1.5–2 kb enrichment):**
- Tris-HCl (1 M → 10 mM final)
- EDTA (0.5 M → 2.5 mM final)
- NaCl (5 M → 100 mM final)
- PEG 8000 (40% w/v → 16% w/v final; critical: accurately pipette 548 µl using wide-bore tips)

**Key Ratios:**
- 0.7× AMPure XP beads → optimal selection for >2 kb fragments (improves median read length of fragmented gDNA)
- 0.6× ratio used in Rapid PCR Barcoding Kit cleanup
- Standard ratios: 1.8× removes >50 bp; 0.8× enriches >300 bp

**Used in:** Puregene Cell Kit protocol (SPRI size selection on 3 µg eluate); Blood and Cell Culture DNA Midi Kit (buffy coat — SPRI bead size selection on 3 µg extracted DNA); Rapid PCR Barcoding Kit cleanup; M. tuberculosis PrepMan Ultra extraction (AMPure XP bead cleanup)

---

### 4.2 Semi-Selective Precipitation (Puregene / Blood & Cell Culture)

**Mechanism:** Uses polyvinylpyrrolidone (PVP 360,000) and NaCl to selectively precipitate shorter DNA fragments while longer molecules remain in solution. The PVP acts as a molecular crowding agent that preferentially interacts with shorter DNA chains.

**Composition:**
- 2.5% w/v PVP 360,000 (polyvinylpyrrolidone, MW 360 kDa)
- 1.2 M NaCl

**Used in:** C. elegans DNA extraction; frog muscle DNA extraction; lizard tail DNA extraction; human saliva DNA extraction — all followed by this size selection step before library prep

---

## 5. Specialized Methods and Consumables

### 5.1 Phenol-Chloroform Extraction from Agarose Plugs

**Type:** Organic extraction, HMW DNA preservation

**Mechanism:** Cells embedded in low-melting point agarose plugs are lysed in situ (minimizing shear forces). The melted agarose is then extracted with phenol to remove proteins and lipids, followed by chloroform extraction. DNA is precipitated from the aqueous phase using ammonium acetate and ethanol.

**Protocol Steps:**
1. Transfer agarose plug (~3–6 µg DNA) to 2 ml tube + TE buffer + NaCl to ~200 mM final
2. Melt agarose at 70°C until transparent and homogeneous (~5 minutes)
3. Phenol extraction: add 1 volume phenol, rotate on HulaMixer for 2 hours at room temperature (in fume hood)
4. Centrifuge 5 min at 9400 × g → transfer supernatant to new tube
5. Repeat with chloroform
6. Precipitate DNA with ammonium acetate and ethanol

**Sample Types:** Lambda DNA, *S. cerevisiae* — validated for HMW DNA preservation; preferred for large plasmids (>30 kb) where column shear forces would fragment DNA

---

### 5.2 Whatman FTA Cards + QIAGEN EZ2 Connect Automation

**Type:** Dried blood spot collection + automated extraction

**Mechanism:** Blood is applied to Whatman FTA cards, which contain chemicals that lyse cells and denature proteins while immobilizing DNA on the card matrix. The cards allow room-temperature storage and transport of samples without cold chain. DNA is then extracted from punched discs using the QIAGEN EZ2 Connect automated system with tissue protocol.

**Protocol:**
1. Punch 3 mm discs from FTA card (maximum 10 for consistent recovery)
2. Pre-lyse discs for 1 hour
3. Load into QIAGEN EZ2 Connect → tissue protocol (15 min purification)
4. Prepare library with Ligation Sequencing Kit, sequence on PromethION

**Sample Types:** Human blood collected on FTA cards — validated for nanopore sequencing

---

### 5.3 Ficoll-Paque Density Gradient Centrifugation

**Type:** Buffy coat isolation from whole blood

**Mechanism:** Anticoagulated blood is layered over Ficoll-Paque PREMIUM density gradient medium and centrifuged. Cells separate by density: RBCs pellet at the bottom, WBCs and platelets form a buffy coat layer at the interface, and plasma remains on top. The buffy coat (WBC/platelet fraction) is collected for DNA extraction.

**Protocol:**
1. Start with 10 ml rabbit blood in anticoagulant
2. Layer over Ficoll-Paque PREMIUM → centrifuge
3. Collect buffy coat layer at interface
4. Extract DNA using QIAGEN MagAttract HMW DNA kit
5. Size select 3 µg extracted DNA using SPRI beads before library prep

**Sample Types:** Rabbit blood (validated); applicable to human and other mammalian blood

---

## 6. Comparison Table

### 6.1 Extraction Kits — Feature Comparison

| Kit | Manufacturer | Type | Input Range | Typical Yield | Automation | HMW Preservation | Best For |
|-----|-------------|------|-------------|---------------|------------|------------------|----------|
| MagAttract HMW DNA | QIAGEN (67270) | Magnetic beads | 25 mg tissue / blood | 8–15 µg | Yes (KingFisher) | Excellent | Brain, buffy coat, fish blood/tissue |
| Puregene Cell Kit | QIAGEN (D-5943) | Semi-selective precipitation | 5×10⁶ cells / 3 mg pellet | 20–30 µg (cells); 1–2 µg (bacteria) | No | Best (no column shear) | Human cell lines, C. elegans, gram-positive bacteria |
| Blood & Cell Culture DNA Midi | QIAGEN (13362) | Genomic-tip + precipitation | 10⁸ cells / 80 mg tissue | 400–450 ng/µl | No | Excellent | Large-scale cell lines, animal tissues, saliva |
| QIAamp MinElute ccfDNA Midi | QIAGEN (55134) | Silica column (small elution vol.) | 1–5 ml plasma/serum | Variable (≥6 ng/barcode optimal) | No | N/A (short cfDNA) | Cell-free DNA, liquid biopsy, multiplex sequencing |
| DNeasy Blood & Tissue | QIAGEN (69504) | Silica column | 200 µl blood / tissue | Variable (µg range) | No | Good | General-purpose; stool (custom buffer); blood culture (after SPS removal) |
| DNeasy PowerMax Soil | QIAGEN (MAX96) | Bead-beating + silica column | Up to 10 g soil | Variable | No | Moderate | Soil, environmental samples, microbial communities |
| Plasmid Plus Midi | QIAGEN (12363) | Alkaline lysis + silica column | 50–150 ml culture | 20–30 µg plasmid DNA | No | Good (for plasmids <15 kb) | Plasmid sequencing, Rapid Sequencing V14 |
| ZymoBIOMICS DNA Miniprep | Zymo Research (D4302) | Bead-beating + silica column | Variable | Variable | No | Moderate | Environmental water eDNA — best community representation |

### 6.2 Shearing Methods — Feature Comparison

| Method | Manufacturer | Mechanism | Input | Throughput | Fragment Size Control | Best For |
|--------|-------------|-----------|-------|------------|----------------------|----------|
| Covaris g-TUBE | Covaris | Centrifugal force shearing | 100 ng–4 µg | Low (single tube) | Excellent (~8 kb at 6000 rpm) | Low-input samples, reproducible fragmentation |
| Megaruptor 3 | Diagenode (E07010003) | Acoustic shearing | 2 µg in 100 µl | Medium | Good (kit-optimized) | PromethION workflows, reduced pore blocking |
| FastPrep-96 | MP Biomedicals/Teknor | Mechanical bead-beating | 30 ng/µl × 120 µl | High (192 samples) | Adjustable (10–30 kb N50) | High-throughput shearing, brain tissue workflows |

### 6.3 Lysis Buffers — Feature Comparison

| Buffer | Primary Chaotrope | Detergent | Role | Compatible Kits |
|--------|-------------------|-----------|------|-----------------|
| ATL | Guanidine HCl (~4 M) | Triton X-100 | Cell lysis + initial protein denaturation | DNeasy Blood & Tissue; Genomic-tip (ATL variant) |
| AL | Guanidine isothiocyanate (~5 M) | Proprietary blend | Optimizes silica-column binding conditions | DNeasy Blood & Tissue; blood culture extraction |
| G2 | Guanidinium salts | Proprietary | Tissue lysis + overnight digestion at 50°C | Blood & Cell Culture DNA Midi (tissue protocols) |
| Lytic Enzyme Solution | N/A (lysozyme) | N/A | Peptidoglycan digestion for gram-positive bacteria | Puregene Cell Kit (gram-positive protocol) |

### 6.4 Size Selection Methods — Feature Comparison

| Method | Mechanism | Target Size | Reagents | Used With |
|--------|-----------|-------------|----------|-----------|
| SPRI Beads (AMPure XP) | PEG/NaCl paramagnetic binding | Adjustable by ratio (0.7× → >2 kb; 0.6× cleanup) | AMPure XP beads + custom buffer | Puregene, Blood & Cell Culture Midi, Rapid PCR Barcoding, PrepMan Ultra |
| Semi-Selective Precipitation | PVP 360,000 + NaCl molecular crowding | Enriches >long fragments (removes short) | 2.5% w/v PVP 360,000 + 1.2 M NaCl | Puregene Cell Kit, Blood & Cell Culture Midi (C. elegans, frog, lizard, saliva) |

---

## 7. Analysis and Recommendations

### 7.1 Choosing the Right Extraction Kit

**For HMW DNA (>50 kb) for Nanopore sequencing:**
- **Best overall:** QIAGEN Puregene Cell Kit — no column shear forces; spooling option for visual confirmation of HMW integrity
- **Automatable alternative:** MagAttract HMW DNA Kit — magnetic beads eliminate spin-column shear; compatible with KingFisher automation
- **Large-scale cell lines:** Blood and Cell Culture DNA Midi Kit — gravity-flow Genomic-tip columns minimize shear

**For microbial community/environmental samples:**
- **Best community representation:** ZymoBIOMICS DNA Miniprep Kit — validated against defined microbial standards for eDNA
- **Soil:** DNeasy PowerMax Soil Kit — bead-beating essential; do not exceed 10 g input

**For clinical/diagnostic applications:**
- **Blood culture broth:** DNeasy Blood & Tissue Kit with SPS removal (centrifugation + ethanol wash) — standard protocol without SPS removal gives zero PCR amplification
- **Mycobacteria:** PrepMan Ultra Reagent + bead beating — rapid pathogen inactivation; validated for XDR M. tuberculosis nanopore sequencing
- **cfDNA/liquid biopsy:** QIAamp MinElute ccfDNA Midi Kit — small elution volume concentrates dilute cfDNA

**For plasmid sequencing:**
- **Standard plasmids (<15 kb):** Plasmid Plus Midi Kit — Oxford Nanopore's recommended method; 20–30 µg yield from 50–150 ml culture
- **Large plasmids (>30 kb) / BACs:** Agarose plug method with phenol-chloroform extraction — avoids column shear forces

### 7.2 Key Protocol Considerations

**SPS Removal (Blood Culture Broth):** The single most critical modification for blood culture DNA extraction. SPS inhibits DNA polymerases, interferes with restriction enzymes, and binds silica membranes. Centrifugation at 20,000 × g for 10 minutes + ethanol wash is the validated approach. Without this step, standard DNeasy kit protocol yields zero amplifiable DNA.

**Chloramphenicol Pre-Treatment (Gram-Negative Bacteria):** Adding chloramphenicol to 180 µg/ml one hour before culture collection increases yield ~4.5× by stopping cell division while allowing DNA replication completion. Simple, inexpensive optimization with dramatic impact.

**Lytic Enzyme Solution (Gram-Positive Bacteria):** Essential for breaking down thick peptidoglycan cell walls. Without enzymatic pre-treatment, chemical lysis buffers cannot penetrate gram-positive cell walls effectively. For recalcitrant species: add 80°C heat lysis step for 5 minutes.

**Semi-Selective Precipitation vs SPRI Beads:** Both methods enrich for longer DNA fragments. Semi-selective precipitation (PVP + NaCl) is used with Puregene and Blood & Cell Culture Midi protocols. SPRI beads are more flexible (adjustable ratio) but require careful pipetting of PEG solutions.

**Shearing Trade-offs:** All three shearing methods (g-TUBE, Megaruptor 3, FastPrep-96) increase sequencing output by generating more molecules for the flow cell, but reduce read N50. Choose based on throughput needs: g-TUBE for low-input precision, Megaruptor 3 for PromethION workflows, FastPrep-96 for high-throughput batch processing.

### 7.3 Cost and Throughput Considerations

| Priority | Recommended Approach |
|----------|---------------------|
| Lowest cost per sample | Puregene Cell Kit (reagent costs lower than column-based kits; no columns to replace) |
| Highest throughput | FastPrep-96 shearing + MagAttract HMW DNA Kit automation on KingFisher |
| Best HMW preservation | Puregene Cell Kit with spooling → visual confirmation before library prep |
| Fastest turnaround | Rapid PCR Barcoding Kit (SQK-RBK114) — ~10 min hands-on from colony to library |
| Most versatile | DNeasy Blood & Tissue Kit — works across blood, tissue, stool (with custom buffer), and blood culture (after SPS removal) |

---

## 8. Sources

This document synthesizes information from 34 LLM Wiki concept pages created on 2026-06-19, each derived from:
- Oxford Nanopore Technologies protocol documents (primary source for all kit protocols)
- Peer-reviewed literature cited in wiki pages (Villumsen et al. 2010; Bainomugisa et al. 2018; Maudet et al.; Uematsu & Baskin 2025; Li et al. 2024)
- QIAGEN product documentation and handbooks (DNeasy Blood & Tissue Kit Handbook, Genomic DNA Handbook)
- Manufacturer specifications (Covaris g-TUBE, Diagenode Megaruptor 3, Beckman Coulter AMPure XP)

Full source URLs are embedded in individual wiki concept pages under `/root/wiki/concepts/`.
