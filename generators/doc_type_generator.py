from .section_generator import SectionGenerator, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import TYPE_PROMPT

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
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
