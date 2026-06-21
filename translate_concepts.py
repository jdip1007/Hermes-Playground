#!/usr/bin/env python3
"""Translate Chinese text to English in concept markdown files using local LLM."""

import os
import sys
import re
import json
import time
import httpx

BASE = "/root/Hermes-Playground"
LLM_URL = "http://172.21.176.1:1234/v1/chat/completions"
MODEL = "qwen/qwen3.6-27b-mtp"

FILES = [
    ("docs/concepts/smart-model-routing.md", 3118),
    ("docs/concepts/multi-agent-architecture.md", 3464),
    ("docs/concepts/skills-system-architecture.md", 3985),
    ("docs/concepts/context-compressor-architecture.md", 5126),
    ("docs/concepts/security-defense-system.md", 5584),
    ("docs/concepts/messaging-gateway-architecture.md", 6007),
]

SYSTEM_PROMPT = """You are a technical documentation translator. Translate Chinese text to English while preserving:
1. ALL markdown formatting (headers #, ##, ###, lists -, *, bold **, italic *, strikethrough ~~)
2. ALL code references in backticks like `filename.py`, `function_name()`, commit hashes, PR numbers (#12345)
3. ALL inline code blocks with triple backticks - do NOT modify content inside ``` blocks
4. ALL URLs and link syntax [text](url), reference links [[name|key]]
5. ALL technical terms: Gateway, Agent, SessionStore, PlatformRegistry, AIAgent, etc.
6. ALL YAML frontmatter structure (--- delimiters, key: value pairs)
7. Reference markers like [1] at end of sentences
8. Table formatting with | separators and --- dividers
9. All code comments in code blocks should remain as-is

Only translate Chinese prose text to English. Do not modify any code, file paths, function names, or technical identifiers."""

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def split_into_blocks(content):
    """Split markdown content into blocks: yaml_frontmatter, code_block, prose.
    Returns list of (type, original_text) tuples."""
    blocks = []
    lines = content.split('\n')
    i = 0
    
    # YAML frontmatter
    if lines and lines[0].strip() == '---':
        end_idx = -1
        for j in range(1, len(lines)):
            if lines[j].strip() == '---':
                end_idx = j
                break
        if end_idx > 0:
            blocks.append(('yaml', '\n'.join(lines[:end_idx+1])))
            i = end_idx + 1
    
    while i < len(lines):
        # Code block (triple backticks)
        if lines[i].startswith('```'):
            start = i
            j = i + 1
            while j < len(lines) and not (lines[j].strip() == '```' or lines[j].startswith('```\n')):
                j += 1
            # Find closing ```
            if j < len(lines):
                # Check if line is just ```
                if lines[j].strip() == '```':
                    j += 1
                else:
                    # Line starts with ``` but has more - find actual end
                    while j < len(lines) and not lines[j].strip().startswith('```'):
                        j += 1
                    if j < len(lines):
                        j += 1
            blocks.append(('code', '\n'.join(lines[start:j])))
            i = j
        else:
            # Prose block - collect until next code block or end
            start = i
            while i < len(lines) and not lines[i].startswith('```'):
                i += 1
            if i > start:
                blocks.append(('prose', '\n'.join(lines[start:i])))
    
    return blocks

def translate_block(text, block_type):
    """Translate a single block of text."""
    if not has_chinese(text):
        return text
    
    if block_type == 'code':
        # Don't translate code blocks (preserve comments as-is)
        return text
    
    if block_type == 'yaml':
        # Translate YAML values that contain Chinese
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            if ':' in line and not line.startswith('-') and not line.strip().startswith('#'):
                key, _, val = line.partition(':')
                if has_chinese(val) and key.strip() in ('title', 'description'):
                    translated_val = translate_text_inline(val.strip())
                    new_lines.append(f"{key}: {translated_val}")
                else:
                    new_lines.append(line)
            elif line.startswith('- ') and has_chinese(line):
                val = line[2:]
                if has_chinese(val):
                    # Don't translate tags that are just identifiers
                    translated_val = translate_text_inline(val.strip())
                    new_lines.append(f"- {translated_val}")
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        return '\n'.join(new_lines)
    
    # Prose block - full translation
    return translate_prose(text)

def translate_text_inline(text):
    """Translate a short inline text (for YAML values, etc.)."""
    if not has_chinese(text):
        return text
    
    prompt = f'Translate this Chinese text to English. Only output the translated text, nothing else: "{text}"'
    
    try:
        resp = httpx.post(LLM_URL, json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a translator. Translate Chinese to English concisely."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.1,
            "max_tokens": 256,
        }, timeout=30)
        
        if resp.status_code == 200:
            result = resp.json()["choices"][0]["message"]["content"].strip()
            # Remove quotes if added by model
            if result.startswith('"') and result.endswith('"'):
                result = result[1:-1]
            return result
    except Exception as e:
        print(f"  Inline translation error: {e}")
    
    return text

def translate_prose(text):
    """Translate a prose block using the LLM."""
    if not has_chinese(text):
        return text
    
    # For very large blocks, split into smaller chunks by double-newline paragraphs
    if len(text) > 8000:
        paragraphs = re.split(r'(\n\n+)', text)
        translated_parts = []
        for part in paragraphs:
            if has_chinese(part):
                # Further split if still too large
                sub_parts = part.split('\n')
                chunks = []
                current_chunk = []
                current_len = 0
                for line in sub_parts:
                    if current_len + len(line) > 6000 and current_chunk:
                        chunks.append('\n'.join(current_chunk))
                        current_chunk = [line]
                        current_len = len(line)
                    else:
                        current_chunk.append(line)
                        current_len += len(line)
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                
                for chunk in chunks:
                    translated_parts.append(translate_prose(chunk))
            else:
                translated_parts.append(part)
        return '\n'.join(translated_parts)
    
    try:
        resp = httpx.post(LLM_URL, json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Translate the following Chinese text to English:\n\n{text}"}
            ],
            "temperature": 0.1,
            "max_tokens": 4096,
        }, timeout=120)
        
        if resp.status_code == 200:
            result = resp.json()["choices"][0]["message"]["content"].strip()
            return result
        else:
            print(f"  LLM error: {resp.status_code}")
            return text
    except Exception as e:
        print(f"  Translation error: {e}")
        return text

def process_file(filepath):
    """Process a single file."""
    full_path = os.path.join(BASE, filepath)
    
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cn_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    print(f"\n{'='*60}")
    print(f"Processing: {filepath} ({cn_chars} CN chars)")
    
    if cn_chars == 0:
        print("No Chinese text found, skipping.")
        return True
    
    blocks = split_into_blocks(content)
    translated_blocks = []
    
    for idx, (block_type, block_text) in enumerate(blocks):
        if has_chinese(block_text):
            print(f"  [{idx}] Translating {block_type} block ({len(block_text)} chars)...")
            translated = translate_block(block_text, block_type)
            translated_blocks.append(translated)
            
            # Check remaining Chinese in translated text
            remaining = len(re.findall(r'[\u4e00-\u9fff]', translated))
            if remaining > 0:
                print(f"    Remaining CN chars: {remaining}")
        else:
            translated_blocks.append(block_text)
        
        time.sleep(0.5)  # Rate limiting
    
    new_content = '\n'.join(translated_blocks)
    
    # Write back with backup
    backup_path = full_path + '.bak'
    os.rename(full_path, backup_path)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    remaining_cn = len(re.findall(r'[\u4e00-\u9fff]', new_content))
    print(f"  Done! Remaining Chinese chars: {remaining_cn}")
    return True

if __name__ == "__main__":
    # Test LLM connection first
    print("Testing LLM connection...")
    try:
        resp = httpx.post(LLM_URL, json={
            "model": MODEL,
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 10,
        }, timeout=15)
        if resp.status_code == 200:
            print(f"LLM connected: {resp.json()['choices'][0]['message']['content'][:50]}")
        else:
            print(f"LLM error: {resp.status_code}")
    except Exception as e:
        print(f"Cannot connect to LLM: {e}")
        sys.exit(1)
    
    for filepath, _ in FILES:
        process_file(filepath)
    
    print("\n\nAll files processed!")
