import logging
from ollama import Client
from typing import Dict, Any, List
import json

logger = logging.getLogger(__name__)

class TagRefinementLLM:
    """
    Box: Tag Refinement LLM

    Input: Tag analysis report
    Output: Tag refinement suggestions from LLM
    Responsibility: Generate intelligent refinement recommendations
    """

    REFINEMENT_PROMPT = '''You are a documentation taxonomy expert. Analyze these tags used in a software documentation system.

**Tag Frequency (Top 50):**
{tag_list}

**Patterns Found:**
{patterns}

**Task:** Suggest tag refinements to improve organization and reduce redundancy.
**IMPORTANT TAGGING RULES:**
1. **No "none" tags:** Do not suggest or keep any tag that is or contains "none" (e.g., #none, #none-tag).
2. **Single-worded tags:** Tags must be a single word after the '#' prefix (e.g., #python, #feature).
3. **No separators in tags:** Tags must not contain spaces, hyphens, underscores, or other separators within the single word (e.g., NOT #data-processing, NOT #data_processing). If a concept requires multiple words, either find a single word equivalent or consider it a compound tag which should be suggested for merging into a single word, or removed.

**Output Format (JSON):**
{
  "refinements": [
    {
      "old_tags": ["#sensor-config", "#sensor-configuration"],
      "new_tag": "#sensorconfig",
      "reason": "Standardize naming, prefer shorter form and enforce single word rule"
    },
    {
      "old_tags": ["#data-processing", "#datahandler"],
      "new_tag": "#dataprocessing",
      "reason": "Consolidate related data operations and enforce single word rule"
    }
  ],
  "new_tags": [
    {
      "tag": "#corearchitecture",
      "reason": "Group all architectural tags",
      "merge_from": ["#architecture", "#design", "#structure"]
    }
  ],
  "keep_as_is": ["#python", "#typescript", "#api"],
  "delete": ["#temp", "#old", "#deprecated"]
}

**Guidelines:**
1. Strictly adhere to the **IMPORTANT TAGGING RULES** above.
2. Prefer shorter, clearer single-word tag names
3. Avoid overly specific tags (merge similar ones)
4. Keep language/framework tags (if single-worded)
5. Suggest hierarchies where appropriate (but new tags must be single-worded)
6. Confidence: high (clear duplicates/typos), medium (similar concepts), low (semantic relationships)'''

    def __init__(self, client: Client, model: str = "ministral-3:3b"):
        self.client = client
        self.model = model

    def generate_refinements(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use LLM to generate tag refinement suggestions.

        Args:
            analysis: Tag analysis report from TagAnalyzer.

        Returns:
            Refinement guide JSON.
        """
        logger.info("Generating tag refinement suggestions using LLM.")
        # Prepare tag list
        tag_freq = analysis.get('tag_frequency', {})
        sorted_tags = sorted(tag_freq.items(), key=lambda x: x[1], reverse=True)[:50]
        tag_list = '\n'.join([f"- {tag}: {count} uses" for tag, count in sorted_tags])

        # Prepare patterns
        patterns_text = self._format_patterns(analysis.get('patterns', []))

        # Build prompt
        prompt = self.REFINEMENT_PROMPT.format(
            tag_list=tag_list,
            patterns=patterns_text
        )
        logger.debug("LLM Refinement Prompt:\n%s", prompt)

        # Call LLM
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': 'You are a taxonomy expert. Respond only with valid JSON.'},
                    {'role': 'user', 'content': prompt}
                ],
                format='json',
                options={'temperature': 0.2}
            )

            # Parse JSON response
            refinement_guide = json.loads(response['message']['content'])
            logger.info("Successfully generated refinement guide from LLM.")
            return refinement_guide
        except json.JSONDecodeError as e:
            logger.error("LLM response was not valid JSON: %s", e)
            logger.error("Raw LLM response: %s", response.get('message', {}).get('content', 'N/A'))
            return self._fallback_guide(tag_freq, f"LLM response not valid JSON: {e}")
        except Exception as e:
            logger.error("Error calling LLM for tag refinements: %s", e)
            return self._fallback_guide(tag_freq, f"Error calling LLM: {e}")

    def _format_patterns(self, patterns: List) -> str:
        """Format patterns for prompt."""
        if not patterns:
            return "No patterns detected."

        text = []
        for p in patterns[:10]:  # Limit to top 10
            text.append(f"- {p.pattern_type}: {', '.join(p.tags[:5])} -> {p.suggestion}")
        return '\n'.join(text)

    def _fallback_guide(self, tag_freq: Dict[str, int], error_message: str) -> Dict[str, Any]:
        """Returns a fallback guide in case of LLM failure."""
        logger.warning("Returning fallback refinement guide due to error: %s", error_message)
        return {
            'refinements': [],
            'new_tags': [],
            'keep_as_is': list(tag_freq.keys()),
            'delete': [],
            'error': error_message
        }
