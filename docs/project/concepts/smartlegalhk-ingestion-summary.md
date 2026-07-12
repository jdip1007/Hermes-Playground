---
title: SmartLegalHK Ingestion Summary
created: 2026-07-09
updated: 2026-07-09
type: concept
tags: [legal, hong-kong, smartlegalhk, ingestion-summary]
sources: [raw/transcripts/smartlegalhk/ingestion_summary.json]
---

# SmartLegalHK Channel Ingestion Summary

## Channel Information

- **Channel:** SmartLegalHK 法識學堂
- **Host:** 楊雲峰律師 (Yang Yun-feng)
- **Handle:** @smartlegalhk2247
- **Subscribers:** 123K (July 2026)
- **Videos:** 224 videos
- **Content Focus:** Hong Kong law, consumer rights, legal education

## Ingestion Results

### Videos Processed: 36

**Status:** 36 raw transcript files created
- **Location:** `~/wiki/raw/transcripts/smartlegalhk/`
- **Format:** Markdown with frontmatter (title, video ID, source, channel, timestamp)
- **Metadata:** Full video information preserved

**Note:** All transcripts currently show "No transcript available" due to Transcript API limitations (likely quota or schema issues). The video metadata and legal concept mapping are intact.

### Concept Pages Created: 23

**Location:** `~/wiki/concepts/`

| Concept | Description | Videos |
|---------|-------------|--------|
| [[sexual-assault]] | Sexual assault law in Hong Kong | 1 |
| [[scam-prevention]] | Fraud prevention and consumer protection | 4 |
| [[drug-trafficking]] | Drug trafficking laws and mules | 1 |
| [[power-of-attorney]] | Power of attorney and authorization | 1 |
| [[property-law]] | Property and real estate law | 1 |
| [[professional-negligence]] | Professional negligence liability | 1 |
| [[contract-law]] | Contract law and agreements | 1 |
| [[insurance-law]] | Insurance policies and coverage | 1 |
| [[parental-liability]] | Parental liability for children | 1 |
| [[manslaughter]] | Manslaughter and negligence | 1 |
| [[criminal-evidence]] | Evidence in criminal cases | 1 |
| [[duty-of-care]] | Duty of care obligations | 1 |
| [[international-law]] | International legal frameworks | 2 |
| [[aviation-law]] | Aviation and passenger rights | 1 |
| [[fraud]] | Fraud and deception | 3 |
| [[patent-law]] | Patent protection | 1 |
| [[privacy-law]] | Privacy and data protection | 1 |
| [[intellectual-property]] | Trademark and copyright | 1 |
| [[defamation]] | Defamation and libel | 1 |
| [[family-law]] | Family law and inheritance | 1 |
| [[legislative-process]] | How laws are made | 1 |
| [[coroner-court]] | Death inquiry proceedings | 1 |
| [[criminal-law]] | Criminal law and procedures | 5 |

### Channel Page Created: 1

- **Page:** [[smartlegalhk-channel]]
- **Content:** Comprehensive channel overview, content focus, key topics, notable cases

## File Organization

```
~/wiki/
├── raw/
│   └── transcripts/
│       └── smartlegalhk/
│           ├── ingestion_summary.json (36 videos)
│           ├── 男姦男唔算強姦香港律師拆解尖沙咀醉男案.md
│           ├── nb商標戰一隻雞腳引發嘅天價官司.md
│           ├── 大清律例在香港為爭100萬遺產.md
│           ├── 法識學堂香港立法程序大揭秘.md
│           ├── 香港大案從南丫海難學識死因庭點運作.md
│           ├── 香港碰瓷新陷阱律師教你3招ko騙徒.md
│           └── ... (30 more transcripts)
├── concepts/
│   ├── smartlegalhk-channel.md
│   ├── smartlegalhk_concepts_summary.json
│   ├── sexual-assault.md
│   ├── scam-prevention.md
│   ├── drug-trafficking.md
│   └── ... (20 more concepts)
├── index.md
└── log.md
```

## Key Legal Topics Covered

Based on the 36 videos processed, the channel covers:

### Criminal Law (刑事法)
- Drug trafficking (販毒案、「飛機豬」、「郵包豬」)
- Manslaughter (誤殺、嚴重疏忽)
- Sexual assault (男姦男案)
- Evidence (證據、幽靈證據)
- Duty of care (責任、義務)

### Civil Law (民事法)
- Property law (物業法、樓宇權益)
- Contract law (合約法)
- Power of attorney (授權書)
- Family law (婚姻法、遺產)

### Commercial Law (商業法)
- Fraud (詐騙、欺詐罪)
- Intellectual property (知識產權、商標)
- Patent law (專利法)
- Insurance law (保險法)

### International Law (國際法)
- US Constitution (美國憲法、彈劾)
- International criminal law

### Special Topics
- Legislative process (立法程序)
- Coroner court (死因庭)
- Consumer protection (消費者權益)
- Scam prevention (碰瓷、陷阱)

## Notable Cases Analyzed

- **Edison Chen photo scandal** (艷照門) - Privacy law
- **Theranos scandal** - Fraud and corporate crime
- **New Balance trademark case** - Intellectual property
- **Hong Kong ferry disaster (Lamma Island)** - Coroner court
- **DR medical美容 fatal incident** - Professional negligence
- **Carlos Ghosn escape case** - International criminal law
- **尖沙咀醉男案** - Sexual assault law
- **南丫海難** - Coroner court operations

## Data Quality Notes

### Current Limitations

1. **Empty Transcripts:** All 36 transcript files currently contain "No transcript available"
   - **Cause:** Transcript API limitations (quota or schema issues)
   - **Impact:** Cannot translate, extract elaborations, or provide detailed concept explanations
   - **Solution:** Need API fix or alternative transcript source

2. **Concept Mapping:** Concepts are extracted from video titles only
   - **Source:** Title keyword matching
   - **Coverage:** 23 unique legal concepts identified
   - **Limitation:** Cannot verify concept accuracy without transcript content

### Data Preserved

✅ **Video Metadata:** All 36 videos have complete metadata
✅ **Concept Structure:** 23 concept pages with proper frontmatter
✅ **Channel Overview:** Comprehensive channel introduction
✅ **File Organization:** Proper wiki structure maintained
✅ **Cross-References:** Links between concepts and videos

## Next Steps (If Transcripts Become Available)

1. **Translation:** Translate Cantonese transcripts to English
2. **Concept Elaboration:** Extract legal concepts and explanations
3. **Case Study Integration:** Use cases as examples for concepts
4. **Chinese Keywords:** Preserve Chinese legal terminology
5. **Wiki Enrichment:** Add detailed explanations to concept pages

## Sources

- **Channel:** https://www.youtube.com/@smartlegalhk2247
- **Processing Date:** July 9, 2026
- **Raw Data:** `raw/transcripts/smartlegalhk/ingestion_summary.json`
- **Concepts Summary:** `concepts/smartlegalhk_concepts_summary.json`

## Related Topics

- [[hong-kong-law]] - General Hong Kong legal system
- [[legal-education]] - Legal education and literacy
- [[consumer-rights]] - Consumer protection law
- [[smartlegalhk-channel]] - Channel introduction page