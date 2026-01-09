"""
Box: JSON Schema Definition

Responsibility: Define and store the unified JSON schema
"""

RALF_JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "RALFDocumentationSchema",
    "type": "object",
    "required": ["filename", "tags", "type", "summary"],
    "properties": {
        "filename": {
            "type": "string",
            "description": "Base filename without extension",
            "minLength": 1
        },
        "tags": {
            "type": "array",
            "description": "Relevant tags for the document (with # prefix)",
            "items": {
                "type": "string",
                "pattern": "^#[a-z0-9-]+$"
            },
            "minItems": 2,
            "maxItems": 10,
            "uniqueItems": True
        },
        "type": {
            "type": "string",
            "description": "Document type classification",
            "enum": [
                "code-notes",
                "documentation",
                "research",
                "test-reference",
                "configuration",
                "api-reference",
                "architecture",
                "tutorial"
            ]
        },
        "summary": {
            "type": "string",
            "description": "1-2 sentence high-level purpose",
            "minLength": 20,
            "maxLength": 500
        },
        "details": {
            "type": "string",
            "description": "2-4 sentences explaining logic and data flow"
        },
        "key_functions": {
            "type": "array",
            "description": "Important functions, classes, or components",
            "items": {
                "type": "object",
                "required": ["name", "purpose"],
                "properties": {
                    "name": {"type": "string"},
                    "purpose": {"type": "string"},
                    "signature": {"type": "string"},
                    "returns": {"type": "string"}
                }
            }
        },
        "dependencies": {
            "type": "array",
            "description": "External libraries or modules",
            "items": {"type": "string"}
        },
        "usage": {
            "type": "string",
            "description": "How to use this code/system"
        },
        "related": {
            "type": "array",
            "description": "Obsidian wikilinks to related documents",
            "items": {"type": "string"}
        },
        "callouts": {
            "type": "array",
            "description": "Obsidian callout blocks",
            "items": {"type": "string"}
        },
        "code_summary": {
            "type": "string",
            "description": "Key code snippet in markdown code block"
        },
        "security_risks": {
            "type": "string",
            "description": "Optional security considerations"
        },
        "performance_notes": {
            "type": "string",
            "description": "Optional performance characteristics"
        },
        "doc_type_confidence": {
            "type": "number",
            "description": "Confidence in type classification (0-1)",
            "minimum": 0,
            "maximum": 1
        },
        "dependency_graph": {
            "type": "string",
            "description": "Optional mermaid diagram of dependencies"
        }
    }
}

# System prompt for unified JSON generation
UNIFIED_SYSTEM_PROMPT = '''You are an expert technical writer specializing in Obsidian documentation.

Analyze the provided code file and return ONLY valid JSON - NO markdown wrappers, NO backticks, NO ``` blocks.

**CRITICAL:** Return PURE JSON ONLY. Start with { and end with }.

**EXACT FORMAT:**
{
  "filename": "base_filename_without_extension",
  "tags": ["#tag1", "#tag2", "#tag3"],
  "type": "code-notes",
  "summary": "One sentence explaining the high-level purpose",
  "details": "2-4 sentences describing logic, data flow, and architecture",
  "key_functions": [
    {
      "name": "function_name",
      "purpose": "What this function does",
      "signature": "optional_function_signature",
      "returns": "optional_return_description"
    }
  ],
  "dependencies": ["library1", "library2"],
  "usage": "Detailed usage instructions with examples",
  "related": ["[[Related Document 1]]", "[[Related Document 2]]"],
  "callouts": [
    "> [!INFO]- Key insight or takeaway",
    "> [!WARNING]- Important warning or gotcha"
  ],
  "code_summary": "```language\\nkey code snippet\\n```",
  "security_risks": "Optional: Security considerations",
  "performance_notes": "Optional: Performance characteristics"
}

**VALIDATION RULES:**
1. filename: Must not include file extension
2. tags: 2-10 tags, all lowercase with #, use hyphens not spaces
3. type: Must be one of: code-notes, documentation, research, test-reference, configuration, api-reference, architecture, tutorial
4. summary: 1-2 sentences, 20-500 characters
5. details: 2-4 sentences, 50-1500 characters
6. key_functions: 0-15 functions with name and purpose
7. related: Use Obsidian [[wikilink]] format
8. callouts: Use Obsidian > [!TYPE] format (INFO, WARNING, TIP, NOTE)
9. code_summary: Wrap in ``` blocks with language

**EXAMPLE TAG CATEGORIES:**
- Language: #python, #javascript, #rust, #go
- Domain: #api, #database, #simulation, #testing, #documentation
- Tech: #docker, #ollama, #cesium, #openstreetmap
- Purpose: #automation, #optimization, #analysis

Return ONLY the JSON object. No explanations. No markdown.'''
