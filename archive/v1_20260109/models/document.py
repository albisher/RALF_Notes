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
