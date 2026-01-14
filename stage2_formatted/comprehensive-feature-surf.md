**Tags:** #automated-testing, #web-scraping, #puppeteer, #api-testing, #frontend-validation
**Created:** 2026-01-13
**Type:** code-notes

# comprehensive-feature-surf

## Summary

```
Automated web application feature validation using Puppeteer to test API endpoints, UI elements, and authentication flows with screenshot capture.
```

## Details

> This script implements a comprehensive automated testing framework for web applications using Puppeteer. It initializes a browser session, validates critical UI elements (health checks, landing pages, authentication flows, and dashboards), and captures screenshots for debugging. The helper class (`CheckHelper`) records test results with pass/fail statuses and descriptive messages. The `config` module provides URL and timeout settings, while `CheckHelper` manages result aggregation.

## Key Functions

### ``ComprehensiveFeatureSurf``

Main class orchestrating all tests.

### ``init()``

Sets up a timestamped screenshot directory.

### ``getScreenshotName(feature, description)``

Generates filenames with date, counter, and sanitized feature descriptions.

### ``takeScreenshot(page, feature, description)``

Captures browser page snapshots with error handling.

### ``testHealthCheck(page)``

Validates API health endpoint response via content check.

### ``testLandingPage(page)``

Checks for a non-empty page title.

### ``testAuthentication(page)``

Verifies login/register form existence on `/login` and `/register` routes.

### ``testDashboard(page)``

Confirms dashboard element visibility via CSS selector.

## Usage

1. Initialize with `new ComprehensiveFeatureSurf()`.
2. Call `init()` to create a date-stamped screenshot directory.
3. Execute test methods sequentially (e.g., `await surf.testHealthCheck(browser)`).
4. Results are logged via `helper.addResult()` and stored in `CheckHelper`.

## Dependencies

> `puppeteer`
> `chalk`
> `fs`
> `path`
> `config (local)`
> `CheckHelper (local)`

## Related

- [[`config]]
- [[`check-helper]]

>[!INFO] Important Note
> Screenshots are saved in `./feature-screenshots/<YYYY-MM-DD>/` with sequential numbering. Always check `this.screenshotDir` before running tests.

>[!WARNING] Caution
> Timeout values (`config.timeouts.pageLoad`) must be sufficiently high for slow pages. Exceeding them may cause `page.goto()` to fail silently.
