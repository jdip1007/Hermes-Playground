---
title: "Academic Research Skills (ARS) Suite"
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [ai-tools, academic-writing, research-pipeline, llm-skills, literature-review, paper-writing]
sources:
  - type: web
    url: "https://github.com/Imbad0202/academic-research-skills"
    title: "Academic Research Skills for Claude Code (upstream)"
    date: 2026-06-08
  - type: web
    url: "https://github.com/Imbad0202/academic-research-skills-codex"
    title: "Academic Research Skills for Codex (adapter fork)"
    date: 2026-06-08
  - type: paper
    url: "https://arxiv.org/abs/2605.07723"
    title: "Zhao et al. — Citation Hallucination Audit (111M references, 2.5M papers)"
    date: 2026-05
  - type: paper
    url: "https://www.nature.com/articles/s41586-026-XXXXX"
    title: "Lu et al. — The AI Scientist (Nature 651:914-919, ICLR 2025 workshop)"
    date: 2026
confidence: high
contested: false
---

# Academic Research Skills (ARS) Suite

## Overview

**Academic Research Skills (ARS)** is a comprehensive LLM skill suite for academic research workflows — from research question formulation through literature review, paper drafting, peer review simulation, and full end-to-end research-to-publication pipelines. Originally built for Claude Code, with an adapter fork for OpenAI Codex.[1][2]

- **Maintainer:** Cheng-I Wu[1]
- **Upstream repo:** `Imbad0202/academic-research-skills` (Claude Code) — 28,811 stars[1]
- **Codex adapter:** `Imbad0202/academic-research-skills-codex` — 3,277 stars[2]
- **License:** CC BY-NC 4.0 (non-commercial only)[1]
- **Current version:** v3.11.1 (upstream), v0.1.11 (Codex adapter)[1][2]
- **Languages:** English + Traditional Chinese bilingual support[1]

## Architecture

Single router skill that dispatches to **5 workflows**, each with its own agent team:[1]

| Workflow | Agents | Purpose | Key Modes |
|---|---|---|---|
| `deep-research` | 14 | Literature review, systematic review, meta-analysis, fact-checking | full research, quick brief, paper review, lit-review, fact-check, Socratic guided dialogue, systematic review |
| `academic-paper` | 12 | Paper writing, outlining, abstracts, revision | full/plan/outline/revision/abstract/lit-review/format-convert/citation-check/disclosure |
| `academic-pipeline` | 5 | End-to-end research→paper with integrity gates | staged pipeline with review/revision/finalization checkpoints |
| `academic-paper-reviewer` | 7 | Peer review simulation, editorial decisions | full review, methodology focus, calibration mode |
| `experiment-agent` | 2 | Experiment planning, study protocols, statistical interpretation | code experiment plan, human study protocol, reproducibility validation |

## Core Design Philosophy

**Human-in-the-loop, not full automation.** ARS explicitly rejects the "fully autonomous AI researcher" model. Its design is motivated by:[1]

1. **Lu et al. (2026, Nature)** — "The AI Scientist" published through blind peer review at ICLR 2025 workshop but documented failure modes: implementation bugs, hallucinated results, shortcut reliance, methodology fabrication, frame-lock, citation hallucinations.[4]

2. **Zhao et al. (2026-05, arXiv)** — Audit of 111M references across 2.5M papers found ~147K hallucinated citations in 2025 alone, with an observed mid-2024 inflection point. ARS v3.7+ added trust-chain frontmatter and three-layer citation anchors to address this.[3]

3. **PaperOrchestra (Song et al., 2026, Google)** — Inspired ARS v3.3 features: Semantic Scholar API verification, anti-leakage protocol, VLM figure verification, score trajectory tracking.[1]

## Key Features

### Citation Integrity System (v3.11)[1]
- **Four-index cross-check:** Semantic Scholar + OpenAlex + Crossref + arXiv API[1]
- **Persistent SQLite cache** (`~/.cache/ars/verification.db`, 90-day TTL)[1]
- **Contamination signals:** k=0..4 triangulation advisory matrix (how many indexes confirm a citation)[1]
- **Terminal policy opt-in:** Default advisory mode, user can enable `strict` to block on unverified citations[1]
- **Claim audit pass** (`ARS_CLAIM_AUDIT=1`): Fetches cited source against each anchor and judges claim support[1]

### Socratic Research Question Refinement[1]
- Dedicated `socratic_mentor_agent` — Q1 journal editor-in-chief persona[1]
- Never gives direct answers; asks precise, layered questions[1]
- Wording-pattern advisory (WP01-WP16) detects generic research question phrasings ("exploring the impact of X on Y") and suggests domain-native alternatives[1]

### Style Calibration[1]
- Learns writing voice from 3+ past papers (sentence rhythm, vocabulary preferences, citation integration style)[1]
- Applied as soft guide during drafting; discipline conventions take priority[1]

### Writing Quality Check[1]
- Catches AI-typical overused terms, em dash overuse, throat-clearing openers, uniform paragraph lengths, monotonous sentence rhythm[1]
- Framed as "good writing rules" not detection evasion[1]

### Material Passport System[1]
- YAML-based state tracking between pipeline phases[1]
- Tracks citation provenance, claim audit results, version records, temporal audit trails[1]
- Handoff schemas define exact data contracts between stages[1]

## Claude Code vs Codex Adapter

The upstream ARS is designed for **Claude Code's multi-agent architecture** (Agent Team, Task tool, subagent spawning). The Codex adapter translates these concepts:[2]

| Upstream (Claude Code) | Codex/Hermes equivalent |
|---|---|
| Agent Team dispatch | Read agent `.md` as role prompt, execute inline |
| Subagent spawning | `delegate_task` only when explicitly requested |
| `/ars-*` slash commands | Plain alias text (`ars-plan`, `ars-reviewer`) |
| SessionStart hooks | Not applicable — no hook system in Hermes |
| PreToolUse guards | Prompt-level enforcement only |

## File Structure (Selective Install)

**Core files (~35, ~25K lines):**[1]
- 1 router SKILL.md (293 lines)[1]
- 5 WORKFLOW.md files (2,208 lines total)[1]
- 40 agent prompt files (13,947 lines — detailed role definitions)[1]
- 14 command alias recipes (`ars-plan`, `ars-reviewer`, etc.)[1]
- Shared schemas and protocols[1]

**Utility scripts (~8 useful for Hermes):**[1]
- `arxiv_client.py` — arXiv API wrapper with rate limiting (208 lines)[1]
- `crossref_client.py` — DOI lookup via Crossref (203 lines)[1]
- `openalex_client.py` — OpenAlex bibliographic search (174 lines)[1]
- `semantic_scholar_client.py` — Semantic Scholar API (272 lines)[1]
- `ars_mark_read.py` — citation human-read tracking (207 lines)[1]
- `verify_passport.py` — material passport validation (115 lines)[1]

**Bloat (~900 files, ~12MB — not needed for Hermes):**[1]
- 81 pytest test scripts + fixtures[1]
- 60 eval gold-set files[1]
- 47 design spec docs[1]
- 75 "check_*" CI consistency validators[1]
- Claude Code hooks (`hooks.json`)[1]
- Codex full-runtime adapter (planner-driven agent teams)[2]

## Hermes Integration Notes

### What Works Well[1]
- Agent prompts are high-quality, detailed role definitions that work as inline instructions[1]
- WORKFLOW.md files provide clear phase-by-phase execution contracts[1]
- Citation verification scripts are standalone Python utilities — directly usable[1]
- Socratic mentoring mode is genuinely useful for research question refinement[1]
- Bilingual support (English + Traditional Chinese)[1]

### What Doesn't Translate[1]
- **Material Passport YAML state** — Over-engineered for single-session Telegram use. The passport system assumes multi-session persistence with file-based handoffs between Claude Code subagents.[1]
- **Phase boundary enforcement** — v3.9.2 rules about "don't produce downstream deliverables" are designed for multi-agent sessions where each agent has a narrow scope. In Hermes, the LLM handles everything inline.[1]
- **Claude hooks** — SessionStart, PreToolUse hooks are Claude Code-specific and useless in Hermes.[1]
- **Slash commands** — `/ars-plan` etc. don't exist in Telegram interface. Use plain text aliases instead.[1]

### Recommended Approach for Hermes[1]
Install only the core workflows + agents + citation scripts. Skip:[1]
- Test fixtures (pytest)[1]
- CI validators (`check_*`)[1]
- Claude hooks[1]
- Codex full-runtime adapter[2]
- Eval gold sets[1]
- Design spec docs[1]

The LLM loads relevant agent prompts on-demand from WORKFLOW.md references — no need to preload everything.[1]

## Citation Verification Scripts Detail

All four bibliographic clients follow the same pattern:[1]
1. **DOI/arXiv ID-first lookup** with title cross-check (ID_MISMATCH detection)[1]
2. **Title-similarity fallback** when exact ID fails[1]
3. **Rate limiting:** 429 → 2s backoff × 3 retries, 5xx → skip[1]
4. **Persistent cache** via `verification_cache.py` (SQLite WAL mode, 90-day TTL)[1]

Usage example:
```python
from scripts.crossref_client import CrossrefClient
client = CrossrefClient(polite_email="user@example.com")
result = client.doi_lookup_with_title_check("10.1038/s41586-026-XXXXX", expected_title="...")
# Returns: {doi, title, year, matched, mismatch_type}
```

## Version History Highlights[1]

| Version | Key Addition | Date |
|---|---|---|
| v3.7.x | Trust-chain frontmatter, three-layer citation anchors (motivated by Zhao et al.)[3] | 2026-04 |
| v3.8 | Claim audit pass (`ARS_CLAIM_AUDIT=1`) — fetches cited source against each anchor | 2026-05 |
| v3.9.x | Phase boundary enforcement (v3.9.2), cross-index triangulation advisory | 2026-05 |
| v3.10 | Terminal policies opt-in model, contamination signals k=0..3 | 2026-05 |
| v3.11 | arXiv resolver (four-index: S2+OpenAlex+Crossref+arXiv), persistent verification cache | 2026-06-04 |
| v3.11.1 | Security hardening, cross-model consent gates, correctness fixes | 2026-06-06 |

## References

- **Upstream ARS:** https://github.com/Imbad0202/academic-research-skills (28,811 stars)
- **Codex adapter:** https://github.com/Imbad0202/academic-research-skills-codex (3,277 stars)
- **Zhao et al. 2026:** "Citation Hallucination in AI-Generated Academic Text" — arXiv:2605.07723
- **Lu et al. 2026:** "The AI Scientist" — Nature 651:914-919, ICLR 2025 workshop
- **PaperOrchestra:** Song, Song, Pfister & Yoon (Google) — arXiv:2604.05018
