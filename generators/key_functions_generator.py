from .section_generator import SectionGenerator, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import KEY_FUNCTIONS_PROMPT

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
            prompt_template=KEY_FUNCTIONS_PROMPT,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
