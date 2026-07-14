#!/usr/bin/env python3
"""
Hermes-Wiki Integrity Checker v2
Validates the Hermes-Wiki repository at /tmp/Hermes-Wiki
- Handles Obsidian flat wikilinks correctly
- Ignores legitimate inline code references like [[as_document]]
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

WIKI_PATH = "/tmp/Hermes-Wiki"

# Inline code references that should NOT be treated as wikilinks
INLINE_CODE_REFS = {
    'as_document',
    'audio_as_voice',
}

def extract_wikilinks(content):
    """Extract wikilinks from markdown content, excluding inline code refs."""
    # Match [[path/to/file.md]] or [[file]] or [[file|label]]
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    links = []
    for match in matches:
        # Split on | if there's a label
        link = match.split('|')[0].strip()
        
        # Skip inline code references
        if link in INLINE_CODE_REFS:
            continue
            
        # Skip fragment-only links like [[page#section]]
        if '#' in link:
            # Extract just the page part
            link = link.split('#')[0]
            
        links.append(link)
    return links

def normalize_link(link):
    """Normalize wikilink to filesystem path."""
    # Remove .md extension if present
    link = link.replace('.md', '')
    
    # If link starts with concepts/ or entities/ etc, keep it
    # Otherwise, assume it's a concept
    if not any(link.startswith(prefix) for prefix in ['concepts/', 'entities/', 'changelog/', 'references/', 'raw/']):
        # Check if it's a changelog entry
        if re.match(r'\d{4}-\d{2}-\d{2}', link):
            link = f'changelog/{link}'
        elif '-' in link and not re.match(r'[a-z]+-[^-]+-[^-]+', link):
            # Likely a changelog update
            link = f'changelog/{link}'
        else:
            # Default to concepts
            link = f'concepts/{link}'
    
    return link

def read_index_pages(index_path):
    """Parse index.md to get list of all pages."""
    if not index_path.exists():
        return set()
    
    content = index_path.read_text(encoding='utf-8')
    pages = set()
    
    # Extract wikilinks from index
    for link in extract_wikilinks(content):
        # Filter out references/ links
        if not link.startswith('references/'):
            pages.add(link.replace('.md', ''))
    
    return pages

def get_all_wiki_files(wiki_path):
    """Get all markdown files in wiki."""
    wiki_files = set()
    
    for md_file in Path(wiki_path).rglob('*.md'):
        # Skip index.md, log.md, README.md
        if md_file.name not in ['index.md', 'log.md', 'README.md', 'SCHEMA.md']:
            # Get relative path from wiki root
            rel_path = md_file.relative_to(wiki_path)
            # Remove .md extension
            wiki_files.add(str(rel_path).replace('.md', ''))
    
    return wiki_files

def check_link_exists(link, wiki_path):
    """Check if a wikilink points to an existing file."""
    normalized = normalize_link(link)
    full_path = Path(wiki_path) / (normalized + '.md')
    return full_path.exists()

def main():
    wiki_path = Path(WIKI_PATH)
    
    if not wiki_path.exists():
        print(f"❌ Wiki path not found: {wiki_path}")
        sys.exit(1)
    
    print(f"# Hermes-Wiki Integrity Report (v2)")
    print(f"**Generated:** {datetime.now().isoformat()}")
    print(f"**Wiki Path:** {wiki_path}")
    print()
    
    # Get all wiki files
    wiki_files = get_all_wiki_files(wiki_path)
    print(f"## 📊 Total Pages")
    print(f"- Total markdown files: {len(wiki_files)}")
    print()
    
    # Read index.md
    index_path = wiki_path / 'index.md'
    index_pages = read_index_pages(index_path)
    print(f"## 📋 Index Pages")
    print(f"- Pages in index.md: {len(index_pages)}")
    print()
    
    # Check for broken wikilinks in all pages
    print(f"## 🔍 Checking Wikilinks")
    broken_links = defaultdict(list)
    
    for page_path in wiki_files:
        full_path = wiki_path / (page_path + '.md')
        content = full_path.read_text(encoding='utf-8', errors='ignore')
        links = extract_wikilinks(content)
        
        for link in links:
            # Skip external links
            if link.startswith('http://') or link.startswith('https://'):
                continue
            if link.startswith('references/'):
                continue
            
            if not check_link_exists(link, wiki_path):
                broken_links[page_path].append(link)
    
    # Report broken links
    print()
    print(f"## ⚠️ Broken Wikilinks ({len(broken_links)} pages with issues)")
    for page, links in sorted(broken_links.items()):
        print(f"- **{page}**: {', '.join(f'[[{link}]]' for link in links)}")
    
    # Check for pages missing from index
    missing_from_index = wiki_files - index_pages
    print()
    print(f"## ⚠️ Pages Missing from Index ({len(missing_from_index)} pages)")
    for page in sorted(missing_from_index):
        print(f"- [[{page}]]")
    
    # Check for pages in index but missing from files
    missing_files = index_pages - wiki_files
    print()
    print(f"## ⚠️ Pages in Index But Missing from Files ({len(missing_files)} pages)")
    for page in sorted(missing_files):
        print(f"- [[{page}]]")
    
    # Check for broken reference links
    print()
    print(f"## 📚 Checking Reference Files")
    ref_links = set()
    for page_path in wiki_files:
        full_path = wiki_path / (page_path + '.md')
        content = full_path.read_text(encoding='utf-8', errors='ignore')
        links = extract_wikilinks(content)
        
        for link in links:
            if link.startswith('references/'):
                ref_links.add(link)
    
    broken_refs = []
    for ref in ref_links:
        full_path = wiki_path / (ref + '.md')
        if not full_path.exists():
            broken_refs.append(ref)
    
    if broken_refs:
        print(f"## ⚠️ Broken Reference Links ({len(broken_refs)} found)")
        for ref in sorted(broken_refs):
            print(f"- [[{ref}]]")
    else:
        print(f"## ✅ All References Valid ({len(ref_links)} files)")
    
    # Summary
    print()
    print(f"## 📈 Summary")
    total_issues = len(broken_links) + len(missing_from_index) + len(missing_files) + len(broken_refs)
    
    if total_issues == 0:
        print(f"✅ **No issues found. Wiki is healthy!**")
        sys.exit(0)
    else:
        print(f"⚠️ **{total_issues} issues found.** Review above details.")
        sys.exit(1)

if __name__ == '__main__':
    main()