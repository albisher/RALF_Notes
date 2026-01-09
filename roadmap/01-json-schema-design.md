# Unified JSON Schema Design

**Date:** 2026-01-09
**Purpose:** Define the single JSON schema that replaces 9 separate generators

---

## Schema Overview

The unified JSON schema combines all document sections into one structured response. The model generates this once, and Python post-processing formats it into Obsidian markdown.

---

## Complete JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RALFDocumentationSchema",
  "type": "object",
  "required": ["filename", "tags", "type", "summary"],
  "properties": {
    "filename": {
      "type": "string",
      "description": "Base filename without extension",
      "minLength": 1
    },
    "tags": {
      "type": "array",
      "description": "Relevant tags for the document (with # prefix)",
      "items": {
        "type": "string",
        "pattern": "^#[a-z0-9-]+$"
      },
      "minItems": 2,
      "maxItems": 10,
      "uniqueItems": true
    },
    "type": {
      "type": "string",
      "description": "Document type classification",
      "enum": [
        "code-notes",
        "documentation",
        "research",
        "test-reference",
        "configuration",
        "api-reference",
        "architecture",
        "tutorial"
      ]
    },
    "summary": {
      "type": "string",
      "description": "1-2 sentence high-level purpose",
      "minLength": 20,
      "maxLength": 500
    },
    "details": {
      "type": "string",
      "description": "2-4 sentences explaining logic and data flow",
      "minLength": 50,
      "maxLength": 1500
    },
    "key_functions": {
      "type": "array",
      "description": "Important functions, classes, or components",
      "items": {
        "type": "object",
        "required": ["name", "purpose"],
        "properties": {
          "name": {
            "type": "string",
            "description": "Function/class name",
            "minLength": 1
          },
          "purpose": {
            "type": "string",
            "description": "What it does",
            "minLength": 10,
            "maxLength": 300
          },
          "signature": {
            "type": "string",
            "description": "Optional function signature"
          },
          "returns": {
            "type": "string",
            "description": "Optional return value description"
          }
        }
      },
      "minItems": 0,
      "maxItems": 15
    },
    "dependencies": {
      "type": "array",
      "description": "External libraries, modules, or systems",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "uniqueItems": true
    },
    "usage": {
      "type": "string",
      "description": "How to use this code/system",
      "minLength": 20,
      "maxLength": 1000
    },
    "related": {
      "type": "array",
      "description": "Obsidian wikilinks to related documents",
      "items": {
        "type": "string",
        "pattern": "^\\[\\[.*\\]\\]$"
      },
      "uniqueItems": true
    },
    "callouts": {
      "type": "array",
      "description": "Obsidian callout blocks for key info",
      "items": {
        "type": "string",
        "pattern": "^> \\[!(INFO|WARNING|TIP|NOTE|IMPORTANT)"
      },
      "maxItems": 5
    },
    "code_summary": {
      "type": "string",
      "description": "Key code snippet in markdown code block",
      "pattern": "^```[a-z]*\\n[\\s\\S]*\\n```$"
    },
    "security_risks": {
      "type": "string",
      "description": "Optional security considerations",
      "maxLength": 1000
    },
    "performance_notes": {
      "type": "string",
      "description": "Optional performance characteristics",
      "maxLength": 500
    },
    "doc_type_confidence": {
      "type": "number",
      "description": "Confidence in type classification (0-1)",
      "minimum": 0,
      "maximum": 1
    },
    "dependency_graph": {
      "type": "string",
      "description": "Optional mermaid diagram of dependencies",
      "pattern": "^```mermaid\\n[\\s\\S]*\\n```$"
    }
  }
}
```

---

## Field Descriptions

### Core Fields (Required)

#### `filename`
**Type:** `string`
**Required:** ✅
**Example:** `"recursive_obsidian_checks"`

The base filename without extension. Used as H1 header.

#### `tags`
**Type:** `array<string>`
**Required:** ✅
**Min Items:** 2
**Max Items:** 10
**Pattern:** `^#[a-z0-9-]+$`

Tags for Obsidian frontmatter and organization.

**Examples:**
```json
["#python", "#documentation", "#automation"]
["#openstreetmap", "#gps", "#3d-tiles", "#kuwait"]
```

#### `type`
**Type:** `enum<string>`
**Required:** ✅
**Values:**
- `code-notes` - Documentation of source code
- `documentation` - General documentation
- `research` - Research findings
- `test-reference` - Test data/locations
- `configuration` - Config file documentation
- `api-reference` - API documentation
- `architecture` - System architecture
- `tutorial` - How-to guides

#### `summary`
**Type:** `string`
**Required:** ✅
**Length:** 20-500 chars

High-level purpose in 1-2 sentences.

**Example:**
```json
"summary": "Explores methods to derive real-world street maps and 3D building data from GPS coordinates for HMRS simulation system."
```

---

### Content Fields (Optional but Recommended)

#### `details`
**Type:** `string`
**Length:** 50-1500 chars

Detailed explanation of logic, data flow, and architecture.

**Example:**
```json
"details": "The document analyzes GPS coordinate formats (decimal degrees, DMS, DDM) and their usage in HMRS, focusing on OpenStreetMap (OSM) as the primary free solution. It details OSM's global coverage, 3D tile formats, and APIs (Overpass, Nominatim) for querying building/road data."
```

#### `key_functions`
**Type:** `array<object>`
**Min Items:** 0
**Max Items:** 15

Important functions, classes, or components.

**Schema:**
```json
{
  "name": "function_name",
  "purpose": "What it does",
  "signature": "Optional: def func(arg1, arg2)",
  "returns": "Optional: Return value description"
}
```

**Example:**
```json
"key_functions": [
  {
    "name": "recursive_summarize",
    "purpose": "Chunks large files and recursively summarizes them for context compression",
    "signature": "recursive_summarize(content, chunk_size=100000)",
    "returns": "Condensed content suitable for LLM processing"
  },
  {
    "name": "extract_json",
    "purpose": "Robust JSON extraction from messy model output with multiple fallback strategies"
  }
]
```

#### `dependencies`
**Type:** `array<string>`
**Unique:** ✅

External libraries, modules, or systems.

**Example:**
```json
"dependencies": ["ollama", "rich", "typer", "pathlib", "datetime"]
```

#### `usage`
**Type:** `string`
**Length:** 20-1000 chars

How to use this code/system.

**Example:**
```json
"usage": "Run with `python RalfNotes.py [path]` to generate Obsidian docs. Use `--dry-run` to preview without writing files. Use `--overwrite` to regenerate existing docs. Check configuration with `python RalfNotes.py status`."
```

#### `related`
**Type:** `array<string>`
**Pattern:** `^\\[\\[.*\\]\\]$`
**Unique:** ✅

Obsidian wikilinks to related documents.

**Example:**
```json
"related": [
  "[[HMRS GPS Tracker]]",
  "[[CesiumJS Integration Guide]]",
  "[[OpenStreetMap API Docs]]"
]
```

#### `callouts`
**Type:** `array<string>`
**Max Items:** 5
**Pattern:** `^> \\[!(INFO|WARNING|TIP|NOTE|IMPORTANT)`

Obsidian callout blocks for highlighting key information.

**Example:**
```json
"callouts": [
  "> [!INFO]- **Key OSM Advantage**: Free, global coverage, and ODbL license enable open-source reuse without restrictions.",
  "> [!WARNING]- **Rate Limits**: Nominatim's 1 request/second limit may require caching for high-frequency queries.",
  "> [!TIP]- **Kuwait Focus**: Prioritize OSM data from Kuwait's region to ensure local accuracy."
]
```

#### `code_summary`
**Type:** `string`
**Pattern:** `^```[a-z]*\\n[\\s\\S]*\\n```$`

Key code snippet in markdown code block.

**Example:**
```json
"code_summary": "```python\ndef generate_obsidian_doc(file_path: str) -> str:\n    raw_content = Path(file_path).read_text()\n    processed = recursive_summarize(raw_content)\n    response = client.generate(model=MODEL, prompt=processed)\n    return format_obsidian_markdown(extract_json(response))\n```"
```

---

### Extended Fields (Optional)

#### `security_risks`
**Type:** `string`
**Length:** Max 1000 chars

Security considerations for the code.

**Example:**
```json
"security_risks": "File path injection risk if user input is not sanitized. Recommend using Path().resolve() to canonicalize paths and checking against allowed directories."
```

#### `performance_notes`
**Type:** `string`
**Length:** Max 500 chars

Performance characteristics.

**Example:**
```json
"performance_notes": "Processing time scales linearly with file count. Large files (>100KB) trigger recursive summarization which adds ~2-5s per file. Consider parallel processing for >100 files."
```

#### `doc_type_confidence`
**Type:** `number`
**Range:** 0-1

Model's confidence in type classification.

**Example:**
```json
"doc_type_confidence": 0.95
```

#### `dependency_graph`
**Type:** `string`
**Pattern:** `^```mermaid\\n[\\s\\S]*\\n```$`

Mermaid diagram of dependencies.

**Example:**
```json
"dependency_graph": "```mermaid\ngraph TD\n  A[RalfNotes] --> B[Ollama Client]\n  A --> C[Rich Console]\n  A --> D[Typer CLI]\n  B --> E[LLM Model]\n```"
```

---

## Prompt Template

```python
SYSTEM_PROMPT = '''You are an expert technical writer specializing in Obsidian documentation.

Analyze the provided code file and return ONLY valid JSON - NO markdown wrappers, NO backticks, NO ``` blocks.

**CRITICAL:** Return PURE JSON ONLY. Start with { and end with }.

**EXACT FORMAT:**
{
  "filename": "base_filename_without_extension",
  "tags": ["#tag1", "#tag2", "#tag3"],
  "type": "code-notes",
  "summary": "One sentence explaining the high-level purpose",
  "details": "2-4 sentences describing logic, data flow, and architecture",
  "key_functions": [
    {
      "name": "function_name",
      "purpose": "What this function does",
      "signature": "optional_function_signature",
      "returns": "optional_return_description"
    }
  ],
  "dependencies": ["library1", "library2"],
  "usage": "Detailed usage instructions with examples",
  "related": ["[[Related Document 1]]", "[[Related Document 2]]"],
  "callouts": [
    "> [!INFO]- Key insight or takeaway",
    "> [!WARNING]- Important warning or gotcha"
  ],
  "code_summary": "```language\\nkey code snippet\\n```",
  "security_risks": "Optional: Security considerations",
  "performance_notes": "Optional: Performance characteristics"
}

**VALIDATION RULES:**
1. filename: Must not include file extension
2. tags: 2-10 tags, all lowercase with #, use hyphens not spaces
3. type: Must be one of: code-notes, documentation, research, test-reference, configuration, api-reference, architecture, tutorial
4. summary: 1-2 sentences, 20-500 characters
5. details: 2-4 sentences, 50-1500 characters
6. key_functions: 0-15 functions with name and purpose
7. related: Use Obsidian [[wikilink]] format
8. callouts: Use Obsidian > [!TYPE] format (INFO, WARNING, TIP, NOTE)
9. code_summary: Wrap in ``` blocks with language

**EXAMPLE TAG CATEGORIES:**
- Language: #python, #javascript, #rust, #go
- Domain: #api, #database, #simulation, #testing, #documentation
- Tech: #docker, #ollama, #cesium, #openstreetmap
- Purpose: #automation, #optimization, #analysis

Return ONLY the JSON object. No explanations. No markdown.'''
```

---

## User Prompt Template

```python
def format_user_prompt(filename: str, content: str) -> str:
    return f"""Analyze this file and return documentation JSON.

**File:** {filename}

**Content:**
{content}

Remember: Return ONLY valid JSON. No markdown. No backticks."""
```

---

## Example Complete Response

```json
{
  "filename": "RalfNotes",
  "tags": ["#python", "#ollama", "#documentation", "#automation", "#obsidian"],
  "type": "code-notes",
  "summary": "AI-powered Obsidian documentation generator that analyzes code files and creates structured markdown notes using local LLM inference.",
  "details": "RalfNotes.py implements a TUI-based documentation pipeline using Ollama for AI analysis and Rich for terminal display. It processes source files recursively, generates JSON-structured analysis via LLM, extracts and validates the JSON, then formats it into Obsidian-compatible markdown with frontmatter, sections, and callouts. Features include dry-run mode, overwrite control, and chunked processing for large files.",
  "key_functions": [
    {
      "name": "recursive_summarize",
      "purpose": "Chunks files exceeding 100KB and recursively summarizes them to fit context windows",
      "signature": "recursive_summarize(content, chunk_size=100000)",
      "returns": "Condensed content string suitable for LLM processing"
    },
    {
      "name": "extract_json",
      "purpose": "Robustly extracts JSON from model output using regex patterns and fallback strategies",
      "signature": "extract_json(raw_response)",
      "returns": "Dictionary parsed from JSON, or empty dict on failure"
    },
    {
      "name": "format_obsidian_markdown",
      "purpose": "Converts JSON analysis dictionary into formatted Obsidian markdown with frontmatter and sections",
      "signature": "format_obsidian_markdown(filename, analysis)",
      "returns": "Complete markdown document string"
    },
    {
      "name": "generate_obsidian_doc",
      "purpose": "Main pipeline: reads file, summarizes, calls LLM, extracts JSON, formats markdown",
      "signature": "generate_obsidian_doc(file_path: str)",
      "returns": "Formatted markdown string ready to write"
    },
    {
      "name": "process_files",
      "purpose": "Batch processes multiple files with progress reporting and error handling",
      "signature": "process_files(paths, dry_run=False, overwrite=False)"
    }
  ],
  "dependencies": ["ollama", "rich", "typer", "pathlib", "datetime", "json", "re"],
  "usage": "Run `python RalfNotes.py` to process configured SOURCE_PATHS. Use `python RalfNotes.py /custom/path` for specific directory. Options: `--dry-run` for preview without writing, `--overwrite` to regenerate existing docs. Check configuration with `python RalfNotes.py status`. Requires Ollama running locally with ministral-3:3b model.",
  "related": [
    "[[recursive_obsidian_checks]]",
    "[[Ollama Configuration]]",
    "[[Obsidian Markdown Syntax]]"
  ],
  "callouts": [
    "> [!INFO]- **Architecture**: Uses two-phase processing - LLM generates raw JSON analysis, Python post-processes into formatted markdown for deterministic output.",
    "> [!TIP]- **Large Files**: Automatically triggers recursive summarization for files >100KB to prevent context overflow.",
    "> [!WARNING]- **JSON Extraction**: Current regex-based extraction may fail with heavily malformed output. Consider adding retry logic with corrective prompts."
  ],
  "code_summary": "```python\ndef generate_obsidian_doc(file_path: str) -> str:\n    raw_content = Path(file_path).read_text()\n    processed = recursive_summarize(raw_content)\n    \n    response = client.generate(\n        model=MODEL_NAME,\n        system=SYSTEM_PROMPT,\n        prompt=f\"File: {filename}\\nContent:\\n{processed}\",\n        options=OPTIONS\n    )\n    \n    analysis = extract_json(response['response'])\n    return format_obsidian_markdown(filename, analysis)\n```",
  "performance_notes": "Single-threaded processing at ~10-15 seconds per file. Potential 5-10x speedup with parallel processing. Memory usage scales with file size during chunking.",
  "doc_type_confidence": 0.98
}
```

---

## Validation Implementation

```python
import json
from jsonschema import validate, ValidationError

RALF_SCHEMA = {
    # ... (schema from above)
}

def validate_json_response(data: dict) -> tuple[bool, list[str]]:
    """
    Validate JSON against schema.

    Returns:
        (is_valid, error_messages)
    """
    errors = []

    try:
        validate(instance=data, schema=RALF_SCHEMA)
    except ValidationError as e:
        errors.append(f"Schema validation failed: {e.message}")
        return (False, errors)

    # Additional custom validation
    if not data.get('filename'):
        errors.append("filename is required")

    if len(data.get('tags', [])) < 2:
        errors.append("At least 2 tags required")

    if len(data.get('summary', '')) < 20:
        errors.append("summary must be at least 20 characters")

    return (len(errors) == 0, errors)
```

---

## Next Steps

1. **Implement schema validator** → See `02-architecture-refactoring.md`
2. **Create formatting pipeline** → See `02-architecture-refactoring.md`
3. **Add error recovery** → See `03-error-handling-strategy.md`
4. **Build TUI** → See `04-tui-implementation.md`

---

## Summary

This unified JSON schema replaces 9 separate generators with a single structured response:

- ✅ **Complete**: Covers all sections (summary, details, key functions, etc.)
- ✅ **Extensible**: Easy to add new fields
- ✅ **Validatable**: JSON Schema for automated validation
- ✅ **Clear**: Explicit types and constraints
- ✅ **Obsidian-compatible**: Designed for markdown output

**Key benefit:** One LLM call produces everything needed for a complete Obsidian note.
