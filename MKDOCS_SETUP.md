# MkDocs + LLM Wiki

Hermes-Playground repository configured for automatic HTML deployment via MkDocs and GitHub Pages.

## Current Setup

✅ **MkDocs Configuration**
- Material theme with light/dark mode
- LLM Wiki navigation structure
- Search functionality enabled
- Code highlighting and math support

✅ **GitHub Pages Workflow**
- `.github/workflows/mkdocs.yml` created
- Auto-builds on main branch push
- Deploys to GitHub Pages
- Uses Python 3.11 with pip caching

✅ **Deployed Content**
- 382 wiki files (concepts, entities, raw sources)
- Wiki index and schema
- Complete markdown content structure

## Repository URLs

- **Source:** https://github.com/jdip1007/Hermes-Playground
- **GitHub Pages:** https://jdip1007.github.io/Hermes-Playground/
- **Wiki Directory:** `/wiki/` subdirectory

## How to Update

```bash
# 1. Edit wiki content
cd ~/projects/Hermes-Playground/wiki

# 2. Add/update markdown files
# (Use llm-wiki skill guidelines)

# 3. Commit changes
git add wiki/
git commit -m "docs: update wiki content"

# 4. Push to GitHub
git push origin main

# 5. GitHub Actions auto-deploys to Pages
# Site updates in ~2-3 minutes
```

## MkDocs Configuration Structure

```yaml
nav:
  - Home: index.md
  - LLM Wiki:
    - Wiki Index: wiki/index.md
    - Wiki Schema: wiki/SCHEMA.md
    - Wiki Log: wiki/log.md
    - Concepts:
      - wiki/concepts/overview.md
    - Entities:
      - wiki/entities/index.md
    - References:
      - wiki/references/obsidian-cheat-sheet.md
```

## Local Testing

```bash
# Install MkDocs and dependencies
pip install mkdocs-material pymdown-extensions

# Build locally
cd ~/projects/Hermes-Playground
mkdocs build

# Serve locally for preview
mkdocs serve
# Opens at http://127.0.0.1:8000
```

## Next Steps

⏳ Enable GitHub Pages in repository settings
1. Go to https://github.com/jdip1007/Hermes-Playground/settings/pages
2. Source: GitHub Actions
3. Save settings

⏳ Wait for first deployment to complete
- Check: https://github.com/jdip1007/Hermes-Playground/actions
- View site: https://jdip1007.github.io/Hermes-Playground/

⏳ Update wiki navigation structure
- Create `wiki/concepts/overview.md` with concept categories
- Create `wiki/entities/index.md` with entity list
- Update `mkdocs.yml` nav section as needed

## Material Theme Features

✅ **Navigation**
- Instant loading
- Section-based organization
- Expandable/collapsible sections
- Back to top button

✅ **Content**
- Code copy buttons
- Search with highlighting
- Admonitions (notes, warnings, tips)
- Tables and footnotes
- Emoji support
- Math notation (LaTeX)
- Mermaid diagrams

✅ **Appearance**
- Light/dark mode toggle
- System preference support
- Custom fonts (Inter text, JetBrains Mono code)
- Material Design icons

## Troubleshooting

### Deployment Fails
```bash
# Check workflow status
# https://github.com/jdip1007/Hermes-Playground/actions

# Common issues:
# 1. GitHub Pages not enabled in settings
# 2. Python dependency conflicts
# 3. MkDocs build errors
```

### Local Build Errors
```bash
# Install dependencies
pip install -r requirements.txt  # Create this file

# Install MkDocs extensions
pip install mkdocs-material pymdown-extensions

# Test build
mkdocs build --verbose
```

### Navigation Missing
- Update `mkdocs.yml` nav section
- Ensure referenced files exist
- Check file paths are correct

## Integration with Skills

### llm-wiki Skill
- Creates/manages wiki content
- Follows Karpathy's LLM Wiki pattern
- Markdown format with YAML frontmatter

### hermes-playground-maintenance Skill
- Handles daily sync operations
- Monitors repository status
- Manages translation system
- GitHub integration

## Performance

- **Build Time:** ~30-60 seconds
- **Page Load:** <1 second (with instant navigation)
- **Search:** Client-side, instant results
- **Site Size:** ~5-10 MB (after minification)

---

**Last Updated:** 2026-07-11
**MkDocs Version:** 1.5.x
**Material Theme Version:** 9.5.x