**Tags:** #authentication, #testing, #api-integration, #frontend-validation, #puppeteer
**Created:** 2026-01-13
**Type:** code-test

# auth-check

## Summary

```
Automated authentication validation for frontend/backend systems, testing UI elements, API endpoints, and error states.
```

## Details

> This script performs end-to-end authentication checks using Puppeteer to verify frontend UI elements and API endpoints. It:
> 1. Validates the presence of registration/login elements in the frontend UI via screenshot comparisons.
> 2. Tests backend API endpoints (register/login) with valid/invalid credentials.
> 3. Verifies protected endpoint access using JWT tokens.
> 4. Checks error handling for invalid credentials.
> 
> The workflow uses a helper class (`CheckHelper`) to manage results, screenshots, and API calls, with configurable paths and timeouts.

## Key Functions

### ``runAuthChecks()``

Orchestrates the entire authentication validation process.

### ``CheckHelper.takeScreenshot()``

Captures and stores UI screenshots for comparison.

### ``CheckHelper.checkApiEndpoint()``

Tests backend API endpoints with specified HTTP methods and payloads.

### ``helper.addResult()``

Records test outcomes (pass/fail/warning) with metadata.

## Usage

1. Configure `config` with:
   - Puppeteer launch options (`config.puppeteer`).
   - Frontend/backend URLs (`config.urls.frontend`, `config.urls.backend`).
   - Timeout settings (`config.timeouts.pageLoad`).
2. Run `runAuthChecks()` to execute all tests.
3. Analyze results via `helper.addResult()` calls, which log pass/fail statuses with details.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`

## Related

- [[auth-config]]
- [[puppeteer-testing-guide]]

>[!INFO] Important Note
> The script assumes `config` contains valid URLs and credentials. Hardcoded test email/password (`test-auth@example.com`) may need adjustment for production environments.

>[!WARNING] Caution
> Screenshot storage relies on `helper.takeScreenshot()`; ensure `config` specifies valid output paths to avoid disk errors. API calls use hardcoded test data; avoid exposing credentials in logs.
