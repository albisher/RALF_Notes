"""
Box: JSON Validator

Input: Parsed JSON dictionary
Output: (is_valid, errors)
Responsibility: Schema validation and business rules
"""

from typing import List, Tuple, Dict, Any


class JSONValidator:
    """
    Box: JSON Validator

    Input: Parsed JSON dictionary
    Output: (is_valid, error_messages)
    Responsibility: Validate structure and fix common issues
    """

    VALID_TYPES = [
        'code-notes', 'documentation', 'research', 'test-reference',
        'configuration', 'api-reference', 'architecture', 'tutorial'
    ]

    def __init__(self):
        """Initialize validator."""
        pass

    def validate(self, data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate JSON against business rules.

        Args:
            data: Parsed JSON dictionary

        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []

        # Required fields
        if not data.get('filename'):
            errors.append("filename is required")

        # Tag validation
        tags = data.get('tags', [])
        if len(tags) < 2:
            errors.append("At least 2 tags required")

        for tag in tags:
            if not isinstance(tag, str):
                errors.append(f"Tag must be string: {tag}")
                continue
            if not tag.startswith('#'):
                errors.append(f"Tag must start with #: {tag}")
            if ' ' in tag:
                errors.append(f"Tag cannot contain spaces: {tag}")

        # Summary validation
        summary = data.get('summary', '')
        if len(summary) < 20:
            errors.append("Summary must be at least 20 characters")
        if len(summary) > 500:
            errors.append("Summary must be at most 500 characters")

        # Type validation
        if data.get('type') not in self.VALID_TYPES:
            errors.append(f"Invalid type: {data.get('type')}. Must be one of: {', '.join(self.VALID_TYPES)}")

        # Key functions validation
        key_funcs = data.get('key_functions', [])
        if len(key_funcs) > 15:
            errors.append("Too many key functions (max 15)")

        for func in key_funcs:
            if not isinstance(func, dict):
                errors.append("Key function must be a dictionary")
                continue
            if not func.get('name'):
                errors.append("Key function missing name")
            if not func.get('purpose'):
                errors.append(f"Key function '{func.get('name', 'unknown')}' missing purpose")

        # Related links validation
        related = data.get('related', [])
        for link in related:
            if not isinstance(link, str):
                continue
            if not link.startswith('[[') or not link.endswith(']]'):
                errors.append(f"Invalid wikilink format: {link}")

        # Callout validation
        callouts = data.get('callouts', [])
        if len(callouts) > 5:
            errors.append("Too many callouts (max 5)")

        for callout in callouts:
            if not isinstance(callout, str):
                continue
            if not callout.startswith('> [!'):
                errors.append(f"Invalid callout format: {callout[:30]}")

        return (len(errors) == 0, errors)

    def validate_and_fix(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and attempt to fix common issues.

        Args:
            data: Parsed JSON dictionary

        Returns:
            Fixed dictionary
        """
        # Fix missing required fields
        if 'filename' not in data or not data['filename']:
            data['filename'] = 'unknown'

        # Fix tags
        if 'tags' not in data or len(data.get('tags', [])) < 2:
            data['tags'] = ['#documentation', '#auto-generated']
        else:
            # Fix tags format
            fixed_tags = []
            for tag in data.get('tags', []):
                if not isinstance(tag, str):
                    continue
                tag = tag.strip().lower()
                if not tag.startswith('#'):
                    tag = f"#{tag}"
                tag = tag.replace(' ', '-')
                fixed_tags.append(tag)
            data['tags'] = list(set(fixed_tags))  # Remove duplicates

        # Fix type
        if 'type' not in data or data.get('type') not in self.VALID_TYPES:
            data['type'] = 'code-notes'

        # Fix summary
        if 'summary' not in data or len(data.get('summary', '')) < 20:
            data['summary'] = 'Documentation summary unavailable'

        # Ensure arrays exist
        for key in ['key_functions', 'dependencies', 'related', 'callouts']:
            if key not in data:
                data[key] = []

        return data
