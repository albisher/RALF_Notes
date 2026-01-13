import logging
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class FolderStrategist:
    """
    Box: Folder Strategist

    Responsibility: Determine the destination folder for a file
    """

    def get_target_path(self,
                        filename: str,
                        file_metadata: Dict[str, Any],
                        strategy: str = 'flat') -> Path:
        """
        Calculate relative destination path.
        
        Strategies:
        - flat: Return filename (no subfolders)
        - type: Use metadata['type'] as folder
        - tag: Use first tag as folder
        """
        if strategy == 'type':
            doc_type = file_metadata.get('type', 'Other')
            # Clean folder name
            clean_type = self._clean_folder_name(doc_type)
            return Path(clean_type) / filename
            
        elif strategy == 'tag':
            tags = file_metadata.get('tags', [])
            if tags:
                first_tag = tags[0].lstrip('#')
                clean_tag = self._clean_folder_name(first_tag)
                return Path(clean_tag) / filename
            return Path('uncategorized') / filename
            
        return Path(filename)

    def _clean_folder_name(self, name: str) -> str:
        """Make string safe for folder name."""
        import re
        # Remove non-alphanumeric except space/hyphen
        clean = re.sub(r'[^\w\s-]', '', name)
        # Normalize spaces to hyphens
        clean = re.sub(r'[\s_]+', '-', clean).strip('-')
        return clean or 'Other'
