"""
Box: Document Pipeline

Input: File path
Output: Formatted Obsidian markdown
Responsibility: Orchestrate generation → extraction → validation → formatting
"""

from pathlib import Path
from typing import Tuple, Dict, Any, Optional
from .models import GenerationContext
from .structured_text_generator import StructuredTextGenerator
from .text_parser import TextParser
from .note_formatter import NoteFormatter
from ollama._types import ResponseError
import logging # ADD THIS IMPORT

logger = logging.getLogger(__name__) # ADD THIS LINE


class DocumentPipeline:
    """
    Box: Document Pipeline

    Input: File path
    Output: (markdown_content, metadata)
    Responsibility: Orchestrate the complete generation flow
    """

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
            metadata contains: cached, valid, errors, data
        """
        filename = file_path.stem
        logger.info("Generating document for file: %s", file_path) # ADD LOGGING

        try:
            # 1. Read file
            content = file_path.read_text(encoding='utf-8')
            logger.debug("Read content for %s", filename) # ADD LOGGING

            # 2. Generate structured text (single LLM call!)
            context = GenerationContext(
                filename=filename,
                content=content,
                file_path=str(file_path)
            )
            raw_text = self.generator.generate(context) # CORRECTED LINE
            logger.debug("Generated raw text for %s", filename) # ADD LOGGING

            # 3. Parse text
            parsed_data = self.parser.parse_or_fallback(raw_text, filename)
            logger.debug("Parsed data for %s", filename) # ADD LOGGING
            
            # 4. Format markdown
            markdown = self.formatter.format(parsed_data)
            logger.debug("Formatted markdown for %s", filename) # ADD LOGGING

            is_valid = "#parsing-failed" not in parsed_data.get("tags", [])
            if not is_valid:
                logger.warning("Generated document for %s is invalid (parsing failed tag present).", filename) # ADD LOGGING

            metadata = {
                'cached': False,
                'valid': is_valid,
                'errors': [] if is_valid else [parsed_data.get("details", "")],
                'data': parsed_data
            }
            logger.info("Document generation complete for %s", filename) # ADD LOGGING

            return (markdown, metadata)

        except ResponseError as oe:
            error_message = f"Ollama API Error: {oe}"
            logger.error("Ollama API Error during generation for %s: %s", filename, error_message, exc_info=True) # ADD LOGGING
            error_markdown = f"""# {filename}

> [!ERROR] Generation Failed: Ollama API Error
> Error: {error_message}

**File:** {file_path}

Manual review required."""
            metadata = {
                'cached': False,
                'valid': False,
                'errors': [error_message],
                'data': {}
            }
            return (error_markdown, metadata)
        except Exception as e:
            # Error handling
            import traceback
            error_message = f"Unexpected Error during document generation: {e}\n{traceback.format_exc()}"
            logger.error("Unexpected Error during generation for %s: %s", filename, error_message, exc_info=True) # ADD LOGGING
            error_markdown = f"""# {filename}

> [!ERROR] Generation Failed: Unexpected Error
> Error: {error_message}

**File:** {file_path}

Manual review required."""

            metadata = {
                'cached': False,
                'valid': False,
                'errors': [error_message],
                'data': {}
            }

            return (error_markdown, metadata)
