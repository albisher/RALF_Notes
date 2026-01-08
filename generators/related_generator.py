from .section_generator import SectionGenerator, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import RELATED_PROMPT

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
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
