**Tags:** #automation, #web-scraping, #puppeteer, #testing, #screenshot
**Created:** 2026-01-13
**Type:** code-notes

# simple-screenshot-test

## Summary

```
Automated screenshot capture and UI validation for a local web application using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a local web application (running on `localhost:5173`), and capture a full-page screenshot. It dynamically checks for UI elements like login forms, password fields, and submit buttons while logging the page title and screenshot path. The directory structure for screenshots is timestamped to avoid conflicts, and the script includes error handling and cleanup of the browser instance.

## Key Functions

### `takeScreenshot()`

Core function that launches Puppeteer, captures a screenshot, validates UI elements, and returns metadata.

### `Browser initialization`

Configures Puppeteer with security and performance flags for stability.

### `Directory creation`

Dynamically creates a timestamped folder for screenshots if it doesn’t exist.

### `UI validation`

Checks for common login-related elements (e.g., `input[type="text"]`, `button[type="submit"]`).

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node simple-screenshot-test.js`.
3. Outputs:
   - Screenshot saved at `feature-screenshots/<YYYYMMDD>-<timestamp>-landing-page.png`.
   - Console logs for UI validation results and page title.
   - Exit code `0` on success, `1` on failure.

## Dependencies

> `puppeteer`
> `path`
> `fs`

## Related

- [[puppeteer-testing-guide]]
- [[local-web-app-validation]]

>[!INFO] Important Note
> The script uses `networkidle2` to ensure all resources (e.g., images, scripts) load before capturing the screenshot. Adjust `timeout` if the page takes longer to load.

>[!WARNING] Caution
> Avoid running this on production servers—it requires `localhost` and may conflict with existing screenshots if the timestamp format overlaps. Use `--no-sandbox` cautiously in restricted environments.
