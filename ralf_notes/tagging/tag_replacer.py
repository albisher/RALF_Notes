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

    def _build_replacement_map(self) -> Dict[str, Optional[str]]:
        """Build old_tag -> new_tag mapping."""
        mapping: Dict[str, Optional[str]] = {}

        # Build from refinements
        for refinement in self.guide.get('refinements', []):
            new_tag = refinement['new_tag']
            for old_tag in refinement['old_tags']:
                mapping[old_tag] = new_tag
                logger.debug("Mapping old tag '%s' to new tag '%s' from refinement.", old_tag, new_tag)

        # Build from new_tags (merges)
        for new_tag_entry in self.guide.get('new_tags', []):
            new_tag = new_tag_entry['tag']
            for old_tag in new_tag_entry.get('merge_from', []):
                mapping[old_tag] = new_tag
                logger.debug("Mapping old tag '%s' to new tag '%s' from new_tags merge.", old_tag, new_tag)

        # Tags to delete map to None
        for delete_tag in self.guide.get('delete', []):
            mapping[delete_tag] = None
            logger.debug("Mapping tag '%s' for deletion.", delete_tag)

        return mapping

    def apply_refinements(self,
                          directory: Path,
                          dry_run: bool = False,
                          backup: bool = True) -> Dict[str, Any]:
        """
        Apply tag refinements to all markdown files.

        Args:
            directory: The directory containing markdown files.
            dry_run: If True, do not write changes to files.
            backup: If True, create a backup of the directory before making changes.

        Returns:
            Statistics about changes made.
        """
        results = {
            'files_processed': 0,
            'files_modified': 0,
            'tags_replaced': 0,
            'errors': [],
            'backup_path': None
        }

        if backup and not dry_run:
            backup_dir = directory.parent / f"{directory.name}_backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            try:
                shutil.copytree(directory, backup_dir)
                results['backup_path'] = str(backup_dir)
                logger.info("Created backup of '%s' at '%s'.", directory, backup_dir)
            except Exception as e:
                logger.error("Failed to create backup of directory '%s': %s", directory, e)
                results['errors'].append({'action': 'backup', 'error': str(e)})
                # Decide whether to proceed without backup or abort
                return results # Abort for safety

        logger.info("Applying tag refinements to files in directory: %s (Dry Run: %s)", directory, dry_run)

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
                                replacement = self.replacement_map[tag]
                                if replacement is None:
                                    fm_modified = True
                                    total_replaced += 1
                                elif replacement != tag:
                                    new_tags_set.add(replacement)
                                    fm_modified = True
                                    total_replaced += 1
                                else:
                                    new_tags_set.add(tag)
                            else:
                                new_tags_set.add(tag)
                        
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
        for old_tag, new_tag in self.replacement_map.items():
            if old_tag.lower() == "none": continue
            pattern = r'(?<![a-zA-Z0-9])' + re.escape(old_tag) + r'(?![a-zA-Z0-9])'
            
            if re.search(pattern, new_content):
                if new_tag:
                    new_content, count = re.subn(pattern, new_tag, new_content)
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
