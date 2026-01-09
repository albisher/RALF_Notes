from .section_generator import SectionGenerator, GenerationContext
from prompts import TYPE_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class DocTypeGenerator(SectionGenerator):
    """
    Box: Document Type generator

    Input: GenerationContext
    Output: Cleaned, validated document type text
    Responsibility: Generate the document type for a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=TYPE_PROMPT,
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
