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
            try:
                content = md_file.read_text(encoding='utf-8')
                tags = self._extract_tags_from_frontmatter(content)

                if tags:
                    file_count += 1
                    for tag in tags:
                        tag_frequency[tag] += 1
                        if tag not in tag_to_files:
                            tag_to_files[tag] = []
                        tag_to_files[tag].append(md_file.name)
            except Exception as e:
                logger.warning("Error collecting tags from file %s: %s", md_file, e)
                # Continue processing other files

        logger.info("Finished collecting tags. Found %d files, %d unique tags.", file_count, len(tag_frequency))
        return {
            'tag_frequency': dict(tag_frequency),
            'tag_to_files': tag_to_files,
            'total_files': file_count,
            'total_unique_tags': len(tag_frequency)
        }

    def _extract_tags_from_frontmatter(self, content: str) -> List[str]:
        """
        Extract tags from YAML frontmatter, applying new tag rules.

        Rules:
        - Filter out any tags that are "none" (case-insensitive) or contain "none".
        - Filter out any tags that contain spaces or multiple words with separators.
        - Tags should be single words (after removing '#').
        """
        tags_found = []
        if not content.startswith('---'):
            return []

        try:
            # Find end of frontmatter
            end_idx = content.find('---', 3)
            if end_idx == -1:
                return []

            # Parse YAML
            frontmatter_str = content[3:end_idx].strip()
            data = yaml.safe_load(frontmatter_str)

            if not data or 'tags' not in data:
                return []

            # Handle both "tag1, tag2" and ["tag1", "tag2"] formats
            tags_value = data['tags']
            if isinstance(tags_value, list):
                raw_tags = tags_value
            elif isinstance(tags_value, str):
                raw_tags = [tag.strip() for tag in tags_value.split(',')]
            else:
                return []
            
            for tag in raw_tags:
                clean_tag = tag.strip().lower()

                # Rule 1: Filter out "none" tags
                if "none" in clean_tag:
                    logger.debug("Filtered out tag '%s' due to 'none' rule.", tag)
                    continue
                
                # Ensure it starts with #
                if not tag.startswith('#'):
                    tag = f'#{tag}'
                
                # Rule 2: Single-worded tags (no spaces or internal separators like -, _)
                # This check ensures it's one word after the #, and doesn't contain common separators.
                # A simple regex for single word characters after # is [a-zA-Z0-9]+
                # If the user clarifies compound tags like #some-tag are allowed, this rule might change.
                # For now, interpret "single worded tags no double words or more with separators in between"
                # as strictly single alphabetical/numerical word tags (after '#')
                
                # Check for spaces first
                if ' ' in tag.lstrip('#'):
                    logger.debug("Filtered out tag '%s' due to containing spaces.", tag)
                    continue

                # Check for other common separators within the word
                if re.search(r'[_\-\.]', tag.lstrip('#')): # If it contains hyphen, underscore, or dot
                    logger.debug("Filtered out tag '%s' due to containing separators.", tag)
                    continue
                
                # Final check for alphanumeric single word
                if re.fullmatch(r'#[a-zA-Z0-9]+', tag):
                    tags_found.append(tag)
                else:
                    logger.debug("Filtered out tag '%s' due to not being a single alphanumeric word.", tag)


        except Exception as e:
            logger.warning("Error parsing frontmatter for tags: %s", e)
            return []
        
        return tags_found
