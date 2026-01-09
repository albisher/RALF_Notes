from .section_generator import SectionGenerator, GenerationContext
from prompts import DEPENDENCY_GRAPH_PROMPT, SYSTEM_PROMPT_FOR_GENERATORS

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
        )

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)
