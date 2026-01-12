**Tags:** #verification, #ui-testing, #web-automation, #selenium, #api-testing, #hmrs
**Created:** 2026-01-12
**Type:** code-notes

# verify_hmrs_live_ui

## Summary

```
Script verifies HMRS Live Simulation UI functionality, checks API endpoints, and captures UI issues via Selenium and HTTP requests.
```

## Details

> This script performs automated verification of the HMRS Live Simulation UI by:
> 1. Validating the backend server is running at `localhost:5007`.
> 2. Testing four critical API endpoints (`/api/state`, `/api/data`, `/api/communication`, `/api/realtime-status`) for responsiveness and JSON validity.
> 3. Using Selenium to interact with the UI (e.g., capturing screenshots on failures) and logging browser console errors.
> 4. Documenting all issues (e.g., HTTP errors, missing elements) in a structured format for debugging.
> 
> The script prioritizes error handling for network/API failures and logs detailed metrics (status codes, response times, data structure).

## Key Functions

### `take_screenshot(driver, filename)`

Saves browser snapshots to `simulation_output/hmrs_live_verification` with timestamps.

### `get_console_errors(driver)`

Extracts `SEVERE`-level browser console logs via `driver.get_log('browser')`.

### `check_api_endpoints()`

Tests HTTP endpoints with `requests.get()`, records status codes, response times, and JSON validity.

### `verify_hmrs_live_ui()`

Orchestrates the full verification workflow (server check + API/UI tests), returns issues as a list.

## Usage

1. Run as a standalone script to validate HMRS Live UI.
2. Call `verify_hmrs_live_ui()` programmatically to trigger automated checks.
3. Use `take_screenshot()`/`get_console_errors()` for custom UI/API diagnostics.

## Dependencies

> `requests`
> `selenium-webdriver`
> `datetime`
> `os`
> `json`

## Related

- [[`verify_hmrs_api`]]
- [[`hmrs_backend_config`]]

>[!INFO] Important Note
> The script assumes the backend server runs on `localhost:5007`. Adjust `base_url` in `check_api_endpoints()` if the endpoint differs.

>[!WARNING] Caution
> Timeout exceptions may occur if the server is unresponsive. Increase `timeout` values (e.g., `5` seconds) for flaky environments.
