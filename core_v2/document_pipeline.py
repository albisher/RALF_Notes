"""
Box: Document Pipeline

Input: File path
Output: Formatted Obsidian markdown
Responsibility: Orchestrate generation → extraction → validation → formatting
"""

from pathlib import Path
from typing import Tuple, Dict, Any, Optional
from .models import GenerationContext
from .json_generator import JSONGenerator
from .json_extractor import JSONExtractor
from .json_validator import JSONValidator
from .markdown_formatter import MarkdownFormatter


class DocumentPipeline:
    """
    Box: Document Pipeline

    Input: File path
    Output: (markdown_content, metadata)
    Responsibility: Orchestrate the complete generation flow
    """

    def __init__(self,
                 json_generator: JSONGenerator,
                 json_extractor: JSONExtractor,
                 json_validator: JSONValidator,
                 markdown_formatter: MarkdownFormatter):
        """
        Initialize pipeline with all components.

        Args:
            json_generator: Component for LLM generation
            json_extractor: Component for JSON extraction
            json_validator: Component for validation
            markdown_formatter: Component for markdown formatting
        """
        self.generator = json_generator
        self.extractor = json_extractor
        self.validator = json_validator
        self.formatter = markdown_formatter

    def generate_document(self, file_path: Path) -> Tuple[str, Dict[str, Any]]:
        """
        Generate Obsidian document for file.

        Args:
            file_path: Path to source file

        Returns:
            Tuple of (markdown_content, metadata)
            metadata contains: cached, valid, errors, json_data
        """
        filename = file_path.stem

        try:
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
                # Use fallback
                parsed = self.extractor.extract_or_fallback(raw_json, filename)

            # 4. Validate and fix
            is_valid, errors = self.validator.validate(parsed)
            if not is_valid:
                parsed = self.validator.validate_and_fix(parsed)

            # 5. Format markdown
            markdown = self.formatter.format(parsed)

            metadata = {
                'cached': False,
                'valid': is_valid,
                'errors': errors if not is_valid else [],
                'json_data': parsed
            }

            return (markdown, metadata)

        except Exception as e:
            # Error handling
            error_markdown = f"""# {filename}

> [!ERROR] Generation Failed
> Error: {str(e)}

**File:** {file_path}

Manual review required."""

            metadata = {
                'cached': False,
                'valid': False,
                'errors': [str(e)],
                'json_data': {}
            }

            return (error_markdown, metadata)
