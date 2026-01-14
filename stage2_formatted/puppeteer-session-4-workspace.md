**Tags:** #automated-web-testing, #puppeteer, #web-scraping, #workspace-analysis, #interactive-element-check
**Created:** 2026-01-13
**Type:** code-test

# puppeteer-session-4-workspace

## Summary

```
Automated Puppeteer test script to validate and analyze a writer workspace application, checking for content, interactive elements, and screenshot capture.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local writer workspace application (running on `localhost:5173/workspace`), and perform automated checks. It captures screenshots at key stages, extracts page content via `page.evaluate()`, and verifies the presence of workspace-specific keywords (e.g., "workspace," "Cyberpunk Neo-Tokyo 2087"). The script also inspects interactive elements (inputs, buttons, dropdowns) and logs findings. The results are returned as an object with boolean flags for detected features.

## Key Functions

### `testWorkspace()`

Orchestrates the entire session, including browser launch, page navigation, content analysis, and screenshot capture.

### `takeScreenshot(name)`

Captures a full-page screenshot with a timestamped filename and logs success/failure.

### `page.evaluate()`

Extracts the inner text of the webpage body for keyword-based analysis.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run the script (`node puppeteer-session-4-workspace`).
3. The script will:
   - Launch a headless browser with custom Puppeteer options.
   - Navigate to `http://localhost:5173/workspace`.
   - Capture screenshots at three stages (workspace load, analysis, interactions).
   - Log keyword matches (e.g., "writing tools," "Cyberpunk Neo-Tokyo 2087").
   - Return an object with boolean flags for detected features.
   - Save screenshots to a `screenshots/session-4-workspace` directory.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-testing-guide]]
- [[local-web-app-validation]]

>[!INFO] Important Note
> The script assumes the target application is running on `localhost:5173/workspace`. If the URL changes, update the `page.goto()` path accordingly.
>

>[!WARNING] Caution
> Disabling security features (`--disable-web-security`) may expose the browser to security risks. Use only in controlled environments.
