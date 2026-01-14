**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #functional-testing
**Created:** 2026-01-13
**Type:** code-notes

# simple-fixed-test

## Summary

```
Automated UI test script for verifying a web dashboard's "Create World" functionality using Puppeteer.
```

## Details

> This script automates a fixed workflow to test a web application's dashboard functionality, specifically the "Create World" feature. It launches a browser, navigates to a local web app (running on `localhost:5173`), and systematically verifies:
> 1. Dashboard loading
> 2. Button detection and interaction
> 3. Dialog verification
> 4. Form input identification and filling
> 5. Final creation attempt
> 
> The test captures screenshots at key steps and logs detailed progress. It includes error handling for robustness and uses Puppeteer's headless mode with security-disabling flags for testing.

## Key Functions

### `simpleFixedTest`

Main async function orchestrating the entire test workflow.

### `takeScreenshot`

Helper function to capture page snapshots with timestamped filenames.

### `puppeteer.launch`

Configures browser instance with security-disabling flags.

### `page.goto`

Navigates to the target URL with timeout handling.

### `page.$$()`

Selects multiple elements by CSS selector.

## Usage

1. Save as `simple-fixed-test.js`
2. Run with `node simple-fixed-test.js`
3. Ensure target app is running on `localhost:5173`
4. Outputs console logs and screenshots to `screenshots/simple-fixed-test/`

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Web Application Architecture]]
- [[Puppeteer Test Framework]]

>[!WARNING] Caution
> **Security Note**: The script uses `--disable-web-security` and other security-disabling flags. Only use in controlled environments for testing purposes.
> **Headless Mode**: Runs in headless mode (`headless: true`) which may not work in all environments.
> **Localhost Dependency**: Requires the target application to be running on `localhost:5173` for testing.

>[!INFO] Important Note
> **Error Handling**: Basic error handling is implemented but may not cover all edge cases. Consider adding more granular error handling for production use.
> **Screenshots**: Screenshots are saved to a `screenshots` directory with timestamped filenames. Ensure the directory exists before running.
