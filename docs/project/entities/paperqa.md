---
title: "PaperQA"
created: 2026-06-04
updated: 2026-06-04
type: entity
tags: [ai-ml, bioinformatics]
sources:
  - type: paper
    url: "https://www.nature.com/articles/s41586-026-10652-y"
    title: "A multi-agent system for automating scientific discovery" (Ghareeb et al., Nature 2026)
    date: 2026-05-12
confidence: high
contested: false
---

# PaperQA

## Overview

PaperQA is a literature search and summarization system that achieves expert-level performance in scientific information retrieval[1]. Version 2 (PaperQA2) powers the Crow and Falcon agents within [Robin Multi Agent System](entities/robin-multi-agent-system.md)[1].

## Capabilities

- Access to scientific literature, clinical trial reports, and Open Targets Platform[1]
- Expert-level information retrieval and summarization[1]
- Two operational modes:
  - **Concise mode** (Crow): Rapid literature summaries for hypothesis generation[1]
  - **Deep analysis mode** (Falcon): Comprehensive evaluation reports with justification and limitations[1]

## Performance

- Analyzes ~400 papers relating to RPE phagocytosis and dAMD therapeutic landscape in minutes[1]
- Falcon's deep analysis successfully masks hallucinated references from Crow's initial searches[1]
- Ablation study: replacing PaperQA2 agents with o4-mini produced 44.5% hallucinated references vs zero for PaperQA2-based agents[1]

## Use Cases

- Disease mechanism identification (10 causal mechanisms proposed for dAMD)[1]
- In vitro model proposal and ranking[1]
- Drug candidate evaluation (30 candidates assessed with comprehensive reports)[1]
- Literature-grounded hypothesis generation for therapeutic discovery[1]

## Related Systems

- [Robin Multi Agent System](entities/robin-multi-agent-system.md) — Multi-agent system using PaperQA2 as its literature search backbone
- [Finch Agent](entities/finch-agent.md) — Complementary data analysis agent in Robin workflow
