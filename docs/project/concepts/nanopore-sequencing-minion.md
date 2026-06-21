---
title: "Nanopore Sequencing (MinION)"
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [sequencing, metagenomics, emerging-diseases, technique]
sources:
  - type: paper
    url: "https://wwwnc.cdc.gov/EID/article/22/2/15-1796.pdf"
    title: "Nanopore Sequencing as a Rapidly Deployable Ebola Outbreak Tool"
    date: 2016-02
confidence: high
contested: false
---

# Nanopore Sequencing (MinION)

## Overview

Oxford Nanopore Technologies' MinION is a pocket-sized DNA/RNA sequencer (~10 × 4 × 2 cm, 75 g) that senses individual nucleic acid molecules based on modulation of ion currents across nanopores as molecules pass through. Nucleotide sequence determination depends on the physical properties of each base [1].

Unlike conventional [Next Generation Sequencing](concepts/next-generation-sequencing.md) platforms (Illumina MiSeq: ~40–100 kg), MinION requires no special setup or calibration and becomes operational immediately upon arrival at a site — making it uniquely suited for field deployment in resource-limited settings.

## How It Works

- DNA/RNA molecules pass through protein nanopores embedded in a membrane
- Each nucleotide causes a characteristic disruption in ionic current
- Current modulations are decoded into base calls by software (e.g., ONT Metrichor)
- Long reads possible — no amplification bias from short fragments required

## Key Performance Metrics (EBOV study, 2014–2015)

| Metric | Value |
|--------|-------|
| Single-read accuracy | ~84% [1] |
| Average read depth per position | ~7,038 reads [1] |
| Coverage threshold for reliable consensus | >33x at all positions (TPMB <5%) [1] |
| Capacity (single operator, 2 devices) | 4 full-length genomes/day [1] |

Read depth compensates for individual miscalls — piling up reads covering the same region allows high-confidence consensus calling despite lower per-read accuracy.

## Field Deployment: Ebola Outbreak in Liberia

**Study:** Hoenen et al., CDC/NIH field laboratory, Monrovia, Liberia (August 2014–May 2015) [1]

### Protocol
- Two-step RT-PCR amplification of whole EBOV genomes in overlapping fragments
- Library prep: SQK-MAP004 kit (ONT)
- Flow cells: R7.3
- Base calling: ONT Metrichor v2.25.1 (cloud-based via 4G cellular network)
- Bioinformatics pipeline: Poretools → lastal alignment → Samtools pileup → custom Perl consensus caller

### Results
- **8 of 9 high-virus-load samples** (Ct <21): complete genome sequences obtained [1]
- Lower virus-load samples yielded incomplete genomes but with high read depth in covered regions — suggesting PCR optimization could improve coverage [1]
- Even partial genomes provided valuable outbreak data: individual gene analysis and transmission chain tracing [1]

### Environmental Challenges
- Laboratory temperatures: 28–32°C required improvised heat sink (metal plate ~30 × 30 cm) to prevent device overheating [1]
- All equipment transported as checked luggage by a single person on commercial carrier [1]
- Internet connectivity via Novafone 4G cellular network for cloud-based base calling [1]

### Phylogenetic Findings
- Liberian EBOV sequences clustered distinctly from Sierra Leone and early Guinea strains — suggesting **single introduction or limited introductions** of genetically similar viruses into Liberia [1]
- Nucleotide substitution rate: **1.36 × 10⁻³** (consistent with published values) [1]
- Few mutations observed, mostly in noncoding regions or synonymous changes; none affected siRNA targets or diagnostic assay targets [1]
- EBOV remained genetically stable during the outbreak [1]

## Advantages for Outbreak Response

1. **Portability** — pocket-sized device transportable as hand luggage
2. **Rapid deployment** — no calibration, operational immediately
3. **Fast turnaround** — real-time sequencing enables rapid diagnostic decisions
4. **Resource-light** — modest infrastructure requirements vs. conventional sequencers
5. **Versatile** — applicable to any RNA/DNA pathogen; metagenomic approaches (not requiring prior pathogen identification) under development [1,7]

## Limitations and Challenges

- Single-read accuracy (~84%) requires high coverage depth for reliable consensus
- Initial PCR optimization needed for field conditions (nested PCR improved yields)
- Cloud-based base calling dependent on internet connectivity — local algorithms in development at time of study
- Bioinformatics analysis initially done post-mission to maximize data acquisition time

## Comparison with Conventional Platforms

| Feature | MinION (ONT) | Illumina MiSeq | Sanger |
|---------|-------------|----------------|--------|
| Size/weight | 10×4×2 cm, 75 g | ~40–100 kg | Bench-top |
| Setup/calibration | None required | Field engineer needed | Calibration required |
| Read length | Long reads | Short reads | Medium (~800 bp) |
| Portability | Hand-carry | Checked luggage only | Limited |
| Accuracy (single read) | ~84% | >99.9% | >99.99% |
| Field deployment proven | Yes (Liberia 2014–2015) [1] | Yes (Liberia, Feb 2015) [5] | No |

## Related Technologies and Concepts

- [Next Generation Sequencing](concepts/next-generation-sequencing.md) — broader category of high-throughput sequencing
- [Metagenomics](concepts/metagenomics.md) — nanopore enables real-time metagenomic pathogen identification in clinical samples [7]
- [Crispr Amr Diagnostics](concepts/crispr-amr-diagnostics.md) — complementary rapid diagnostic approach for antimicrobial resistance detection
- [Phylogenetics Phylodynamics](concepts/phylogenetics-phylodynamics.md) — phylogenetic analysis of outbreak sequences (BEAST2, Bayesian coalescent)

## References

[1] Hoenen T et al. Nanopore Sequencing as a Rapidly Deployable Ebola Outbreak Tool. *Emerg Infect Dis*. 2016;22(2):331–334. doi:10.3201/eid2202.151796

[5] Kugelman JR et al. Monitoring of Ebola Virus Makona Evolution through Establishment of Advanced Genomic Capability in Liberia. *Emerg Infect Dis*. 2015;21:1135–43. doi:10.3201/eid2107.15052

[7] Greninger AL et al. Rapid metagenomic identification of viral pathogens in clinical samples by real-time nanopore sequencing analysis. *Genome Med*. 2015;7(1):99. doi:10.1186/s13073-015-0220-9
