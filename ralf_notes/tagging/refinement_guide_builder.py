import logging
from pathlib import Path
from typing import Dict, Any
import json

logger = logging.getLogger(__name__)

class RefinementGuideBuilder:
    """
    Box: Refinement Guide Builder

    Input: LLM suggestions + Analysis
    Output: Final refinement guide (JSON)
    Responsibility: Combine and validate refinement recommendations
    """

    def build_guide(self,
                    llm_suggestions: Dict[str, Any],
                    analysis: Dict[str, Any],
                    output_path: Path) -> Dict[str, Any]:
        """
        Build final refinement guide.

        Args:
            llm_suggestions: Dictionary of tag refinement suggestions from LLM.
            analysis: Tag analysis report from TagAnalyzer.
            output_path: Path to save the refinement guide JSON.

        Returns:
            The complete refinement guide JSON.
        """
        logger.info("Building refinement guide.")
        guide = {
            'version': '1.0',
            'generated_at': str(Path.cwd()),
            'total_tags_analyzed': len(analysis.get('tag_frequency', {})),
            'refinements': llm_suggestions.get('refinements', []),
            'new_tags': llm_suggestions.get('new_tags', []),
            'keep_as_is': llm_suggestions.get('keep_as_is', []),
            'delete': llm_suggestions.get('delete', []),
            'statistics': analysis.get('statistics', {}),
            'patterns_found': analysis.get('total_patterns', 0), # Corrected from len(analysis.get('patterns', []))
            'llm_error': llm_suggestions.get('error', None) # Include LLM error if any
        }

        # Save guide
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(guide, indent=2), encoding='utf-8')
            logger.info("Refinement guide saved to: %s", output_path)
        except Exception as e:
            logger.error("Error saving refinement guide to %s: %s", output_path, e)
            guide['save_error'] = str(e) # Add save error to guide
            
        return guide
