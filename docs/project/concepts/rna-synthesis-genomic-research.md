# RNA Synthesis — Glen Research Application Note on Long Oligonucleotide Production

## Overview

A technical application note from **Glen Research** (Genomic Research) providing quantitative assessment of factors impacting long RNA oligonucleotide synthesis quality. Compares coupling efficiencies of DNA, TBDMS-protected, and TOM-protected RNA phosphoramidites across two universal solid supports (US III PS and Glen UnySupport™ CPG). Key finding: **TOM monomers offer higher coupling efficiency than TBDMS**, with significant impact on longer syntheses — extrapolated 100mer purity of 33% for TOM vs. 27% for TBDMS.

## Citation

> Glen Research (Genomic Research). "Application Note: RNA Synthesis." Technical note, version 073124.
> Glen Research, Inc., 22825 Davis Drive, Sterling, VA 20164. glenresearch.com

## Background and Motivation

Long RNA synthesis (>100mer) has become increasingly important for:
- **CRISPR technology**: sgRNA constructs (Zhao et al. 2014; Briner et al. 2014)
- **Real-time PCR**: Long RNA probes and templates
- **mRNA therapeutics**: Short mRNA sequences for therapeutic applications (Abe et al. 2022)
- **Genomic pathway studies**: Functional analysis of long non-coding RNAs (Statello et al. 2021)

### The RNA Synthesis Challenge
RNA synthesis is inherently less efficient than DNA due to:
1. **2′-O-protecting group requirement**: Bulky silyl groups cause steric hindrance during coupling
2. **Secondary structure**: RNA forms stable secondary structures complicating isolation of single-stranded products

### Protecting Group Comparison
| Protecting Group | Full Name | Characteristics |
|---|---|---|
| **TBDMS** | tert-Butyldimethylsilyl | Standard 2′-silyl group; bulkier, more steric hindrance |
| **TOM** | Triisopropylsilyloxymethyl | Oxymethyl spacer extends silyl group further from phosphoramidite center; recommended for long RNA |

## Experimental Design

### Synthesis Conditions
- Platform: **ABI 394 synthesizer**, 1.0 µmol scale
- Test sequence (20mer): `5′-UUG UUC UUA UUG UUC UUA UU*-3′` (T for DNA control)
- Coupling time: **6 minutes** per cycle
- Activator: **0.25M ETT** (5-Ethylthio-1H-Tetrazole) in anhydrous acetonitrile
- Deblocking: **DCA** (3% dichloroacetic acid in dichloromethane) — mimics recommended conditions for long oligonucleotide synthesis

### Cleavage and Deprotection Protocols

#### US III PS Support
1. Incubate in 2M ammonia in methanol, 60 min at RT
2. Add equal volume AMA (Ammonium Hydroxide/Methanol/Acetonitrile)
3. Continue deprotection: **10 min at 65°C**

#### Glen UnySupport™ CPG Support
1. Incubate in AMA, **60 min at 65°C** (harsher conditions required for complete cleavage)

### Post-Synthesis Processing
- **2′-Desilylation**: DMSO dissolution → TEA + TEA·3HF → 65°C water bath, 2.5 hours → RNA quenching buffer
- **Desalting**: Glen Gel-Pak™ 1.0 desalting column, elution in 0.1M RNase-free TEAA
- **Analysis**: RP-HPLC

## Key Results

### Coupling Efficiencies (Table 1)
| Universal Support | Monomer Type | Coupling Efficiency |
|---|---|---|
| US III PS | DNA | **99.7%** |
| US III PS | TOM RNA | **98.9%** |
| US III PS | TBDMS RNA | **98.7%** |
| UnySupport CPG | TBDMS RNA | **97.7%** |

### Crude Purity (20mer on US III PS)
- TOM: **80.1%** crude purity
- TBDMS: **77.6%** crude purity

### Extrapolated 100mer Purity
Using the formula: CEL = CE^L (where CE = coupling efficiency as decimal, L = length)
- **TOM 100mer**: ~33% expected crude purity
- **TBDMS 100mer**: ~27% expected crude purity

### DMT Loss Issue
Small but unavoidable loss of the trityl (DMT) group detected during:
- Drying step for cleavage/deprotection
- 2′-Desilylation reaction
- Implication: Full-length DMT-OFF oligonucleotide co-elutes with failure sequences in RP-HPLC

### Support Comparison
**US III PS outperformed UnySupport CPG**:
- UnySupport requires harsher cleavage conditions (AMA at 65°C for 1 hour vs. 10 min)
- Harsh conditions caused strand cleavage yielding shorter DMT-ON fragments
- These fragments cannot be distinguished from full-length DMT-ON sequence during reverse phase cartridge purification

## Solid Support Pore Size Guidelines

| Support Type | Maximum Synthesis Length |
|---|---|
| 500 Å CPG | Up to **50mer** |
| 1000 Å CPG | Compatible with **75–100mer** |
| 2000 Å CPG | For **>100mer** |
| PS (Polystyrene) | Comparable to **1000 Å CPG** |

## Key Takeaways and Recommendations

### Monomer Selection
- **TOM preferred over TBDMS** for long RNA synthesis — the ~0.2% per-cycle efficiency difference compounds significantly with length
- For 100mer: TOM provides ~6 percentage points higher crude purity than TBDMS

### Purification Strategy
- **Avoid DMT-ON reverse phase purification** for long RNA due to unavoidable trityl loss and finite hydrophobicity of the trityl group on polar phosphate backbones
- **Recommended alternatives**: Ion exchange chromatography or PAGE (polyacrylamide gel electrophoresis) purification

### Support Selection
- **US III PS recommended over UnySupport CPG** for cleaner crude results
- Avoid UnySupport if using reverse phase cartridge purification due to cleavage fragment contamination risk

## Critical Analysis

### Strengths
- Quantitative, data-driven comparison rather than qualitative claims
- Extrapolation methodology provides practical guidance for longer syntheses
- Addresses real-world complications (DMT loss, secondary structure) that affect downstream applications
- Clear product catalog references enable direct procurement

### Limitations
- **20mer test only**: Extrapolation to 100mer assumes constant per-cycle efficiency — actual long RNA synthesis may have additional failure modes (secondary structure interference, incomplete deblocking in longer sequences)
- **Single sequence tested**: Results may vary with GC content and secondary structure propensity of different sequences
- **No yield data**: Purity ≠ yield; a 33% pure product from low-yield synthesis is still impractical
- **Commercial bias**: Glen Research evaluates their own products (US III PS, UnySupport)

### Relevance to CRISPR and Therapeutic RNA Work
For sgRNA synthesis in CRISPR applications:
- Typical sgRNA length: ~100–120 nucleotides
- TOM monomers on US III PS would be the recommended combination
- PAGE purification preferred over DMT-ON cartridge for final product

## Cross-References

[Crispr Cas9](concepts/crispr-cas9.md) — CRISPR-Cas9 sgRNA synthesis applications requiring long RNA oligonucleotides
[Crispr Amr Diagnostics](concepts/crispr-amr-diagnostics.md) — CRISPR-based diagnostic platforms (SHERLOCK, DETECTR) require synthetic RNA components
[Bioinformatics](concepts/bioinformatics.md) — Computational design of RNA sequences for therapeutic and research applications
