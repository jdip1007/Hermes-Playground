# Wiki Schema

## Domain
Linux technology, hardware, kernel development, graphics drivers, open-source software

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `reactos-half-life-2.md`)
- Every wiki page starts with YAML frontmatter (see below)
- **Linking:** Use [[wikilinks]] following Obsidian conventions (see [[references/obsidian-cheat-sheet]])
  - Internal page: [[page-name]]
  - Link to header: [[page-name#Header]]
  - Custom text: [[page-name|display text]]
  - External URL: [text](https://example.com/)
  - Minimum 2 outbound [[wikilinks]] per page
- **References:** Use ^[footnote-style] for inline source attribution on multi-source pages
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [from taxonomy below]
  sources: [raw/articles/source-name.md]
  # Optional quality signals:
  confidence: high | medium | low
  contested: true
  contradictions: [other-page-slug]
  ---
  ```

### raw/ Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest>
---
```

## Tag Taxonomy
### Topics
- linux-kernel
- graphics
- drivers
- hardware
- open-source
- performance
- gaming
- security
- virtualization
- networking

### Entities
- company (AMD, Intel, NVIDIA)
- project (ReactOS, OpenRazer)
- product (GPU, CPU)

### Meta
- news
- analysis
- benchmark
- comparison
- controversy

Rule: every tag on a page must appear in this taxonomy.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when its content is fully superseded

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

## Reference Materials
Store external documentation, templates, and cheat sheets in `references/`:
- [[references/obsidian-cheat-sheet]] — Obsidian linking conventions
- Use [[wikilinks]] to reference these from schema and other pages