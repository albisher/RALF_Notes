**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-verification, #frontend-validation
**Created:** 2026-01-13
**Type:** code-notes

# final-user-friendly-verification

## Summary

```
Automated UI verification tool using Puppeteer to test user-friendly content on a web application.
```

## Details

> This script automates UI verification for a web application by performing login and validating the "World Assets" page. It captures screenshots, checks for raw JSON indicators, and evaluates user-friendly content (e.g., descriptive terms like "arms," "eyes"). The tool also counts asset cards and logs analysis results. It uses Puppeteer to control a headless Chrome browser, ensuring visual and textual consistency with user-friendly design standards.

## Key Functions

### `FinalUserFriendlyVerification`

Main class initializing browser launch, credentials, and screenshot handling.

### `getScreenshotName(feature, description)`

Generates filenames with timestamp, counter, and feature description.

### `takeScreenshot(page, feature, description)`

Captures full-page screenshots and saves them to a directory.

### `runTest()`

Orchestrates the entire test workflow (login → World Assets page validation).

### `testLogin(page)`

Handles automated login with test credentials and verifies successful navigation.

### `testWorldAssetsPage(page)`

Validates the World Assets page by checking for raw JSON, user-friendly content, and asset card count.

## Usage

1. Initialize the class: `const verifier = new FinalUserFriendlyVerification();`
2. Run the test: `await verifier.runTest();`
3. Customize `baseUrl`, `testCredentials`, or screenshot directory as needed.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[User-Friendly Design Checklist]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script logs detailed analysis results (e.g., "Raw JSON Detected: ❌ YES") for debugging. Ensure the target URL (`baseUrl`) matches the actual application endpoint.


>[!WARNING] Caution
> Avoid running in headless mode (`headless: true`) if debugging UI interactions is required. The script uses Chrome’s executable path (`/Applications/Google Chrome.app`), which may need adjustment for non-Mac systems.
