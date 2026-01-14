**Tags:** #API-Testing, #Export-Endpoint, #Backend-Verification, #Blob-Response, #Authentication-Handling
**Created:** 2026-01-13
**Type:** code-notes

# test-export-api-endpoints

## Summary

```
Tests and validates export API endpoints for JSON, Markdown, and PDF formats, including authentication checks and response validation.
```

## Details

> This script performs a comprehensive test suite for an export API, verifying backend accessibility via a health check, and validating responses from multiple export endpoints (`/export`, `/export/summary`, `/export/preview`). It uses Axios to fetch data with custom HTTPS agents (disabling SSL verification for local testing) and checks response statuses, MIME types, filenames, and content validity for each format. The test handles authentication errors gracefully and logs detailed validation results for each endpoint.

## Key Functions

### `testExportApiEndpoints`

Orchestrates the entire test suite, including health checks, format-specific exports, and summary/preview endpoints.

### `axios.get()`

Used for HTTP requests with custom headers and response handling.

### `Blob response parsing`

Extracts text/PDF data from binary responses for validation.

### `Authentication checks`

Differentiates between expected auth failures (401/403) and unexpected errors (e.g., 501).

## Usage

1. Run via Node.js: `node test-export-api-endpoints.js`.
2. Configure `world_id` and `baseUrl` (default: `localhost:8443`).
3. Adjust `httpsAgent` settings if needed (e.g., for production with proper SSL).
4. Extend `formats` array to test additional export types.

## Dependencies

> `axios`
> `Node.js built-in modules (`https``
> ``require`)`
> ``Blob` (browser/Node.js compatibility).`

## Related

- [[API-Design-Documentation]]
- [[Backend-Export-Implementation]]
- [[Test-Suite-Architecture]]

>[!INFO] Local Testing Note
> Disables SSL certificate validation (`rejectUnauthorized: false`) for local testing only. Use with caution in production environments.

>[!WARNING] Authentication Handling
> Logs expected auth errors (401/403) as warnings but treats unexpected errors (e.g., 501) as failures. Ensure backend endpoints are documented for these status codes.
