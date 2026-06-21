# Genome-Based Salmonella Serotyping as the New Gold Standard

> **Citation:** Banerji S, Simon S, Tille A, Fruth A, Flieger A. "Genome-based Salmonella serotyping as the new gold standard." *Scientific Reports* 10 (2020): 4333. DOI: [10.1038/s41598-020-61254-1](https://doi.org/10.1038/s41598-020-61254-1)
> **Authors:** Sangeeta Banerji, Sandra Simon, Andreas Tille, Angelika Fruth, Antje Flieger* (Robert Koch-Institute, National Reference Center for Salmonella and other Bacterial Enteric Pathogens, Wernigerode, Germany)
> **Published:** 2020 | Open Access

## Overview

This study evaluates the feasibility of replacing classical serotyping with genome-based *in silico* serotyping for routine *Salmonella enterica* surveillance at the German National Reference Center (NRC). Using 520 isolates across 20 serotypes, the authors benchmark two tools — **SeqSero** (O/H antigen gene detection) and **7-gene MLST via Enterobase/SeqSphere+** — against classical White-Kauffmann-Le Minor scheme serotyping. Combined concordance exceeded 99%, but both tools exhibited systematic misidentification of monophasic variants, particularly the epidemiologically important monophasic *S.* Typhimurium.

## Key Findings

### Overall Concordance
| Method | Concordance with Classical Serotyping |
|--------|--------------------------------------|
| SeqSero alone | 98% (correlation + ambiguous predictions) |
| MLST alone | 95% |
| **SeqSero + MLST combined** | **>99%** |

### Dataset Composition
- **520 *Salmonella* isolates**, mainly human origin, predominantly from years 2014–2018
- **20 different serotypes** tested, including:
  - Most common German serotypes: *S.* Enteritidis and *S.* Typhimurium
  - Less frequent serotypes: *S.* Infantis, *S.* Derby, *S.* Choleraesuis, etc.
- Monophasic variants and rough phenotypes specifically included

### SeqSero Performance Details
- **84%** predicted exact classical serovar match
- **14%** ambiguous predictions (antigenic formula shared by multiple serovars, e.g., 6,7:c:1,5 = Choleraesuis/Typhisuis/Paratyphi C) — counted as correlating since these require additional testing regardless of method
- **1% prediction failure** (n=5): all involved failed O-7 antigen detection
- **1% miscorrelation**: monophasic *S.* Typhimurium and *S.* Choleraesuis misidentified

### Monophasic Variant Problem
The most significant finding: both tools struggle with monophasic variants.

**Case 1 — ERR2003330:** Phenotypically monophasic but predicted biphasic by SeqSero 1.0 (raw reads). De novo assembly revealed ~250 nt deletion in *fljB* gene + complete loss of *hin* invertase gene due to transposase (*tnpA*) integration. SeqSero 1.0 only checks for presence/absence of *fliC* and *fljB* alleles, not regulatory genes. **SeqSero 2.0 (k-mer mode) correctly classified this as monophasic** from raw reads.

**Case 2 — ERR2003327:** Transposon integrated into *fljB* gene rendering it non-functional but fully present in sequence. Both SeqSero 1.0 and 2.0 (raw reads) predicted biphasic because the gene is intact at the DNA level despite being phenotypically silent. **Assembled contigs correctly classified as monophasic by both versions.**

### Data Quality Threshold
- Analysis failed for raw read files <50,000 kbytes
- Minimum coverage target: ≥10-fold (consistent with SeqSero 1.0 requirements)
- For *Salmonella* (~4.8 Mb genome): minimum ~80,000 reads per direction for paired-end 300 bp reads

### Tools Evaluated
| Tool | Approach | Input Type | Offline? | Used in Study? |
|------|----------|-----------|----------|----------------|
| **SeqSero** | O/H antigen gene detection | Raw reads or assembled | Yes (CLI) | ✅ Primary tool |
| **MLST/Enterobase** | 7-gene MLST → serotype mapping | Assembled genomes | Yes (SeqSphere+) | ✅ Primary tool |
| MOST | Modified SRST + local DB | Short reads | No | ❌ Not compatible with pipeline |
| SalmonellaTypeFinder | SeqSero + in-house MLST | Assembled | No | ❌ Different MLST algorithm |
| SISTR | In silico hybridization + eMLST | Assembled genomes | Yes | ❌ Requires assembly |

## Methodology

### Classical Serotyping (Reference Standard)
- White-Kauffmann-Le Minor Scheme: antigenic formula O:H1:H2
- Phase 1 flagellin (*fliC*) and phase 2 flagellin (*fljB*), regulated by invertase *hin* and repressor *fljA*
- O antigens determined within hours; H phases may require up to 7 days

### In Silico Serotyping Pipeline
1. Raw Illumina paired-end reads → quality check (≥80,000 reads/direction)
2. SeqSero 1.0 analysis on raw reads (command-line mode)
3. Ridom SeqSphere+ MLST typing via Enterobase scheme
4. Comparison with classical serotyping results from NRC laboratory

### Validation Approach
- Concordance defined as: exact match + ambiguous predictions (where multiple serovars share antigenic formula)
- Monophasic variants analyzed separately due to known challenges
- SeqSero 2.0 tested on discordant cases during manuscript preparation

## Critical Analysis

### Strengths
1. **Real-world validation**: Tested against actual NRC routine isolates (not curated reference strains), reflecting practical deployment conditions
2. **Raw reads approach**: Avoiding genome assembly saves time and compute — critical for high-throughput surveillance processing 3,000–5,000 isolates/year
3. **Combined method strategy**: SeqSero + MLST achieving >99% concordance provides a robust dual-verification framework
4. **Detailed failure analysis**: Monophasic variant misidentification thoroughly investigated with de novo assembly and gene-level resolution

### Limitations
1. **SeqSero 2.0 not fully benchmarked**: Only tested on discordant cases, not the full dataset — performance comparison between versions incomplete
2. **Limited serotype diversity**: 20 serotypes tested; *Salmonella* has >2,600 serovars globally. Rare serotypes may present different challenges
3. **No assessment of rough phenotypes' impact on MLST**: Rough variants (defective O-antigen) could affect both methods differently
4. **Single-laboratory setting**: German NRC experience may not generalize to laboratories with different isolate populations or sequencing platforms
5. **Classical serotyping success rate context**: Worldwide average 82% correct results (European: 89%) — the in silico methods outperform even expert classical serotyping, but this comparison is rarely emphasized

### Clinical/Public Health Relevance
- Supports transition from labor-intensive classical serotyping to NGS-based surveillance for national reference laboratories
- Monophasic *S.* Typhimurium (particularly ST31 clone) is an important multidrug-resistant lineage in Europe — accurate detection essential for outbreak tracking
- Combined SeqSero + MLST approach provides >99% concordance, exceeding even expert classical serotyping success rates
- Raw-reads workflow compatible with existing Ridom SeqSphere+ pipeline at NRC

## Cross-References

See also: [Next Generation Sequencing](next-generation-sequencing.md), [Antimicrobial Resistance](antimicrobial-resistance.md), [Phylogenetics Phylodynamics](phylogenetics-phylodynamics.md)
