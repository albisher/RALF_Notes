import logging
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from .name_sanitizer import NameSanitizer
from .folder_strategist import FolderStrategist

logger = logging.getLogger(__name__)

class FileMover:
    """
    Box: File Mover

    Responsibility: Execute reorganization of files
    """

    def __init__(self):
        self.sanitizer = NameSanitizer()
        self.strategist = FolderStrategist()

    def organize_directory(self,
                           directory: Path,
                           strategy: str = 'flat',
                           clean_names: bool = True,
                           dry_run: bool = False) -> Dict[str, Any]:
        """
        Organize an existing directory.
        """
        results = {
            'processed': 0,
            'moved': 0,
            'errors': []
        }

        # We need metadata for type/tag strategy. 
        # This requires parsing each file frontmatter.
        from ..core.text_parser import TextParser
        parser = TextParser()

        files = list(directory.glob('**/*.md'))
        
        for md_file in files:
            if md_file.name in ['applied_tags.md', 'applied_links.md', 'unique_tags.txt']:
                continue
                
            results['processed'] += 1
            
            try:
                # 1. Get metadata
                content = md_file.read_text(encoding='utf-8')
                metadata = parser.parse_markdown(content)
                
                # 2. Calculate new name
                new_name = self.sanitizer.sanitize(md_file.name) if clean_names else md_file.name
                
                # 3. Calculate target path
                rel_path = self.strategist.get_target_path(new_name, metadata, strategy)
                target_full_path = directory / rel_path
                
                if md_file == target_full_path:
                    continue
                
                if not dry_run:
                    target_full_path.parent.mkdir(parents=True, exist_ok=True)
                    # Handle name collision
                    if target_full_path.exists():
                        target_full_path = self._handle_collision(target_full_path)
                    
                    md_file.rename(target_full_path)
                    results['moved'] += 1
                else:
                    logger.info("Dry run: Would move %s to %s", md_file.name, rel_path)
                    results['moved'] += 1

            except Exception as e:
                logger.error("Failed to organize %s: %s", md_file.name, e)
                results['errors'].append({'file': md_file.name, 'error': str(e)})

        return results

    def _handle_collision(self, path: Path) -> Path:
        """Add suffix if file exists."""
        counter = 1
        while path.exists():
            name = f"{path.stem}_{counter}{path.suffix}"
            path = path.with_name(name)
            counter += 1
        return path
