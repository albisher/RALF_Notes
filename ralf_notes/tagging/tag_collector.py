import re
import yaml
import logging
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import Counter

logger = logging.getLogger(__name__)

class TagCollector:
    """
    Box: Tag Collector

    Input: Directory of markdown files
    Output: Tag frequency map with file associations
    Responsibility: Parse frontmatter and extract all tags
    """

    def collect_tags(self, directory: Path) -> Dict[str, Any]:
        """
        Collect all tags from markdown files.

        Returns:
            {
                'tag_frequency': Counter({'#python': 45, '#core': 30, ...}),
                'tag_to_files': {'#python': ['file1.md', 'file2.md'], ...},
                'total_files': 462,
                'total_unique_tags': 127
            }
        """
        tag_frequency = Counter()
        tag_to_files = {}
        file_count = 0

        logger.info("Collecting tags from markdown files in directory: %s", directory)

        for md_file in directory.glob('**/*.md'):
            file_count += 1
            try:
                content = md_file.read_text(encoding='utf-8')
                tags = self._extract_tags(content)

                if tags:
                    for tag in tags:
                        tag_frequency[tag] += 1
                        if tag not in tag_to_files:
                            tag_to_files[tag] = []
                        tag_to_files[tag].append(md_file.name)
            except Exception as e:
                logger.warning("Error collecting tags from file %s: %s", md_file, e)

        logger.info("Finished collecting tags. Found %d files, %d unique tags.", file_count, len(tag_frequency))
        return {
            'tag_frequency': dict(tag_frequency),
            'tag_to_files': tag_to_files,
            'total_files': file_count,
            'total_unique_tags': len(tag_frequency)
        }

    def _extract_tags(self, content: str) -> List[str]:
        """
        Extract all tags from content.
        Looks in frontmatter and general body text.
        """
        tags_found = set()

        # 1. Try YAML frontmatter
        if content.startswith('---'):
            try:
                end_idx = content.find('---', 3)
                if end_idx != -1:
                    frontmatter_str = content[3:end_idx].strip()
                    data = yaml.safe_load(frontmatter_str)
                    if data and 'tags' in data:
                        raw_tags = data['tags']
                        if isinstance(raw_tags, list):
                            for t in raw_tags: tags_found.add(self._clean_tag(str(t)))
                        elif isinstance(raw_tags, str):
                            for t in raw_tags.split(','): tags_found.add(self._clean_tag(t))
            except Exception as e:
                logger.debug("Error parsing frontmatter: %s", e)

        # 2. Extract from body using regex
        # Pattern matches # followed by alphanumeric, hyphen, or underscore
        # Must be preceded by start of line, space, or certain punctuation
        # and followed by end of line, space, comma, or punctuation.
        body_tags = re.findall(r'(?:^|\s|[,;])#([a-zA-Z0-9\-_.]+)', content)
        for t in body_tags:
            cleaned = self._clean_tag(t)
            if cleaned:
                tags_found.add(cleaned)

        return sorted(list(filter(None, tags_found)))

    def _clean_tag(self, tag: str) -> str:
        """Basic cleaning of a tag string."""
        tag = tag.strip().lower()
        if not tag: return ""
        if tag == "none": return "" # Still skip "none"
        if not tag.startswith('#'):
            tag = f'#{tag}'
        return tag

