from typing import List
import re
from .base_cleaner import BaseCleaner

class SummaryCleaner(BaseCleaner):
    """
    Box: Summary cleaner

    Input: raw summary text
    Output: cleaned summary text
    Responsibility: Remove unwanted elements from summary
    """

    def __init__(self, max_words: int = 150):
        self.max_words = max_words

    def clean(self, text: str) -> str:
        """
        Clean summary text.

        Input: raw text
        Output: cleaned text
        """
        # Remove code fences
        text = re.sub(r'```[a-zA-Z]*\n', '', text)
        text = text.replace('```', '')

        # Remove dates
        text = re.sub(r'\d{4}-\d{2}-\d{2}', '', text)

        lines = text.strip().split('\n')
        cleaned_lines = []

        for line in lines:
            stripped_line = line.strip()

            # Skip unwanted lines
            if self._should_skip_line(stripped_line):
                continue

            cleaned_lines.append(line)

        # Join and trim
        final_summary = " ".join([line.strip() for line in cleaned_lines]).strip()

        # Enforce word limit
        words = final_summary.split()
        if len(words) > self.max_words:
            final_summary = " ".join(words[:self.max_words]) + "..."

        return final_summary

    def _should_skip_line(self, line: str) -> bool:
        """Check if line should be skipped."""
        if not line:
            return True
        if line.startswith(('tags:', 'created:', 'type:', '---')):
            return True
        if re.match(r'^#+\s', line):
            return True
        if '**tags**' in line.lower():
            return True
        return False
