from .section_generator import SectionGenerator, GenerationContext
from prompts import RELATED_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class RelatedGenerator(SectionGenerator):
    """
    Box: Related generator

    Input: GenerationContext
    Output: Cleaned, validated section text
    Responsibility: Generate the Related section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=RELATED_PROMPT,
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        num_links = self._get_dynamic_count(context.file_size, 2, 30, 10000)
        return self.prompt_template.format(
            processed_content=context.content,
            num_links=num_links
        )

    def _get_dynamic_count(self, file_size: int, min_count: int, max_count: int, max_count_file_size: int) -> int:
        """Calculates the number of tags/links based on file size."""
        if file_size >= max_count_file_size:
            return max_count
        scale_factor = file_size / max_count_file_size
        return int(min_count + (max_count - min_count) * scale_factor)
