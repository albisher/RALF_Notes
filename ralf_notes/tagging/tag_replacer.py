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

        for md_file in directory.glob('**/*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                new_content, modified, replaced_count = self._replace_tags_in_file(content)

                results['files_processed'] += 1

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
        
        logger.info("Finished applying tag refinements.")
        return results

    def _replace_tags_in_file(self, content: str) -> tuple[str, bool, int]:
        """
        Replace tags in file content.

        Returns: (new_content, was_modified, tags_replaced_count)
        """
        if not content.startswith('---'):
            return content, False, 0

        # Find frontmatter boundaries
        end_idx = content.find('---', 3)
        if end_idx == -1:
            return content, False, 0

        frontmatter_yaml_block = content[3:end_idx].strip()
        body = content[end_idx + 3:]

        try:
            data = yaml.safe_load(frontmatter_yaml_block)
            if not data or 'tags' not in data:
                return content, False, 0

            # Get current tags
            current_tags = self._parse_tags(data['tags'])

            # Apply replacements
            new_tags_set: Set[str] = set() # Use a set to avoid duplicate tags
            modified = False
            replaced_count = 0

            for tag in current_tags:
                if tag in self.replacement_map:
                    replacement = self.replacement_map[tag]
                    if replacement is None: # Tag marked for deletion
                        modified = True
                        replaced_count += 1
                        logger.debug("Deleting tag '%s'.", tag)
                    elif replacement != tag: # Tag marked for replacement
                        new_tags_set.add(replacement)
                        modified = True
                        replaced_count += 1
                        logger.debug("Replacing tag '%s' with '%s'.", tag, replacement)
                    else: # Tag is in map but maps to itself (keep as is explicitly)
                        new_tags_set.add(tag)
                else: # Tag not in map, keep as is
                    new_tags_set.add(tag)
            
            # Sort new tags for consistent output
            final_tags = sorted(list(new_tags_set))

            if not modified:
                return content, False, 0

            # Rebuild frontmatter
            data['tags'] = final_tags # Ensure tags are stored as a list for cleaner YAML
            new_frontmatter = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False).strip() # Preserve order if possible
            new_content = f"---\n{new_frontmatter}\n---{body}"

            return new_content, True, replaced_count
        except Exception as e:
            logger.error("Error processing frontmatter in file content: %s", e)
            return content, False, 0 # Return original content on error

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
