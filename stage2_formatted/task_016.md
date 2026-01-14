**Tags:** #backend, #data_export, #api, #excel, #word_document, #openpyxl, #python-docx
**Created:** 2026-01-13
**Type:** documentation

# task_016

## Summary

```
Implements backend API endpoints for exporting structured world data to Excel (.xlsx) and Word (.docx) formats.
```

## Details

> This task extends an existing `/api/worlds/<id>/export` endpoint to support file-based data exports. The implementation uses `OpenPyXL` for Excel and `python-docx` for Word, organizing data into sheets/tables with structured formatting. The backend dynamically routes requests based on the requested format (`xlsx`/`docx`) and returns downloadable files with appropriate headers.

## Key Functions

### ``/api/worlds/<id>/export``

Handles format parameter (`xlsx`/`docx`) and generates/downloads files.

### ``OpenPyXL``

Creates Excel workbooks with sheets for characters/locations/data.

### ``python-docx``

Constructs Word documents with headings/tables for world elements.

## Usage

1. Call `/api/worlds/<id>/export?format=xlsx` or `docx` with a valid `<id>`.
2. Server generates the file in-memory and sends it as a downloadable response.
3. Client opens the file in Excel/Word or a compatible viewer.

## Dependencies

> ``OpenPyXL``
> ``python-docx``
> `Flask/FastAPI (backend framework)`
> `existing `/api/worlds/<id>` route.`

## Related

- [[Task 008]]
- [[World Data API Documentation]]

>[!INFO] Important Note
> Ensure the backend validates `<id>` and query parameters (`format`) to prevent malformed requests.
>

>[!WARNING] Caution
> File sizes may exceed server limits; test with large datasets to avoid memory issues.
