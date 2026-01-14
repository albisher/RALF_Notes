**Tags:** #visual-testing, #puppeteer, #automated-testing, #web-api, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-notes

# basic-visual-test

## Summary

```
Automated visual testing framework using Puppeteer to validate web application health, login functionality, and public page accessibility via screenshots and error checks.
```

## Details

> This script implements a `BasicVisualTest` class that initializes a headless Puppeteer browser, navigates to specified endpoints, and performs visual validation checks. It captures screenshots of critical pages, logs test results, and verifies API health, form presence, and page content. The framework logs detailed success/failure statuses for each test case.

## Key Functions

### ``init()``

Launches a headless Puppeteer browser with customizable Chrome options.

### ``takeScreenshot(name, description)``

Captures a full-page screenshot with timestamped filename.

### ``logResult(testName, success, details)``

Records test outcomes in an array and logs console output.

### ``testHealthCheck()``

Validates API health by checking for `"status":"healthy"` in response content.

### ``testLoginPage()``

Verifies login form elements (form, username, password, submit button) exist.

### ``testPublicPages()``

Iterates through predefined public routes, checks for errors, and validates content presence.

### ``testErrorHandling()``

*(Incomplete in provided snippet; intended to test error page rendering.)*

## Usage

1. Instantiate `BasicVisualTest` and call `init()` to launch the browser.
2. Call test methods sequentially (e.g., `testHealthCheck()`, `testLoginPage()`).
3. Review `testResults` array for aggregated outcomes or console logs for real-time feedback.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[BasicVisualTest Usage Guide]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> The `testErrorHandling()` method is incomplete in the snippet and may need additional logic (e.g., triggering intentional errors) to fully validate error page rendering.

>[!WARNING] Caution
> Headless mode may not fully simulate user interactions. For dynamic content, consider adding explicit waits or element interactions.
