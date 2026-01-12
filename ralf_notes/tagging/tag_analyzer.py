import logging
from typing import Dict, List, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class TagPattern:
    """Represents a pattern found in tags."""
    pattern_type: str  # 'prefix', 'suffix', 'compound', 'similar'
    tags: List[str]
    suggestion: str
    confidence: float

class TagAnalyzer:
    """
    Box: Tag Analyzer

    Input: Tag frequency map
    Output: Analysis report with patterns
    Responsibility: Identify tag patterns and grouping opportunities
    """

    def analyze(self, tag_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze tags for patterns and issues.

        Args:
            tag_data: Dictionary containing 'tag_frequency', 'tag_to_files', etc.

        Returns:
            {
                'patterns': [TagPattern, ...],
                'statistics': {...},
                'total_patterns': int
            }
        """
        logger.info("Starting tag analysis.")
        tag_frequency = tag_data.get('tag_frequency', {})
        
        patterns = []

        # 1. Find compound tags (e.g., #sensor-configuration, #sensor-data)
        logger.debug("Finding compound tag patterns.")
        patterns.extend(self._find_compound_patterns(tag_frequency))

        # 2. Find similar tags (e.g., #config vs #configuration)
        logger.debug("Finding similar tags.")
        patterns.extend(self._find_similar_tags(tag_frequency))

        # 3. Find rare vs common tags statistics
        logger.debug("Calculating tag usage statistics.")
        stats = self._calculate_statistics(tag_frequency)

        # 4. Find hierarchical opportunities - currently a placeholder
        logger.debug("Finding hierarchical opportunities (placeholder).")
        patterns.extend(self._find_hierarchies(tag_frequency))

        logger.info("Finished tag analysis. Found %d patterns.", len(patterns))
        return {
            'patterns': patterns,
            'statistics': stats,
            'total_patterns': len(patterns)
        }

    def _find_compound_patterns(self, tag_freq: Dict[str, int]) -> List[TagPattern]:
        """Find tags with common prefixes/suffixes."""
        patterns = []
        prefixes = {}

        for tag in tag_freq.keys():
            # Remove # and split on -
            clean = tag.lstrip('#')
            if '-' in clean:
                prefix = clean.split('-')[0]
                if prefix not in prefixes:
                    prefixes[prefix] = []
                prefixes[prefix].append(tag)

        # Find prefixes with 2+ tags
        for prefix, tags in prefixes.items():
            if len(tags) >= 2:
                patterns.append(TagPattern(
                    pattern_type='compound',
                    tags=tags,
                    suggestion=f"Group under #{prefix}",
                    confidence=0.8
                ))
                logger.debug("Found compound pattern: prefix '%s' for tags %s", prefix, tags)

        return patterns

    def _find_similar_tags(self, tag_freq: Dict[str, int]) -> List[TagPattern]:
        """Find tags that are variations of each other."""
        patterns = []
        tags = list(tag_freq.keys())

        # Simple similarity: check for substring matches
        for i, tag1 in enumerate(tags):
            similar = []
            clean1 = tag1.lstrip('#').lower()

            for j, tag2 in enumerate(tags):
                if i >= j:
                    continue

                clean2 = tag2.lstrip('#').lower()

                # Check if one is substring of other
                if (clean1 in clean2 and len(clean1) > 2) or (clean2 in clean1 and len(clean2) > 2): # Avoid very short substrings
                    similar.append(tag2)

            if similar:
                similar.append(tag1)
                patterns.append(TagPattern(
                    pattern_type='similar',
                    tags=similar,
                    suggestion=f"Consider standardizing to one tag",
                    confidence=0.7
                ))
                logger.debug("Found similar tags pattern: %s", similar)

        return patterns

    def _find_hierarchies(self, tag_freq: Dict[str, int]) -> List[TagPattern]:
        """Find potential parent-child tag relationships (placeholder)."""
        # Advanced: Use word embeddings or LLM to find semantic relationships
        # For now, simple heuristic
        return []

    def _calculate_statistics(self, tag_freq: Dict[str, int]) -> Dict[str, Any]:
        """Calculate tag usage statistics."""
        counts = list(tag_freq.values())
        if not counts:
            return {
                'mean_usage': 0,
                'max_usage': 0,
                'min_usage': 0,
                'rare_tags': [],
                'common_tags': []
            }
        
        stats = {
            'mean_usage': sum(counts) / len(counts),
            'max_usage': max(counts),
            'min_usage': min(counts),
            'rare_tags': [tag for tag, count in tag_freq.items() if count == 1],
            'common_tags': [tag for tag, count in tag_freq.items() if count >= 20] # Threshold of 20 for common tags
        }
        logger.debug("Tag usage statistics calculated: %s", stats)
        return stats