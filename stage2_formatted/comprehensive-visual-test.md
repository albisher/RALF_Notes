**Tags:** #visual-testing, #puppeteer, #automated-testing, #web-api, #headless-browser
**Created:** 2026-01-13
**Type:** code-notes

# comprehensive-visual-test

## Summary

```
Automated visual and functional testing framework for web applications using Puppeteer.
```

## Details

> This script implements a `ComprehensiveVisualTest` class to perform automated visual and functional tests on a web application running on `localhost:8443`. It uses Puppeteer to launch a headless browser, captures screenshots, and validates API responses and UI elements. The class includes methods for health checks, login page validation, and authentication testing, logging results to track test success/failure.

## Key Functions

### ``init()``

Initializes browser, creates screenshot directory, and launches Puppeteer.

### ``takeScreenshot(name, description)``

Captures a screenshot of the current page with a timestamped filename.

### ``logResult(testName, success, details)``

Records test outcomes in an array and logs them to the console.

### ``testHealthCheck()``

Verifies API health by checking for `"status":"healthy"` in the response.

### ``testLoginPage()``

Validates the presence of login form elements (form, username, password, submit button).

### ``testAuthentication()``

Simulates login with test credentials and checks for successful redirection to a dashboard.

## Usage

1. Instantiate `ComprehensiveVisualTest` and call `init()` to set up the browser.
2. Call test methods sequentially (e.g., `testHealthCheck()`, `testLoginPage()`) to validate functionality.
3. Review `testResults` array for aggregated outcomes or log entries for debugging.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Visual Regression Testing Guide]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> The script uses a headless browser with aggressive security flags (`--disable-web-security`, `--ignore-ssl-errors`), which may not work in production environments. Test locally first.

>[!WARNING] Caution
> Avoid hardcoding credentials in `testAuthentication()`. Use environment variables or a secure config file instead.
