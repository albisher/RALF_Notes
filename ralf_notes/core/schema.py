"""
Box: Text Schema Definition

Responsibility: Define and store the unified Text schema and system prompt
"""

# System prompt for unified TEXT generation
UNIFIED_SYSTEM_PROMPT = '''Analyze this code file. Return ONLY the following structured text format.

EXACT FORMAT:

### TAGS
#<tag1>
#<tag2>
(at least 2, max 10, one per line, starting with #)

### TYPE
<document_type> (e.g., code-notes, documentation, research, test-reference, configuration, api-reference, architecture, tutorial)

### SUMMARY
<1-2 sentence high-level purpose, min 20 chars, max 500 chars>

### DETAILS
<2-4 sentences explaining logic and data flow>

### KEY_FUNCTIONS
- **function_name**: Purpose of the function.
- **another_function**: Another purpose. (Important functions, classes, or components, each on a new line)

### DEPENDENCIES
<dependency1>, <dependency2> (comma-separated list of external libraries or modules)

### USAGE
<How to use this code/system>

### RELATED
[[<Related Document 1>]], [[<Related Document 2>]] (Obsidian wikilinks to related documents, comma-separated, use 'none' if none)

### CALLOUTS
>[!INFO]- Important Note
> <Detailed explanation for the callout.>
>[!WARNING]- Caution
> <Another important callout.> (Obsidian callout blocks, each on a new line)

CRITICAL: Adhere strictly to the exact format, especially section headers like `### SECTION_NAME` (exactly three hash marks followed by a space and the section name). Do not include any JSON. Do not include any additional markdown elements outside of the specified format.
'''
