from typing import Tuple
import re
from .base_validator import BaseValidator

class TagsValidator(BaseValidator):
    """
    Box: Tags validator

    Input: tags text
    Output: (is_valid, error_message)
    Responsibility: Validate tags format
    """

    def __init__(self):
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai", "tags:", "taglist:", "list of tags:", "here are the tags:"
        ]

    def validate(self, text: str) -> Tuple[bool, str]:
        """Validate tags text."""

        if '?' in text:
            return False, "Contains question marks"

        if any(text.lower().strip().startswith(phrase) for phrase in self.conversational_starts):
            return False, "Starts with conversational filler"

        tags = text.strip().split()
        for tag in tags:
            if not tag.startswith('#'):
                return False, f"Tag '{tag}' does not start with '#'"
            if re.search(r'[^\w\-]', tag[1:]):
                return False, f"Tag '{tag}' contains invalid characters"

        return True, ""
