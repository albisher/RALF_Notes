"""
Box: Structured Text Generator

Input: GenerationContext (file path, content, metadata)
Output: Raw structured text from LLM
Responsibility: Single LLM call to generate structured analysis
"""

from typing import Optional
from ollama import Client
from .models import GenerationContext, StructuredTextGeneratorConfig
from .schema import UNIFIED_SYSTEM_PROMPT


class StructuredTextGenerator:
    """
    Box: Structured Text Generator

    Input: GenerationContext
    Output: Raw structured text from LLM
    Responsibility: Single LLM call to generate structured documentation
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

    def _prepare_content(self, content: str) -> str:
        """
        Chunk and summarize large files.

        Args:
            content: Raw file content

        Returns:
            Processed content suitable for LLM
        """
        if len(content) <= self.config.chunk_size:
            # Truncate for reliability using config value
            return content[:self.config.max_content_length]

        # Need to chunk and summarize
        return self._recursive_summarize(content)

    def _recursive_summarize(self, content: str) -> str:
        """
        Recursively summarize large content.

        Args:
            content: Large content that exceeds chunk size

        Returns:
            Condensed summary
        """
        chunks = [
            content[i:i + self.config.chunk_size]
            for i in range(0, len(content), self.config.chunk_size)
        ]

        summaries = []
        for i, chunk in enumerate(chunks, 1):
            # Summarize each chunk (matches original PoC format, uses config value)
            prompt = f"Summarize this code:\n\n{chunk[:self.config.max_chunk_summary_length]}"
            try:
                response = self.client.generate(
                    model=self.config.model_name,
                    prompt=prompt,
                    options={
                        "num_ctx": self.config.num_ctx,
                        "temperature": self.config.temperature
                    }
                )
                summaries.append(response['response'])
            except Exception:
                # Fallback on error
                summaries.append(chunk[:1000])

        # Combine summaries
        combined = '\n\n'.join(summaries)

        # Recursively summarize if still too large
        if len(combined) > self.config.chunk_size:
            return self._recursive_summarize(combined)

        return combined

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
