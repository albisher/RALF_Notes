import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
import shutil
import datetime
import re

logger = logging.getLogger(__name__)

class LinkRefiner:
    """
    Box: Link Refiner

    Input: Directory + Refinement guide
    Output: Updated files
    Responsibility: Apply link fixes to all files
    """

    def __init__(self, guide: Dict[str, Any]):
        self.guide = guide
        # Group fixes by file for efficient processing
        self.file_fixes = {}
        for fix in guide.get('fixes', []):
            filename = fix['file']
            if filename not in self.file_fixes:
                self.file_fixes[filename] = []
            self.file_fixes[filename].append(fix)

    def apply_fixes(
                    self,
                    directory: Path,
                    dry_run: bool = False,
                    backup: bool = True) -> Dict[str, Any]:
        """Apply link fixes."""
        results = {
            'files_processed': 0,
            'files_modified': 0,
            'links_fixed': 0,
            'errors': [],
            'backup_path': None
        }

        if backup and not dry_run:
            backup_dir = directory.parent / f"{directory.name}_links_backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            try:
                shutil.copytree(directory, backup_dir)
                results['backup_path'] = str(backup_dir)
            except Exception as e:
                logger.error("Backup failed: %s", e)
                return results

        valid_links = set()

        for md_file in directory.glob('**/*.md'):
            if md_file.name == "applied_links.md": continue
            
            results['files_processed'] += 1
            filename = md_file.name
            
            try:
                content = md_file.read_text(encoding='utf-8')
                new_content = content
                modified = False
                
                # Apply fixes for this file
                if filename in self.file_fixes:
                    for fix in self.file_fixes[filename]:
                        old_link = fix['old']
                        new_link = fix['new']
                        
                        # Regex to match [[link]], [[link|alias]], etc.
                        # We want to replace just the target part
                        pattern = r'\[\[' + re.escape(old_link) + r'([|#][^\]]+)?\]\]'
                        
                        if new_link:
                            replacement = f'[[{new_link}\\1]]'
                            new_content, count = re.subn(pattern, replacement, new_content)
                        else:
                            # Removal
                            new_content, count = re.subn(pattern, '', new_content)
                        
                        if count > 0:
                            modified = True
                            results['links_fixed'] += count

                if modified and not dry_run:
                    md_file.write_text(new_content, encoding='utf-8')
                    results['files_modified'] += 1
                
                # Collect valid links from final content for the report
                # Pattern: [[link]]
                found_links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', new_content)
                for l in found_links:
                    valid_links.add(l.strip())

            except Exception as e:
                logger.error("Error processing %s: %s", filename, e)
                results['errors'].append({'file': filename, 'error': str(e)})

        # Save Report
        if not dry_run:
            self._save_report(directory, valid_links, self.guide.get('orphans', []), results)

        return results

    def _save_report(self, directory: Path, valid_links: set, orphans: List[str], results: dict):
        report_path = directory / "applied_links.md"
        
        sorted_links = sorted(list(valid_links))
        sorted_orphans = sorted(orphans)
        
        report_content = f"""# Applied Link Schema
**Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Files Processed:** {results['files_processed']}
**Links Fixed/Removed:** {results['links_fixed']}

## Active Wikilinks
{chr(10).join([f'- [[{l}]]' for l in sorted_links]) if sorted_links else "No active links."} 

## Orphan Files (Not linked to by any other file)
{chr(10).join([f'- {o}' for t in sorted_orphans]) if sorted_orphans else "No orphan files."} 
"""
        try:
            report_path.write_text(report_content, encoding='utf-8')
        except Exception as e:
            logger.error("Failed to save report: %s", e)
