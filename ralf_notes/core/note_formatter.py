
"""
Box: Note Formatter

Input: Parsed Dictionary (structured text)
Output: Formatted Obsidian markdown
Responsibility: Convert parsed data to beautiful Obsidian markdown
"""

import datetime
from typing import Dict, Any, List, Optional

class NoteFormatter:
    """
    Box: Note Formatter

    Input: Parsed Dictionary (structured text)
    Output: Formatted Obsidian markdown
    Responsibility: Convert parsed data to Obsidian markdown.
    """

    def format(self, data: Dict[str, Any]) -> str:
        """
        Convert parsed data to Obsidian markdown.

        Args:
            data: Parsed Dictionary (structured text)

        Returns:
            Complete formatted markdown document
        """
        sections = [
            self._format_frontmatter(data),
            self._format_header(data),
            self._format_summary(data),
            self._format_details(data),
            self._format_key_functions(data),
            self._format_usage(data),
            self._format_code_summary(data),
            self._format_dependencies(data),
            self._format_dependency_graph(data),
            self._format_security_risks(data),
            self._format_performance_notes(data),
            self._format_related(data),
            self._format_callouts(data),
        ]

        # Filter out None/empty sections
        content = '\n\n'.join(s for s in sections if s)

        return content.strip() + '\n'

    def _format_frontmatter(self, data: Dict[str, Any]) -> str:
        """Generate YAML frontmatter."""
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        tags = ', '.join(data.get('tags', ['#documentation']))
        doc_type = data.get('type', 'code-notes')

        return f"""---
tags: {tags}
created: {date}
type: {doc_type}
---"""

    def _format_header(self, data: Dict[str, Any]) -> str:
        """Generate H1 header."""
        return f"# {data.get('filename', 'Untitled')}"

    def _format_summary(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Summary section."""
        summary = data.get('summary', '')
        if not summary:
            return None

        return f"""## Summary

{summary}"""

    def _format_details(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Details section."""
        details = data.get('details', '')
        if not details:
            return None

        return f"""## Details

{details}"""

    def _format_key_functions(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Key Functions section."""
        functions = data.get('key_functions', [])
        if not functions:
            return None

        content = "## Key Functions\n\n"

        for func in functions:
            name = func.get('name', 'unknown')
            purpose = func.get('purpose', 'No description')
            signature = func.get('signature', '')
            returns = func.get('returns', '')

            content += f"### `{name}`\n\n"
            content += f"{purpose}\n\n"

            if signature:
                content += f"**Signature:** `{signature}`\n\n"

            if returns:
                content += f"**Returns:** {returns}\n\n"

        return content.strip()

    def _format_usage(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Usage section."""
        usage = data.get('usage', '')
        if not usage:
            return None

        return f"""## Usage

{usage}"""

    def _format_code_summary(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate code summary section."""
        code = data.get('code_summary', '')
        if not code:
            return None

        return f"""## Code Summary

{code}"""

    def _format_dependencies(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Dependencies section."""
        deps = data.get('dependencies', [])
        if not deps:
            return None

        deps_list = ', '.join(f"`{dep}`" for dep in deps)
        return f"""## Dependencies

{deps_list}"""

    def _format_dependency_graph(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Dependency Graph section."""
        graph = data.get('dependency_graph', '')
        if not graph:
            return None

        return f"""## Dependency Graph

{graph}"""

    def _format_security_risks(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Security Risks section."""
        risks = data.get('security_risks', '')
        if not risks:
            return None

        return f"""## Security Risks

{risks}"""

    def _format_performance_notes(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Performance Notes section."""
        notes = data.get('performance_notes', '')
        if not notes:
            return None

        return f"""## Performance

{notes}"""

    def _format_related(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate Related section."""
        related = data.get('related', [])
        if not related:
            return None

        links = '\n'.join(f"- {link}" for link in related)
        return f"""## Related

{links}"""

    def _format_callouts(self, data: Dict[str, Any]) -> Optional[str]:
        """Generate callouts."""
        callouts = data.get('callouts', [])
        if not callouts:
            return None

        return '\n\n'.join(callouts)
