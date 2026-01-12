from typing import Optional
from pathlib import Path
from ollama import Client
from .models import GenerationContext, StructuredTextGeneratorConfig
from .schema import UNIFIED_SYSTEM_PROMPT
import time
import logging # ADD THIS IMPORT

logger = logging.getLogger(__name__) # ADD THIS LINE


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
        logger.info("Starting text generation for file: %s", context.filename)
        # 1. Prepare content (chunk/summarize if needed)
        processed_content = self._prepare_content(context.content, context) # Pass context for logging
        logger.debug("Content prepared for %s", context.filename)

        # 2. Build user prompt
        user_prompt = self._format_prompt(context.filename, processed_content)
        logger.debug("User prompt built for %s", context.filename)

        # Retrieve retry settings from config
        max_retries = self.config.retry_attempts
        initial_backoff = self.config.initial_backoff_seconds
        backoff_multiplier = self.config.backoff_multiplier
        logger.debug("Retry settings: max_retries=%d, initial_backoff=%.2f, backoff_multiplier=%.2f",
                     max_retries, initial_backoff, backoff_multiplier)

        for attempt in range(max_retries):
            try:
                logger.debug("Attempt %d of %d for %s. Making LLM call...", attempt + 1, max_retries, context.filename)
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
                logger.info("Successfully generated text for %s", context.filename)
                return response['response']
            except Exception as e:
                logger.error("Error during LLM generation for %s (attempt %d/%d): %s",
                             context.filename, attempt + 1, max_retries, e, exc_info=True)
                if attempt < max_retries - 1:
                    current_backoff = initial_backoff * (backoff_multiplier ** attempt)
                    logger.warning("Retrying %s in %.2f seconds...", context.filename, current_backoff)
                    time.sleep(current_backoff)
                else:
                    logger.error("All %d retry attempts failed for %s", max_retries, context.filename)
                    raise # Re-raise the last exception if all retries fail
    
    def generate_and_save_raw(self, context: GenerationContext, output_path: Path) -> None:
        logger.info("Generating and saving raw output for %s to %s", context.filename, output_path)
        raw_output = self.generate(context)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(raw_output, encoding='utf-8')
        logger.info("Raw output saved for %s", context.filename)

    def _prepare_content(self, content: str, context: GenerationContext) -> str: # Add context parameter
        """
        Prepare content for LLM for fastest raw generation (Phase 1).
        Prioritizes single LLM call by truncating if content is too large.
        """
        if len(content) <= self.config.max_content_length:
            logger.debug("Content length within limits for %s", context.filename) # ADDED context.filename
            return content
        else:
            logger.warning("Content too large (%d chars), truncating to %d for %s",
                           len(content), self.config.max_content_length, context.filename)
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
