import re
import logging
from pathlib import Path
from typing import Dict, List, Any, Set

logger = logging.getLogger(__name__)

class LinkCollector:
    """
    Box: Link Collector

    Input: Directory of markdown files
    Output: Link map and file index
    Responsibility: Extract all wikilinks from all files
    """

    # Matches [[link]], [[link|alias]], or [[link#heading]]
    LINK_PATTERN = r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]'

    def collect_links(self, directory: Path) -> Dict[str, Any]:
        """
        Collect all links from markdown files.

        Returns:
            {
                'link_map': {'file1.md': ['link1', 'link2'], ...},
                'file_index': {'file1.md', 'file2.md', ...},
                'total_files': 462,
                'total_links': 1270
            }
        """
        link_map = {}
        file_index = set()
        total_links = 0
        file_count = 0

        logger.info("Collecting links from markdown files in directory: %s", directory)

        # First pass: Build file index (all valid .md files)
        for md_file in directory.glob('**/*.md'):
            file_index.add(md_file.name)
            file_count += 1

        # Second pass: Extract links from each file
        for md_file in directory.glob('**/*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                links = self._extract_links(content)
                
                if links:
                    link_map[md_file.name] = links
                    total_links += len(links)
            except Exception as e:
                logger.warning("Error collecting links from file %s: %s", md_file, e)

        logger.info("Finished collecting links. Found %d files, %d total links.", file_count, total_links)
        return {
            'link_map': link_map,
            'file_index': file_index,
            'total_files': file_count,
            'total_links': total_links
        }

    def _extract_links(self, content: str) -> List[str]:
        """Extract links from content using regex."""
        links = re.findall(self.LINK_PATTERN, content)
        # Clean up links (strip and lowercase for matching)
        return [l.strip() for l in links if l.strip()]
