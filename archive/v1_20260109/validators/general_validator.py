from typing import Tuple
from .base_validator import BaseValidator

class GeneralValidator(BaseValidator):
    """
    Box: General purpose validator

    Input: text
    Output: (is_valid, error_message)
    Responsibility: Validate for common issues like questions and conversational filler.
    """

    def __init__(self):
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai", "i can help", "i've extracted",
            "below is", "okay, here's", "the type is", "i would classify this as", "it is a",
            "here's a list", "the following are", "below is the", "here are the"
        ]

    def validate(self, text: str) -> Tuple[bool, str]:
        """Validate for questions and conversational filler."""
        if '?' in text:
            return False, f"Question mark found in generated text: '{text}'"
        
        text_lower = text.lower().strip()
        for phrase in self.conversational_starts:
            if text_lower.startswith(phrase):
                return False, f"Conversational start found in generated text: '{text}'"
        
        return True, ""
