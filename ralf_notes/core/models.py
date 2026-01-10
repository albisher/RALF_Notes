"""
Box: Data Models

Responsibility: Define data structures for V2 architecture
"""

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
    filename: str
    content: str
    file_path: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KeyFunction:
    """
    Box: Key Function Model

    Responsibility: Represent a function/class in documentation
    """
    name: str
    purpose: str
    signature: Optional[str] = None
    returns: Optional[str] = None


@dataclass
class RALFDocument:
    """
    Box: RALF Document Model

    Responsibility: Complete documentation structure
    """
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


@dataclass
class StructuredTextGeneratorConfig:
    """
    Box: Structured Text Generator Configuration

    Responsibility: Configuration for LLM generation
    """
    model_name: str = 'ministral-3:3b'
    num_ctx: int = 10000
    temperature: float = 0.1
    chunk_size: int = 100000
    max_content_length: int = 8000
    max_chunk_summary_length: int = 4000
    ollama_host: str = 'http://127.0.0.1:11434'
