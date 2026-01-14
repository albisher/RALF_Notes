**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #functional-testing
**Created:** 2026-01-13
**Type:** code-notes

# better-fixed-test

## Summary

```
Automated UI test suite for verifying world creation functionality in a web application using Puppeteer.
```

## Details

> This script automates a multi-step UI test for creating a world in a web application (likely a game or dashboard). It uses Puppeteer to interact with the page, verify form inputs, and check post-submission UI elements. The test captures screenshots at key steps for debugging and logs detailed progress. It includes error handling for missing elements and validates both the created world's visibility and total world count.

## Key Functions

### `betterFixedTest`

Orchestrates the full test workflow, including browser launch, UI interactions, and result validation.

### `takeScreenshot`

Helper function to capture page snapshots with timestamps and save them to a directory.

### `createWorldButton search`

Dynamically locates and clicks the "Create World" button using button text matching.

## Usage

1. Run as a Node.js script to execute the automated test.
2. Ensure the target application is running at `http://localhost:5173`.
3. The script creates a `screenshots` directory with subfolder `better-fixed-test` for saved images.
4. Outputs test results and screenshots to the working directory.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-test-framework]]
- [[web-application-ui-testing]]

>[!INFO] Important Note
> The script uses aggressive Puppeteer launch options (`--disable-web-security`, `--disable-sandbox`) for testing, which may not be safe for production environments. Use cautiously in restricted environments.

>[!WARNING] Caution
> If the target application uses HTTPS or custom headers, modify the `page.goto()` URL or add required headers to avoid security warnings. The current setup may trigger browser warnings due to disabled security features.
