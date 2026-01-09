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

# System prompt for unified JSON generation (from original PoC)
UNIFIED_SYSTEM_PROMPT = '''Analyze this code file. Return ONLY valid JSON - NO markdown, NO backticks, NO ``` blocks.

EXACT FORMAT:
{"filename":"FILENAME","tags":["#tag1","#tag2"],"type":"code-notes","summary":"One sentence purpose","details":"2-3 sentences logic","key_functions":[{"name":"func1","purpose":"Does X"}],"dependencies":["lib1"],"usage":"How to use","related":["[[Other]]"],"callouts": ["> [!INFO]- Key point"],"code_summary":"```python\nkey code snippet\n```"}

CRITICAL: Pure JSON only. No wrappers.'''
