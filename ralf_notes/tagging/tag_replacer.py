import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
import yaml
import shutil
import datetime

logger = logging.getLogger(__name__)

class TagReplacer:
    """
    Box: Tag Replacer

    Input: Directory + Refinement guide
    Output: Updated files
    Responsibility: Apply tag refinements to all files
    """

    def __init__(self, guide: Dict[str, Any]):
        self.guide = guide
        self.replacement_map = self._build_replacement_map()
        logger.info("TagReplacer initialized with %d replacements.", len(self.replacement_map))

    def _build_replacement_map(self) -> Dict[str, Optional[List[str]]]:
        """Build old_tag -> [new_tag1, new_tag2] mapping."""
        mapping: Dict[str, Optional[List[str]]] = {}

        # Build from refinements
        for refinement in self.guide.get('refinements', []):
            new_tag = refinement.get('new_tags') # Prefer new_tags list
            if not new_tag:
                new_tag_str = refinement.get('new_tag') # Fallback to single string
                if new_tag_str:
                    new_tag = [new_tag_str]
            
            if new_tag:
                for old_tag in refinement['old_tags']:
                    mapping[old_tag] = new_tag
                    logger.debug("Mapping old tag '%s' to new tags '%s' from refinement.", old_tag, new_tag)

        # Build from new_tags (merges)
        for new_tag_entry in self.guide.get('new_tags', []):
            new_tag_str = new_tag_entry['tag']
            new_tag_list = [new_tag_str]
            for old_tag in new_tag_entry.get('merge_from', []):
                mapping[old_tag] = new_tag_list
                logger.debug("Mapping old tag '%s' to new tag '%s' from new_tags merge.", old_tag, new_tag_str)

        # Tags to delete map to None
        for delete_tag in self.guide.get('delete', []):
            mapping[delete_tag] = None
            logger.debug("Mapping tag '%s' for deletion.", delete_tag)

        return mapping

    def apply_refinements(self,
                          directory: Path,
                          dry_run: bool = False,
                          backup: bool = True) -> Dict[str, Any]:
        # ... (rest of method same as previous state)
        logger.info("Applying tag refinements to files in directory: %s (Dry Run: %s)", directory, dry_run)

        results = {
            'files_processed': 0,
            'files_modified': 0,
            'tags_replaced': 0,
            'errors': [],
            'backup_path': None
        }

        final_unique_tags = set()

        for md_file in directory.glob('**/*.md'):
            # Skip the report file itself if it exists
            if md_file.name == "applied_tags.md": continue

            try:
                content = md_file.read_text(encoding='utf-8')
                new_content, modified, replaced_count, current_file_tags = self._replace_tags_in_file(content)

                results['files_processed'] += 1
                
                # Collect tags for final report
                for t in current_file_tags:
                    final_unique_tags.add(t)

                if modified:
                    results['files_modified'] += 1
                    results['tags_replaced'] += replaced_count
                    if not dry_run:
                        md_file.write_text(new_content, encoding='utf-8')
                        logger.debug("Modified file: %s", md_file)
                    else:
                        logger.debug("Dry run: Would modify file: %s", md_file)

            except Exception as e:
                logger.error("Error applying refinements to file %s: %s", md_file, e)
                results['errors'].append({
                    'file': str(md_file),
                    'error': str(e)
                })
        
        # Save applied tags report (Unique tags list)
        if final_unique_tags and not dry_run:
            report_path = directory / "applied_tags.md"
            sorted_tags = sorted(list(final_unique_tags))
            
            report_content = f"""# Applied Tag Schema
**Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Unique Tags:** {len(sorted_tags)}
**Files Processed:** {results['files_processed']}

## Tag List
{chr(10).join([f"- {t}" for t in sorted_tags])}
"""
            try:
                report_path.write_text(report_content, encoding='utf-8')
                logger.info("Saved applied tags report to: %s", report_path)
            except Exception as e:
                logger.error("Failed to save applied tags report: %s", e)

        logger.info("Finished applying tag refinements.")
        return results

    def _replace_tags_in_file(self, content: str) -> tuple[str, bool, int, List[str]]:
        """
        Replace tags in file content (frontmatter and body).

        Returns: (new_content, was_modified, tags_replaced_count, final_tags_list)
        """
        import re
        modified = False
        total_replaced = 0
        new_content = content
        final_tags = set()

        # 1. Process Frontmatter
        if content.startswith('---'):
            end_idx = content.find('---', 3)
            if end_idx != -1:
                frontmatter_yaml_block = content[3:end_idx].strip()
                body = content[end_idx + 3:]
                try:
                    data = yaml.safe_load(frontmatter_yaml_block)
                    if data and 'tags' in data:
                        current_tags = self._parse_tags(data['tags'])
                        new_tags_set = set()
                        fm_modified = False
                        
                        for tag in current_tags:
                            # Filter "none" explicitly
                            if tag.lower() in ["none", "#none"]:
                                fm_modified = True
                                continue

                            if tag in self.replacement_map:
                                replacements = self.replacement_map[tag]
                                if replacements is None: # Deletion
                                    fm_modified = True
                                    total_replaced += 1
                                else: # Replacement list
                                    # Sanitize new tags before adding
                                    sanitized_replacements = []
                                    for r in replacements:
                                        sanitized_replacements.extend(self._sanitize_tag(r))
                                    
                                    # Check if replacement is actually different
                                    if len(sanitized_replacements) == 1 and sanitized_replacements[0] == tag:
                                        new_tags_set.add(tag)
                                    else:
                                        for r in sanitized_replacements:
                                            new_tags_set.add(r)
                                        fm_modified = True
                                        total_replaced += 1
                            else:
                                # Sanitize existing tags too!
                                sanitized_existing = self._sanitize_tag(tag)
                                if len(sanitized_existing) == 1 and sanitized_existing[0] == tag:
                                    new_tags_set.add(tag)
                                else:
                                    for r in sanitized_existing: new_tags_set.add(r)
                                    fm_modified = True
                        
                        if fm_modified:
                            sorted_fm_tags = sorted(list(new_tags_set))
                            data['tags'] = sorted_fm_tags
                            new_frontmatter = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
                            new_content = f"---\n{new_frontmatter}\n---{body}"
                            modified = True
                            for t in sorted_fm_tags: final_tags.add(t)
                        else:
                            for t in current_tags: final_tags.add(t)
                except Exception as e:
                    logger.error("Error processing frontmatter: %s", e)

        # 2. Process Body (Global replacement)
        for old_tag, new_tags_list in self.replacement_map.items():
            if old_tag.lower() == "none": continue
            pattern = r'(?<![a-zA-Z0-9])' + re.escape(old_tag) + r'(?![a-zA-Z0-9])'
            
            if re.search(pattern, new_content):
                if new_tags_list:
                    # For body text, if replacing one tag with multiple, join them with spaces
                    # Sanitize replacement tags first
                    sanitized_list = []
                    for t in new_tags_list: sanitized_list.extend(self._sanitize_tag(t))
                    replacement_str = ' '.join(sanitized_list)
                    new_content, count = re.subn(pattern, replacement_str, new_content)
                else:
                    new_content, count = re.subn(pattern, '', new_content)
                    new_content = re.sub(r',\s*,', ',', new_content)
                
                if count > 0:
                    modified = True

        # Extract all tags from the final content to return the complete set for this file
        from .tag_collector import TagCollector
        collector = TagCollector()
        final_tags = collector._extract_tags(new_content)
        
        return new_content, modified, total_replaced, final_tags

    def _sanitize_tag(self, tag: str) -> List[str]:
        """
        Enforce single-word, no-separator, singular rules.
        Splits tags like #data-processing into [#data, #processing].
        Removes separators like _ and -.
        Naively singularizes tags.
        """
        clean_tag = tag.strip().lower()
        if not clean_tag.startswith('#'):
            clean_tag = f'#{clean_tag}'
        
        # Remove # for processing
        body = clean_tag[1:]
        
        # Split by common separators
        parts = re.split(r'[-_]', body)
        
        # Filter empty parts
        valid_parts = [p for p in parts if p]
        
        sanitized = []
        for part in valid_parts:
            # Naive singularization: remove 's' at end if word is long enough
            # Avoid changing words like 'bus', 'process', 'status', 'analysis'
            if len(part) > 3 and part.endswith('s') and not part.endswith(('ss', 'is', 'us')):
                part = part[:-1]
            
            sanitized.append(f"#{part}")
            
        if not sanitized:
            return []
            
        return sanitized


    def _parse_tags(self, tags_value: Any) -> List[str]:
        """Parse tags from YAML value (supports list or comma-separated string)."""
        if isinstance(tags_value, list):
            return tags_value
        elif isinstance(tags_value, str):
            # Split by comma and strip whitespace for each tag
            return [t.strip() for t in tags_value.split(',') if t.strip()]
        else:
            logger.info("Unexpected tags format: %s. Expected list or string.", type(tags_value))
            return []
