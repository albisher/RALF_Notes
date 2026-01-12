# Tag Refinement System Design

**Date:** 2026-01-11
**Purpose:** Design system for analyzing and refining tags across all generated documentation
**Status:** 📋 Design Phase
**Priority:** 🟢 Enhancement (Phase 9)

---

## Problem Statement

### User Observation

After generating 462 files, noticed tags like:
- `#sensor-configuration`
- `#sensor-data`
- `#configuration-management`
- `#data-processing`

**Issue:** Similar/redundant tags that could be consolidated for better organization

**Goal:** Intelligent tag refinement system that:
1. Collects all tags from generated files
2. Analyzes for patterns, duplicates, and grouping opportunities
3. Suggests refinements via LLM
4. Applies refinements across all files

---

## System Architecture

### 2-Phase Approach

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1: Tag Analysis & Refinement Guide Generation            │
├─────────────────────────────────────────────────────────────────┤
│ Input:  All generated markdown files                            │
│ Output: Tag refinement guide (JSON)                             │
│                                                                   │
│ Flow:  Collect Tags → Analyze → LLM Suggestions → Guide         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Phase 2: Tag Application (Apply Refinements)                   │
├─────────────────────────────────────────────────────────────────┤
│ Input:  Files + Tag refinement guide                            │
│ Output: Updated files with refined tags                         │
│                                                                   │
│ Flow:  Read Files → Replace Tags → Write Files                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Tag Analysis & Guide Generation

### 1.1 Tag Collector Box

```
Box: Tag Collector

Input: Directory of markdown files
Output: Tag frequency map
Responsibility: Extract all tags from YAML frontmatter
```

**Implementation:**

```python
from pathlib import Path
from typing import Dict, List, Set
from collections import Counter
import yaml

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
                # Log error, continue processing
                pass

        return {
            'tag_frequency': dict(tag_frequency),
            'tag_to_files': tag_to_files,
            'total_files': file_count,
            'total_unique_tags': len(tag_frequency)
        }

    def _extract_tags_from_frontmatter(self, content: str) -> List[str]:
        """Extract tags from YAML frontmatter."""
        if not content.startswith('---'):
            return []

        try:
            # Find end of frontmatter
            end_idx = content.find('---', 3)
            if end_idx == -1:
                return []

            # Parse YAML
            frontmatter = content[3:end_idx].strip()
            data = yaml.safe_load(frontmatter)

            if not data or 'tags' not in data:
                return []

            # Handle both "tag1, tag2" and ["tag1", "tag2"] formats
            tags_str = data['tags']
            if isinstance(tags_str, list):
                return tags_str
            elif isinstance(tags_str, str):
                return [tag.strip() for tag in tags_str.split(',')]
            else:
                return []
        except Exception:
            return []
```

---

### 1.2 Tag Analyzer Box

```
Box: Tag Analyzer

Input: Tag frequency map
Output: Tag analysis report
Responsibility: Identify patterns, clusters, and redundancies
```

**Implementation:**

```python
from typing import Dict, List, Any
from dataclasses import dataclass

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

        Returns:
            {
                'patterns': [TagPattern, ...],
                'statistics': {...},
                'recommendations': [...]
            }
        """
        tag_frequency = tag_data['tag_frequency']

        patterns = []

        # 1. Find compound tags (e.g., #sensor-configuration, #sensor-data)
        patterns.extend(self._find_compound_patterns(tag_frequency))

        # 2. Find similar tags (e.g., #config vs #configuration)
        patterns.extend(self._find_similar_tags(tag_frequency))

        # 3. Find rare vs common tags
        stats = self._calculate_statistics(tag_frequency)

        # 4. Find hierarchical opportunities
        patterns.extend(self._find_hierarchies(tag_frequency))

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
                if clean1 in clean2 or clean2 in clean1:
                    similar.append(tag2)

            if similar:
                similar.append(tag1)
                patterns.append(TagPattern(
                    pattern_type='similar',
                    tags=similar,
                    suggestion=f"Consider standardizing to one tag",
                    confidence=0.7
                ))

        return patterns

    def _find_hierarchies(self, tag_freq: Dict[str, int]) -> List[TagPattern]:
        """Find potential parent-child tag relationships."""
        # Advanced: Use word embeddings or LLM to find semantic relationships
        # For now, simple heuristic
        return []

    def _calculate_statistics(self, tag_freq: Dict[str, int]) -> Dict[str, Any]:
        """Calculate tag usage statistics."""
        counts = list(tag_freq.values())
        return {
            'mean_usage': sum(counts) / len(counts) if counts else 0,
            'max_usage': max(counts) if counts else 0,
            'min_usage': min(counts) if counts else 0,
            'rare_tags': [tag for tag, count in tag_freq.items() if count == 1],
            'common_tags': [tag for tag, count in tag_freq.items() if count >= 20]
        }
```

---

### 1.3 Tag Refinement LLM Box

```
Box: Tag Refinement LLM

Input: Tag analysis report
Output: LLM-suggested refinement guide
Responsibility: Use LLM to suggest intelligent tag refinements
```

**Implementation:**

```python
from ollama import Client
from typing import Dict, Any, List
import json

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

**Output Format (JSON):**
{{
  "refinements": [
    {{
      "old_tags": ["#sensor-config", "#sensor-configuration"],
      "new_tag": "#sensor-config",
      "reason": "Standardize naming, prefer shorter form",
      "confidence": "high"
    }},
    {{
      "old_tags": ["#data-processing", "#data-handler", "#data-management"],
      "new_tag": "#data-processing",
      "reason": "Consolidate related data operations",
      "confidence": "medium"
    }}
  ],
  "new_tags": [
    {{
      "tag": "#core-architecture",
      "reason": "Group all architectural tags",
      "merge_from": ["#architecture", "#design", "#structure"]
    }}
  ],
  "keep_as_is": ["#python", "#typescript", "#api"],
  "delete": ["#temp", "#old", "#deprecated"]
}}

**Guidelines:**
1. Prefer shorter, clearer tag names
2. Use hyphens for compound tags (#data-processing)
3. Avoid overly specific tags (merge similar ones)
4. Keep language/framework tags (#python, #javascript)
5. Suggest hierarchies where appropriate
6. High confidence: Clear duplicates/typos
7. Medium confidence: Similar concepts
8. Low confidence: Semantic relationships'''

    def __init__(self, client: Client, model: str = "ministral-3:3b"):
        self.client = client
        self.model = model

    def generate_refinements(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use LLM to generate tag refinement suggestions.

        Returns refinement guide JSON.
        """
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
            return refinement_guide
        except Exception as e:
            # Return fallback guide
            return {
                'refinements': [],
                'new_tags': [],
                'keep_as_is': list(tag_freq.keys()),
                'delete': [],
                'error': str(e)
            }

    def _format_patterns(self, patterns: List) -> str:
        """Format patterns for prompt."""
        if not patterns:
            return "No patterns detected."

        text = []
        for p in patterns[:10]:  # Limit to top 10
            text.append(f"- {p.pattern_type}: {', '.join(p.tags[:5])} → {p.suggestion}")
        return '\n'.join(text)
```

---

### 1.4 Refinement Guide Builder Box

```
Box: Refinement Guide Builder

Input: LLM suggestions + Analysis
Output: Final refinement guide (JSON)
Responsibility: Combine and validate refinement recommendations
```

**Implementation:**

```python
from pathlib import Path
from typing import Dict, Any
import json

class RefinementGuideBuilder:
    """
    Box: Refinement Guide Builder

    Input: LLM suggestions, tag analysis
    Output: Validated refinement guide
    Responsibility: Build and save refinement guide
    """

    def build_guide(self,
                    llm_suggestions: Dict[str, Any],
                    analysis: Dict[str, Any],
                    output_path: Path) -> Dict[str, Any]:
        """
        Build final refinement guide.

        Returns guide and saves to JSON.
        """
        guide = {
            'version': '1.0',
            'generated_at': str(Path.cwd()),
            'total_tags_analyzed': len(analysis.get('tag_frequency', {})),
            'refinements': llm_suggestions.get('refinements', []),
            'new_tags': llm_suggestions.get('new_tags', []),
            'keep_as_is': llm_suggestions.get('keep_as_is', []),
            'delete': llm_suggestions.get('delete', []),
            'statistics': analysis.get('statistics', {}),
            'patterns_found': len(analysis.get('patterns', []))
        }

        # Save guide
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(guide, indent=2), encoding='utf-8')

        return guide
```

---

## Phase 2: Tag Application

### 2.1 Tag Replacer Box

```
Box: Tag Replacer

Input: Files + Refinement guide
Output: Updated files
Responsibility: Apply tag refinements to all files
```

**Implementation:**

```python
from pathlib import Path
from typing import Dict, List, Any
import yaml

class TagReplacer:
    """
    Box: Tag Replacer

    Input: Directory + Refinement guide
    Output: Files with updated tags
    Responsibility: Apply tag replacements across all files
    """

    def __init__(self, guide: Dict[str, Any]):
        self.guide = guide
        self.replacement_map = self._build_replacement_map()

    def _build_replacement_map(self) -> Dict[str, str]:
        """Build old_tag -> new_tag mapping."""
        mapping = {}

        # Build from refinements
        for refinement in self.guide.get('refinements', []):
            new_tag = refinement['new_tag']
            for old_tag in refinement['old_tags']:
                mapping[old_tag] = new_tag

        # Build from new_tags (merges)
        for new_tag_entry in self.guide.get('new_tags', []):
            new_tag = new_tag_entry['tag']
            for old_tag in new_tag_entry.get('merge_from', []):
                mapping[old_tag] = new_tag

        # Tags to delete map to None
        for delete_tag in self.guide.get('delete', []):
            mapping[delete_tag] = None

        return mapping

    def apply_refinements(self,
                          directory: Path,
                          dry_run: bool = False) -> Dict[str, Any]:
        """
        Apply tag refinements to all markdown files.

        Returns statistics about changes made.
        """
        results = {
            'files_processed': 0,
            'files_modified': 0,
            'tags_replaced': 0,
            'errors': []
        }

        for md_file in directory.glob('**/*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                new_content, modified = self._replace_tags_in_file(content)

                results['files_processed'] += 1

                if modified:
                    results['files_modified'] += 1
                    if not dry_run:
                        md_file.write_text(new_content, encoding='utf-8')
            except Exception as e:
                results['errors'].append({
                    'file': str(md_file),
                    'error': str(e)
                })

        return results

    def _replace_tags_in_file(self, content: str) -> tuple[str, bool]:
        """
        Replace tags in file content.

        Returns: (new_content, was_modified)
        """
        if not content.startswith('---'):
            return content, False

        # Find frontmatter boundaries
        end_idx = content.find('---', 3)
        if end_idx == -1:
            return content, False

        frontmatter = content[3:end_idx].strip()
        body = content[end_idx + 3:]

        try:
            data = yaml.safe_load(frontmatter)
            if not data or 'tags' not in data:
                return content, False

            # Get current tags
            current_tags = self._parse_tags(data['tags'])

            # Apply replacements
            new_tags = []
            modified = False

            for tag in current_tags:
                if tag in self.replacement_map:
                    replacement = self.replacement_map[tag]
                    if replacement is None:
                        # Delete tag
                        modified = True
                        continue
                    elif replacement != tag:
                        # Replace tag
                        new_tags.append(replacement)
                        modified = True
                    else:
                        new_tags.append(tag)
                else:
                    new_tags.append(tag)

            if not modified:
                return content, False

            # Rebuild frontmatter
            data['tags'] = ', '.join(new_tags)
            new_frontmatter = yaml.dump(data, default_flow_style=False, allow_unicode=True).strip()
            new_content = f"---\n{new_frontmatter}\n---{body}"

            return new_content, True
        except Exception:
            return content, False

    def _parse_tags(self, tags_value: Any) -> List[str]:
        """Parse tags from YAML value."""
        if isinstance(tags_value, list):
            return tags_value
        elif isinstance(tags_value, str):
            return [t.strip() for t in tags_value.split(',')]
        else:
            return []
```

---

## CLI Commands

### Command 1: Analyze Tags

```bash
ralf-notes tags analyze [TARGET_DIR] --output guide.json
```

**What it does:**
1. Collects all tags from markdown files
2. Analyzes for patterns
3. Calls LLM for refinement suggestions
4. Saves refinement guide to JSON

**Options:**
- `--model`: LLM model to use (default: ministral-3:3b)
- `--output`: Output JSON file (default: tag_refinement_guide.json)
- `--max-tags`: Max tags to send to LLM (default: 100)

### Command 2: Apply Tag Refinements

```bash
ralf-notes tags apply [TARGET_DIR] --guide guide.json
```

**What it does:**
1. Loads refinement guide
2. Applies tag replacements to all files
3. Shows summary of changes

**Options:**
- `--guide`: Path to refinement guide JSON (required)
- `--dry-run`: Preview changes without writing
- `--backup`: Create backup before modifying (default: true)

### Command 3: Show Tag Statistics

```bash
ralf-notes tags stats [TARGET_DIR]
```

**What it does:**
- Shows tag frequency
- Most/least used tags
- Files per tag

---

## Example Workflow

### Step 1: Generate Documentation
```bash
ralf-notes generate ~/my-project
# → Generates 462 files with tags
```

### Step 2: Analyze Tags
```bash
ralf-notes tags analyze ~/to_obsidian --output tag_guide.json
```

**Output:**
```
📊 Tag Analysis Results

Total files analyzed: 462
Total unique tags: 127

Patterns found: 23
- Compound tags: 8 groups
- Similar tags: 12 groups
- Rare tags (1 use): 34

🤖 LLM Analysis complete
Refinement guide saved: tag_guide.json

Suggestions:
✅ 45 tag refinements (high confidence)
⚠️  18 tag refinements (medium confidence)
🗑️  12 tags to delete

Review tag_guide.json before applying.
```

### Step 3: Review Guide
```bash
cat tag_guide.json
```

```json
{
  "refinements": [
    {
      "old_tags": ["#sensor-config", "#sensor-configuration"],
      "new_tag": "#sensor-config",
      "reason": "Standardize naming, prefer shorter form",
      "confidence": "high"
    }
  ]
}
```

### Step 4: Apply Refinements
```bash
# Preview first
ralf-notes tags apply ~/to_obsidian --guide tag_guide.json --dry-run

# Apply if looks good
ralf-notes tags apply ~/to_obsidian --guide tag_guide.json
```

**Output:**
```
🏷️  Applying Tag Refinements

Files processed: 462
Files modified: 287
Tags replaced: 456
Backup created: ~/to_obsidian_backup_20260111

✅ Tag refinement complete!
```

### Step 5: Verify
```bash
ralf-notes tags stats ~/to_obsidian
```

**Shows updated tag distribution**

---

## Implementation Plan

### Phase 1: Core Boxes (Week 1)
- [ ] Implement TagCollector
- [ ] Implement TagAnalyzer
- [ ] Implement TagRefinementLLM
- [ ] Implement RefinementGuideBuilder
- [ ] Add `tags analyze` command

### Phase 2: Application (Week 2)
- [ ] Implement TagReplacer
- [ ] Add `tags apply` command
- [ ] Add `tags stats` command
- [ ] Add backup mechanism

### Phase 3: Polish (Week 3)
- [ ] Add comprehensive tests
- [ ] Add progress bars
- [ ] Add detailed logging
- [ ] Update documentation
- [ ] Add examples

---

## Testing Strategy

### Unit Tests
- Test tag extraction from various frontmatter formats
- Test pattern detection algorithms
- Test tag replacement logic
- Test JSON guide validation

### Integration Tests
- Test full analyze → apply workflow
- Test with 100+ files
- Test with various tag formats
- Test error handling

### Edge Cases
- Empty frontmatter
- Malformed YAML
- Unicode in tags
- Very long tag lists
- Circular refinements

---

## Benefits

### For Users
- ✅ Cleaner, more consistent tags
- ✅ Better Obsidian navigation
- ✅ Reduced redundancy
- ✅ AI-powered suggestions

### For Codebase
- ✅ Follows Boxes methodology
- ✅ Testable, modular design
- ✅ Reusable components
- ✅ CLI-first approach

---

## Future Enhancements

### V2 Features
1. **Interactive Mode** - User approves each suggestion
2. **Tag Hierarchies** - Support nested tags (#backend/api/rest)
3. **Semantic Analysis** - Use embeddings for similarity
4. **Tag Templates** - Predefined tag sets by language/domain
5. **Undo Command** - Revert tag changes

---

## Conclusion

This tag refinement system provides:
- 🎯 **Intelligent analysis** of tag usage
- 🤖 **LLM-powered suggestions** for improvements
- ⚡ **Automated application** of refinements
- 📊 **Statistics and insights** into tag distribution

**Status:** Design complete, ready for Phase 9 implementation

---

**Document Version:** 1.0
**Date:** 2026-01-11
**Type:** Enhancement Design
**Phase:** 9 (Advanced Features)
