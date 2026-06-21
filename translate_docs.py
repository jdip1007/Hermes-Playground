#!/usr/bin/env python3
"""
Translate Chinese text in markdown documentation files to English using Google Translate API.
Preserves: YAML frontmatter, code blocks, inline code, links, tables structure, technical terms.
Skips: iching-life-crossroads.md (intentional Chinese content)

Strategy: Extract prose from each line, translate only the prose parts, then reassemble.
"""

import re
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout
from deep_translator import GoogleTranslator

DOCS_DIR = Path("/root/Hermes-Playground/docs/concepts")
SKIP_FILES = {"iching-life-crossroads.md"}


class BatchTranslator:
    """Thread-safe batch translator with caching and timeout handling."""
    
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.cache = {}
        self.error_count = 0
    
    def translate(self, text: str) -> str:
        """Translate a single piece of Chinese text to English."""
        if not text or not any('\u4e00' <= c <= '\u9fff' for c in text):
            return text
        
        clean = ' '.join(text.split())
        
        # Check cache
        if clean in self.cache:
            return self.cache[clean]
        
        try:
            t = GoogleTranslator(source='zh-CN', target='en')
            result = t.translate(clean, language_pair='zh-CN-en')
            self.cache[clean] = result
            return result
        except Exception as e:
            self.error_count += 1
            print(f"    Translation error: {e}", file=sys.stderr)
            time.sleep(2)
            try:
                t = GoogleTranslator(source='zh-CN', target='en')
                result = t.translate(clean, language_pair='zh-CN-en')
                self.cache[clean] = result
                return result
            except Exception as e2:
                print(f"    Retry failed: {e2}", file=sys.stderr)
                return clean


def extract_prose_for_translation(text: str):
    """Extract Chinese prose from text, replacing inline code with placeholders.
    
    Returns (prose_to_translate, placeholder_map).
    """
    # Replace inline code with placeholders to protect them
    placeholders = {}
    counter = [0]
    
    def replace_code(match):
        key = f"__CODE{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    # Replace inline code blocks
    processed = re.sub(r'`[^`]+`', replace_code, text)
    
    # Replace markdown links [text](url) with placeholders  
    def replace_link(match):
        key = f"__LINK{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'\[[^\]]*\]\([^)]+\)', replace_link, processed)
    
    # Replace reference markers [1], [2] etc.
    def replace_ref(match):
        key = f"__REF{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'\[\d+\]', replace_ref, processed)
    
    # Replace issue references like #21193
    def replace_issue(match):
        key = f"__ISSUE{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'#\d+', replace_issue, processed)
    
    # Replace version numbers like v0.13.x, v2026.5.7
    def replace_version(match):
        key = f"__VER{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'v\d+\.\d+(\.\w+)?', replace_version, processed)
    
    # Replace file paths and code identifiers (backtick-free ones in prose)
    def replace_path(match):
        key = f"__PATH{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'[a-zA-Z_][\w./-]+\.\w+', replace_path, processed)
    
    # Replace environment variables and config keys
    def replace_env(match):
        key = f"__ENV{counter[0]}__"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key
    
    processed = re.sub(r'(?:DISCORD_|ALLOWED_|\$)\w+', replace_env, processed)
    
    # Replace remaining technical identifiers (all-caps or camelCase words that look like code)
    def replace_tech(match):
        word = match.group(0)
        if len(word) > 3 and any(c.isupper() for c in word[1:]):
            key = f"__TECH{counter[0]}__"
            placeholders[key] = word
            counter[0] += 1
            return key
        return word
    
    # Only replace longer camelCase words (likely technical terms)
    processed = re.sub(r'\b[A-Z][a-z]{2,}[A-Z]\w*\b', replace_tech, processed)
    
    return processed, placeholders


def restore_placeholders(text: str, placeholders: dict) -> str:
    """Restore placeholders back to original text."""
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


def translate_prose(text: str, translator: BatchTranslator) -> str:
    """Translate Chinese prose while protecting technical elements."""
    if not any('\u4e00' <= c <= '\u9fff' for c in text):
        return text
    
    # Extract prose and protect technical elements
    prose, placeholders = extract_prose_for_translation(text)
    
    if not any('\u4e00' <= c <= '\u9fff' for c in prose):
        return text
    
    # Translate the cleaned prose
    translated = translator.translate(prose)
    
    # Restore protected elements
    result = restore_placeholders(translated, placeholders)
    
    return result


def translate_table_row(text: str, translator: BatchTranslator) -> str:
    """Translate a table row preserving pipe structure."""
    cells = text.split('|')
    translated_cells = []
    
    for cell in cells:
        stripped = cell.strip()
        if not stripped or re.match(r'^[\-: ]+$', stripped):
            translated_cells.append(cell)
            continue
        
        has_cn = any('\u4e00' <= c <= '\u9fff' for c in stripped)
        if has_cn:
            translated = translate_prose(stripped, translator)
            # Preserve whitespace
            orig_leading = len(cell) - len(cell.lstrip())
            orig_trailing = len(cell) - len(cell.rstrip())
            translated_cells.append(' ' * orig_leading + translated.strip() + ' ' * orig_trailing)
        else:
            translated_cells.append(cell)
    
    return '|'.join(translated_cells)


def process_file(filepath: Path, translator: BatchTranslator) -> bool:
    """Process a single markdown file."""
    print(f"\n{'='*60}")
    print(f"Processing: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    result_lines = []
    
    in_frontmatter = False
    frontmatter_end = -1
    
    if len(lines) > 0 and lines[0].strip() == '---':
        in_frontmatter = True
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                frontmatter_end = i
                break
    
    cn_segment_count = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Frontmatter - translate title only
        if in_frontmatter and i <= frontmatter_end:
            match = re.match(r'^(title:\s*)(.*)', line)
            if match:
                prefix = match.group(1)
                title_val = match.group(2).strip().strip("'\"")
                has_cn = any('\u4e00' <= c <= '\u9fff' for c in title_val)
                if has_cn:
                    cn_segment_count += 1
                    translated_title = translate_prose(title_val, translator)
                    result_lines.append(f"{prefix}{translated_title}")
                else:
                    result_lines.append(line)
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # Code blocks - preserve entirely
        if line.strip().startswith('```'):
            block_lines = [line]
            i += 1
            while i < len(lines):
                block_lines.append(lines[i])
                if lines[i].strip().startswith('```'):
                    break
                i += 1
            result_lines.extend(block_lines)
            i += 1
            continue
        
        # Table separator - preserve as-is
        if re.match(r'^\s*\|[\s\-:|]+\|\s*$', line):
            result_lines.append(line)
            i += 1
            continue
        
        # Regular table rows (with pipes, not headers or blockquotes)
        if '|' in line and not line.strip().startswith('#') and not line.startswith('>'):
            has_cn = any('\u4e00' <= c <= '\u9fff' for c in line)
            if has_cn:
                cn_segment_count += 1
                translated = translate_table_row(line, translator)
                result_lines.append(translated)
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # Blockquote with table
        if line.startswith('> ') and '|' in line:
            inner = line[2:]
            has_cn = any('\u4e00' <= c <= '\u9fff' for c in inner)
            if has_cn:
                cn_segment_count += 1
                translated_inner = translate_table_row(inner, translator)
                result_lines.append(f"> {translated_inner}")
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # Headers (# ## ### etc.)
        header_match = re.match(r'^(#+)\s*(.*)', line)
        if header_match:
            prefix = header_match.group(1) + ' '
            text = header_match.group(2).strip()
            has_cn = any('\u4e00' <= c <= '\u9fff' for c in text)
            if has_cn:
                cn_segment_count += 1
                translated = translate_prose(text, translator)
                result_lines.append(prefix + translated)
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # Blockquotes (non-table)
        if line.startswith('> '):
            text = line[2:]
            has_cn = any('\u4e00' <= c <= '\u9fff' for c in text)
            if has_cn:
                cn_segment_count += 1
                translated = translate_prose(text, translator)
                result_lines.append(f"> {translated}")
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # List items (-, *, numbered)
        list_match = re.match(r'^(\s*[-*+]|\s*\d+\.)\s+(.*)', line)
        if list_match:
            prefix = list_match.group(1) + ' '
            text = list_match.group(2)
            has_cn = any('\u4e00' <= c <= '\u9fff' for c in text)
            if has_cn:
                cn_segment_count += 1
                translated = translate_prose(text, translator)
                result_lines.append(prefix + translated)
            else:
                result_lines.append(line)
            i += 1
            continue
        
        # Regular prose or empty lines
        has_cn = any('\u4e00' <= c <= '\u9fff' for c in line) if line.strip() else False
        if has_cn:
            cn_segment_count += 1
            translated = translate_prose(line, translator)
            result_lines.append(translated)
        else:
            result_lines.append(line)
        
        i += 1
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result_lines))
    
    print(f"  ✓ Translated {cn_segment_count} segments")
    return True


def get_files_to_translate():
    """Get list of markdown files to translate."""
    files = []
    
    for f in sorted(DOCS_DIR.glob("*.md")):
        if f.name in SKIP_FILES:
            print(f"Skipping (intentional Chinese): {f.name}")
            continue
        
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        
        cn_count = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
        if cn_count > 50:
            files.append((f, cn_count))
    
    files.sort(key=lambda x: x[1], reverse=True)
    return files


def main():
    print("=" * 60)
    print("Hermes Agent Documentation Translator")
    print(f"Target directory: {DOCS_DIR}")
    print("=" * 60)
    
    files = get_files_to_translate()
    if not files:
        print("No files with significant Chinese content found.")
        return
    
    print(f"\nFound {len(files)} files to translate:")
    for f, count in files[:25]:
        print(f"  - {f.name}: {count} CN chars")
    if len(files) > 25:
        print(f"  ... and {len(files) - 25} more files")
    
    translator = BatchTranslator(max_workers=3)
    success_count = 0
    error_files = []
    
    for filepath, cn_count in files:
        try:
            if process_file(filepath, translator):
                success_count += 1
                time.sleep(0.5)  # Rate limiting between files
        except Exception as e:
            import traceback
            print(f"  ✗ Error processing {filepath.name}: {e}", file=sys.stderr)
            traceback.print_exc()
            error_files.append((filepath.name, str(e)))
    
    print("\n" + "=" * 60)
    print(f"Translation complete!")
    print(f"  Success: {success_count}/{len(files)} files")
    print(f"  Translation errors: {translator.error_count}")
    if error_files:
        print(f"  File errors ({len(error_files)}):")
        for name, err in error_files:
            print(f"    - {name}: {err}")
    print("=" * 60)


if __name__ == "__main__":
    main()
