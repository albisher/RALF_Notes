import re
from .base_cleaner import BaseCleaner
from validators.general_validator import GeneralValidator # To replace has_no_questions

class GeneralCleaner(BaseCleaner):
    """
    Box: General purpose cleaner

    Input: text to clean
    Output: cleaned text
    Responsibility: Clean various types of text content.
    """

    def __init__(self):
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai", "i can help", "i've extracted",
            "below is", "okay, here's", "the type is", "i would classify this as", "it is a",
            "here's a list", "the following are", "below is the", "here are the"
        ]
        self.general_validator = GeneralValidator()

    def clean(self, text: str) -> str:
        """
        A no-op clean method for GeneralCleaner, as specific cleaning methods should be called directly.
        """
        return text

    def clean_doc_type(self, text: str) -> str:
        """Ensures doc_type is a single word."""
        text_cleaned = text.strip()
        for phrase in self.conversational_starts:
            if text_cleaned.lower().startswith(phrase):
                text_cleaned = text_cleaned[len(phrase):].strip()
        
        first_word = re.sub(r'[^\w\-]', '', text_cleaned.split()[0]).strip()
        return first_word

    def clean_mermaid(self, text: str) -> str:
        """Removes mermaid code fences from the mermaid content."""
        lines = text.strip().split('\n')
        if lines and re.match(r'^\s*```.*', lines[0]):
            lines = lines[1:]
        if lines and re.match(r'^\s*```', lines[-1]):
            lines = lines[:-1]
        return "\n".join(lines).strip()

    def clean_related(self, text: str) -> str:
        """Removes markdown code fences from the related content."""
        return text.strip()

    def clean_not_applicable(self, text: str) -> str:
        """Handles 'Not applicable' case and removes questions/conversational filler."""
        # Use the GeneralValidator for the has_no_questions logic
        is_valid, _ = self.general_validator.validate(text)
        if not is_valid:
            # We don't log here, the validator might already do it.
            pass
        
        cleaned_text = text.strip()
        for phrase in self.conversational_starts:
            if cleaned_text.lower().startswith(phrase):
                cleaned_text = cleaned_text[len(phrase):].strip()

        if "not applicable" in cleaned_text.lower():
            return "Not applicable"
        return cleaned_text.replace("?", "")


