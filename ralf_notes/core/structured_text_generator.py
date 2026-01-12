from typing import Optional
from pathlib import Path # Add Path import
from ollama import Client
from .models import GenerationContext, StructuredTextGeneratorConfig
from .schema import UNIFIED_SYSTEM_PROMPT


class StructuredTextGenerator:
    """
    Box: Structured Text Generator

    Input: GenerationContext (file path, content, metadata)
    Output: Raw structured text from LLM
    Responsibility: Single LLM call to generate structured analysis
    """

    def __init__(self,
                 ollama_client: Client,
                 config: StructuredTextGeneratorConfig,
                 system_prompt: Optional[str] = None):
        """
        Initialize Structured Text Generator.

        Args:
            ollama_client: Ollama client for LLM calls
            config: Generator configuration
            system_prompt: Optional custom system prompt (uses default if None)
        """
        self.client = ollama_client
        self.config = config
        self.system_prompt = system_prompt or UNIFIED_SYSTEM_PROMPT

    def generate(self, context: GenerationContext) -> str:
        """
        Generate structured text documentation for file.

        Args:
            context: Generation context with file data

        Returns:
            Raw structured text from LLM
        """
        # 1. Prepare content (chunk/summarize if needed)
        processed_content = self._prepare_content(context.content)

        # 2. Build user prompt
        user_prompt = self._format_prompt(context.filename, processed_content)

        # 3. Call LLM
        response = self.client.generate(
            model=self.config.model_name,
            system=self.system_prompt,
            prompt=user_prompt,
            options={
                "num_ctx": self.config.num_ctx,
                "temperature": self.config.temperature
            }
        )

        return response['response']
    
    def generate_and_save_raw(self, context: GenerationContext, output_path: Path) -> None:
        """
        Generate raw structured text documentation and save it to a file.

        Args:
            context: Generation context with file data
            output_path: Path to save the raw LLM output
        """
        raw_output = self.generate(context)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(raw_output, encoding='utf-8')

    def _prepare_content(self, content: str) -> str:
        """
        Prepare content for LLM for fastest raw generation (Phase 1).
        Prioritizes single LLM call by truncating if content is too large.
        """
        if len(content) <= self.config.max_content_length:
            return content
        else:
            return content[:self.config.max_content_length]


    def _format_prompt(self, filename: str, content: str) -> str:
        """
        Format user prompt (matches original PoC format).

        Args:
            filename: File name
            content: Processed file content

        Returns:
            Formatted prompt string
        """
        return f"File: {filename}\nContent:\n{content}"
