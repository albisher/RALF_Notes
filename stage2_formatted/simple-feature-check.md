**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #error-handling
**Created:** 2026-01-13
**Type:** code-notes

# simple-feature-check

## Summary

```
Automated UI feature verification tool using Puppeteer to validate web application pages and capture screenshots.
```

## Details

> This script automates UI feature checks by launching a Puppeteer browser instance, navigating to predefined URLs, and capturing screenshots of each page. It evaluates page titles to determine if pages load successfully, logs results, and organizes screenshots in a timestamped directory. The tool handles errors gracefully by saving additional screenshots for failed tests.

## Key Functions

### `SimpleFeatureCheck`

Main class managing screenshot directory, URL testing, and Puppeteer browser lifecycle.

### ``init()``

Sets up the screenshot directory with a date-based naming convention.

### ``getScreenshotName(feature, description)``

Generates filenames by cleaning descriptions and appending timestamp/counter.

### ``takeScreenshot(page, feature, description)``

Captures a full-page screenshot and logs success/failure.

### ``testPage(page, url, feature, description)``

Navigates to a URL, takes a screenshot, and checks page title validity.

### `runAllTests()`

Orchestrates the entire test suite, launches Puppeteer, executes tests sequentially, and aggregates results.

## Usage

1. Initialize the class: `const checker = new SimpleFeatureCheck();`
2. Run tests: `await checker.runAllTests();`
3. Configure `baseUrl` in constructor if needed (defaults to `localhost:8443`).
4. Extend the `tests` array in `runAllTests()` to include additional endpoints.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-testing-guide]]
- [[web-automation-best-practices]]

>[!INFO] Important Note
> Screenshots are saved in `./feature-screenshots/<YYYYMMDD>/` with filenames like `YYYYMMDD-0001-feature-description.png`. Always check this directory for test results.

>[!WARNING] Caution
> Avoid running this in production environments without proper sandboxing. The script uses `--no-sandbox` for testing, which may expose security risks. Use `--headless: new` for modern browser rendering.
