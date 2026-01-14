**Tags:** #export-formats, #documentation-testing, #json-markdown-pdf, #backend-integration, #test-automation
**Created:** 2026-01-13
**Type:** test-reference

# test-all-export-formats

## Summary

```
Comprehensive test suite validating JSON, Markdown, and PDF export functionality for documentation systems.
```

## Details

> This script tests the `DocumentationExporter` class by validating its ability to generate structured JSON, Markdown, and PDF exports for a given world ID. It performs structural, content, and format-specific checks for each export type, ensuring data integrity and proper formatting. The tests verify the presence of required sections, metadata, and correct data structures (e.g., lists/dictionaries) while handling conditional error cases.
> 
> The test suite uses assertions to validate:
> - **JSON**: Metadata fields (`world_id`, `export_timestamp`, `export_format`) and nested content sections (e.g., `history`, `story_logs`).
> - **Markdown**: Section headers, table of contents (TOC) links, world ID, and timestamp inclusion.
> - **PDF**: Valid PDF header (`%PDF`), version marker (`%PDF-1.`), EOF marker (`%%EOF`), and substantial content size.

## Key Functions

### `test_json_export()`

Validates JSON export structure, metadata, and nested section integrity.

### `test_markdown_export()`

Ensures Markdown formatting correctness, section presence, and TOC links.

### `test_pdf_export()`

Checks PDF file validity (header, version, EOF) and content size.

### `DocumentationExporter`

Core class exporting data in JSON, Markdown, or PDF formats.

## Usage

1. Run the script directly (`python test-all-export-formats.py`).
2. Each test function (`test_json_export`, `test_markdown_export`, `test_pdf_export`) validates one export format independently.
3. Returns `True` on success, `False` on failure, with detailed error messages.

## Dependencies

> ``export_service``
> ``subprocess``
> ``tempfile``
> ``json``
> ``sys``
> ``os` (Python standard library)
External: `backend` directory (imported via `sys.path.append()`).`

## Related

- [[Backend Documentation]]
- [[Export Service API]]
- [[Test Suite: Export Validation]]

>[!INFO] Conditional Assertions
> Tests skip error sections (e.g., `if 'error' not in history`) to avoid false negatives for non-fatal data issues. This ensures robustness against missing optional fields.


>[!WARNING] PDF Size Threshold
> The test enforces a minimum PDF size (`>10000 bytes`) to avoid flakiness with empty or minimal exports. Adjust thresholds if testing edge cases.
