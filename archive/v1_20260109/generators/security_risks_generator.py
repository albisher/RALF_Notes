from .section_generator import SectionGenerator, GenerationContext
from prompts import SECURITY_RISKS_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

class SecurityRisksGenerator(SectionGenerator):
    """
    Box: Security Risks generator

    Input: GenerationContext
    Output: Cleaned, validated section text
    Responsibility: Generate the Security Risks section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=SECURITY_RISKS_PROMPT,
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
