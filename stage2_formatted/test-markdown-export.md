**Tags:** #testing, #api-integration, #markdown, #backend-validation
**Created:** 2026-01-13
**Type:** test-reference

# test-markdown-export

## Summary

```
Validates Markdown export functionality for a backend API endpoint.
```

## Details

> This script tests the export capabilities of a backend API by verifying:
> 1. **Health check** of the backend service.
> 2. **Markdown export endpoint** (with `format=md` query parameter) for:
>    - Correct HTTP status (401/403 expected due to auth).
>    - Proper MIME type (`text/markdown`).
>    - Expected filename in `Content-Disposition` header.
>    - Presence of key markdown sections (headers like `# World Documentation`, `## Table of Contents`, etc.).
> 3. **Export summary endpoint** (accessibility and response structure).
> 4. **Export preview endpoint** (basic accessibility check).
> 
> The script logs detailed validation results and saves a truncated sample of the markdown output for inspection.

## Key Functions

### ``testMarkdownExport()``

Orchestrates all export endpoint tests.

### ``axios.get()``

Used internally to fetch API responses (with custom `httpsAgent` for localhost).

### ``fs.writeFileSync()``

Saves a truncated markdown sample to disk for manual review.

## Usage

1. Run the script in a Node.js environment.
2. Ensure the backend API (`https://localhost:8443`) is accessible and running.
3. Authenticate if required (authentication errors are expected and logged).
4. Verify logs for pass/fail indicators and inspect `checks/sample-markdown-export.md` for content.

## Dependencies

> ``axios``
> ``node:https``
> ``node:fs``

## Related

- [[none]]

>[!INFO] Authentication Handling
> The script intentionally logs 401/403 responses as expected, since authentication is required for export endpoints. This avoids false negatives for missing auth logic.


>[!WARNING] Localhost Security
> The `httpsAgent` configuration (`rejectUnauthorized: false`) disables SSL certificate validation for localhost. Use this only in development environments with trusted certificates.
