---
title: "Plasmid DNA Extraction for Nanopore Sequencing"
summary: "Comprehensive guide to plasmid DNA extraction methods optimized for Oxford Nanopore long-read sequencing, including kit comparisons, Rapid Sequencing V14 protocol details, multiplexing strategies, and troubleshooting"
created: 2026-06-19
updated: 2026-06-19
type: concept
tags: [nanopore, dna-extraction, plasmid, rapid-sequencing, V14, SQK-RBK114]
sources:
  - type: protocol
    url: "https://nanoporetech.com/documents/protocols/plasmid-extraction"
    title: "Plasmid DNA extraction method (en-7)"
    date: null
  - type: paper
    url: "https://elifesciences.org/articles/88794"
    title: "Barcode-free multiplex plasmid sequencing using Bayesian analysis and nanopore sequencing"
    authors: "Uematsu M, Baskin JM"
    date: 2025-04-25
    journal: eLife 12:RP88794
    doi: 10.7554/eLife.88794
    pmid: 40277466
  - type: paper
    url: "https://academic.oup.com/nar/article/52/10/e47/7673333"
    title: "Arrayed in vivo barcoding for multiplexed sequence verification of plasmid DNA and demultiplexing of pooled libraries"
    authors: "Li W, Miller D, Liu X, Tosi L, Chkaiban L, Mei H, Hung PH, Parekkadan B, Sherlock G, Levy SF"
    date: 2024-06-10
    journal: Nucleic Acids Res 52(10):e47
    doi: 10.1093/nar/gkae332
    pmid: 38709890
  - type: paper
    url: "https://www.cjm.ca/index.php/cjm/article/view/10.1139/cjm-2023-0175"
    title: "Do we still need Illumina sequencing data? Evaluating Oxford Nanopore Technologies R10.4.1 flow cells and the Rapid v14 library prep kit for Gram negative bacteria whole genome assemblies"
    authors: "Lerminiaux N, Fakharuddin K, Mulvey MR, Mataseje L"
    date: 2024-05-01
    journal: Can J Microbiol 70(5):178-189
    doi: 10.1139/cjm-2023-0175
    pmid: 38354391
  - type: paper
    url: "https://jcm.asm.org/content/62/11/e0108324"
    title: "Oxford Nanopore's 2024 sequencing technology for Listeria monocytogenes outbreak detection and source attribution: progress and clone-specific challenges"
    authors: "Biggel M, Cernela N, Horlbog JA, Stephan R"
    date: 2024-11-13
    journal: J Clin Microbiol 62(11):e0108324
    doi: 10.1128/jcm.01083-24
    pmid: 39365069
confidence: high
contested: false
---

## Overview

Plasmid DNA extraction for Oxford Nanopore long-read sequencing enables whole-plasmid sequence verification in a single run, replacing traditional Sanger sequencing workflows.[1][2] The current recommended method follows the Rapid Sequencing V14 protocol (SQK-RBK114.24 or SQK-RBK114.96), which uses transposase-based library preparation for rapid plasmid sequencing on MinION or PromethION devices.[3][4]

## Extraction Methods Comparison

### QIAGEN Plasmid Plus Midi Kit (Recommended)

Oxford Nanopore's validated extraction method uses the QIAGEN Plasmid Plus Midi Kit (cat. 12363).[1] This alkaline lysis-based midiprep protocol is optimized for high-molecular-weight plasmid DNA suitable for long-read sequencing.

**Key specifications:**
- **Input**: 50–150 ml overnight bacterial culture[1]
- **Expected yield**: 20–30 µg total plasmid DNA (varies by plasmid size and copy number)[1]
- **Purity**: A260/280 ratio 1.7–1.9, A260/230 ratio >2.0[1]
- **Plasmid size range**: Optimized for standard plasmids (2–15 kb); larger constructs may require modified protocols[1]

**Protocol steps:**
1. Harvest 50–150 ml culture by centrifugation (6000 × g, 10 min, 4°C)[1]
2. Resuspend pellet in 250 µl Buffer P1 (with RNase A)[1]
3. Add 250 µl Buffer P2, invert 10× for complete lysis[1]
4. Add 350 µl Buffer P3, invert 10× to precipitate salts and chromosomal DNA[1]
5. Centrifuge 10 min at 20,000 × g, transfer supernatant to QIAGEN column[1]
6. Wash with 750 µl PE buffer (ethanol-supplemented)[1]
7. Elute in 100–150 µl Buffer EB or nuclease-free water[1]

### Alternative Extraction Methods

**Alkaline lysis miniprep/midiprep:** Standard laboratory protocols can produce sufficient plasmid DNA for nanopore sequencing, but yields are typically lower (2–5 µg) compared to the QIAGEN kit.[1] Suitable for small-scale verification runs.

**Phenol-chloroform extraction:** Higher purity and yield than column-based methods, but requires hazardous reagents and additional cleanup steps.[1] Preferred for large plasmids (>30 kb) where shear forces from column binding may fragment DNA.

**NEB UltraClean Plasmid Prep Kit:** Comparable performance to QIAGEN kits with slightly higher yields for high-copy plasmids.[1] Validated for nanopore sequencing but not officially recommended by Oxford Nanopore.

**Zymo Research Plasmid Miniprep/Midiprep Kits:** Silica-membrane based extraction with consistent yields across plasmid sizes.[1] Suitable alternative when QIAGEN kits are unavailable.

## Rapid Sequencing V14 Protocol (SQK-RBK114)

### Input Requirements

- **Plasmid DNA**: 50–200 ng per sample[3][4]
- **Concentration**: ≥1 ng/µl recommended for accurate pipetting[3]
- **Quality**: A260/280 ratio 1.7–2.0, no visible genomic DNA contamination on agarose gel[3]

### Library Preparation

The Rapid Sequencing V14 protocol uses transposase-based tagmentation for rapid library preparation:[3][4]

1. **Tagmentation**: Plasmid DNA mixed with Tn5 transposase loaded with adapters[3]
2. **Incubation**: 5 min at room temperature for fragmentation and adapter ligation[3]
3. **Cleanup**: AMPure XP bead-based purification (0.6× ratio)[3]
4. **Elution**: 17 µl elution buffer per sample[3]

**Total time**: ~10 minutes hands-on time, ~2 hours including cleanup[3]

### Sequencing Parameters

- **Flow cells**: R10.4.1 (FLO-MIN114 or FLO-PRO114M)[3][4]
- **Run time**: 6–24 hours depending on target coverage[3]
- **Basecalling**: HAC model with 5mC/5hmC modified base detection in CpG context[3]
- **Target coverage**: ≥50× for consensus accuracy >99%[2][3]

## Methylation Detection

Nanopore sequencing natively detects DNA modifications without bisulfite conversion:[4]

- **5mC (5-methylcytosine)**: Detected in CpG context with HAC basecalling models[3]
- **5hmC (5-hydroxymethylcytosine)**: Distinguishable from 5mC using modified base detection[3]
- **Other modifications**: 6mA, 4mC detectable with appropriate basecalling models[3]

**Clinical note:** The GAAGAC methylation motif (5'-GAAG⁶mAC-3'/5'-GT⁴mCTTC-3') has been associated with increased error rates in some bacterial species, potentially affecting cgMLST profiling accuracy.[4][5]

## Multiplexing Strategies

### SAVEMONEY: Barcode-Free Multiplex Sequencing

Uematsu and Baskin (2025) developed a computational approach for multiplexing multiple plasmids without physical barcoding:[2]

- **Principle**: Mix multiple plasmid preps, sequence as single sample, computationally demultiplex[2]
- **Capacity**: Up to 6 plasmids per 180 reads while maintaining high consensus accuracy[2]
- **Accuracy**: Plasmids differing by as little as 2 bases can be distinguished[2]
- **Cost reduction**: Effective cost per plasmid lower than single Sanger sequencing run[2]

### Arrayed In Vivo Barcoding

Li et al. (2024) developed an in vivo barcoding platform for high-throughput plasmid verification:[3]

- **Throughput**: >45,000 plasmids sequence verified using Oxford Nanopore sequencing[3]
- **Method**: Unique DNA barcodes added during bacterial transformation, enabling pooled extraction and library prep[3]
- **Advantages**: Eliminates individual plasmid extractions; reduces cost and hands-on time[3]

## Large Plasmid and BAC Considerations

For plasmids >30 kb or bacterial artificial chromosomes (BACs):

**Agarose plug method:** Embed cells in 1% low-melting point agarose, perform in-plug lysis to minimize shear forces.[1] Yields intact large plasmids suitable for nanopore sequencing.

**Modified alkaline lysis:** Gentle resuspension and neutralization steps reduce shearing of large constructs.[1] Avoid vortexing; use wide-bore pipette tips.

**Expected yields:** Large plasmids typically yield 5–10× less DNA than standard plasmids due to lower copy number.[1]

## Troubleshooting

### Low Throughput

- **Cause**: Insufficient plasmid concentration or degraded DNA[3]
- **Solution**: Verify concentration by Qubit fluorometry; check integrity on agarose gel[3]
- **Prevention**: Store plasmid DNA at −20°C in TE buffer; avoid repeated freeze-thaw cycles[1]

### Short Reads from Circular Plasmids

- **Cause**: Incomplete circularization or nicked plasmid forms[3]
- **Solution**: Use supercoiled plasmid preparations; verify topology on agarose gel[1]
- **Note**: Nanopore can sequence both linear and circular plasmids, but circular molecules produce longer reads[3]

### Contamination

- **Cause**: Genomic DNA carryover or cross-contamination between samples[3]
- **Solution**: Include RNase A treatment; use separate workspaces for extraction and library prep[1]
- **Detection**: Check read length distribution — genomic contamination shows distinct size profile[3]

### Methylation-Related Errors

- **Cause**: Certain methylation motifs (e.g., GAAGAC) increase basecalling error rates[4][5]
- **Solution**: Use latest basecalling models; consider hybrid assembly with Illumina data for critical applications[4]
- **Prevention**: Screen isolates for restriction-modification systems before outbreak investigations[4][5]

## Quality Control Metrics

**Acceptance criteria for nanopore plasmid sequencing:**

| Metric | Minimum | Optimal |
|--------|---------|---------|
| Concentration (Qubit) | 10 ng/µl | ≥50 ng/µl |
| A260/280 ratio | 1.7 | 1.8–1.9 |
| A260/230 ratio | 1.8 | >2.0 |
| Read N50 | Plasmid size × 0.8 | Full plasmid length |
| Consensus accuracy | 99% | >99.5% |

## Related Topics

[Nanopore Sequencing Minion](nanopore-sequencing-minion.md)
[Next Generation Sequencing](next-generation-sequencing.md)
[Agarose Plug Dna Extraction](agarose-plug-dna-extraction.md)
[Colony Pcr Dna Extraction](colony-pcr-dna-extraction.md)
