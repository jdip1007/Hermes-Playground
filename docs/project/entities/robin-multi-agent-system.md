---
title: "Robin Multi-Agent System"
created: 2026-06-04
updated: 2026-06-04
type: entity
tags: [ai-ml, bioinformatics, company]
sources:
  - type: paper
    url: "https://www.nature.com/articles/s41586-026-10652-y"
    title: "A multi-agent system for automating scientific discovery"
    date: 2026-05-12
confidence: high
contested: false
---

# Robin Multi-Agent System

## Overview

Robin is the first multi-agent system capable of fully automating both hypothesis generation and data analysis for experimental biology [1]. Developed by FutureHouse in collaboration with University of Oxford and Fordham University, it represents a paradigm shift in AI-driven scientific discovery [Automated Scientific Discovery](concepts/automated-scientific-discovery.md).

**Key achievement:** Identified novel therapeutic candidates for dry age-related macular degeneration (dAMD) through an iterative lab-in-the-loop framework — proposing ripasudil (a clinically-approved ROCK inhibitor never previously suggested for dAMD) and KL001 as enhancers of RPE phagocytosis [1].

## Architecture

Robin integrates three specialized language agents in a structured workflow [1]:

### Crow
- **Role:** Concise literature search agent based on PaperQA2 [Paperqa](entities/paperqa.md)
- **Function:** Conducts rapid literature summaries, identifies disease mechanisms, proposes in vitro models [1]
- **Performance:** Expert-level information retrieval across scientific literature, clinical trial reports, and Open Targets Platform [1]

### Falcon
- **Role:** Deep literature analysis agent (also PaperQA2-based)
- **Function:** Generates comprehensive evaluation reports on drug candidates with justification and limitations [1]
- **Quality control:** Masks hallucinated references from Crow's initial searches — ablation studies showed 44.5% of o4-mini references were hallucinated vs. zero for Falcon [1]

### Finch
- **Role:** Scientific data analysis agent [Finch Agent](entities/finch-agent.md)
- **Function:** Analyzes experimental data (RNA-seq, flow cytometry) via Jupyter notebooks [1]
- **Consensus mechanism:** Launches 8 independent analysis trajectories, then synthesizes consensus-driven conclusions to handle biological data ambiguity [1]

## Workflow

1. **Disease input** → Robin receives disease of interest (e.g., "dry age-related macular degeneration") [1]
2. **Mechanism identification** → Crow reviews literature, proposes 10 causal disease mechanisms with in vitro models [1]
3. **LLM tournament ranking** → Pairwise comparisons rank mechanisms and experimental strategies [1]
4. **Drug candidate generation** → Robin proposes 30 therapeutic candidates based on top-ranked mechanism [1]
5. **Falcon evaluation** → Comprehensive reports on each candidate (rationale, pharmacological profile, limitations) [1]
6. **Human review + lab testing** → Scientists execute experiments using Robin's proposed assay [1]
7. **Finch analysis** → Autonomous data analysis with consensus across 8 trajectories [1]
8. **Iterative refinement** → Results inform next round of hypothesis generation [1]

## Performance Metrics

| Metric | Robin | Human Equivalent | Speedup |
|--------|-------|------------------|---------|
| Paper synthesis (551 papers) | 30 minutes | ~540 hours | ~200x [1] |
| Total discovery cycle | <2 hours | 872-937 hours | ~500x [1] |
| Cost per workflow run | $10.76 | N/A | — [1] |

Configuration: num_queries=5, num_assays=10, num_candidates=30 → 45 Crow calls ($4.33 avg) + 30 Falcon calls ($6.43 avg) [1].

## Validation Results

### dAMD Drug Discovery
- **Round 1:** Tested Exendin-4, Fingolimod, MFGE8, Y-27632, AICAR+TUDCA in ARPE-19 cells (flow cytometry phagocytosis assay) [1]
- **Y-27632 hit:** Confirmed ROCK inhibitor enhances RPE phagocytosis [[rock-inhibitors]] [1]
- **RNA-seq analysis:** Finch identified 3-fold upregulation of ABCA1 (lipid efflux pump, adj p=2.13×10⁻⁸³) — potential novel therapeutic target linked to Apo-E genetic susceptibility for AMD [1]

### Round 2: Ripasudil Discovery
- **Ripasudil:** Clinically-approved ROCK inhibitor for glaucoma (Japan), never previously proposed for dAMD [1]
- **Performance:** 1.89-fold increase in RPE phagocytosis vs DMSO controls (Finch analysis; human analysis confirmed 1.75-fold) [1]
- **Dose response:** Confirmed superior potency over Y-27632 in ARPE-19 cells [1]
- **Primary cell validation:** Ripasudil and KL001 both hit in patient-derived RPE stem cells (>60yo donor) using bovine rod outer segments [1]

### KL001 Discovery
- Circadian clock modulator (prevents CRY protein ubiquitin-dependent degradation) [1]
- Proposed by Robin based on circadian control of RPE phagocytosis [1]
- First proposal of KL001 as phagocytosis enhancer (to authors' knowledge) [1]

## Architecture Validation

### Ablation Studies
- Replacing Crow/Falcon with o4-mini → dramatic increase in hallucinated references [1]
- Falcon ablation alone → significant quality degradation [1]
- Crow-only ablation → Falcon successfully masks Crow's hallucinations in final reports [1]

### Finch Benchmarking (BixBench)
- Overall: 22.8% accuracy vs 1.6% for Sonnet 3.7 alone on 170 bioinformatics/statistics tasks [1]
- Statistics subset: 47.9% (single-step computations on clean data) [1]
- Bioinformatics subset: 15.3% (multi-step pipelines, parameter-sensitive) [1]

### Comparison with Deep Research
- OpenAI's Deep Research given same prompt → generated 17 unique drug candidates [1]
- **Zero hits** in RPE phagocytosis assay; did not propose ROCK inhibition strategy [1]

## Safety Guardrails

1. Prioritizes candidates with established safety profiles [1]
2. Searches for known toxicities/off-target interactions [1]
3. Lab-in-the-loop design — outputs treated as hypotheses requiring pre-clinical validation [1]
4. LLM classifier filters unsafe topics before query execution [1]
5. Uses safety-aligned frontier LLMs (red-teamed, RLHF-trained) [1]

## Limitations & Future Work

- Does not yet produce precise executable protocols (only experimental outlines) [1]
- Finch relies on domain expert prompt engineering for reliable analysis [1]
- Model-agnostic architecture — will scale with foundation model improvements [1]
- Bioinformatics pipeline execution remains a weakness area (15.3% on BixBench bioinformatics subset) [1]

## Authors & Affiliations

**Lead authors:** Ali Essam Ghareeb, Benjamin Chang (equal contribution) [1]
**Supervising authors:** Andrew D. White, Michaela M. Hinks, Samuel G. Rodriques [1]

- FutureHouse, San Francisco, USA [1]
- University of Oxford, UK [1]
- Fordham University, New York, USA [1]

## Publication Details

- **Journal:** Nature (Accelerated Article Preview) [1]
- **DOI:** 10.1038/s41586-026-10652-y [1]
- **Received:** May 23, 2025 | **Accepted:** May 12, 2026 [1]
- **Raw source:** [[raw/papers/robin-paper-full-text.md]]
