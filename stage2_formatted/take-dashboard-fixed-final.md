**Tags:** #automation, #web-scraping, #puppeteer, #dashboard-testing, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-notes

# take-dashboard-fixed-final

## Summary

```
Automated screenshot capture for a fixed dashboard and interactive page using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a dashboard at `http://localhost:3001/dashboard`, and capture full-page screenshots. It first takes a screenshot of the dashboard with fixed-position cards (no underlines) and then simulates clicking the "Worlds" card to navigate to the World Map page, capturing that screenshot as well. The script includes error handling and ensures the browser closes properly after execution.

## Key Functions

### `takeDashboardFixedFinal`

Orchestrates the entire process: browser launch, navigation, screenshot capture, and cleanup.

### `puppeteer.launch`

Initializes a headless Chrome instance with security flags.

### `page.goto`

Navigates to the dashboard URL with network idle wait.

### `page.screenshot`

Captures full-page screenshots at specified paths.

### `page.click`

Simulates clicking the "Worlds" card link to trigger navigation.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node take-dashboard-fixed-final.js`.
3. Ensure `http://localhost:3001/dashboard` is accessible and the dashboard has the expected structure (e.g., clickable "Worlds" card).

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `--no-sandbox` and `--disable-setuid-sandbox` for security, which may not work in restricted environments (e.g., Docker without proper permissions).
> Ensure the target URL (`localhost:3001`) resolves correctly and the dashboard renders fully before execution.

>[!WARNING] Caution
> Headless mode (`headless: true`) may not work in all environments. Test in a local environment first.
> Screenshots are saved as `dashboard-fixed-final.png` and `world-map-page.png` in the working directory.
