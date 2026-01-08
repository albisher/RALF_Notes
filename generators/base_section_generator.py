from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass
import logging

from config import MODEL_NAME

@dataclass
class GenerationContext:
    """Context for section generation"""
    content: str
    file_size: int
    options: dict

class BaseSectionGenerator(ABC):
    """
    Box: Section generator interface

    Input: content, context
    Output: generated section text
    Responsibility: Generate one document section
    """

    def __init__(
        self,
        ollama_client,
        validator,
        cleaner,
        prompt_template: str,
        system_prompt: str
    ):
        self.ollama = ollama_client
        self.validator = validator
        self.cleaner = cleaner
        self.prompt_template = prompt_template
        self.system_prompt = system_prompt
        self.logger = logging.getLogger(__name__)


    def generate(self, context: GenerationContext) -> str:
        """
        Generate section.

        Input: generation context
        Output: cleaned, validated section text
        """
        # Format prompt
        prompt = self._format_prompt(context)

        # Generate
        raw_response = self.ollama.generate(
            model=self._get_model(),
            prompt=prompt,
            system=self.system_prompt,
            options=context.options
        )

        # Validate and regenerate if needed
        validated = self._validate_and_regenerate(raw_response, context)

        # Clean
        cleaned = self.cleaner.clean(validated)

        return cleaned

    @abstractmethod
    def _format_prompt(self, context: GenerationContext) -> str:
        """Format prompt with context data."""
        pass

    def _get_model(self) -> str:
        """Get model name for this section. Can be overridden for specific models."""
        return MODEL_NAME

    def _build_correction_prompt(self, invalid_text: str, error_msg: str, context: GenerationContext) -> str:
        """Build a correction prompt for regeneration."""
        correction_instruction = (
            "The previous output was not valid and contained conversational elements or did not follow the required format. "
            "Re-generate the content STRICTLY adhering to the original instructions. Your output MUST ONLY be the requested content, "
            "with no introductory phrases, conversational filler, or questions. If the content is 'Not applicable', output only that. "
            "Do not explain or comment."
        )
        original_prompt_reformatted = self._format_prompt(context) # Re-format original prompt
        
        return (
            f"{correction_instruction}\n\n"
            f"Original prompt instructions:\n{original_prompt_reformatted}\n\n"
            f"Invalid output received (Error: {error_msg}):\n{invalid_text}\n\n"
            f"Re-generate now:"
        )


    def _validate_and_regenerate(
        self,
        text: str,
        context: GenerationContext,
        max_attempts: int = 3
    ) -> str:
        """Validate and retry if needed."""
        for attempt in range(max_attempts):
            is_valid, error_msg = self.validator.validate(text)
            if is_valid:
                return text

            self.logger.warning(f"Validation failed for {self.__class__.__name__}. Regenerating... (Attempt {attempt+1}/{max_attempts}) Error: {error_msg}")
            # Regenerate with correction
            correction_prompt = self._build_correction_prompt(text, error_msg, context)
            
            # Assuming self.ollama.generate takes 'model', 'prompt', 'system', 'options'
            text = self.ollama.generate(
                model=self._get_model(),
                prompt=correction_prompt,
                system=self.system_prompt,
                options=context.options
            )

        self.logger.error(f"Failed to generate valid output for {self.__class__.__name__} after {max_attempts} attempts. Returning last invalid output.")
        return text  # Return last attempt even if invalid
