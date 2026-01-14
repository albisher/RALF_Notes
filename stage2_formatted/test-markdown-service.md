**Tags:** #test-script, #markdown-processing, #documentation-export, #backend-integration
**Created:** 2026-01-13
**Type:** test-reference

# test-markdown-service

## Summary

```
Test script validates Markdown export functionality for world documentation.
```

## Details

> This script tests the `DocumentationExporter` class from the backend module to verify that it correctly generates Markdown content for a specified world ID (e.g., `9`). It validates the presence of expected sections (e.g., "World Documentation," "Table of Contents") and saves the output to a file for inspection. The test prints success/failure status, section verification, and a preview of the exported content.

## Key Functions

### ``test_markdown_export()``

Orchestrates the test workflow, initializes the exporter, exports content, and validates its structure.

### ``DocumentationExporter.export_to_markdown(world_id)``

Core method that generates Markdown-formatted documentation for a given world ID.

## Usage

1. Run the script directly (`python test-markdown-service.py`).
2. It exports world documentation (e.g., world ID `9`) to `checks/test-markdown-output.md`.
3. Output includes success/failure status, section validation, and a preview of the first 500 characters.

## Dependencies

> ``backend/export_service.py` (contains `DocumentationExporter` class)`
> ``sys``
> ``os`.`

## Related

- [[export_service]]
- [[test-markdown-output]]

>[!INFO] Expected Sections
> The script checks for predefined sections like "World Documentation" and "Story Logs" in the exported Markdown. Missing any will trigger a failure.

>[!WARNING] File Path Handling
> Ensure the `backend` directory is in `sys.path`; otherwise, the script may fail to import `DocumentationExporter`.
