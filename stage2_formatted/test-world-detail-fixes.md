**Tags:** #automated-testing, #puppeteer, #web-scraping, #ui-testing, #frontend-validation, #world-detail-page, #character-creation
**Created:** 2026-01-13
**Type:** code-test

# test-world-detail-fixes

## Summary

```
Automated UI test suite for verifying fixes in a world detail page, including login, character creation, and Quick Actions functionality.
```

## Details

> This script uses Puppeteer to automate browser interactions for testing a web application’s world detail page. It launches a headless browser, logs in (if required), navigates to a specific world detail URL, and verifies UI elements like the "Add Character" button and asset creation dialog. The test captures screenshots of key interactions, such as the asset creator dialog and hash-based character generation workflow.
> 
> The script follows a structured flow:
> 1. **Browser Launch & Setup**: Configures Puppeteer with security bypass flags and sets viewport dimensions.
> 2. **Login Handling**: Detects and automates login if needed, filling credentials and submitting the form.
> 3. **World Detail Navigation**: Redirects to a world detail page (e.g., `/worlds/27`) and captures a screenshot.
> 4. **Quick Actions Testing**: Focuses on the "Add Character" button, checks for an asset creation dialog, and validates pre-selected asset type (e.g., "character") and hash-based generation workflow.

## Key Functions

### `testWorldDetailFixes`

Orchestrates the entire test suite, including browser setup, navigation, and UI validation.

### `page.goto()`

Navigates to URLs with configurable wait times and error handling.

### `page.evaluateHandle()`

Locates and interacts with dynamic UI elements (e.g., buttons, inputs).

### `page.screenshot()`

Captures visual snapshots of pages/dialogs for debugging.

### `page.fill()`

Automates form input for login or character creation.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-world-detail-fixes.js`.
3. Ensure the target application (`https://localhost:8443`) is running and accessible.
4. Verify the test outputs (console logs + screenshots in `checks/screenshots/`).

## Dependencies

> `puppeteer`
> `Node.js runtime.`

## Related

- [[Test-World-Login-Fixes]]
- [[UI-Character-Creation-Guide]]
- [[Puppeteer-Configuration-Docs]]

>[!INFO] Important Note
> The script uses `--disable-web-security` and `--ignore-ssl-errors` flags, which may expose the target application to security risks if misconfigured. Use only in controlled environments with proper safeguards.

>[!WARNING] Caution
> Timeout values (e.g., `waitUntil: 'networkidle0'`, `timeout: 15000`) are arbitrary and may fail if the target page loads unpredictably. Adjust based on application performance.
