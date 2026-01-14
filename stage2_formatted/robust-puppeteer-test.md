**Tags:** #automated-testing, #puppeteer, #web-testing, #ui-automation, #error-handling
**Created:** 2026-01-13
**Type:** code-notes

# robust-puppeteer-test

## Summary

```
Automated UI testing framework using Puppeteer to validate web application robustness with screenshot logging and credential-based testing.
```

## Details

> This script implements a **RobustPuppeteerTest** class for automated UI testing of web applications. It initializes a Puppeteer instance, handles screenshot generation for debugging, and performs connection and login flow validation. The class dynamically searches for form elements using multiple selectors to ensure compatibility with varying UI implementations. Error handling is robust, capturing failures gracefully while logging detailed diagnostics.
> 
> The core logic includes:
> 1. **Initialization** – Creates a screenshot directory and logs test setup.
> 2. **Screenshot Management** – Generates timestamped filenames for UI checks.
> 3. **Connection Testing** – Validates basic HTTP access and page title retrieval.
> 4. **Login Flow** – Automates credential input and submission, with fallback for missing buttons.

## Key Functions

### ``init()``

Sets up directory structure and logs test metadata.

### ``getScreenshotName(feature, description)``

Generates a sanitized filename combining feature, timestamp, and description.

### ``takeScreenshot(page, feature, description)``

Captures a full-page screenshot with error handling.

### ``testBasicConnection(page)``

Verifies HTTP connectivity and page title via Puppeteer.

### ``testLoginFlow(page)``

Attempts to log in using predefined credentials, with fallback for missing UI elements.

## Usage

```javascript
const test = new RobustPuppeteerTest();
await test.init();
const browser = await puppeteer.launch();
const page = await browser.newPage();
await test.testBasicConnection(page);
await test.testLoginFlow(page);
await browser.close();
```

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Puppeteer Test Framework Guide]]
- [[UI Automation Best Practices]]

>[!INFO] Important Note
> **Dynamic Selectors**: The script uses fallback selectors (e.g., `input[name="username"]`, `input[type="text"]`) to adapt to varying UI structures. If no matching element is found, it logs an error and takes a screenshot for debugging.


>[!WARNING] Caution
> **Timeouts**: Explicit timeouts (e.g., `timeout: 30000`) are used for `page.goto()` to prevent hanging. Adjust values based on application latency. **Avoid `waitForTimeout` in production**—use explicit waits or `page.waitForSelector()` instead.
