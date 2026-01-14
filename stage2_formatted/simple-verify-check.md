**Tags:** #automated-ui-testing, #web-scraping, #puppeteer, #screenshot-capture, #verification-check
**Created:** 2026-01-13
**Type:** code-notes

# simple-verify-check

## Summary

```
Automated UI verification script using Puppeteer to test and capture screenshots of key frontend pages.
```

## Details

> This script uses Puppeteer to launch a browser in non-headless mode, navigate to multiple frontend pages (main, login, elements, debug), and capture screenshots for each. It logs test progress, handles errors, and generates a report via a helper function. The browser remains open for manual inspection after execution.

## Key Functions

### `runSimpleVerifyCheck()`

Orchestrates the entire verification workflow, including browser launch, page navigation, screenshot capture, and error handling.

### `CheckHelper.takeScreenshot()`

Captures UI screenshots with metadata (e.g., filename, config context).

### `CheckHelper.addResult()`

Records pass/fail results for each test case.

### `CheckHelper.generateReport()`

Compiles results into a structured report (likely JSON/HTML).

## Usage

1. Install dependencies (`npm install puppeteer chalk`).
2. Configure `./config` with frontend URLs and Puppeteer options.
3. Run script directly (`node simple-verify-check.js`) or import `runSimpleVerifyCheck()` in another file.
4. Review browser output and generated report for verification results.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local ./config)`
> `utils/check-helper (local ./utils/check-helper)`

## Related

- [[config]]
- [[check-helper]]

>[!INFO] Important Note
> The script intentionally keeps the browser open post-execution for manual inspection. Close it manually to avoid lingering processes.

>[!WARNING] Caution
> Ensure `config.urls.frontend` resolves to a valid base URL. Incorrect paths may cause navigation errors or failed tests.
