---
tags: #json, #schema, #documentation, #obsidian, #metadata, #structure
created: 2026-01-09
type: documentation
---

# schema_json_definition

## Summary

Defines a standardized JSON schema for Obsidian documentation metadata

## Details

This schema enforces a consistent structure for Obsidian notes, ensuring proper validation of metadata fields like filename, tags, type, and related documentation links. It includes validation rules for required fields, tag patterns, and document classification. The schema supports optional fields like callouts, code snippets, and performance notes for extensibility. The design prioritizes clarity and maintainability while allowing flexibility for future expansions.

## Key Functions

### `RALF_JSON_SCHEMA`

Defines the core JSON schema structure for Obsidian documentation metadata

**Signature:** `dict`

**Returns:** A validated JSON schema object defining all required and optional fields

### `UNIFIED_SYSTEM_PROMPT`

Provides the template and rules for generating Obsidian documentation from code analysis

**Signature:** `str`

**Returns:** A structured prompt for consistent documentation output

## Usage

To use this schema, implement it in Obsidian notes by defining all required fields (filename, tags, type, summary) and optionally others (key_functions, dependencies, etc.). Example: ```json
{
  "filename": "my_note",
  "tags": ["#example", "#test"],
  "type": "code-notes",
  "summary": "Example note demonstrating schema usage"
}
``` Validate against this schema to ensure consistency across documentation.

## Code Summary

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "RALFDocumentationSchema",
  "type": "object",
  "required": ["filename", "tags", "type", "summary"],
  ...
}
```

## Dependencies

`#json`, `#regex`, `#array-validation`

## Security Risks

No direct security risks, but improperly structured metadata could lead to validation failures in downstream systems relying on this schema.

## Performance

Schema validation can be computationally intensive for large arrays (e.g., tags or dependencies). Consider caching validated schemas for performance optimization.

## Related

- [[Obsidian Metadata Best Practices]]
- [[JSON Schema Validation Guide]]

> [!INFO]- Key insight: This schema enforces Obsidian-specific conventions like Obsidian wikilink format (e.g., `[[Related Document]]`) and tag patterns (e.g., `#tag-name` with no spaces).

> [!WARNING]- Important warning: Required fields must adhere to strict rules (e.g., tags must be 2-10 items, type must be one of the predefined values). Missing required fields will invalidate the schema.

> [!TIP]- Tip: Use the `doc_type_confidence` field (0-1) to indicate confidence in classification (e.g., 0.9 for high confidence).
