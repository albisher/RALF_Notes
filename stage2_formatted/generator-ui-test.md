**Tags:** #automated-testing, #ui-testing, #puppeteer, #web-scraping, #end-to-end-test
**Created:** 2026-01-13
**Type:** test-reference

# generator-ui-test

## Summary

```
Automated UI test suite for a generator application using Puppeteer to validate login and elements page functionality.
```

## Details

> This script automates a UI test for a web-based generator application, focusing on login functionality and the elements page. It uses Puppeteer to interact with the frontend, captures screenshots, and logs console messages. The test sequence includes navigating to the login page, filling credentials, submitting login, and verifying the elements page displays expected UI elements (selectors, inputs, buttons, lists). The test also captures screenshots at key stages (before/after login, elements page) and validates UI structure via JavaScript evaluation.

## Key Functions

### `runGeneratorUITest`

Orchestrates the entire test workflow, initializing browser, handling navigation, and reporting results.

### `CheckHelper.takeScreenshot`

Captures page snapshots for debugging/verification.

### `page.evaluate()`

Executes client-side logic to inspect DOM elements dynamically.

### `page.waitForSelector()`

Waits for specific UI elements to appear or interact with forms.

### `consoleLogs capture`

Logs browser console messages for debugging.

## Usage

1. Install dependencies (`puppeteer`, `chalk`).
2. Configure `./config` with frontend URLs and timeout settings.
3. Run script: `node generator-ui-test.js`.
4. Results are logged via `helper.addResult()` and stored in screenshots.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `CheckHelper (local)`
> `config.urls.frontend`
> `config.timeouts.pageLoad`

## Related

- [[Test Report: Generator UI Test Results]]
- [[Documentation: Puppeteer Best Practices]]

>[!INFO] Important Note
> The script uses `headless: false` for visual debugging but may fail in CI environments. Adjust `config.puppeteer` to `headless: true` for production.

>[!WARNING] Caution
> Hardcoded credentials (`user@spacepearl.com`, `password123`) are used for testing. Replace with environment variables or a test config for security.
