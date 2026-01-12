# OOP Refactoring - Boxes Methodology

## Philosophy: The Boxes Methodology

Each "box" (class or module) should be:
1. **Single Responsibility:** Does ONE thing well
2. **Known Interface:** Clear inputs and outputs
3. **Reusable:** Can be used independently
4. **Testable:** Easy to unit test
5. **Small Files:** < 300 lines per file
6. **Type-Safe:** Uses type hints

---

## Current Architecture Problems

### main.py (680 lines) - Violates Single Responsibility

Current functions doing multiple things:
- `generate_obsidian_doc()` - 142 lines doing: file I/O, token estimation, prompting, validation, cleaning, assembly
- `clean_details()` - 45 lines doing: regex processing, callout handling, markdown filtering
- `safe_generate()` - 32 lines doing: retry logic, streaming, logging

### Lack of Clear Boundaries

- Prompting logic mixed with validation
- Cleaning functions scattered throughout
- No separation between business logic and I/O
- Configuration mixed with constants

---

## Proposed OOP Architecture

### Directory Structure

```
RALF_Notes/
├── main.py                      # Entry point only (50 lines)
├── config.py                    # Configuration only
├── prompts.py                   # Prompts (unchanged)
│
├── core/
│   ├── __init__.py
│   ├── ollama_client.py         # OllamaClient box
│   ├── document_generator.py   # DocumentGenerator box
│   └── section_manager.py      # SectionManager box
│
├── models/
│   ├── __init__.py
│   ├── document.py              # Document dataclass
│   ├── section.py               # Section dataclass
│   └── generation_options.py   # GenerationOptions dataclass
│
├── validators/
│   ├── __init__.py
│   ├── base_validator.py        # BaseValidator interface
│   ├── summary_validator.py     # SummaryValidator box
│   ├── tags_validator.py        # TagsValidator box
│   └── structure_validator.py   # StructureValidator box
│
├── cleaners/
│   ├── __init__.py
│   ├── base_cleaner.py          # BaseCleaner interface
│   ├── summary_cleaner.py       # SummaryCleaner box
│   ├── tags_cleaner.py          # TagsCleaner box
│   └── details_cleaner.py       # DetailsCleaner box
│
├── generators/
│   ├── __init__.py
│   ├── base_section_generator.py  # BaseSectionGenerator
│   ├── summary_generator.py       # SummaryGenerator box
│   ├── details_generator.py       # DetailsGenerator box
│   └── tags_generator.py          # TagsGenerator box
│
├── utils/
│   ├── __init__.py
│   ├── token_estimator.py       # TokenEstimator box
│   ├── file_processor.py        # FileProcessor box
│   ├── logger_factory.py        # LoggerFactory box
│   └── retry_manager.py         # RetryManager box
│
└── cache/
    ├── __init__.py
    └── cache_manager.py         # CacheManager box
```

---

## Box Definitions

### Box 1: OllamaClient

**Responsibility:** Communicate with Ollama API

**File:** `core/ollama_client.py` (~100 lines)

```python
from typing import Optional, Dict, Any
from ollama import Client, ResponseError
from dataclasses import dataclass

@dataclass
class ModelInfo:
    name: str
    size: int
    family: str
    context_size: int

class OllamaClient:
    """
    Box: Ollama API client wrapper

    Input: host URL
    Output: API responses
    Responsibility: Manage connection to Ollama
    """

    def __init__(self, host: str = 'http://127.0.0.1:11434'):
        self.host = host
        self._client = Client(host=host)

    def generate(
        self,
        model: str,
        prompt: str,
        system: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        stream: bool = True
    ) -> str:
        """
        Generate response from Ollama.

        Input: model name, prompt, options
        Output: generated text
        """
        kwargs = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        if system:
            kwargs["system"] = system
        if options:
            kwargs["options"] = options

        if stream:
            stream_resp = self._client.generate(**kwargs)
            return "".join(chunk['response'] for chunk in stream_resp)
        else:
            return self._client.generate(**kwargs)['response']

    def list_models(self) -> Dict[str, ModelInfo]:
        """
        List available models.

        Input: none
        Output: dict of model name → ModelInfo
        """
        response = self._client.list()
        models = {}
        for model in response.get('models', []):
            models[model['name']] = ModelInfo(
                name=model['name'],
                size=model.get('size', 0),
                family=model['name'].split(':')[0],
                context_size=self._detect_context_size(model['name'])
            )
        return models

    def model_exists(self, model_name: str) -> bool:
        """Check if model is available."""
        return model_name in self.list_models()

    def _detect_context_size(self, model_name: str) -> int:
        """Detect context size for model."""
        # Logic from Enhancement 2
        try:
            show_response = self._client.show(model_name)
            # ... context detection logic
        except:
            return 8192
```

**Test:**
```python
def test_ollama_client():
    client = OllamaClient()
    assert client.model_exists('ministral-3:3b')
    models = client.list_models()
    assert 'ministral-3:3b' in models
```

---

### Box 2: Document (Data Model)

**Responsibility:** Hold document data

**File:** `models/document.py` (~50 lines)

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class DocumentMetadata:
    """Document frontmatter metadata"""
    tags: List[str]
    created: str
    doc_type: str

@dataclass
class DocumentSections:
    """Document content sections"""
    summary: str
    details: str
    key_functions: str
    usage: str
    related: str
    dependency_graph: str
    security_risks: str

@dataclass
class Document:
    """
    Box: Document data structure

    Input: metadata + sections
    Output: formatted markdown
    Responsibility: Hold and format document data
    """
    file_name: str
    metadata: DocumentMetadata
    sections: DocumentSections

    def to_markdown(self) -> str:
        """
        Convert document to Obsidian markdown.

        Input: self
        Output: formatted markdown string
        """
        md = f"""tags: {' '.join(self.metadata.tags)}
created: {self.metadata.created}
type: {self.metadata.doc_type}

---

# {self.file_name}

## Summary
```
{self.sections.summary}
```

## Details
{self.sections.details}

## Dependency Graph
```mermaid
{self.sections.dependency_graph}
```

## Key Functions/Classes
{self.sections.key_functions}

## Usage/Examples
{self.sections.usage}

## Security Risks
{self.sections.security_risks}

## Related
{self.sections.related}
"""
        return md
```

**Test:**
```python
def test_document_to_markdown():
    metadata = DocumentMetadata(
        tags=['#test', '#python'],
        created='2026-01-08',
        doc_type='code'
    )
    sections = DocumentSections(
        summary='Test summary',
        details='Test details',
        # ...
    )
    doc = Document('test', metadata, sections)
    md = doc.to_markdown()
    assert '# test' in md
    assert '#test #python' in md
```

---

### Box 3: BaseValidator (Interface)

**Responsibility:** Define validation contract

**File:** `validators/base_validator.py` (~30 lines)

```python
from abc import ABC, abstractmethod
from typing import Tuple

class BaseValidator(ABC):
    """
    Box: Validator interface

    Input: text to validate
    Output: (is_valid, error_message)
    Responsibility: Define validation contract
    """

    @abstractmethod
    def validate(self, text: str) -> Tuple[bool, str]:
        """
        Validate text.

        Returns:
            (True, "") if valid
            (False, "error message") if invalid
        """
        pass

    def __call__(self, text: str) -> bool:
        """Allow validator(text) syntax"""
        is_valid, _ = self.validate(text)
        return is_valid
```

---

### Box 4: SummaryValidator

**Responsibility:** Validate summaries

**File:** `validators/summary_validator.py` (~50 lines)

```python
from typing import Tuple
import re
from .base_validator import BaseValidator

class SummaryValidator(BaseValidator):
    """
    Box: Summary validator

    Input: summary text
    Output: (is_valid, error_message)
    Responsibility: Validate summary format
    """

    def __init__(self, max_lines: int = 20):
        self.max_lines = max_lines
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai"
        ]

    def validate(self, text: str) -> Tuple[bool, str]:
        """Validate summary text."""

        # Check for questions
        if '?' in text:
            return False, "Contains question marks"

        # Check line count
        lines = text.strip().split('\n')
        if len(lines) > self.max_lines:
            return False, f"Exceeds {self.max_lines} lines"

        # Check for multiple paragraphs
        if re.search(r'\n\s*\n', text.strip()):
            return False, "Contains multiple paragraphs"

        # Check for conversational filler
        text_lower = text.lower().strip()
        for phrase in self.conversational_starts:
            if text_lower.startswith(phrase):
                return False, f"Starts with '{phrase}'"

        return True, ""
```

**Test:**
```python
def test_summary_validator():
    validator = SummaryValidator(max_lines=5)

    valid, _ = validator.validate("This is a good summary.")
    assert valid

    valid, msg = validator.validate("Is this valid?")
    assert not valid
    assert "question" in msg
```

---

### Box 5: SummaryCleaner

**Responsibility:** Clean summary text

**File:** `cleaners/summary_cleaner.py` (~70 lines)

```python
from typing import List
import re
from .base_cleaner import BaseCleaner

class SummaryCleaner(BaseCleaner):
    """
    Box: Summary cleaner

    Input: raw summary text
    Output: cleaned summary text
    Responsibility: Remove unwanted elements from summary
    """

    def __init__(self, max_words: int = 150):
        self.max_words = max_words

    def clean(self, text: str) -> str:
        """
        Clean summary text.

        Input: raw text
        Output: cleaned text
        """
        # Remove code fences
        text = re.sub(r'```[a-zA-Z]*\n', '', text)
        text = text.replace('```', '')

        # Remove dates
        text = re.sub(r'\d{4}-\d{2}-\d{2}', '', text)

        lines = text.strip().split('\n')
        cleaned_lines = []

        for line in lines:
            stripped_line = line.strip()

            # Skip unwanted lines
            if self._should_skip_line(stripped_line):
                continue

            cleaned_lines.append(line)

        # Join and trim
        final_summary = " ".join([line.strip() for line in cleaned_lines]).strip()

        # Enforce word limit
        words = final_summary.split()
        if len(words) > self.max_words:
            final_summary = " ".join(words[:self.max_words]) + "..."

        return final_summary

    def _should_skip_line(self, line: str) -> bool:
        """Check if line should be skipped."""
        if not line:
            return True
        if line.startswith(('tags:', 'created:', 'type:', '---')):
            return True
        if re.match(r'^#+\s', line):
            return True
        if '**tags**' in line.lower():
            return True
        return False
```

---

### Box 6: SectionGenerator

**Responsibility:** Generate one section

**File:** `generators/base_section_generator.py` (~80 lines)

```python
from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

@dataclass
class GenerationContext:
    """Context for section generation"""
    content: str
    file_size: int
    options: dict

class BaseSectionGenerator(ABC):
    """
    Box: Section generator interface

    Input: content, context
    Output: generated section text
    Responsibility: Generate one document section
    """

    def __init__(
        self,
        ollama_client,
        validator,
        cleaner,
        prompt_template: str,
        system_prompt: str
    ):
        self.ollama = ollama_client
        self.validator = validator
        self.cleaner = cleaner
        self.prompt_template = prompt_template
        self.system_prompt = system_prompt

    def generate(self, context: GenerationContext) -> str:
        """
        Generate section.

        Input: generation context
        Output: cleaned, validated section text
        """
        # Format prompt
        prompt = self._format_prompt(context)

        # Generate
        raw_response = self.ollama.generate(
            model=self._get_model(),
            prompt=prompt,
            system=self.system_prompt,
            options=context.options
        )

        # Validate and regenerate if needed
        validated = self._validate_and_regenerate(raw_response, context)

        # Clean
        cleaned = self.cleaner.clean(validated)

        return cleaned

    @abstractmethod
    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        pass

    @abstractmethod
    def _get_model(self) -> str:
        """Get model name for this section."""
        pass

    def _validate_and_regenerate(
        self,
        text: str,
        context: GenerationContext,
        max_attempts: int = 3
    ) -> str:
        """Validate and retry if needed."""
        for attempt in range(max_attempts):
            is_valid, error_msg = self.validator.validate(text)
            if is_valid:
                return text

            # Regenerate with correction
            correction_prompt = self._build_correction_prompt(text, error_msg, context)
            text = self.ollama.generate(
                model=self._get_model(),
                prompt=correction_prompt,
                system=self.system_prompt,
                options=context.options
            )

        return text  # Return last attempt even if invalid
```

---

### Box 7: DocumentGenerator (Orchestrator)

**Responsibility:** Orchestrate document generation

**File:** `core/document_generator.py` (~150 lines)

```python
from typing import Dict
from pathlib import Path
from models.document import Document, DocumentMetadata, DocumentSections
from generators.base_section_generator import GenerationContext

class DocumentGenerator:
    """
    Box: Document generator orchestrator

    Input: file path
    Output: Document object
    Responsibility: Coordinate section generation
    """

    def __init__(
        self,
        ollama_client,
        section_generators: Dict[str, BaseSectionGenerator],
        token_estimator,
        file_processor
    ):
        self.ollama = ollama_client
        self.section_generators = section_generators
        self.token_estimator = token_estimator
        self.file_processor = file_processor

    def generate(self, file_path: Path) -> Document:
        """
        Generate documentation for file.

        Input: file path
        Output: Document object
        """
        # Read and validate file
        content = self.file_processor.read_file(file_path)

        # Build context
        context = self._build_context(content, file_path)

        # Generate each section
        sections = self._generate_sections(context)

        # Generate metadata
        metadata = self._generate_metadata(context)

        # Assemble document
        doc = Document(
            file_name=file_path.stem,
            metadata=metadata,
            sections=sections
        )

        return doc

    def _build_context(self, content: str, file_path: Path) -> GenerationContext:
        """Build generation context."""
        file_size = len(content)
        estimated_tokens = self.token_estimator.estimate(content)

        options = {
            "num_ctx": min(estimated_tokens + 2048, 16384),
            "temperature": 0.2,
            "keep_alive": "30m"
        }

        return GenerationContext(
            content=content,
            file_size=file_size,
            options=options
        )

    def _generate_sections(self, context: GenerationContext) -> DocumentSections:
        """Generate all sections."""
        return DocumentSections(
            summary=self.section_generators['summary'].generate(context),
            details=self.section_generators['details'].generate(context),
            key_functions=self.section_generators['key_functions'].generate(context),
            usage=self.section_generators['usage'].generate(context),
            related=self.section_generators['related'].generate(context),
            dependency_graph=self.section_generators['dependency_graph'].generate(context),
            security_risks=self.section_generators['security_risks'].generate(context)
        )

    def _generate_metadata(self, context: GenerationContext) -> DocumentMetadata:
        """Generate metadata."""
        return DocumentMetadata(
            tags=self.section_generators['tags'].generate(context).split(),
            created=datetime.now().strftime('%Y-%m-%d'),
            doc_type=self.section_generators['type'].generate(context)
        )
```

---

### Box 8: Main (Entry Point)

**Responsibility:** Wire dependencies and run

**File:** `main.py` (~50 lines)

```python
from pathlib import Path
from config import *
from core.ollama_client import OllamaClient
from core.document_generator import DocumentGenerator
from utils.file_processor import FileProcessor
from utils.token_estimator import TokenEstimator
from generators.summary_generator import SummaryGenerator
from validators.summary_validator import SummaryValidator
from cleaners.summary_cleaner import SummaryCleaner

def build_document_generator() -> DocumentGenerator:
    """
    Dependency injection: wire all boxes together.
    """
    # Core
    ollama = OllamaClient(host=OLLAMA_HOST)
    file_processor = FileProcessor()
    token_estimator = TokenEstimator()

    # Section generators
    section_generators = {
        'summary': SummaryGenerator(
            ollama_client=ollama,
            validator=SummaryValidator(),
            cleaner=SummaryCleaner(),
            prompt_template=SUMMARY_PROMPT,
            system_prompt=SYSTEM_PROMPT
        ),
        # ... other generators
    }

    # Document generator
    return DocumentGenerator(
        ollama_client=ollama,
        section_generators=section_generators,
        token_estimator=token_estimator,
        file_processor=file_processor
    )

def main():
    """Main entry point."""
    generator = build_document_generator()

    # Get files
    files = FileProcessor().get_all_files(SOURCE_PATHS)

    # Process each file
    for file_path in files:
        doc = generator.generate(Path(file_path))
        output_path = Path(TARGET_DIR) / f"{file_path.stem}.md"
        output_path.write_text(doc.to_markdown())

if __name__ == "__main__":
    main()
```

---

## Benefits of This Architecture

### 1. Testability
Each box can be tested independently:
```python
def test_summary_cleaner():
    cleaner = SummaryCleaner(max_words=10)
    raw = "```python\nThis is code\n```\nSummary here"
    cleaned = cleaner.clean(raw)
    assert "```" not in cleaned
    assert "Summary here" in cleaned
```

### 2. Reusability
Boxes can be used in other projects:
```python
# Use cleaner in different project
from cleaners.summary_cleaner import SummaryCleaner
cleaner = SummaryCleaner()
clean_text = cleaner.clean(dirty_text)
```

### 3. Maintainability
Small files (50-150 lines each) are easy to understand and modify

### 4. Extensibility
Add new section types by creating new generators:
```python
class AuthorGenerator(BaseSectionGenerator):
    def generate(self, context):
        # Extract author from git blame
        ...
```

### 5. Dependency Injection
Easy to swap implementations:
```python
# Use different cleaner
generator = SummaryGenerator(
    ollama_client=ollama,
    validator=SummaryValidator(),
    cleaner=AdvancedSummaryCleaner(),  # Different implementation
    prompt_template=SUMMARY_PROMPT,
    system_prompt=SYSTEM_PROMPT
)
```

---

## Migration Path

### Phase 1: Extract Utilities (Week 1)
1. Create `utils/token_estimator.py`
2. Create `utils/file_processor.py`
3. Create `utils/logger_factory.py`
4. Update `main.py` to use utilities

### Phase 2: Create Data Models (Week 1)
1. Create `models/document.py`
2. Create `models/section.py`
3. Update `generate_obsidian_doc()` to return Document

### Phase 3: Extract Validators (Week 2)
1. Create `validators/base_validator.py`
2. Create `validators/summary_validator.py`
3. Create remaining validators
4. Update validation logic

### Phase 4: Extract Cleaners (Week 2)
1. Create `cleaners/base_cleaner.py`
2. Create `cleaners/summary_cleaner.py`
3. Create remaining cleaners
4. Update cleaning logic

### Phase 5: Extract Generators (Week 3)
1. Create `generators/base_section_generator.py`
2. Create `generators/summary_generator.py`
3. Create remaining generators
4. Update generation logic

### Phase 6: Create Orchestrator (Week 3)
1. Create `core/document_generator.py`
2. Wire dependencies
3. Update `main.py`

### Phase 7: Testing & Cleanup (Week 4)
1. Add unit tests for each box
2. Remove old code from `main.py`
3. Update documentation
4. Performance testing

---

## Testing Strategy

### Unit Tests (Box Level)
```python
# Test each box independently
def test_summary_cleaner():
    cleaner = SummaryCleaner()
    assert cleaner.clean("```code```\nSummary") == "Summary"

def test_summary_validator():
    validator = SummaryValidator()
    assert validator.validate("Good summary.")[0] == True
    assert validator.validate("Bad summary?")[0] == False
```

### Integration Tests (Box Interactions)
```python
def test_summary_generation_pipeline():
    ollama = Mock(OllamaClient)
    validator = SummaryValidator()
    cleaner = SummaryCleaner()

    generator = SummaryGenerator(ollama, validator, cleaner, SUMMARY_PROMPT, SYSTEM_PROMPT)

    context = GenerationContext(content="test", file_size=100, options={})
    result = generator.generate(context)

    assert isinstance(result, str)
    assert len(result) > 0
```

### End-to-End Tests
```python
def test_full_document_generation():
    generator = build_document_generator()
    doc = generator.generate(Path('test_file.py'))

    assert doc.file_name == 'test_file'
    assert doc.sections.summary
    assert doc.sections.details
```

---

## Checklist

- [ ] Create directory structure
- [ ] Extract TokenEstimator box
- [ ] Extract FileProcessor box
- [ ] Create Document data model
- [ ] Create BaseValidator interface
- [ ] Create validators (Summary, Tags, etc.)
- [ ] Create BaseCleaner interface
- [ ] Create cleaners (Summary, Tags, Details)
- [ ] Create BaseSectionGenerator
- [ ] Create section generators
- [ ] Create DocumentGenerator orchestrator
- [ ] Update main.py
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Update documentation
- [ ] Remove old code
