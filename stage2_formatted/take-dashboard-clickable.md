**Tags:** #automation, #web-scraping, #puppeteer, #dashboard-testing, #click-testing
**Created:** 2026-01-13
**Type:** code-notes

# take-dashboard-clickable

## Summary

```
Automates Puppeteer-based screenshot capture and click testing for a dashboard UI.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a local dashboard (localhost:3001), and capture screenshots of the dashboard before and after clicking a card link. It records the UI state with clickable elements (e.g., cards) to verify interactive functionality. The process includes viewport setup, network idle waiting, and error handling for robustness.

## Key Functions

### `takeDashboardClickableScreenshot()`

Orchestrates the entire workflow: browser launch, navigation, screenshot capture, click simulation, and cleanup.

### `puppeteer.launch()`

Initializes a headless Chrome instance with security flags.

### `page.goto()`

Navigates to the dashboard URL with network idle wait.

### `page.screenshot()`

Captures full-page screenshots at two stages (initial and post-click).

### `page.click()`

Simulates clicking a card link (e.g., `/elements`).

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node take-dashboard-clickable.js`.
3. Ensure the dashboard is accessible at `http://localhost:3001/dashboard`.

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the dashboard is hosted locally on port 3001. Adjust the URL if needed.

>[!WARNING] Caution
> Headless mode may block certain security features. Use `--no-sandbox` and `--disable-setuid-sandbox` for testing on non-root systems. Avoid running in production.
