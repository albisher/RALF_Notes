**Tags:** #automation, #web-scraping, #puppeteer, #screenshot, #testing
**Created:** 2026-01-13
**Type:** code-notes

# take-screenshots-fixed

## Summary

```
Automates capturing full-page screenshots of a fixed application state using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless Chrome browser, navigate to a local web application (`http://localhost:3001`), and systematically capture screenshots of predefined pages (`dashboard`, `timeline`, `characters`, `elements`). It includes error handling and logging for debugging. The screenshots are saved as `fixed-initial-state.png` and `fixed-{pageName}.png`.

## Key Functions

### `takeScreenshotsFixed`

Orchestrates the entire screenshot capture process, including browser initialization, navigation, and cleanup.

### `page.goto()`

Navigates to each specified URL with a delay to ensure page content loads.

### `page.screenshot()`

Captures full-page screenshots at each step.

### `browser.close()`

Ensures browser resources are released after completion.

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node take-screenshots-fixed.js`.
3. Ensure the target application (`http://localhost:3001`) is running before execution.

## Dependencies

> `puppeteer`
> `fs`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `--no-sandbox` and `--disable-setuid-sandbox` for security, which may not work in restricted environments (e.g., Docker without proper permissions).
> Ensure the target application is fully loaded before screenshots are taken to avoid partial captures.

>[!WARNING] Caution
> Headless mode (`headless: true`) may not work in all environments. If Puppeteer fails silently, check logs for errors like `Failed to launch browser`.
