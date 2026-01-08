from .section_generator import SectionGenerator, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import SECURITY_RISKS_PROMPT

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
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
