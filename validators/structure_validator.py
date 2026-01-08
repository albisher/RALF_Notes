from typing import Tuple
import re
from .base_validator import BaseValidator

class StructureValidator(BaseValidator):
    """
    Box: Structure validator

    Input: markdown text
    Output: (is_valid, error_message)
    Responsibility: Validate markdown structure
    """

    def validate(self, text: str) -> Tuple[bool, str]:
        """Validate markdown structure."""
        required_elements = {
            "summary": "## Summary",
            "details": "## Details",
            "dependency_graph": "## Dependency Graph",
            "key_functions": "## Key Functions/Classes",
            "usage_examples": "## Usage/Examples",
            "security_risks": "## Security Risks",
            "related": "## Related",
            "callout": "> [!INFO]"
        }
        
        missing = []
        for key, element in required_elements.items():
            if key == "callout":
                if not re.search(r'>\s*\[!INFO\]', text):
                    missing.append(element)
            elif element not in text:
                missing.append(element)

        if missing:
            return False, f"Missing elements: {', '.join(missing)}"

        return True, ""
