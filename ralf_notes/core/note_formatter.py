"""
Box: Note Formatter

Input: Parsed Dictionary (structured text)
Output: Formatted Obsidian markdown
Responsibility: Convert parsed data to beautiful Obsidian markdown
"""
import re
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import logging # ADD THIS IMPORT

logger = logging.getLogger(__name__) # ADD THIS LINE

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
        filename = data.get('filename', 'Untitled')
        logger.debug("Starting markdown formatting for file: %s", filename) # ADD LOGGING

        sections = [
            self._format_frontmatter(data),
            self._format_header(data),
            self._format_summary(data),
            self._format_details(data),
            self._format_key_functions(data),
            self._format_usage(data),
            self._format_dependencies(data),
            self._format_related(data),
            self._format_callouts(data),
        ]

        # Filter out None/empty sections
        content = '\n\n'.join(s for s in sections if s)
        logger.debug("Finished markdown formatting for file: %s", filename) # ADD LOGGING
        return content.strip() + '\n'

    def _format_frontmatter(self, data: Dict[str, Any]) -> str:
        logger.debug("Formatting frontmatter.") # ADD LOGGING
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        tags = ', '.join(data.get('tags', ['#documentation']))
        doc_type = data.get('type', 'code-notes')

        return f"""**Tags:** {tags}
**Created:** {date}
**Type:** {doc_type}"""

    def _format_header(self, data: Dict[str, Any]) -> str:
        logger.debug("Formatting header.") # ADD LOGGING
        return f"# {data.get('filename', 'Untitled')}"

    def _format_summary(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting summary.") # ADD LOGGING
        summary = data.get('summary', '')
        if not summary:
            return None
        return f"""## Summary

```
{summary}
```"""

    def _format_details(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting details.") # ADD LOGGING
        details = data.get('details', '')
        if not details:
            return None
        indented_details = '\n> '.join(details.split('\n'))
        return f"""## Details

> {indented_details}"""

    def _format_key_functions(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting key functions.") # ADD LOGGING
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
        logger.debug("Formatting usage.") # ADD LOGGING
        usage = data.get('usage', '')
        if not usage:
            return None
        return f"""## Usage

{usage}"""

    def _format_dependencies(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting dependencies.") # ADD LOGGING
        deps = data.get('dependencies', [])
        if not deps:
            return None
        deps_list = '\n> '.join([f"`{dep}`" for dep in deps])
        return f"""## Dependencies

> {deps_list}"""

    def _format_related(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting related links.") # ADD LOGGING
        related = data.get('related', [])
        if not related:
            return None
        links = '\n'.join(f"- [[{Path(link).stem}]]" for link in related)
        return f"""## Related

{links}"""

    def _format_callouts(self, data: Dict[str, Any]) -> Optional[str]:
        logger.debug("Formatting callouts.") # ADD LOGGING
        callouts = data.get('callouts', [])
        if not callouts:
            return None
        formatted_callouts = []
        for callout in callouts:
            formatted_callout = re.sub(r'(>\[!\w+\])-', r'\1', callout)
            formatted_callouts.append(formatted_callout)
        return '\n\n'.join(formatted_callouts)
