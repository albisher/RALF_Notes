**Tags:** #browser-debug, #puppeteer, #vue-app-check, #frontend-validation, #console-logging, #network-inspection
**Created:** 2026-01-13
**Type:** code-notes

# browser-debug-check

## Summary

```
Automated browser debugging tool to validate frontend functionality, Vue app state, and UI elements via Puppeteer.
```

## Details

> This script uses Puppeteer to launch a non-headless browser, interact with frontend pages (main and login), and perform checks for Vue app presence, UI elements, and network/console logs. It captures screenshots, evaluates page content via `page.evaluate()`, and logs detailed debugging data for manual inspection. The script runs through a sequence of navigation and validation steps, categorizing results as pass/fail based on Vue app detection and login form presence.

## Key Functions

### `runBrowserDebugCheck()`

Orchestrates the entire debugging workflow, including browser launch, page navigation, and result aggregation.

### `CheckHelper.takeScreenshot()`

Captures UI screenshots with relative paths for reporting.

### `page.evaluate()`

Executes client-side JavaScript to inspect Vue app state and DOM elements.

### `consoleLogs/NetworkLogs capture`

Logs browser console and network activity for debugging.

## Usage

1. Require and call `runBrowserDebugCheck()` directly or via `module.exports`.
2. Configure `config` (e.g., Puppeteer options, URLs, timeouts).
3. Manually inspect the browser window after execution (browser remains open unless commented out).
4. Review generated report via `helper.generateReport()`.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper`

## Related

- [[Browser Debug Configuration]]
- [[Vue Frontend Validation Guide]]

>[!INFO] Important Note
> The browser remains open for manual inspection unless explicitly closed via `await browser.close()`. Ensure the script is run in a controlled environment with proper cleanup.


>[!WARNING] Caution
> Avoid running this in production environments without proper error handling. Network/console logs may contain sensitive data if not sanitized.
