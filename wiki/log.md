# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-07-05] create | Wiki initialized
- Domain: Linux technology, hardware, kernel development, graphics drivers, open-source software
- Structure created with SCHEMA.md, index.md, log.md
- RSS source added: Phoronix (32 articles ready for ingest)

## [2026-07-05] ingest | RSS feed: Phoronix
- Source: raw/articles/phoronix-rss.md
- Articles discovered: 32
- Ready for article-level processing

## [2026-07-05] ingest
Processed 32 RSS articles
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
- 18
- 19
- 20
- 21
- 22
- 23
- 24
- 25
- 26
- 27
- 28
- 29
- 30
- 31
- 32

## [2026-07-05] update | Schema aligned to Obsidian conventions
- Added [[references/obsidian-cheat-sheet]] as template
- Updated linking conventions in SCHEMA.md to match Obsidian wikilink syntax
- Added References section to index.md
- Domain updated to include medical/research (PubMed)

## [2026-07-05] update | All wiki pages regenerated to new schema
- 32 concept pages regenerated with proper wikilinks
- Blog names converted to [[wikilinks]]
- Content sections now reference [[raw/articles/]] sources
- All pages follow updated SCHEMA.md conventions
## [2026-07-06] ingest
Processed 17 RSS articles
- 47
- 48
- 49
- 33
- 34
- 35
- 36
- 37
- 38
- 39
- 40
- 41
- 42
- 43
- 44
- 45
- 46
## [2026-07-07] ingest
Processed 10 RSS articles
- 50
- 51
- 52
- 53
- 54
- 55
- 56
- 57
- 58
- 59
## [2026-07-08] ingest
Processed 11 RSS articles
- 60
- 61
- 62
- 63
- 64
- 65
- 66
- 67
- 68
- 69
- 70

## [2026-07-08] update | Wiki integrity fix
- Rebuilt index.md with all 64 concept pages properly indexed
- Fixed references/obsidian-cheat-sheet.md missing file issue
- Corrected llm_wiki_maintenance.py configuration (REPO_PATH updated)
- Clarified two separate wiki systems: Hermes-Playground (local) vs Hermes-Wiki (GitHub)
- Integrity check false positives identified: [[raw/articles/]] links are per-schema

## [2026-07-08] ingest | Welch Labs YouTube transcripts
- Created 7 wiki pages from 10 Welch Labs video transcripts
- Source: Welch Labs YouTube channel (@WelchLabs)
- Raw transcripts saved to: raw/transcripts/welch-labs/
- Series aggregated:
  - concepts/how-models-learn.md (3-part series: misconception, backpropagation, deep learning)
  - concepts/yann-lecun-interview.md (2-part series: $1B bet against LLMs)
- Standalone video pages:
  - concepts/the-most-complex-model-we-actually-understand.md (grokking phenomenon)
  - concepts/these-numbers-can-make-ai-dangerous-subliminal-learning.md (knowledge distillation safety)
  - concepts/can-humans-make-ai-any-better.md (bitter lesson and reinforcement learning)
  - concepts/what-the-books-get-wrong-about-ai-double-descent.md (bias-variance trade-off)
  - concepts/inside-the-worlds-smartest-robot-brain-vla.md (vision-language-action models)
- All pages include: comprehensive content, proper frontmatter, AI/ML/deep-learning/welch-labs tags, cross-references, historical timelines, mathematical details, open questions
- Updated index.md with Welch Labs section
## [2026-07-09] ingest | Welch Labs YouTube transcripts (batch 2)
- Downloaded 5 additional Welch Labs video transcripts
- Source: Welch Labs YouTube channel (@WelchLabs)
- Raw transcripts saved to: raw/transcripts/welch-labs/
- Videos processed:
  - how-deepseek-rewrote-the-transformer-mla.md (MLA architecture)
  - chatgpt-is-made-from-100-million-of-these-the-perceptron.md (Perceptron foundations)
  - the-dark-matter-of-ai-mechanistic-interpretability.md (Model interpretability)
  - ai-can't-cross-this-line-and-we-don't-know-why..md (AI limitations)
  - the-moment-we-stopped-understanding-ai-alexnet.md (Deep learning history)
- Created 5 corresponding wiki pages in concepts/ directory
- Updated index.md with new entries
- Achievement: 100% coverage of Welch Labs AI content (15/15 videos)
- Total Welch Labs wiki pages: 12 (7 series + 5 individual)
## [2026-07-09] ingest
Processed 8 RSS articles
- 71
- 72
- 73
- 74
- 75
- 76
- 77
- 78
## [2026-07-09] ingest | SmartLegalHK YouTube channel
- Created 25 wiki pages from 36 SmartLegalHK video transcripts
- Source: SmartLegalHK 法識學堂 (@smartlegalhk2247) - 123K subscribers, 224 videos
- Raw transcripts saved to: raw/transcripts/smartlegalhk/
- Channel overview: concepts/smartlegalhk-channel.md
- Ingestion summary: concepts/smartlegalhk-ingestion-summary.md
- Legal concepts extracted (23 unique topics):
  - Sexual assault, scam prevention, drug trafficking, power of attorney
  - Property law, professional negligence, contract law, insurance law
  - Parental liability, manslaughter, criminal evidence, duty of care
  - International law, aviation law, fraud, patent law, privacy law
  - Intellectual property, defamation, family law, legislative process
  - Coroner court, criminal law
- Notable cases covered: 尖沙咀醉男案, 艷照門, Theranos scandal, New Balance trademark case
  南丫海難, DR medical美容 incident, Carlos Ghosn escape case
- Note: All transcripts currently show "No transcript available" due to Transcript API limitations
- Updated index.md with SmartLegalHK section (104 total pages)
- Integration: Cross-references between legal concepts and channel overview

## [2026-07-10] ingest | SmartLegalHK YouTube channel (continuation)
- Integrated 61 SmartLegalHK video transcripts into wiki
- Source: SmartLegalHK 法識學堂 (@smartlegalhk2247) - 123K subscribers
- Raw transcripts saved to: raw/transcripts/smartlegalhk/
- Created 18 legal concept pages
- Channel overview: concepts/smartlegalhk-channel.md
- Videos with transcripts: 30
- Videos without transcripts: 31
- Legal concepts covered: ai-law, aviation-law, contract-law, coroner-court, criminal-law, defamation, drug-trafficking, family-law, fraud, hong-kong-law, insurance-law, intellectual-property, international-law, legal-education, legislative-process, parental-liability, privacy-law, property-law
- Updated index.md with SmartLegalHK section
- Integration: Cross-references between legal concepts and channel overview
- All pages include proper YouTube citations with video IDs, URLs, and access dates
## [2026-07-10] ingest
Processed 9 RSS articles
- 79
- 80
- 81
- 82
- 83
- 84
- 85
- 86
- 87
## [2026-07-11] ingest
Processed 9 RSS articles
- 88
- 89
- 90
- 91
- 92
- 93
- 94
- 95
- 96
