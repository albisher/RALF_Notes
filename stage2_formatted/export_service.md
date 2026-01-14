**Tags:** #documentation_export, #text_processing, #json_serialization, #file_parsing, #text_structuring
**Created:** 2026-01-13
**Type:** code-notes

# export_service

## Summary

```
Service for structured extraction of documentation content into JSON format.
```

## Details

> This `DocumentationExporter` class processes multiple text files (e.g., `HistoryBook.txt`, `ConventionsBook.txt`) and directories (e.g., `StoryLogs`) to extract and parse historical events, conventions, story logs, and metadata. It organizes parsed data into a standardized JSON structure with timestamps, error handling, and modular parsing methods for each file type. The `_parse_*` methods handle specific file formats, while `export_to_json()` consolidates results into a unified output.

## Key Functions

### ``export_to_json(world_id`

int)`**: Orchestrates the entire export process, initializing a structured JSON payload with metadata and parsed content.

### ``_parse_history()``

Extracts and formats historical events from `HistoryBook.txt`, supporting both year:description and numeric-year + description formats.

### ``_parse_conventions()``

Parses hierarchical sections (e.g., `## Section Title`) from `ConventionsBook.txt`, preserving markdown headers and content.

### ``_parse_story_logs()``

Aggregates all `.txt` files in `StoryLogs`, extracting metadata (year, sol, robot) and log entry titles via regex.

## Usage

1. Initialize with a `documentation_path` (defaults to `"Documentation"`).
2. Call `export_to_json(world_id)` to generate a JSON export.
3. Parse the result to extract structured data (e.g., `export_data["content"]["history"]`).

## Dependencies

> ``pathlib``
> ``typing``
> ``datetime``
> ``re``
> ``json``
> ``os``
> ``io` (standard libraries)
`reportlab` (for PDF generation`
> `though not directly used in this snippet)`

## Related

- [[`export_service` (Obsidian link to full implementation)
`documentation_parsing` (Obsidian notes on text parsing strategies)]]

>[!INFO] **Error Handling**
> Methods return error dictionaries (e.g., `{"error": "HistoryBook.txt not found"}`) if files fail to load or parse, ensuring graceful degradation.

>[!WARNING] **Regex Limitations**
> `_parse_story_logs()` assumes filenames follow `YYYY_SOL_Robot.txt` format. Extensions may break if filenames deviate.
