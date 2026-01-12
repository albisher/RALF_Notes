"""
Box: Validator

Input: Parsed Dictionary (structured text)
Output: (is_valid: bool, errors: List[str])
Responsibility: Validate the structure and content of parsed data
"""

from typing import Dict, Any, List, Tuple

class Validator:
    """
    Box: Validator

    Responsibility: Validate the structure and content of parsed data.
    """

    def __init__(self):
        # Validator can be initialized with rules if needed in future.
        pass

    def validate(self, parsed_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate the parsed data for completeness and basic correctness.

        Args:
            parsed_data: The dictionary of structured text parsed from raw LLM output.

        Returns:
            A tuple: (is_valid, list_of_errors).
            is_valid is True if all critical checks pass, False otherwise.
            list_of_errors contains strings describing any validation failures.
        """
        errors = []

        # --- Critical Section Checks (must be present and not empty) ---
        required_keys = ["filename", "summary", "tags", "type"]
        for key in required_keys:
            value = parsed_data.get(key)
            if not value:
                errors.append(f"Missing or empty required section: '{key.upper()}'")
            elif isinstance(value, list) and not value:
                errors.append(f"Empty required list section: '{key.upper()}'")
            elif isinstance(value, str) and not value.strip():
                errors.append(f"Empty required string section: '{key.upper()}'")
        
        # --- Specific Format Checks ---
        # Tags should be a list of strings starting with '#'
        tags = parsed_data.get("tags")
        if tags and not isinstance(tags, list):
            errors.append("TAGS section is not a list.")
        elif tags:
            for tag in tags:
                if not isinstance(tag, str) or not tag.startswith('#') or len(tag) < 2:
                    errors.append(f"Tag '{tag}' is not correctly formatted (should start with '#' and be at least 2 chars).")

        # Type should be one of the enum values (assuming schema has a list of valid types)
        # For now, just check if it's a non-empty string. More advanced check requires schema.
        doc_type = parsed_data.get("type")
        if doc_type and not isinstance(doc_type, str):
            errors.append("TYPE section is not a string.")

        is_valid = not bool(errors)
        return is_valid, errors
