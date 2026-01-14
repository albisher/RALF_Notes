**Tags:** #automated-testing, #browser-testing, #puppeteer, #vue-app-validation, #robust-configuration
**Created:** 2026-01-13
**Type:** code-notes

# robust-browser-test

## Summary

```
Automated browser test suite for validating a Vue.js application using Puppeteer with robust error handling and screenshot capture.
```

## Details

> This script uses Puppeteer to launch a browser with aggressive security and performance settings, then systematically tests a Vue.js application by navigating through key pages (login, dashboard, elements). It verifies Vue app mounting via `#app` selector, checks for console errors, and captures screenshots of each page. The test includes fallback error screenshot capture if the main test fails.

## Key Functions

### `RobustBrowserTest.init()`

Creates directory for screenshots and logs initialization.

### `RobustBrowserTest.takeScreenshot(page, filename)`

Captures full-page screenshots with error handling.

### `RobustBrowserTest.testApplication()`

Core test method that:

### `main()`

Entry point that instantiates the test class and runs tests.

## Usage

1. Install dependencies: `npm install puppeteer`
2. Configure `baseUrl` to point to your application (default: `https://localhost:8443`)
3. Run script: `node robust-browser-test.js`
4. Screenshots will be saved in `./screenshots/robust-test/`

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Robust Application Testing Guide]]
- [[Puppeteer Configuration Best Practices]]

>[!INFO] Important Note
> The browser launch configuration includes aggressive security flags (`--disable-web-security`, `--ignore-ssl-errors`) that may not be suitable for production environments. Use with caution in development/testing contexts only.


>[!WARNING] Caution
> The test will fail if the application fails to load any page. The error screenshot capture attempts to mitigate this but may not always succeed. Consider adding retry logic for critical pages.
