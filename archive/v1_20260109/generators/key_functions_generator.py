from .section_generator import SectionGenerator, GenerationContext
from prompts import KEY_FUNCTIONS_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class KeyFunctionsGenerator(SectionGenerator):
    """
    Box: Key Functions generator

    Input: GenerationContext
    Output: Cleaned, validated section text
    Responsibility: Generate the Key Functions/Classes section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=KEY_FUNCTIONS_PROMPT
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
