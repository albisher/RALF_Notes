import re
from typing import Dict, Any, List

class TextParser:
    """
    Parses the LLM's structured text output into a dictionary.
    """

    def parse(self, raw_text: str) -> Dict[str, Any]:
        """
        Parses the raw text and returns a dictionary.
        """
        sections = self._split_into_sections(raw_text)
        
        parsed_data = {
            "filename": self._parse_filename(sections.get("FILENAME", "")),
            "summary": self._parse_summary(sections.get("SUMMARY", "")),
            "tags": self._parse_tags(sections.get("TAGS", "")),
            "type": self._parse_type(sections.get("TYPE", "")),
            "key_functions": self._parse_key_functions(sections.get("KEY_FUNCTIONS", "")),
            "details": self._parse_details(sections.get("DETAILS", "")),
            "dependencies": self._parse_dependencies(sections.get("DEPENDENCIES", "")),
            "usage": self._parse_usage(sections.get("USAGE", "")),
            "related": self._parse_related(sections.get("RELATED", "")),
            "callouts": self._parse_callouts(sections.get("CALLOUTS", "")),
        }

        return parsed_data

    def _parse_filename(self, content: str) -> str:
        """Extract filename."""
        return content.strip()

    def _parse_dependencies(self, content: str) -> List[str]:
        """Parse comma-separated dependencies into a list."""
        if not content or content.lower() == 'none':
            return []
        return [dep.strip() for dep in content.split(',') if dep.strip()]

    def _split_into_sections(self, raw_text: str) -> Dict[str, str]:
        """Splits the text into a dictionary of sections."""
        # Pre-process to remove horizontal rules
        processed_text = re.sub(r'^\s*---\s*$', '', raw_text, flags=re.MULTILINE)
        
        sections = {}
        pattern = r"###\s*(?:\*\*)?(?P<name>[A-Z_]+)(?:\*\*)?\s*(?:###)?\s*(?P<content>.*?)(?=\n###|\Z)"
        matches = re.finditer(pattern, processed_text, re.DOTALL)
        for match in matches:
            name = match.group("name").strip()
            content = match.group("content").strip()
            sections[name] = content
        return sections

    def _parse_summary(self, content: str) -> str:
        return content

    def _parse_details(self, content: str) -> str:
        return content

    def _parse_usage(self, content: str) -> str:
        return content
        
    def _parse_type(self, content: str) -> str:
        return content.strip()

    def _parse_tags(self, content: str) -> List[str]:
        """Parses comma-separated tags into a list."""
        if not content:
            return []
        return [tag.strip() for tag in content.split(',') if tag.strip().startswith('#')]

    def _parse_key_functions(self, content: str) -> List[Dict[str, str]]:
        """Parses a bulleted list of key functions."""
        functions = []
        if not content:
            return functions
        
        pattern = r"-\s*\**(?P<name>.*?)\**:\s*(?P<purpose>.*)"
        matches = re.finditer(pattern, content)
        for match in matches:
            functions.append({
                "name": match.group("name").strip(),
                "purpose": match.group("purpose").strip()
            })
        return functions

    def _parse_related(self, content: str) -> List[str]:
        """Parses comma-separated wikilinks into a list."""
        if not content or content.lower() == 'none':
            return []
        return [link.strip() for link in content.split(',') if link.strip()]

    def _parse_callouts(self, content: str) -> List[str]:
        """Parses a bulleted list of callouts."""
        if not content:
            return []
        # Return each line that starts with '- '
        return [line.strip() for line in content.split('\n') if line.strip().startswith('- ')]

    def parse_or_fallback(self, raw_response: str, filename: str) -> Dict[str, Any]:
        """
        Parses the text or returns a fallback structure on failure.
        """
        try:
            parsed_data = self.parse(raw_response)
            # Override filename with provided value (trust file system, not LLM)
            # parsed_data["filename"] = filename # Removed manual override
            if not all([parsed_data.get("summary"), parsed_data.get("tags"), parsed_data.get("type")]) :
                 raise ValueError("Missing one or more required sections: SUMMARY, TAGS, TYPE.")
            return parsed_data
        except Exception as e:
            # Create fallback structure
            return {
                "filename": filename,
                "tags": ["#parsing-failed", "#needs-review"],
                "type": "code-notes",
                "summary": "Documentation generation failed - text parsing error",
                "details": f"Error: {e}",
                "key_functions": [],
                "dependencies": [],
                "usage": "Manual review required",
                "related": [],
                "callouts": [
                    f"> [!WARNING]- Text Parsing Failed\n> {e}\n\n**Raw output (first 500 chars):**\n```text\n{raw_response[:500]}\n```"
                ]
            }