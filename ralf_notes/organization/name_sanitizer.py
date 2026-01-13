import re
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class NameSanitizer:
    """
    Box: Name Sanitizer

    Responsibility: Clean up filenames (remove numeric prefixes, normalize case)
    """

    # Matches prefixes like 001-, 01_, 1., etc.
    PREFIX_PATTERN = r'^\d+[-_.]*'

    def sanitize(self, filename: str, normalize_case: bool = True) -> str:
        """
        Sanitize a filename.
        
        Args:
            filename: Original filename (with extension)
            normalize_case: If True, converts to kebab-case
            
        Returns:
            Cleaned filename
        """
        # Separate name and extension
        import os
        name, ext = os.path.splitext(filename)
        
        # 1. Remove numeric prefix
        clean_name = re.sub(self.PREFIX_PATTERN, '', name)
        
        # 2. Normalize case and spaces
        if normalize_case:
            # Replace underscores and spaces with hyphens
            clean_name = re.sub(r'[\s_]+', '-', clean_name)
            # Convert to lower
            clean_name = clean_name.lower()
            # Clean up double hyphens
            clean_name = re.sub(r'-+', '-', clean_name)
            # Strip hyphens from ends
            clean_name = clean_name.strip('-')
            
        if not clean_name:
            return filename # Fallback to original if we somehow stripped everything
            
        return f"{clean_name}{ext}"
