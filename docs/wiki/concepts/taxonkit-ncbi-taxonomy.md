---
title: "TaxonKit - NCBI Taxonomy Toolkit"
date: 2026-06-08
source: Journal of Genetics and Genomics 48 (2021) 844-850
authors: "Wei Shen, Hong Ren"
doi: "10.1016/j.jgg.2021.03.006"
tags: [bioinformatics, taxonomy, metagenomics]
---

## TaxonKit - A Practical and Efficient NCBI Taxonomy Toolkit

**Authors:** Wei Shen*, Hong Ren*  
**Affiliation:** Institute for Viral Hepatitis, Department of Infectious Diseases, The Second Affiliated Hospital of Chongqing Medical University, China  
**Journal:** Journal of Genetics and Genomics 48 (2021) 844-850  
**DOI:** 10.1016/j.jgg.2021.03.006

### Overview

Command-line toolkit for comprehensive and efficient manipulation of NCBI Taxonomy data. Designed to address limitations of existing tools (E-utilities, Taxize, ETE Toolkit, Taxopy) which are either slow or lack critical features for large-scale metagenomic analysis.

### Seven Core Subcommands

1. **`taxonkit query`** — Query TaxIds by taxonomy names
2. **`taxonkit list`** — List descendants of given TaxIds
3. **`taxonkit filter`** — Filter TaxIds by rank range or other criteria
4. **`taxonkit lineage`** — Retrieve complete taxonomic lineages
5. **`taxonkit reformat`** — Convert lineages into custom formats for standardized metagenomic profiling reports
6. **`taxonkit lca`** — Compute lowest common ancestor from multiple TaxIds
7. **`taxonkit changelog`** — Track taxonomy entry changes over time

### Key Features

- **Standalone binary** — No database building required, parses NCBI dump files directly
- **High performance** — Competitive processing speed vs existing tools, scales with dataset size
- **Plain or gzip-compressed I/O** — Supports standard streams and local files
- **MIT license** — Free access via GitHub, Brewsci, Bioconda

### Why It Matters for Metagenomics

The NCBI Taxonomy is essential for taxonomic classification in metagenomic analysis. Typical workflows require:
- Querying TaxIds by organism names
- Retrieving complete lineages (domain → phylum → class → order → family → genus → species)
- Converting lineages into standardized formats for profiling reports

Existing tools had critical gaps:
- **E-utilities/Taxize:** Web API-based, limited by internet speed, unsuitable for batch querying
- **ETE Toolkit:** Requires SQLite database rebuild on every NCBI update (tedious maintenance)
- **Taxopy:** Missing features like rank-range filtering and custom lineage formatting

### Performance Benchmarks

The paper demonstrates TaxonKit's competitive processing performance across different dataset scales. Key advantages:
- No database building step → faster startup
- Direct parsing of NCBI dump files from `ftp://ftp.ncbi.nih.gov/pub/taxonomy/`
- Memory-efficient for large-scale datasets

### Use Cases in Bioinformatics Pipeline

1. **Metagenomic profiling** — Standardize taxonomic output formats across different classifiers (Kraken2, MetaPhlAn, etc.)
2. **Taxonomic filtering** — Remove contaminants by filtering specific ranks or lineages
3. **LCA computation** — Resolve ambiguous classifications to lowest common ancestor
4. **Change tracking** — Monitor NCBI taxonomy updates that affect downstream analysis

### Installation

```bash
# Bioconda
conda install -c bioconda taxonkit

# Brewsci (macOS)
brew install brewsci/bio/taxonkit

# Direct download from GitHub releases
```

### Cross-References
[Bioinformatics](bioinformatics.md) — Core toolkit for taxonomy operations  
[Metagenomics](metagenomics.md) — Essential for standardized profiling reports  
[Nanopore Applications Virus Research](nanopore-applications-virus-research.md) — Taxonomic classification in sequencing workflows  
[Rna Synthesis Genomic Research](rna-synthesis-genomic-research.md) — Related bioinformatics tools
