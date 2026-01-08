import re
from .base_cleaner import BaseCleaner

class DetailsCleaner(BaseCleaner):
    """
    Box: Details cleaner

    Input: raw details text
    Output: cleaned details text
    Responsibility: Clean and format details content
    """

    def clean(self, text: str) -> str:
        """Aggressively removes frontmatter, markdown headers, separator lines, unwanted callout titles,
        and ensures correct callout formatting for details content."""
        lines = text.strip().split('\n')
        cleaned_lines = []
        in_callout_block = False # To track if we are inside a multi-line callout block
        
        for line in lines:
            stripped_line = line.strip()

            # Check for start of a callout header
            is_callout_header = re.match(r'^\s*>\[!INFO\]', stripped_line)

            # If it's a callout header
            if is_callout_header:
                in_callout_block = True
                # Clean specific unwanted callout titles (e.g., "**Bug Note**") from the callout header
                if re.match(r'^\s*>\[!INFO\]\s*\*\*Bug Note\*\*', stripped_line):
                    stripped_line = re.sub(r'\s*\*\*Bug Note\*\*', '', stripped_line).strip()
                cleaned_lines.append(stripped_line)
                continue

            # If we are inside a callout block
            if in_callout_block:
                if not stripped_line: # An empty line terminates the callout block
                    in_callout_block = False
                    cleaned_lines.append(stripped_line) # Keep the empty line as a separator
                    continue
                elif not stripped_line.startswith('>'): # If a line does not start with '>' it should be prefixed
                    stripped_line = '> ' + stripped_line
                cleaned_lines.append(stripped_line)
                continue
                
            # Lines outside of a callout block - apply existing general cleaning
            # Skip empty lines, frontmatter, markdown headers, and code block fences
            if not stripped_line or \
               stripped_line.startswith(('tags:', 'created:', 'type:', '---')) or \
               re.match(r'^\s*```(\S*|$)', stripped_line) or \
               re.match(r'^#+\s(Summary|Tags|Created|Type)\s*$', stripped_line) or \
               re.match(r'^#+\s', stripped_line) and len(re.findall(r'^#', stripped_line)) < 2:
                continue
            
            cleaned_lines.append(stripped_line)
            
        return "\n".join(cleaned_lines)
