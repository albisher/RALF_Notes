**Tags:** #automated-testing, #web-scraping, #puppeteer, #api-testing, #feature-validation
**Created:** 2026-01-13
**Type:** code-notes

# comprehensive-feature-check

## Summary

```
Automated browser-based feature validation tool using Puppeteer to test web application health, UI elements, and API endpoints.
```

## Details

> This script initializes a Puppeteer browser instance to perform automated checks on a web application. It creates a timestamped directory for screenshots, launches a headless browser with customizable settings, and executes predefined tests (health check, landing page, authentication, and world management). Each test captures screenshots, logs results, and records failures. The `ComprehensiveFeatureCheck` class manages browser lifecycle, test execution, and result aggregation.

## Key Functions

### ``init()``

Configures browser launch with Puppeteer, sets up directory structure, and initializes UI.

### ``getScreenshotName(feature, description)``

Generates a timestamped filename for screenshots with sanitized feature descriptions.

### ``takeScreenshot(feature, description)``

Captures a full-page screenshot and saves it to a structured directory.

### ``logResult(testName, success, details)``

Records test outcomes in an array with timestamp and logs console output.

### ``testHealthCheck()``

Verifies API health by checking for `"status":"healthy"` in the response.

### ``testLandingPage()``

Checks for a valid page title after navigating to the root URL.

### ``testAuthentication()``

Validates presence of login/register forms on `/login` and `/register` endpoints.

### ``testWorldManagement()``

Tests world creation page (incomplete snippet; further methods like `testWorldCreation()` would follow).

## Usage

1. Initialize the class: `const checker = new ComprehensiveFeatureCheck();`
2. Call `checker.init()` to launch the browser.
3. Execute tests sequentially: `await checker.testHealthCheck(); await checker.testLandingPage();`
4. Review `checker.testResults` for aggregated outcomes.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Automated UI Testing Framework]]
- [[Puppeteer Configuration Guide]]

>[!INFO] Important Note
> The script uses a headless browser with aggressive security flags (`--disable-web-security`). Ensure the target environment allows these flags or adjust them for production use.

>[!WARNING] Caution
> Screenshots are saved to `./feature-screenshots/{date}/`. Delete the directory manually to avoid clutter. The `timeout` settings may need adjustment for slow APIs.
