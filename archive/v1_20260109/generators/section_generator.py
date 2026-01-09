from .base_section_generator import BaseSectionGenerator, GenerationContext
from typing import Optional

class SectionGenerator(BaseSectionGenerator):
    """
    Box: Generic Section generator

    Input: GenerationContext, prompt_template, optional model_name
    Output: Cleaned, validated section text
    Responsibility: Generate a generic section of a document.
    """

    def __init__(self, ollama_client, validator, cleaner, prompt_template: str, model_name: Optional[str] = None):
        super().__init__(
            ollama_client=ollama_client,
            validator=validator,
            cleaner=cleaner,
            prompt_template=prompt_template,
            system_prompt=SYSTEM_PROMPT_FOR_GENERATORS
        )
        self._model_name = model_name

    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        return self.prompt_template.format(processed_content=context.content)

    def _get_model(self) -> str:
        """Get model name for this section."""
        if self._model_name:
            return self._model_name
        return super()._get_model()
