# Architecture Refactoring Plan

**Date:** 2026-01-09
**Goal:** Transform current multi-generator architecture to unified JSON approach with TUI

---

## Current vs Target Architecture

### Current Architecture (Complex)

```
┌─────────────────────────────────────────┐
│         DocumentGenerator               │
│  (Orchestrates 9 generators)           │
└──────────────┬──────────────────────────┘
               │
               ├──> SummaryGenerator
               ├──> DetailsGenerator
               ├──> KeyFunctionsGenerator
               ├──> UsageGenerator
               ├──> RelatedGenerator
               ├──> TagsGenerator
               ├──> DocTypeGenerator
               ├──> DependencyGraphGenerator
               └──> SecurityRisksGenerator
                    │
                    ├──> BaseSectionGenerator
                    ├──> SectionGenerator
                    ├──> ResponseCleaner
                    ├──> SectionValidator
                    └──> CacheManager

Total: 9 LLM calls per file
Complexity: High (multiple classes, inheritance)
Speed: Slow (sequential processing)
```

### Target Architecture (Simple)

```
┌─────────────────────────────────────────┐
│          RALFDocumentGenerator          │
│    (Single unified JSON generation)     │
└──────────────┬──────────────────────────┘
               │
               ├──> JSONGenerator
               │    └──> Single LLM call
               │
               ├──> JSONExtractor
               │    └──> Parse & validate
               │
               ├──> MarkdownFormatter
               │    └──> JSON → Obsidian MD
               │
               ├──> CacheManager (reuse!)
               │    └──> Cache JSON results
               │
               └──> TUIManager
                    ├──> Rich Console
                    └──> Typer CLI

Total: 1 LLM call per file
Complexity: Low (simple pipeline)
Speed: Fast (9x speedup)
```

---

## New Module Structure

```
RALF_Notes/
├── main.py                      # CLI entry point (Typer)
├── config.py                    # Configuration
├── prompts.py                   # Unified JSON prompt
│
├── core/
│   ├── __init__.py
│   ├── models.py                # Dataclasses (RALFDocument, etc.)
│   ├── json_generator.py       # LLM → raw JSON
│   ├── json_extractor.py       # Raw response → parsed JSON
│   ├── json_validator.py       # JSON schema validation
│   ├── markdown_formatter.py   # JSON → Obsidian markdown
│   ├── document_pipeline.py    # Orchestrates the flow
│   ├── file_processor.py       # Batch file processing
│   └── cache_manager.py        # ✅ Keep existing (excellent!)
│
├── tui/
│   ├── __init__.py
│   ├── console.py              # Rich console wrapper
│   ├── progress.py             # Progress indicators
│   ├── panels.py               # Panel formatting
│   └── ascii_art.py            # Banner/logo
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py           # File operations
│   ├── text_utils.py           # Text processing
│   └── logger_factory.py       # ✅ Keep existing
│
└── tests/
    ├── test_json_generator.py
    ├── test_json_extractor.py
    ├── test_json_validator.py
    ├── test_markdown_formatter.py
    └── test_pipeline.py
```

---

## Core Components

### 1. JSONGenerator (`core/json_generator.py`)

**Purpose:** Generate raw JSON from file content using single LLM call

```python
from dataclasses import dataclass
from typing import Optional
from ollama import Client
from .models import GenerationContext, GenerationOptions

@dataclass
class JSONGeneratorConfig:
    """Configuration for JSON generation"""
    model_name: str = 'ministral-3:3b'
    num_ctx: int = 10000
    temperature: float = 0.1
    chunk_size: int = 100000

class JSONGenerator:
    """
    Box: JSON Generator

    Input: GenerationContext (file path, content, metadata)
    Output: Raw JSON string from LLM
    Responsibility: Single LLM call to generate structured analysis
    """

    def __init__(self,
                 ollama_client: Client,
                 config: JSONGeneratorConfig,
                 system_prompt: str):
        self.client = ollama_client
        self.config = config
        self.system_prompt = system_prompt

    def generate(self, context: GenerationContext) -> str:
        """Generate JSON documentation for file"""
        # 1. Chunk/summarize if needed
        processed_content = self._prepare_content(context.content)

        # 2. Build user prompt
        user_prompt = self._format_prompt(context.filename, processed_content)

        # 3. Call LLM
        response = self.client.generate(
            model=self.config.model_name,
            system=self.system_prompt,
            prompt=user_prompt,
            options={
                "num_ctx": self.config.num_ctx,
                "temperature": self.config.temperature
            }
        )

        return response['response']

    def _prepare_content(self, content: str) -> str:
        """Chunk and summarize large files"""
        if len(content) <= self.config.chunk_size:
            return content[:8000]  # Truncate for reliability

        return self._recursive_summarize(content)

    def _recursive_summarize(self, content: str) -> str:
        """Recursively summarize large content"""
        # Implementation from PoC
        ...

    def _format_prompt(self, filename: str, content: str) -> str:
        """Format user prompt"""
        return f"""Analyze this file and return documentation JSON.

**File:** {filename}

**Content:**
{content}

Remember: Return ONLY valid JSON. No markdown. No backticks."""
```

---

### 2. JSONExtractor (`core/json_extractor.py`)

**Purpose:** Extract and parse JSON from messy LLM output

```python
import json
import re
from typing import Optional, Tuple
from .models import RALFDocument

class JSONExtractor:
    """
    Box: JSON Extractor

    Input: Raw LLM response string
    Output: Parsed dictionary or None
    Responsibility: Robust JSON extraction with fallbacks
    """

    # Patterns to try in order
    PATTERNS = [
        r'```json\s*(\{.*?\})\s*```',      # ```json {...} ```
        r'```\s*(\{.*?\})\s*```',          # ``` {...} ```
        r'```text\s*(\{.*?\})\s*```',      # ```text {...} ```
        r'(\{.*\})',                        # Raw JSON
    ]

    def extract(self, raw_response: str) -> Tuple[Optional[dict], Optional[str]]:
        """
        Extract JSON from response.

        Returns:
            (parsed_dict, error_message)
        """
        raw = raw_response.strip()

        # Try each pattern
        for pattern in self.PATTERNS:
            match = re.search(pattern, raw, re.DOTALL)
            if match:
                json_str = match.group(1)
                try:
                    return (json.loads(json_str), None)
                except json.JSONDecodeError as e:
                    continue  # Try next pattern

        # Last resort: find any JSON-like object
        try:
            start = raw.find('{')
            end = raw.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = raw[start:end]
                return (json.loads(json_str), None)
        except json.JSONDecodeError as e:
            pass

        return (None, f"Failed to extract valid JSON from response")

    def extract_or_fallback(self, raw_response: str, filename: str) -> dict:
        """Extract JSON or create fallback structure"""
        parsed, error = self.extract(raw_response)

        if parsed:
            return parsed

        # Fallback structure
        return {
            "filename": filename,
            "tags": ["#parsing-failed", "#needs-review"],
            "type": "code-notes",
            "summary": "Documentation generation failed - JSON parsing error",
            "details": f"Error: {error}",
            "key_functions": [],
            "dependencies": [],
            "usage": "Manual review required",
            "related": [],
            "callouts": [
                f"> [!WARNING]- JSON Parsing Failed\n> {error}\n\n**Raw output:**\n```text\n{raw_response[:500]}\n```"
            ]
        }
```

---

### 3. JSONValidator (`core/json_validator.py`)

**Purpose:** Validate JSON against schema and business rules

```python
from typing import List, Tuple
from jsonschema import validate, ValidationError
from .models import RALFDocument

class JSONValidator:
    """
    Box: JSON Validator

    Input: Parsed JSON dictionary
    Output: (is_valid, errors)
    Responsibility: Schema validation and business rules
    """

    def __init__(self, schema: dict):
        self.schema = schema

    def validate(self, data: dict) -> Tuple[bool, List[str]]:
        """
        Validate JSON against schema.

        Returns:
            (is_valid, error_messages)
        """
        errors = []

        # Schema validation
        try:
            validate(instance=data, schema=self.schema)
        except ValidationError as e:
            errors.append(f"Schema error: {e.message}")

        # Business rules
        errors.extend(self._validate_business_rules(data))

        return (len(errors) == 0, errors)

    def _validate_business_rules(self, data: dict) -> List[str]:
        """Custom validation rules"""
        errors = []

        # Required fields
        if not data.get('filename'):
            errors.append("filename is required")

        # Tag validation
        tags = data.get('tags', [])
        if len(tags) < 2:
            errors.append("At least 2 tags required")

        for tag in tags:
            if not tag.startswith('#'):
                errors.append(f"Tag must start with #: {tag}")
            if ' ' in tag:
                errors.append(f"Tag cannot contain spaces: {tag}")

        # Summary validation
        summary = data.get('summary', '')
        if len(summary) < 20:
            errors.append("Summary must be at least 20 characters")
        if len(summary) > 500:
            errors.append("Summary must be at most 500 characters")

        # Type validation
        valid_types = [
            'code-notes', 'documentation', 'research', 'test-reference',
            'configuration', 'api-reference', 'architecture', 'tutorial'
        ]
        if data.get('type') not in valid_types:
            errors.append(f"Invalid type: {data.get('type')}")

        # Key functions validation
        key_funcs = data.get('key_functions', [])
        if len(key_funcs) > 15:
            errors.append("Too many key functions (max 15)")

        for func in key_funcs:
            if not func.get('name'):
                errors.append("Key function missing name")
            if not func.get('purpose'):
                errors.append(f"Key function '{func.get('name')}' missing purpose")

        # Related links validation
        related = data.get('related', [])
        for link in related:
            if not link.startswith('[[') or not link.endswith(']]'):
                errors.append(f"Invalid wikilink format: {link}")

        # Callout validation
        callouts = data.get('callouts', [])
        if len(callouts) > 5:
            errors.append("Too many callouts (max 5)")

        for callout in callouts:
            if not callout.startswith('> [!'):
                errors.append(f"Invalid callout format: {callout[:30]}")

        return errors

    def validate_and_fix(self, data: dict) -> dict:
        """Validate and attempt to fix common issues"""
        # Fix missing required fields
        if 'filename' not in data or not data['filename']:
            data['filename'] = 'unknown'

        # Fix tags
        if 'tags' not in data or len(data.get('tags', [])) < 2:
            data['tags'] = ['#documentation', '#auto-generated']

        # Fix tags format
        fixed_tags = []
        for tag in data.get('tags', []):
            tag = tag.strip().lower()
            if not tag.startswith('#'):
                tag = f"#{tag}"
            tag = tag.replace(' ', '-')
            fixed_tags.append(tag)
        data['tags'] = list(set(fixed_tags))  # Remove duplicates

        # Fix type
        if 'type' not in data:
            data['type'] = 'code-notes'

        # Fix summary
        if 'summary' not in data or len(data.get('summary', '')) < 20:
            data['summary'] = 'Documentation summary unavailable'

        # Ensure arrays exist
        for key in ['key_functions', 'dependencies', 'related', 'callouts']:
            if key not in data:
                data[key] = []

        return data
```

---

### 4. MarkdownFormatter (`core/markdown_formatter.py`)

**Purpose:** Convert validated JSON to Obsidian markdown

```python
from datetime import datetime
from typing import Optional
from .models import RALFDocument

class MarkdownFormatter:
    """
    Box: Markdown Formatter

    Input: Validated JSON dictionary
    Output: Formatted Obsidian markdown string
    Responsibility: Deterministic markdown generation
    """

    def format(self, data: dict) -> str:
        """Convert JSON to Obsidian markdown"""
        sections = [
            self._format_frontmatter(data),
            self._format_header(data),
            self._format_summary(data),
            self._format_details(data),
            self._format_key_functions(data),
            self._format_usage(data),
            self._format_code_summary(data),
            self._format_dependencies(data),
            self._format_dependency_graph(data),
            self._format_security_risks(data),
            self._format_performance_notes(data),
            self._format_related(data),
            self._format_callouts(data),
        ]

        # Filter out None/empty sections
        content = '\n\n'.join(s for s in sections if s)

        return content.strip() + '\n'

    def _format_frontmatter(self, data: dict) -> str:
        """Generate YAML frontmatter"""
        date = datetime.now().strftime("%Y-%m-%d")
        tags = ', '.join(data.get('tags', ['#documentation']))
        doc_type = data.get('type', 'code-notes')

        return f"""---
tags: {tags}
created: {date}
type: {doc_type}
---"""

    def _format_header(self, data: dict) -> str:
        """Generate H1 header"""
        return f"# {data.get('filename', 'Untitled')}"

    def _format_summary(self, data: dict) -> str:
        """Generate Summary section"""
        summary = data.get('summary', '')
        if not summary:
            return None

        return f"""## Summary

{summary}"""

    def _format_details(self, data: dict) -> str:
        """Generate Details section"""
        details = data.get('details', '')
        if not details:
            return None

        return f"""## Details

{details}"""

    def _format_key_functions(self, data: dict) -> str:
        """Generate Key Functions section"""
        functions = data.get('key_functions', [])
        if not functions:
            return None

        content = "## Key Functions\n\n"

        for func in functions:
            name = func.get('name', 'unknown')
            purpose = func.get('purpose', 'No description')
            signature = func.get('signature', '')
            returns = func.get('returns', '')

            content += f"### `{name}`\n\n"
            content += f"{purpose}\n\n"

            if signature:
                content += f"**Signature:** `{signature}`\n\n"

            if returns:
                content += f"**Returns:** {returns}\n\n"

        return content.strip()

    def _format_usage(self, data: dict) -> str:
        """Generate Usage section"""
        usage = data.get('usage', '')
        if not usage:
            return None

        return f"""## Usage

{usage}"""

    def _format_code_summary(self, data: dict) -> str:
        """Generate code summary section"""
        code = data.get('code_summary', '')
        if not code:
            return None

        # Code should already be in ``` blocks
        return f"""## Code Summary

{code}"""

    def _format_dependencies(self, data: dict) -> str:
        """Generate Dependencies section"""
        deps = data.get('dependencies', [])
        if not deps:
            return None

        deps_list = ', '.join(f"`{dep}`" for dep in deps)
        return f"""## Dependencies

{deps_list}"""

    def _format_dependency_graph(self, data: dict) -> str:
        """Generate Dependency Graph section"""
        graph = data.get('dependency_graph', '')
        if not graph:
            return None

        return f"""## Dependency Graph

{graph}"""

    def _format_security_risks(self, data: dict) -> str:
        """Generate Security Risks section"""
        risks = data.get('security_risks', '')
        if not risks:
            return None

        return f"""## Security Risks

{risks}"""

    def _format_performance_notes(self, data: dict) -> str:
        """Generate Performance Notes section"""
        notes = data.get('performance_notes', '')
        if not notes:
            return None

        return f"""## Performance

{notes}"""

    def _format_related(self, data: dict) -> str:
        """Generate Related section"""
        related = data.get('related', [])
        if not related:
            return None

        links = '\n'.join(f"- {link}" for link in related)
        return f"""## Related

{links}"""

    def _format_callouts(self, data: dict) -> str:
        """Generate callouts"""
        callouts = data.get('callouts', [])
        if not callouts:
            return None

        return '\n\n'.join(callouts)
```

---

### 5. DocumentPipeline (`core/document_pipeline.py`)

**Purpose:** Orchestrate the complete generation flow

```python
from typing import Optional
from pathlib import Path
from .models import GenerationContext, RALFDocument
from .json_generator import JSONGenerator
from .json_extractor import JSONExtractor
from .json_validator import JSONValidator
from .markdown_formatter import MarkdownFormatter
from .cache_manager import CacheManager

class DocumentPipeline:
    """
    Box: Document Pipeline

    Input: File path
    Output: Formatted Obsidian markdown
    Responsibility: Orchestrate generation → extraction → validation → formatting
    """

    def __init__(self,
                 json_generator: JSONGenerator,
                 json_extractor: JSONExtractor,
                 json_validator: JSONValidator,
                 markdown_formatter: MarkdownFormatter,
                 cache_manager: Optional[CacheManager] = None):
        self.generator = json_generator
        self.extractor = json_extractor
        self.validator = json_validator
        self.formatter = markdown_formatter
        self.cache = cache_manager

    def generate_document(self, file_path: Path) -> tuple[str, dict]:
        """
        Generate Obsidian document for file.

        Returns:
            (markdown_content, metadata)
        """
        filename = file_path.stem

        # Check cache
        if self.cache:
            cached = self.cache.get_cached_result(str(file_path), 'unified')
            if cached:
                return (cached, {'cached': True})

        # 1. Read file
        content = file_path.read_text(encoding='utf-8')

        # 2. Generate JSON (single LLM call!)
        context = GenerationContext(
            filename=filename,
            content=content,
            file_path=str(file_path)
        )
        raw_json = self.generator.generate(context)

        # 3. Extract JSON
        parsed, error = self.extractor.extract(raw_json)
        if not parsed:
            parsed = self.extractor.extract_or_fallback(raw_json, filename)

        # 4. Validate and fix
        is_valid, errors = self.validator.validate(parsed)
        if not is_valid:
            parsed = self.validator.validate_and_fix(parsed)

        # 5. Format markdown
        markdown = self.formatter.format(parsed)

        # 6. Cache result
        if self.cache:
            self.cache.cache_result(str(file_path), 'unified', markdown)

        metadata = {
            'cached': False,
            'valid': is_valid,
            'errors': errors if not is_valid else []
        }

        return (markdown, metadata)
```

---

### 6. Models (`core/models.py`)

```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class GenerationContext:
    """Context for document generation"""
    filename: str
    content: str
    file_path: str
    metadata: dict = field(default_factory=dict)

@dataclass
class KeyFunction:
    """Function/class documentation"""
    name: str
    purpose: str
    signature: Optional[str] = None
    returns: Optional[str] = None

@dataclass
class RALFDocument:
    """Complete RALF documentation structure"""
    filename: str
    tags: List[str]
    type: str
    summary: str
    details: Optional[str] = None
    key_functions: List[KeyFunction] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    usage: Optional[str] = None
    related: List[str] = field(default_factory=list)
    callouts: List[str] = field(default_factory=list)
    code_summary: Optional[str] = None
    security_risks: Optional[str] = None
    performance_notes: Optional[str] = None
    doc_type_confidence: Optional[float] = None
    dependency_graph: Optional[str] = None
    created: datetime = field(default_factory=datetime.now)
```

---

## Migration Strategy

### Phase 1: Parallel Implementation (Week 1)
- ✅ Create new modules alongside existing code
- ✅ Implement core pipeline components
- ✅ Add comprehensive tests
- ✅ Keep existing generators working

### Phase 2: Integration (Week 2)
- ✅ Add CLI with Typer
- ✅ Integrate Rich TUI
- ✅ Connect cache manager
- ✅ Add migration command to convert between modes

### Phase 3: Testing & Validation (Week 3)
- ✅ Compare outputs (old vs new)
- ✅ Performance benchmarking
- ✅ Fix edge cases
- ✅ User testing

### Phase 4: Cutover (Week 4)
- ✅ Make new pipeline default
- ✅ Archive old generators
- ✅ Update documentation
- ✅ Announce changes

---

## Next Steps

1. **Implement TUI** → See `03-tui-implementation.md`
2. **Error handling strategy** → See `04-error-handling-strategy.md`
3. **Testing plan** → See `05-testing-strategy.md`
4. **Performance optimization** → See `06-performance-optimization.md`

---

## Summary

This refactoring transforms a complex 9-generator system into a simple 4-component pipeline:

1. **JSONGenerator** - Single LLM call
2. **JSONExtractor** - Parse response
3. **JSONValidator** - Validate structure
4. **MarkdownFormatter** - Format output

**Benefits:**
- ✅ 9x faster (1 call vs 9)
- ✅ 90% less code
- ✅ Easier to maintain
- ✅ Better UX (TUI)
- ✅ Keeps excellent caching
