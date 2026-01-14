**Tags:** #API Testing, #Bash Scripting, #Security Validation, #Health Checks
**Created:** 2026-01-13
**Type:** code-notes

# test-api-functionality

## Summary

```
Automated API endpoint validation script for security and functionality checks.
```

## Details

> This Bash script performs automated HTTP requests to validate backend API endpoints, checking for correct HTTP status codes, authentication requirements, and response body integrity. It uses `curl` for HTTP requests and processes responses to determine success/failure, logging results with colored output. The script handles both success and expected error cases (like 401/403 for protected endpoints) gracefully.
> 
> The script dynamically generates a timestamped JSON results file (`test-results-<date>.json`) to log all test outcomes, including detailed response bodies. It includes a modular design with reusable functions for request handling and endpoint-specific tests.

## Key Functions

### `print_status`

Displays colored status messages for test outcomes.

### `make_request`

Executes HTTP requests with configurable method, endpoint, data, and headers using `curl`.

### `test_health_endpoint`

Validates the `/health` endpoint for basic availability.

### `test_config_validation`

Checks `/config/validate` for proper configuration validation.

### `test_api_key_validation`

Tests `/config/api-keys` endpoint for API key management.

### `test_external_api_status`

Verifies `/ai/external-apis/status` endpoint functionality.

### `test_ai_health`

Ensures `/ai/health` endpoint returns expected responses.

### `test_external_api_validation`

Tests POST `/ai/external-apis/validate` with empty JSON payload.

## Usage

1. Save the script as `test-api-functionality`.
2. Set environment variables for `BACKEND_URL` and API credentials if needed.
3. Run with:
   ```bash
   ./test-api-functionality
   ```
4. Review results in `test-results-<timestamp>.json` and console output.

## Dependencies

> `curl`
> `jq`
> `bash`

## Related

- [[Security API Testing Guide]]
- [[Bash HTTP Request Best Practices]]

>[!INFO] Important Note
> The script intentionally logs all responses (including error bodies) to `test-results.json` for debugging. Ensure sensitive data is masked in production.

>[!WARNING] Caution
> The script does not handle rate limiting or retry logic. For production use, add exponential backoff for transient failures.
