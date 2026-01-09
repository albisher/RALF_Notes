#!/Users/amac/Documents/code/RALF_Notes/venv/bin/python3
"""
RALF Note - AI Obsidian docs generator (COMPLETE FIXED VERSION)
"""

import os
import sys
import json
import re
import typer
from datetime import datetime
from pathlib import Path
from typing import Optional, List
from ollama import Client
from rich.console import Console
from rich.panel import Panel

console = Console()
client = Client(host='http://127.0.0.1:11434')
app = typer.Typer(add_completion=False)

# === CONFIG ===
SOURCE_PATHS = ['/Users/amac/Documents/code/WindowCleanner/']
TARGET_DIR = '/Users/amac/Documents/code/RALF_Notes/to_obsidian/'
TEMP_RAW_OUTPUT_DIR = '/Users/amac/Documents/code/RALF_Notes/temp_raw_output/'
MODEL_NAME = 'ministral-3:3b'
OPTIONS = {"num_ctx": 10000, "temperature": 0.1}  # Lower temp for consistency

SYSTEM_PROMPT = '''Analyze this code file. Return ONLY valid JSON - NO markdown, NO backticks, NO ``` blocks.

EXACT FORMAT:
{"filename":"FILENAME","tags":["#tag1","#tag2"],"type":"code-notes","summary":"One sentence purpose","details":"2-3 sentences logic","key_functions":[{"name":"func1","purpose":"Does X"}],"dependencies":["lib1"],"usage":"How to use","related":["[[Other]]"],"callouts": ["> [!INFO]- Key point"],"code_summary":"```python\nkey code snippet\n```"}

CRITICAL: Pure JSON only. No wrappers.'
''' 

def ensure_dir(directory):
    directory.mkdir(parents=True, exist_ok=True)

def get_all_files(paths):
    exts = ('.py','.txt','.md','.sh')
    skip_files = {'recursive_obsidian_checks.py', 'obsidian_generator.py'}
    files = []
    for path in map(Path, paths):
        if not path.exists(): continue
        for p in path.rglob('*'):
            if (p.is_file() and p.suffix in exts and p.name not in skip_files):
                files.append(p)
    return files

def recursive_summarize(content, chunk_size=100000):
    if len(content) <= chunk_size: return content[:8000]  # Truncate for reliability
    
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
    summaries = []
    for i, chunk in enumerate(chunks, 1):
        console.print(f"  Summarizing chunk {i}/{len(chunks)}...")
        try:
            resp = client.generate(model=MODEL_NAME, prompt=f"Summarize this code:\n\n{chunk[:4000]}", 
                                 options=OPTIONS)['response']
            summaries.append(resp)
        except:
            summaries.append(chunk[:1000])  # Fallback
    return recursive_summarize('\n\n'.join(summaries), chunk_size)

def extract_json(raw_response):
    """Robust JSON extraction from messy model output"""
    raw = raw_response.strip()
    
    # Try common wrappers first
    for pattern in [r'```(?:json)?\s*(\{.*\})\s*```', r'```text\s*(\{.*\})\s*```', r'(\{.*\})']:
        match = re.search(pattern, raw, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                continue
    
    # Last resort: find any JSON-like object
    try:
        start = raw.find('{')
        end = raw.rfind('}') + 1
        if start != -1 and end != 0:
            return json.loads(raw[start:end])
    except:
        pass
    
    return {}

def format_obsidian_markdown(filename, analysis):
    date = datetime.now().strftime("%Y-%m-%d")
    frontmatter = f"""
---
tags: {', '.join(analysis.get('tags', ['#documentation']))}
created: {date}
type: {analysis.get('type', 'code-notes')}
---"""
    
    content = f"""# {filename}

## Summary
{analysis.get('summary', 'Code analysis summary unavailable')}

## Details
{analysis.get('details', 'Logic and data flow analysis unavailable')}

## Key Functions
"""
    for func in analysis.get('key_functions', []):
        content += f"- **{func.get('name', 'unknown')}**: {func.get('purpose', 'No description')}\n"
    
    content += f"""

## Usage
{analysis.get('usage', 'Usage information unavailable')}\n\n"""
    
    if code_summary := analysis.get('code_summary'):
        content += f"{code_summary}\n\n"
    
    if deps := analysis.get('dependencies', []):
        content += f"## Dependencies\n{', '.join(deps)}\n\n"
    
    content += "## Related\n"
    for link in analysis.get('related', []):
        content += f"- {link}\n"
    
    for callout in analysis.get('callouts', []):
        content += f"\n{callout}\n"
    
    return frontmatter + '\n\n' + content.strip()

def generate_obsidian_doc(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        console.print(f"[red]❌ Cannot read {file_path}: {e}[/red]")
        return ""

    file_name = Path(file_path).stem
    console.print(f"[blue]📄 Analyzing[/]: {file_name}")
    
    processed_content = recursive_summarize(raw_content)
    final_prompt = f"File: {file_name}\nContent:\n{processed_content}"
    
    try:
        response = client.generate(
            model=MODEL_NAME,
            system=SYSTEM_PROMPT,
            prompt=final_prompt,
            options=OPTIONS,
        )
        raw_response = response.get('response', '').strip()
    except Exception as e:
        console.print(f"[red]❌ Ollama error for {file_name}: {e}[/red]")
        return f"# {file_name}\n\n> [!ERROR] Ollama service error"

    analysis = extract_json(raw_response)
    
    if not analysis:
        console.print(f"[yellow]⚠️ No JSON for {file_name}, saving raw[/yellow]")
        return f"""# {file_name}

> [!WARNING] JSON parsing failed

**Raw model output:**
```text
{raw_response[:2000]}
"""
    else: # Added else block
        console.print(f"[green]✅ Generated doc for {file_name}[/green]")
        return format_obsidian_markdown(file_name, analysis)


def process_files(paths, dry_run=False, overwrite=False):
    ensure_dir(Path(TARGET_DIR))
    files = get_all_files(paths)

    console.print(f"[cyan]Found {len(files)} files to process[/cyan]")

    for i, file_path in enumerate(files, 1):
        src_root = next((p for p in paths if str(file_path).startswith(str(p))), None)
        if not src_root: 
            console.print(f"[yellow]Skipping {file_path.name} (no source root)[/yellow]")
            continue
        
        relative_path = file_path.relative_to(src_root)
        target = Path(TARGET_DIR) / relative_path.with_suffix('.md')
        ensure_dir(target.parent)
        
        if target.exists() and not overwrite:
            console.print(f"[yellow]⏭️  Skip existing: {target.name}[/yellow]")
            continue
            
        console.print(f"[blue][{i}/{len(files)}] Generating: {target.name}[/blue]")
        
        if not dry_run:
            doc_content = generate_obsidian_doc(str(file_path))
            if doc_content.strip():  # Only write non-empty content
                target.write_text(doc_content, encoding='utf-8')
                console.print(f"[green]✅ Saved: {target.name}[/green]")
            else:
                console.print(f"[red]❌ Empty content for {target.name}[/red]")
        else:
            console.print(f"[grey]👁️  DRY RUN: Would save {target}[/grey]")

    console.print(f"\n[bold green]✨ Complete! Processed {len(files)} files[/bold green]")

@app.command()
def main(
    path: Optional[Path] = typer.Argument(None, help="Source path"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview only"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing"),
):
    """Generate Obsidian documentation from code"""
    paths = [str(path)] if path else SOURCE_PATHS
    console.print(Panel("🚀 RALF Note Active", style="bold blue"))
    process_files(paths, dry_run=dry_run, overwrite=overwrite)

@app.command()
def status():
    """Show configuration"""
    console.print("📋 RALF Note Status:")
    console.print(f"  • Source: {SOURCE_PATHS}")
    console.print(f"  • Target: {TARGET_DIR}")
    console.print(f"  • Model: {MODEL_NAME}")


if __name__ == "__main__":
    app()
