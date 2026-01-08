from .base_section_generator import BaseSectionGenerator, GenerationContext, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import TAGS_PROMPT

class TagsGenerator(BaseSectionGenerator):
    """
    Box: Tags generator

    Input: GenerationContext
    Output: Cleaned, validated tags text
    Responsibility: Generate the tags section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=TAGS_PROMPT,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        num_tags = self._get_dynamic_count(context.file_size, 5, 20, 10000)
        return self.prompt_template.format(
            processed_content=context.content,
            num_tags=num_tags
        )

    def _get_dynamic_count(self, file_size: int, min_count: int, max_count: int, max_count_file_size: int) -> int:
        """Calculates the number of tags/links based on file size."""
        if file_size >= max_count_file_size:
            return max_count
        scale_factor = file_size / max_count_file_size
        return int(min_count + (max_count - min_count) * scale_factor)
