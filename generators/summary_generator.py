from typing import Optional
from .base_section_generator import BaseSectionGenerator, GenerationContext
from prompts import SUMMARY_PROMPT, RALF_ANALYST_PERSONA, TASK_ANALYZE_AND_GENERATE, OUTPUT_FRONTMATTER, OUTPUT_DOCUMENT_STRUCTURE, CONTENT_INSTRUCTIONS, CRUCIAL_RULES # Assuming these are defined in prompts.py

# Construct a system prompt suitable for a general section generator
# This can be made more specific per generator if needed
SYSTEM_PROMPT_FOR_GENERATORS = f"{RALF_ANALYST_PERSONA}\n\n{TASK_ANALYZE_AND_GENERATE}\n\n**Output Requirements:**\n{OUTPUT_FRONTMATTER}\n{OUTPUT_DOCUMENT_STRUCTURE}\n{CONTENT_INSTRUCTIONS}\n{CRUCIAL_RULES}\n\nBegin."


class SummaryGenerator(BaseSectionGenerator):
    """
    Box: Summary generator

    Input: GenerationContext
    Output: Cleaned, validated summary text
    Responsibility: Generate the summary section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=SUMMARY_PROMPT,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS # Use the constructed system prompt
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        summary_length = self._get_summary_length(context.file_size)
        return self.prompt_template.format(
            processed_content=context.content,
            summary_length=summary_length
        )

    def _get_summary_length(self, file_size: int, max_size: int = 20000) -> int:
        """Calculates a desired summary length in sentences based on file size."""
        if file_size > max_size:
            return 8 # Max sentences
        return int(2 + 6 * (file_size / max_size))