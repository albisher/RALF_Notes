**Tags:** #automation, #ui-verification, #puppeteer, #web-testing, #dashboard-validation
**Created:** 2026-01-13
**Type:** code-test

# simple-dashboard-verification

## Summary

```
Verifies UI elements and content of a web dashboard using Puppeteer for automated testing.
```

## Details

> This script automates the verification of a web dashboard by launching a headless browser, navigating to a local application, and checking for specific UI elements and text content. It captures screenshots, validates the presence of dashboard components (e.g., stat cards), and confirms the existence of expected keywords like "Space Peral" and "X-Series robots." Error handling includes saving an error screenshot if the verification fails.

## Key Functions

### ``simpleDashboardVerification()``

Orchestrates the entire verification process, including browser launch, UI checks, and error handling.

### ``page.goto()``

Navigates to the dashboard URL with configurable wait and timeout settings.

### ``page.screenshot()``

Captures screenshots for both successful and failed verification states.

### ``page.evaluate()``

Extracts dynamic text content from the page for keyword validation.

### ``page.$()` and `page.$$$()``

Checks for the existence of CSS selectors (e.g., `.dashboard`, `.stat-card`).

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node simple-dashboard-verification.js`.
3. Verify dashboard content by checking the console output and saved screenshots (`checks/screenshots/`).

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses a headless browser with aggressive security flags (`--disable-web-security`) for stability, which may not be suitable for production environments. Consider using a non-headless mode or a more secure sandbox for real-world testing.

>[!WARNING] Caution
> Running with `--disable-web-security` can expose the browser to security risks. Use this only in controlled environments (e.g., local development). Always validate security policies before deploying such configurations.
