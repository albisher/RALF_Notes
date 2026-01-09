from typing import Tuple
import re
from .base_validator import BaseValidator

class SummaryValidator(BaseValidator):
    """
    Box: Summary validator

    Input: summary text
    Output: (is_valid, error_message)
    Responsibility: Validate summary format
    """

    def __init__(self, max_lines: int = 20):
        self.max_lines = max_lines
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai"
        ]

    def validate(self, text: str) -> Tuple[bool, str]:
        """Validate summary text."""

        # Check for questions
        if '?' in text:
            return False, "Contains question marks"

        # Check line count
        lines = text.strip().split('\n')
        if len(lines) > self.max_lines:
            return False, f"Exceeds {self.max_lines} lines"

        # Check for multiple paragraphs
        if re.search(r'\n\s*\n', text.strip()):
            return False, "Contains multiple paragraphs"

        # Check for conversational filler
        text_lower = text.lower().strip()
        for phrase in self.conversational_starts:
            if text_lower.startswith(phrase):
                return False, f"Starts with '{phrase}'"

        return True, ""
