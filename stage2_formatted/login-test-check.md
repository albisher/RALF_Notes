**Tags:** #automated-testing, #web-automation, #login-validation, #puppeteer, #frontend-testing
**Created:** 2026-01-13
**Type:** test-reference

# login-test-check

## Summary

```
Automated login test suite using Puppeteer to validate frontend authentication flow, including UI checks and token verification.
```

## Details

> This script performs an end-to-end login test using Puppeteer to:
> 1. Navigate to the login page, capture screenshots, and fill credentials
> 2. Submit the login form and verify authentication state via localStorage
> 3. Check dashboard access and validate persistent authentication
> 4. Collect console/network logs for debugging
> The test uses a helper class for screenshot management and result reporting, with configurable Puppeteer launch settings.

## Key Functions

### ``runLoginTestCheck()``

Main async function orchestrating the entire login test workflow

### ``CheckHelper.takeScreenshot()``

Captures page snapshots with relative path generation

### ``page.evaluate()``

Executes JavaScript in the browser context to inspect localStorage

### ``page.on('console')`/`page.on('request')`/`page.on('response')``

Event handlers for debugging logs

### ``helper.addResult()``

Records test step outcomes with status (pass/fail/info)

## Usage

1. Install dependencies: `npm install puppeteer chalk`
2. Configure `./config` with:
   - `puppeteer` launch options
   - `urls.frontend` (base URL)
   - `timeouts.pageLoad` (timeout value)
3. Run: `node login-test-check.js`
4. Debug in non-headless mode (`headless: false`) for visual inspection

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`

## Related

- [[Frontend Authentication API Docs]]
- [[Puppeteer Test Suite Architecture]]

>[!INFO] Important Note
> The test relies on localStorage for authentication verification. If the frontend uses cookies instead, modify the `page.evaluate()` calls to check cookies instead.


>[!WARNING] Caution
> Network requests may be logged to `networkLogs` array. For production, consider filtering sensitive requests before analysis.
