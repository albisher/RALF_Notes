# Programming Style Guide - Boxes + OOP + DI

**Author:** RALF Notes Development Team
**Date:** 2026-01-10
**Purpose:** Canonical reference for the project's programming methodology

---

## 🎯 Core Philosophy

This project follows a strict architectural pattern combining:

1. **Boxes Methodology** - Every component is a "box" with clear inputs, outputs, and responsibilities
2. **Object-Oriented Programming** - Classes encapsulate behavior with clear interfaces
3. **Dependency Injection** - All dependencies passed via constructor, never created internally
4. **Type Safety** - Complete type hints on all functions and fields
5. **Dataclasses** - For all data structures and models

**Principle:** Code should be self-documenting, testable, and maintainable through clear architectural patterns.

---

## 📦 The "Box" Pattern

Every class must define itself as a "Box" with three elements:

### Box Documentation Template

```python
"""
Box: [Component Name]

Input: [What data/objects this box receives]
Output: [What data/objects this box produces]
Responsibility: [Single clear responsibility - what does it do?]
"""
```

### Example

```python
"""
Box: Document Pipeline

Input: File path
Output: Formatted Obsidian markdown
Responsibility: Orchestrate generation → extraction → validation → formatting
"""

class DocumentPipeline:
    def __init__(self,
                 structured_text_generator: StructuredTextGenerator,
                 text_parser: TextParser,
                 note_formatter: NoteFormatter):
        """
        Initialize pipeline with all components.

        Args:
            structured_text_generator: Component for LLM generation
            text_parser: Component for parsing structured text
            note_formatter: Component for markdown formatting
        """
        self.generator = structured_text_generator
        self.parser = text_parser
        self.formatter = note_formatter

    def generate_document(self, file_path: Path) -> Tuple[str, Dict[str, Any]]:
        """
        Generate Obsidian document for file.

        Args:
            file_path: Path to source file

        Returns:
            Tuple of (markdown_content, metadata)
        """
        # Implementation
```

---

## 🏗️ Object-Oriented Programming Rules

### 1. Single Responsibility Principle

**Rule:** Each class does ONE thing and does it well.

❌ **Bad:**
```python
class DocumentManager:
    def generate_document(self, file_path):
        # Generates document

    def parse_json(self, text):
        # Parses JSON

    def format_markdown(self, data):
        # Formats markdown

    # Too many responsibilities!
```

✅ **Good:**
```python
class DocumentPipeline:
    """Orchestrates document generation flow."""

class TextParser:
    """Extracts and parses structured text."""

class NoteFormatter:
    """Formats data as markdown."""
```

### 2. Composition Over Inheritance

**Rule:** Prefer composing objects over deep inheritance hierarchies.

❌ **Bad:**
```python
class BaseGenerator:
    pass

class AdvancedGenerator(BaseGenerator):
    pass

class SuperAdvancedGenerator(AdvancedGenerator):
    pass  # Deep hierarchy!
```

✅ **Good:**
```python
class DocumentPipeline:
    def __init__(self,
                 generator: StructuredTextGenerator,
                 parser: TextParser,
                 formatter: NoteFormatter):
        self.generator = generator      # Composed
        self.parser = parser            # Composed
        self.formatter = formatter      # Composed
```

### 3. Clear Public Interfaces

**Rule:** Public methods have clear contracts. Private methods start with `_`.

```python
class TextParser:
    # Public interface
    def parse(self, raw_text: str, filename: str) -> Dict[str, Any]:
        """Parse text into structured data."""
        sections = self._split_into_sections(raw_text)
        return self._build_parsed_data(sections, filename)

    # Private implementation details
    def _split_into_sections(self, text: str) -> Dict[str, str]:
        """Internal: split text into sections."""
        ...

    def _build_parsed_data(self, sections: Dict[str, str], filename: str) -> Dict[str, Any]:
        """Internal: build final data structure."""
        ...
```

---

## 💉 Dependency Injection Rules

### Core Principle

**NEVER create dependencies inside a class. ALWAYS inject them.**

### Pattern

❌ **Bad - Tight Coupling:**
```python
class DocumentPipeline:
    def __init__(self):
        # Creates its own dependencies - BAD!
        self.client = Client()
        self.generator = StructuredTextGenerator(self.client)
        self.parser = TextParser()
```

✅ **Good - Dependency Injection:**
```python
class DocumentPipeline:
    def __init__(self,
                 generator: StructuredTextGenerator,    # Injected
                 parser: TextParser,          # Injected
                 formatter: NoteFormatter):   # Injected
        """All dependencies passed in constructor."""
        self.generator = generator
        self.parser = parser
        self.formatter = formatter
```

### Benefits

1. **Testability:** Easy to inject mocks for testing
2. **Flexibility:** Easy to swap implementations
3. **Clarity:** Dependencies are explicit and visible
4. **No Hidden Coupling:** All dependencies declared upfront

### Example: Building the Pipeline

```python
# Good: Dependencies created at composition root (main/CLI)
def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    """Build the document generation pipeline."""
    # Create dependencies
    client = Client(host=config_manager.get("ollama_host"))

    gen_config = StructuredTextGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature")
    )

    generator = StructuredTextGenerator(client, gen_config)
    parser = TextParser()
    formatter = NoteFormatter()

    # Inject all dependencies
    return DocumentPipeline(generator, parser, formatter)
```

---

## 📊 Dataclasses for Models

### Rule: All Data Structures Use @dataclass

**Use dataclasses for:**
- Configuration objects
- Data transfer objects (DTOs)
- Domain models
- Context objects
- Result objects

### Pattern

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class GenerationContext:
    """
    Box: Generation Context

    Input: File information
    Output: Context for generation
    Responsibility: Hold file data and metadata for processing
    """
    # Required fields
    filename: str
    content: str
    file_path: str

    # Optional fields with defaults
    metadata: Dict[str, Any] = field(default_factory=dict)
    created: datetime = field(default_factory=datetime.now)

@dataclass
class ProcessingResult:
    """Results from file processing."""
    total: int
    success: int
    failed: int
    errors: List[str] = field(default_factory=list)
    duration: float = 0.0
```

### Dataclass Rules

1. **Type all fields** - Every field must have a type hint
2. **Use field(default_factory=...)** - For mutable defaults (lists, dicts)
3. **Document the class** - Use Box pattern docstring
4. **Immutable when possible** - Use `frozen=True` for immutable data
5. **No business logic** - Dataclasses are for data, not behavior

❌ **Bad:**
```python
@dataclass
class User:
    name: str

    def validate_name(self):  # Business logic in dataclass!
        if len(self.name) < 3:
            raise ValueError("Name too short")
```

✅ **Good:**
```python
@dataclass
class User:
    """User data model."""
    name: str
    email: str

class UserValidator:
    """
    Box: User Validator

    Input: User object
    Output: Validation result
    Responsibility: Validate user data
    """
    def validate(self, user: User) -> Tuple[bool, List[str]]:
        errors = []
        if len(user.name) < 3:
            errors.append("Name too short")
        return (len(errors) == 0, errors)
```

---

## 🔤 Type Hints Rules

### Rule: Type EVERYTHING

**Required type hints:**
1. All function parameters
2. All function return values
3. All dataclass fields
4. All class attributes (when not obvious)

### Pattern

```python
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path

class FileProcessor:
    """
    Box: File Processor

    Input: Paths, target directory, options
    Output: Processing results
    Responsibility: Batch process files with statistics
    """

    def __init__(self, pipeline: DocumentPipeline):
        """Initialize with pipeline."""
        self.pipeline: DocumentPipeline = pipeline

    def process_paths(
                      self,
                      source_paths: List[Path],
                      target_dir: Path,
                      dry_run: bool = False,
                      overwrite: bool = False) -> Dict[str, Any]:
        """
        Process multiple source paths.

        Args:
            source_paths: List of paths to process
            target_dir: Output directory
            dry_run: If True, don't write files
            overwrite: If True, replace existing files

        Returns:
            Dictionary with processing statistics
        """
        results: Dict[str, Any] = {
            'total': 0,
            'success': 0,
            'failed': 0
        }

        for path in source_paths:
            markdown, metadata = self._process_file(path)
            # ...

        return results

    def _process_file(self, path: Path) -> Tuple[str, Dict[str, Any]]:
        """
        Process single file.

        Args:
            path: File to process

        Returns:
            Tuple of (markdown content, metadata dict)
        """
        # Implementation
```

### Common Types

```python
from typing import (
    List,           # List[str], List[int]
    Dict,           # Dict[str, Any], Dict[str, int]
    Optional,       # Optional[str] = str | None
    Tuple,          # Tuple[str, int]
    Any,            # Any type (use sparingly)
    Union,          # Union[str, int]
    Callable,       # Callable[[int], str]
)
from pathlib import Path  # Always use Path, not str for file paths
```

---

## 📝 Documentation Standards

### Module Docstring

```python
"""
Box: [Module Name]

Responsibility: [What this module provides]
"""
```

### Class Docstring

```python
class ClassName:
    """
    Box: [Component Name]

    Input: [What it receives]
    Output: [What it produces]
    Responsibility: [What it does]
    """
```

### Method Docstring

```python
def method_name(self, param: str) -> bool:
    """
    Brief description of what method does.

    Args:
        param: Description of parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param is invalid
    """
```

---

## 🏛️ Project Structure

### Directory Organization

```
project/
├── project_name/           # Main package
│   ├── __init__.py
│   ├── cli.py             # CLI entry point
│   ├── config_manager.py  # Configuration
│   │
│   ├── core/              # Core business logic
│   │   ├── __init__.py
│   │   ├── models.py      # All dataclasses
│   │   ├── schema.py      # Schemas and prompts
│   │   ├── component_a.py # Each component in own file
│   │   ├── component_b.py
│   │   └── pipeline.py    # Orchestration
│   │
│   ├── tui/               # Terminal UI
│   │   ├── __init__.py
│   │   ├── console.py
│   │   └── progress.py
│   │
│   └── utils/             # Utilities
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                 # Tests mirror structure
│   ├── test_core/
│   └── test_tui/
│
├── docs/                  # Documentation
├── roadmap/              # Planning documents
└── feedback/             # Code reviews
```

### File Organization Within Modules

```python
"""
Box: Module Name

Responsibility: Brief description
"""

# 1. Standard library imports
import json
from pathlib import Path
from typing import Dict, Any, Optional

# 2. Third-party imports
from ollama import Client
from rich.console import Console

# 3. Local imports
from .models import GenerationContext
from .schema import UNIFIED_SYSTEM_PROMPT
from ..config_manager import ConfigManager

# 4. Constants
DEFAULT_TIMEOUT = 120
MAX_RETRIES = 3

# 5. Classes
class ComponentName:
    """Box documentation."""
    pass

# 6. Functions (if any)
def helper_function():
    """Helper function."""
    pass
```

---

## ✅ Code Quality Checklist

Before committing code, verify:

### Architecture
- [ ] Class has Box docstring (Input/Output/Responsibility)
- [ ] Single Responsibility Principle followed
- [ ] All dependencies injected via constructor
- [ ] No dependencies created inside class

### Type Safety
- [ ] All parameters have type hints
- [ ] All return values have type hints
- [ ] All dataclass fields typed
- [ ] No bare `dict` or `list` (use `Dict[str, Any]`, `List[str]`)

### Documentation
- [ ] Class has clear docstring
- [ ] Public methods have docstrings
- [ ] Args and Returns documented
- [ ] Raises documented (if applicable)

### Code Quality
- [ ] No hardcoded values (use config or constants)
- [ ] Error handling present
- [ ] No bare `except:` clauses
- [ ] Private methods start with `_`
- [ ] Meaningful variable names

### Testing
- [ ] Component can be tested in isolation
- [ ] Dependencies can be mocked
- [ ] No hidden coupling

---

## 🎨 Complete Example

Here's a complete example following all rules:

```python
"""
Box: Document Generator

Responsibility: Generate documentation from source code files
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from ollama import Client


# ============================================================================ 
# MODELS (Dataclasses)
# ============================================================================ 

@dataclass
class GeneratorConfig:
    """
    Box: Generator Configuration

    Responsibility: Hold configuration for document generation
    """
    model_name: str = 'ministral-3:3b'
    temperature: float = 0.1
    num_ctx: int = 10000
    max_content_length: int = 8000


@dataclass
class GenerationContext:
    """
    Box: Generation Context

    Input: File information
    Output: Context for generation
    Responsibility: Hold file data and metadata for processing
    """
    # Required fields
    filename: str
    content: str
    file_path: str

    # Optional fields with defaults
    metadata: Dict[str, Any] = field(default_factory=dict)
    created: datetime = field(default_factory=datetime.now)

@dataclass
class GenerationResult:
    """
    Box: Generation Result

    Responsibility: Hold generation results and metadata
    """
    markdown: str
    valid: bool
    errors: List[str] = field(default_factory=list)


# ============================================================================ 
# COMPONENTS (Classes with DI)
# ============================================================================ 

class StructuredTextGenerator:
    """
    Box: Structured Text Generator

    Input: GenerationContext
    Output: Raw structured text from LLM
    Responsibility: Generate structured analysis via LLM
    """

    def __init__(self,
                 ollama_client: Client,
                 config: GeneratorConfig):
        """
        Initialize generator.

        Args:
            ollama_client: Ollama client for LLM calls
            config: Generator configuration
        """
        self.client: Client = ollama_client
        self.config: GeneratorConfig = config

    def generate(self, context: GenerationContext) -> str:
        """
        Generate documentation text.

        Args:
            context: Generation context with file data

        Returns:
            Raw text from LLM

        Raises:
            ValueError: If context is invalid
        """
        if not context.content:
            raise ValueError("Context content cannot be empty")

        processed_content = self._prepare_content(context.content)

        response = self.client.generate(
            model=self.config.model_name,
            prompt=f"File: {context.filename}\nContent:\n{processed_content}",
            options={
                "num_ctx": self.config.num_ctx,
                "temperature": self.config.temperature
            }
        )

        return response['response']

    def _prepare_content(self, content: str) -> str:
        """
        Prepare content for LLM (private helper).

        Args:
            content: Raw file content

        Returns:
            Processed content
        """
        return content[:self.config.max_content_length]


class TextParser:
    """
    Box: Text Parser

    Input: Raw LLM text, filename
    Output: Parsed dictionary
    Responsibility: Parse structured text into data
    """

    def parse(self, raw_text: str, filename: str) -> Dict[str, Any]:
        """
        Parse text into structured data.

        Args:
            raw_text: Raw text from LLM
            filename: Name of the file being processed

        Returns:
            Parsed data dictionary
        """
        # Implementation
        return {
            "filename": filename,
            "summary": self._extract_summary(raw_text),
            "tags": self._extract_tags(raw_text)
        }

    def _extract_summary(self, text: str) -> str:
        """Extract summary section."""
        # Implementation
        return "Summary"

    def _extract_tags(self, text: str) -> List[str]:
        """Extract tags."""
        # Implementation
        return ["#tag1", "#tag2"]


class NoteFormatter:
    """
    Box: Note Formatter

    Input: Parsed dictionary
    Output: Formatted markdown string
    Responsibility: Format data as Obsidian markdown
    """

    def format(self, data: Dict[str, Any]) -> str:
        """
        Format data as markdown.

        Args:
            data: Parsed data dictionary

        Returns:
            Formatted markdown string
        """
        sections = [
            self._format_frontmatter(data),
            self._format_summary(data)
        ]

        return '\n\n'.join(s for s in sections if s)

    def _format_frontmatter(self, data: Dict[str, Any]) -> str:
        """Format YAML frontmatter."""
        tags = ', '.join(data.get('tags', []))
        return f"---\ntags: {tags}\n---"

    def _format_summary(self, data: Dict[str, Any]) -> str:
        """Format summary section."""
        summary = data.get('summary', '')
        if not summary:
            return ""
        return f"## Summary\n\n{summary}"


class DocumentPipeline:
    """
    Box: Document Pipeline

    Input: File path
    Output: GenerationResult
    Responsibility: Orchestrate generation → parsing → formatting
    """

    def __init__(self,
                 generator: StructuredTextGenerator,
                 parser: TextParser,
                 formatter: NoteFormatter):
        """
        Initialize pipeline.

        Args:
            generator: Text generation component
            parser: Text parsing component
            formatter: Markdown formatting component
        """
        self.generator: StructuredTextGenerator = generator
        self.parser: TextParser = parser
        self.formatter: NoteFormatter = formatter

    def generate_document(self, file_path: Path) -> GenerationResult:
        """
        Generate complete documentation.

        Args:
            file_path: Path to source file

        Returns:
            Generation result with markdown and metadata
        """
        try:
            # Read file
            content = file_path.read_text(encoding='utf-8')

            # Generate
            context = GenerationContext(
                filename=file_path.stem,
                content=content,
                file_path=str(file_path)
            )
            raw_text = self.generator.generate(context)

            # Parse
            parsed_data = self.parser.parse(raw_text, context.filename) # Pass filename to parser

            # Format
            markdown = self.formatter.format(parsed_data)

            return GenerationResult(
                markdown=markdown,
                valid=True,
                errors=[]
            )

        except Exception as e:
            return GenerationResult(
                markdown=f"# Error\n\nGeneration failed: {e}",
                valid=False,
                errors=[str(e)]
            )


# ============================================================================ 
# COMPOSITION ROOT (Where DI happens)
# ============================================================================ 

def build_pipeline(config: GeneratorConfig) -> DocumentPipeline:
    """
    Build document pipeline with all dependencies.

    This is the "composition root" where we create all components
    and wire them together with dependency injection.

    Args:
        config: Configuration for the pipeline

    Returns:
        Fully configured DocumentPipeline
    """
    # Create dependencies
    client = Client(host='http://127.0.0.1:11434')
    generator = StructuredTextGenerator(client, config)
    parser = TextParser()
    formatter = NoteFormatter()

    # Inject dependencies into pipeline
    return DocumentPipeline(generator, parser, formatter)


# ============================================================================ 
# USAGE EXAMPLE
# ============================================================================ 

if __name__ == '__main__':
    # Configure
    config = GeneratorConfig(
        model_name='ministral-3:3b',
        temperature=0.1
    )

    # Build pipeline (DI happens here)
    pipeline = build_pipeline(config)

    # Use pipeline
    result = pipeline.generate_document(Path('example.py'))

    if result.valid:
        print(result.markdown)
    else:
        print(f"Errors: {result.errors}")
```