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
from ollama import OllamaError


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
                 markdown_formatter: MarkdownFormatter):
        """
        Initialize pipeline with all components.

        Args:
            json_generator: Component for LLM generation
            text_parser: Component for parsing structured text
            markdown_formatter: Component for markdown formatting
        """
        self.generator = structured_text_generator
        self.parser = text_parser
        self.formatter = markdown_formatter

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

        try:
            # 1. Read file
            content = file_path.read_text(encoding='utf-8')

            # 2. Generate structured text (single LLM call!)
            context = GenerationContext(
                filename=filename,
                content=content,
                file_path=str(file_path)
            )
            raw_text = self.generator.generate(context)

            # 3. Parse text
            parsed_data = self.parser.parse_or_fallback(raw_text, filename)
            
            # 4. Format markdown
            markdown = self.formatter.format(parsed_data)

            is_valid = "#parsing-failed" not in parsed_data.get("tags", [])

            metadata = {
                'cached': False,
                'valid': is_valid,
                'errors': [] if is_valid else [parsed_data.get("details", "")],
                'data': parsed_data
            }

            return (markdown, metadata)

        except OllamaError as oe:
            error_message = f"Ollama API Error: {oe}"
            error_markdown = f"""# {filename}

> [!ERROR] Generation Failed: Ollama API Error
> Error: {error_message}

**File:** {file_path}

Manual review required."""
            metadata = {
                'cached': False,
                'valid': False,
                'errors': [error_message],
                'json_data': {}
            }
            return (error_markdown, metadata)
        except Exception as e:
            # Error handling
            import traceback
            error_message = f"Unexpected Error during document generation: {e}\n{traceback.format_exc()}"
            error_markdown = f"""# {filename}

> [!ERROR] Generation Failed: Unexpected Error
> Error: {error_message}

**File:** {file_path}

Manual review required."""

            metadata = {
                'cached': False,
                'valid': False,
                'errors': [error_message],
                'json_data': {}
            }

            return (error_markdown, metadata)
