**Tags:** #frontend-verification, #ui-testing, #puppeteer, #web-automation, #design-verification
**Created:** 2026-01-13
**Type:** code-notes

# master-design-verification

## Summary

```
Automated UI design verification tool using Puppeteer to check frontend structure, styling, and components.
```

## Details

> This script automates UI design verification by launching a browser, logging into a local application, and validating the presence of key frontend components (e.g., layout, sidebar, dashboard) and CSS frameworks (Tailwind/Vuetify). It captures screenshots and evaluates DOM structure via `page.evaluate()`, logging results for debugging. The test runs in a controlled environment with Chrome-specific launch options to bypass sandbox restrictions.

## Key Functions

### ``runTest()``

Orchestrates the full test workflow: browser launch, login, UI verification, and screenshot capture.

### ``page.evaluate()``

Executes JavaScript in the rendered page to inspect DOM elements and CSS presence dynamically.

### ``page.goto()``

Navigates to the target URL with network idle wait.

### ``page.type()`/`page.click()``

Simulates user interactions (login).

### ``page.screenshot()``

Captures full-page screenshots for verification.

## Usage

1. Initialize the class: `const verifier = new MasterDesignVerification()`.
2. Call `verifier.runTest()` to execute the full verification pipeline.
3. Review console logs for component presence and screenshot paths.

## Dependencies

> `puppeteer`
> `Chrome browser (bundled via `executablePath`)`

## Related

- [[Design Verification Framework]]
- [[Puppeteer Automation Guide]]

>[!INFO] Important Note
> The script uses Chrome’s `--disable-web-security` flag, which may expose the app to XSS risks in production. Use only in sandboxed environments.

>[!WARNING] Caution
> Hardcoded credentials (`test/testpass`) are insecure. Replace with environment variables or a secure credential manager.
