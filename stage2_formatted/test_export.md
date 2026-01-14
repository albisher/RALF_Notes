**Tags:** #test-script, #export-service, #documentation, #unit-testing
**Created:** 2026-01-13
**Type:** code-notes

# test_export

## Summary

```
Test script validating JSON export functionality for a documentation exporter.
```

## Details

> This script tests the `DocumentationExporter` class by initializing it and calling its `export_to_json()` method with `world_id=1`. It then verifies the exported data structure and prints summaries of key components (e.g., history events, story logs, known robots). The test outputs formatted summaries of the export summary and content details, truncating long descriptions for readability.

## Key Functions

### ``test_export()``

Orchestrates the entire test workflow, including error handling and success reporting.

### ``DocumentationExporter()``

Initializes the exporter instance (assumed to be imported from `export_service`).

### ``export_to_json(world_id)``

Core method to generate JSON export data for a given world ID.

### ``get_export_summary()``

Retrieves metadata about the export (e.g., world ID, timestamp, content counts).

### ``export_data.get('content', {})``

Accesses the nested JSON structure containing parsed content (e.g., history, story logs).

## Usage

1. Run the script directly (`python test_export.py`).
2. The script prints:
   - Export confirmation/errors.
   - Summary of exported world ID, format, and timestamp.
   - Detailed breakdown of content categories (e.g., history events, story logs).
3. Exit code `0` if successful, `1` if an exception occurs.

## Dependencies

> ``export_service``
> ``sys``
> ``os``

## Related

- [[export_service]]
- [[documentation_export_guide]]

>[!INFO] Important Note
> This script assumes `export_service` contains a `DocumentationExporter` class with methods `export_to_json()` and `get_export_summary()`. Verify the class structure matches expectations.

>[!WARNING] Caution
> Truncates long descriptions (e.g., robot descriptions) to 50 chars for readability. Ensure critical data isn’t lost during parsing.
