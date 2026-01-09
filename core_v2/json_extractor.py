"""
Box: JSON Extractor

Input: Raw LLM response string
Output: Parsed dictionary or None
Responsibility: Robust JSON extraction with fallbacks
"""

import json
import re
from typing import Optional, Tuple, Dict, Any


class JSONExtractor:
    """
    Box: JSON Extractor

    Input: Raw LLM response string
    Output: Parsed dictionary or error message
    Responsibility: Extract and parse JSON from messy LLM output
    """

    # Patterns to try in order of likelihood
    PATTERNS = [
        r'```json\s*(\{.*?\})\s*```',      # ```json {...} ```
        r'```\s*(\{.*?\})\s*```',          # ``` {...} ```
        r'```text\s*(\{.*?\})\s*```',      # ```text {...} ```
        r'(\{.*\})',                        # Raw JSON
    ]

    def extract(self, raw_response: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        """
        Extract JSON from response.

        Args:
            raw_response: Raw string from LLM

        Returns:
            Tuple of (parsed_dict, error_message)
            If successful: (dict, None)
            If failed: (None, error_message)
        """
        raw = raw_response.strip()

        # Try each pattern
        for pattern in self.PATTERNS:
            match = re.search(pattern, raw, re.DOTALL)
            if match:
                json_str = match.group(1)
                try:
                    parsed = json.loads(json_str)
                    return (parsed, None)
                except json.JSONDecodeError:
                    continue  # Try next pattern

        # Last resort: find any JSON-like object
        try:
            start = raw.find('{')
            end = raw.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = raw[start:end]
                parsed = json.loads(json_str)
                return (parsed, None)
        except json.JSONDecodeError:
            pass

        return (None, "Failed to extract valid JSON from response")

    def extract_or_fallback(self, raw_response: str, filename: str) -> Dict[str, Any]:
        """
        Extract JSON or create fallback structure.

        Args:
            raw_response: Raw string from LLM
            filename: Filename for fallback

        Returns:
            Parsed dictionary or fallback structure
        """
        parsed, error = self.extract(raw_response)

        if parsed:
            return parsed

        # Create fallback structure
        return {
            "filename": filename,
            "tags": ["#parsing-failed", "#needs-review"],
            "type": "code-notes",
            "summary": "Documentation generation failed - JSON parsing error",
            "details": f"Error: {error}",
            "key_functions": [],
            "dependencies": [],
            "usage": "Manual review required",
            "related": [],
            "callouts": [
                f"> [!WARNING]- JSON Parsing Failed\n> {error}\n\n**Raw output (first 500 chars):**\n```text\n{raw_response[:500]}\n```"
            ]
        }
