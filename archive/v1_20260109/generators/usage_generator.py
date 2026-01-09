from .section_generator import SectionGenerator, GenerationContext
from prompts import USAGE_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class UsageGenerator(SectionGenerator):
    """
    Box: Usage/Examples generator

    Input: GenerationContext
    Output: Cleaned, validated section text
    Responsibility: Generate the Usage/Examples section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=USAGE_PROMPT,
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
