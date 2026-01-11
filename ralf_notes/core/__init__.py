"""
RALF Note V2 - Core Components

Simplified unified structured text architecture
"""

from .models import GenerationContext, KeyFunction, RALFDocument, StructuredTextGeneratorConfig
from .structured_text_generator import StructuredTextGenerator
from .text_parser import TextParser
from .note_formatter import NoteFormatter
from .document_pipeline import DocumentPipeline
from .file_processor import FileProcessor

__all__ = [
    'GenerationContext',
    'KeyFunction',
    'RALFDocument',
    'StructuredTextGeneratorConfig',
    'StructuredTextGenerator',
    'TextParser',
    'NoteFormatter',
    'DocumentPipeline',
    'FileProcessor',
]
