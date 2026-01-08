from .section_generator import SectionGenerator, SYSTEM_PROMPT_FOR_GENERATORS
from prompts import DEPENDENCY_GRAPH_PROMPT

class DependencyGraphGenerator(SectionGenerator):
    """
    Box: Dependency Graph generator

    Input: GenerationContext
    Output: Cleaned, validated section text
    Responsibility: Generate the Dependency Graph section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=DEPENDENCY_GRAPH_PROMPT,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
