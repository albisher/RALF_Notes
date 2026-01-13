import logging
from typing import Dict, List, Any, Set, Optional
from pathlib import Path
import difflib

logger = logging.getLogger(__name__)

class LinkResolver:
    """
    Box: Link Resolver

    Input: Link map and file index
    Output: Refinement guide (suggested fixes)
    Responsibility: Identify broken links and suggest corrections
    """

    def resolve_links(self, link_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze links and find broken ones.

        Returns:
            {
                'fixes': [{'file': 'doc.md', 'old': 'link', 'new': 'target.md'}, ...],
                'orphans': ['file3.md', ...],
                'broken_count': 5
            }
        """
        link_map = link_data['link_map']
        file_index = link_data['file_index']
        
        # Clean file index for easier matching (no extension)
        clean_file_index = {Path(f).stem: f for f in file_index}
        
        fixes = []
        broken_count = 0
        none_count = 0
        
        referenced_files = set()

        for source_file, links in link_map.items():
            for link in links:
                # 1. Check for "none"
                if link.lower() in ['none', 'null', 'nan']:
                    fixes.append({
                        'file': source_file,
                        'old': link,
                        'new': None, # Suggest removal
                        'reason': 'None link'
                    })
                    none_count += 1
                    continue

                # 2. Check if link exists
                # Try exact match, then stem match
                if link in file_index or f"{link}.md" in file_index:
                    referenced_files.add(link if link.endswith('.md') else f"{link}.md")
                    continue
                
                if link in clean_file_index:
                    target = clean_file_index[link]
                    fixes.append({
                        'file': source_file,
                        'old': link,
                        'new': Path(target).stem,
                        'reason': 'Extension fix'
                    })
                    referenced_files.add(target)
                    continue

                # 3. Fuzzy matching
                suggestions = difflib.get_close_matches(link, clean_file_index.keys(), n=1, cutoff=0.6)
                if suggestions:
                    target_stem = suggestions[0]
                    fixes.append({
                        'file': source_file,
                        'old': link,
                        'new': target_stem,
                        'reason': 'Fuzzy match'
                    })
                    referenced_files.add(clean_file_index[target_stem])
                    broken_count += 1
                else:
                    # Mark as broken with no suggestion
                    fixes.append({
                        'file': source_file,
                        'old': link,
                        'new': None,
                        'reason': 'No target found'
                    })
                    broken_count += 1

        # Identify orphans (files in index that are never referenced)
        orphans = [f for f in file_index if f not in referenced_files]

        return {
            'fixes': fixes,
            'orphans': orphans,
            'broken_count': broken_count,
            'none_count': none_count,
            'total_files': link_data['total_files']
        }
