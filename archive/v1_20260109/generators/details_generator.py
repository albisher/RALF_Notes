from .base_section_generator import BaseSectionGenerator, GenerationContext
from prompts import DETAILS_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class DetailsGenerator(BaseSectionGenerator):
    """
    Box: Details generator

    Input: GenerationContext
    Output: Cleaned, validated details text
    Responsibility: Generate the details section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=DETAILS_PROMPT,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
