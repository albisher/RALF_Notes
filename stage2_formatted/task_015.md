**Tags:** #backend, #data_export, #api, #json, #markdown, #pdf, #reportlab
**Created:** 2026-01-13
**Type:** documentation

# task_015

## Summary

```
Implements backend API endpoints for exporting structured world data in JSON, Markdown, and PDF formats.
```

## Details

> This task outlines the implementation of a `/api/worlds/<id>/export` endpoint that supports three export formats via a `format` query parameter. The backend must serialize world data into JSON, format it as Markdown, and generate a PDF using ReportLab. Subtasks include JSON serialization, Markdown formatting, PDF generation, and automated testing for correctness.

## Key Functions

### ``/api/worlds/<id>/export``

Handles export requests for JSON, Markdown, or PDF based on the `format` query parameter.

### ``json.dumps()`/`json.dump()``

Serializes world data into JSON format.

### `Markdown Formatter`

Converts structured data into readable Markdown with headings, lists, and hierarchy.

### `ReportLab PDF Generator`

Creates a PDF with formatted text, tables, or images for the world data.

## Usage

1. Call `/api/worlds/<id>/export?format=json` to export world data as JSON.
2. Call `/api/worlds/<id>/export?format=md` to export as Markdown.
3. Call `/api/worlds/<id>/export?format=pdf` to generate a PDF.

## Dependencies

> ``json``
> ``ReportLab``
> `Python’s built-in `json` module`
> `and backend framework (e.g.`
> `Flask/Django).`

## Related

- [[Task 008]]
- [[World Data Model Documentation]]

>[!INFO] Important Note
> Ensure all world data fields are included in JSON/Markdown exports to avoid missing or truncated content.

>[!WARNING] Caution
> Validate ReportLab PDF generation to prevent crashes or malformed layouts; test with edge cases (e.g., empty data).
