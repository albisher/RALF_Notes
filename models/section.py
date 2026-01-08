from dataclasses import dataclass

@dataclass
class Section:
    """Represents a section of a document."""
    name: str
    content: str
