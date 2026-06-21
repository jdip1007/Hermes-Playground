# Changelog — 2026-06-19

## New Pages

### Concepts (Oxford Nanopore Protocols Batch)

Batch processing of 34 new files from `New folder.zip`. **10 skipped** (already processed in previous session). **28 new wiki pages created**.

#### Sequencing Workflows
- **promethion-24hr-genome-workflow** — PromethION 24-hour genome end-to-end workflow: blood to variant calls using SQK-LSK114, Megaruptor 3 shearing, wf-human-variation EPI2ME analysis (Clair3/Sniffles2/Spectre/Straglr/modkit)
- **adaptive-sampling-nanopore** — Adaptive sampling: real-time read selection via polarity reversal, enrichment/depletion modes, buffer optimization (~5–10× enrichment at <10% target fraction)

#### DNA Extraction Methods (by sample type)
- **agarose-plug-dna-extraction** — Phenol-chloroform extraction from 1% low-melt agarose plugs
- **animal-tissue-re-pore-c-preparation** — Cryo-grinding Rattus norvegicus brain/muscle for RE-Pore-C chromatin conformation analysis
- **brain-tissue-dna-extraction** — Human brain tissue: QIAGEN MagAttract HMW DNA Kit (8–15 µg from 25 mg, automatable)
- **buffy-coat-dna-extraction** — Rabbit buffy coat via Ficoll-Paque density gradient + MagAttract HMW DNA kit
- **c-elegans-dna-extraction** — C. elegans (SX3254/N2): QIAGEN Puregene Cell Kit with semi-selective precipitation
- **colony-pcr-dna-extraction** — Bacterial colony PCR: Rapid PCR Barcoding Kit from plated colonies
- **dry-blood-spots-dna-extraction** — FTA cards: QIAGEN EZ2 Connect automation (10× 3 mm discs optimal)
- **environmental-water-edna-extraction** — eDNA: ZymoBIOMICS DNA Miniprep Kit yields best community representation
- **frog-muscle-dna-extraction** — Xenopus tropicalis muscle: QIAGEN Blood & Cell Culture DNA Midi Kit
- **gram-negative-bacterial-dna-extraction** — E. coli: QIAGEN Genomic-tip 500/G with chloramphenicol pre-treatment (4.5× yield increase)
- **human-saliva-dna-extraction** — Human saliva: QIAGEN Blood & Cell Culture DNA Midi Kit
- **lizard-tissue-dna-extraction** — Anolis carolinensis tail: ethanol-preserved or fresh tissue
- **multiplex-cfdna-extraction** — Multiplex cfDNA: QIAamp MinElute ccfDNA Midi Kit (≥6 ng/barcode optimal)
- **mycobacterium-tuberculosis-dna-extraction** — M. tuberculosis from Löwenstein–Jensen culture: PrepMan Ultra + bead beating
- **plasmid-dna-extraction** — Plasmid DNA: QIAGEN Plasmid Plus Midi Kit, Rapid Sequencing V14 protocol
- **rabbit-liver-dna-extraction** — Rabbit liver: QIAGEN Blood & Cell Culture DNA Midi Kit (up to 80 mg)
- **rat-stool-dna-extraction** — Rat stool: QIAGEN DNeasy Blood & Tissue Kit with custom lysis buffer
- **salmon-blood-dna-extraction** — Atlantic salmon blood: 90% ethanol storage at −80°C (highest output vs tissue)
- **salmon-tissue-dna-extraction** — Atlantic salmon tissue (brain/heart/liver/spleen/fin): MagAttract HMW DNA kit
- **soil-dna-extraction** — Soil: QIAGEN DNeasy PowerMax Soil Kit (8 g starting material)

#### DNA Shearing Methods
- **covaris-g-tube-shearing** — Covaris g-TUBE centrifugal force shearing (6000 rpm, ~8 kb average)
- **fastprep-96-high-throughput-shearing** — FastPrep-96: up to 192 samples at 1600 SPM for 5 min
- **megaruptor-3-extraction-method** — Diagenode Megaruptor 3: reduced input requirements and pore blocking

#### Size Selection & Specialized Methods
- **high-output-human-blood-sequencing** — Human blood high output: flow cell wash/reload yields +25% data, scales to 48 genomes/72h on P48
- **spri-size-selection** — SPRI size selection for >1.5–2 kb fragments using custom 0.7× AMPure XP beads

#### Information Repository
- **cfdna-info-repository** — cfDNA information repository: methods and best practices (~15× coverage per PromethION flow cell)

### Files Skipped (Already Processed)
- rabbit-skin-dna-atl-extraction-method, rabbit-lung-dna-extraction-method, rabbit-lung-dna-atl-extraction-method, rabbit-skin-dna-extraction-method, rabbit-musc-dna-atl-extraction-method, rabbit-muscle-dna-extraction-method, gram-pos-dna-qgn-extraction-method, gram-pos-dna-puregen-extraction-method, cell-line-dna-qgn-extraction-method, cell-line-dna-pure-extraction-method

### Files Not Processed (HTML with no extractable content)
- Knowledge - Contaminants.html, Knowledge - RNA Contaminants.html, Optional fragmentation of gDNA.html (dynamic web pages, JavaScript-only content)
- chemistry_technical_document_document_checklist_en_CHTD_500_v1_revAU.pdf (1-page checklist only)

### Synthesis Pages

#### Kit Comparison & Analysis
- **dna-extraction-kits-comparison** — Comprehensive comparison of 10 DNA extraction kits, 4 lysis buffers, 3 shearing methods, and 2 size selection approaches: catalog numbers, reagent compositions, yields, sample types, protocol details, and usage recommendations. Synthesized from all 34 wiki concept pages created in this batch.

#### Component Analysis
- **lysis-buffer-components** — Comprehensive comparison of lysis buffer components: chaotropic salts (GuHCl, GuSCN), detergents (Triton X-100, SDS, NP-40, CHAPS, N-lauroyl-sarcosine), enzymes (lysozyme, Proteinase K, RNase A), buffers (Tris-HCl) and chelators (EDTA). Properties from manufacturer datasheets (Sigma-Aldrich/Merck, Thermo Fisher Pierce), safety data sheets, and peer-reviewed literature. Created 2026-06-20 as follow-up to kit comparison analysis. Replaces earlier draft with expanded content.
