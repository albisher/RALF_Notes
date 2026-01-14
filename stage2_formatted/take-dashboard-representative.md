**Tags:** #automation, #web-scraping, #puppeteer, #dashboard, #screenshot
**Created:** 2026-01-13
**Type:** code-notes

# take-dashboard-representative

## Summary

```
Automates taking a full-page screenshot of a dashboard with representative data using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless Chrome browser, navigate to a local dashboard endpoint (`http://localhost:3001/dashboard`), and capture a full-page screenshot (`dashboard-representative-numbers.png`). It includes error handling and ensures the browser is closed after execution. The script logs progress and errors to the console.

## Key Functions

### `takeDashboardRepresentative()`

Orchestrates the entire process: browser launch, navigation, screenshot capture, and cleanup.

### `puppeteer.launch()`

Initializes a headless Chrome instance with security flags (`--no-sandbox`, `--disable-setuid-sandbox`).

### `page.goto()`

Navigates to the dashboard URL with a network idle wait.

### `page.screenshot()`

Captures the full-page screenshot at the specified path.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node take-dashboard-representative.js`.
3. Ensure the dashboard is accessible at `http://localhost:3001/dashboard`.

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the dashboard is running locally on port `3001`. Adjust the URL if needed.

>[!WARNING] Caution
> Running Puppeteer in headless mode with `--no-sandbox` may bypass security checks. Use cautiously in production environments.
