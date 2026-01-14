**Tags:** #automated-testing, #web-scraping, #puppeteer, #dashboard-validation, #api-monitoring
**Created:** 2026-01-13
**Type:** code-test

# puppeteer-session-1-dashboard

## Summary

```
Automated dashboard validation script using Puppeteer to test a web application’s frontend and backend interactions.
```

## Details

> This script automates testing of a frontend dashboard by:
> 1. Launching a headless Chrome browser with Puppeteer.
> 2. Navigating to a local web app (Vite dev server at `localhost:5173`).
> 3. Capturing screenshots at key stages (dashboard load, analysis).
> 4. Extracting and validating dashboard metrics (worlds, characters, elements) via regex.
> 5. Monitoring API calls for backend interactions.
> 6. Returning structured results (world/character counts, demo world flag, API request count).
> 
> The script includes error handling, resource cleanup, and logging for debugging.

## Key Functions

### `testDashboard()`

Orchestrates the full session workflow (browser launch, page navigation, analysis, screenshot capture, API monitoring).

### `takeScreenshot(name)`

Captures a full-page screenshot with timestamped filename and logs success/failure.

### `page.on('request', ...)`

Intercepts and logs API requests (URL, method, headers) during execution.

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run script: `node puppeteer-session-1-dashboard.js`.
3. Outputs:
   - Console logs (status, metrics, errors).
   - Screenshots in `./screenshots/session-1-dashboard/`.
   - Structured JSON result object (e.g., `worldCount`, `apiRequests`).

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-testing-framework]]
- [[dashboard-validation-guidelines]]

>[!INFO] Important Note
> The script uses `--disable-web-security` and `--disable-features=VizDisplayCompositor` for compatibility with local development environments. **Avoid production use**—these flags weaken security.

>[!WARNING] Caution
> Headless mode (`--headless`) may fail if the target app relies on visual cues. Test in non-headless mode first to verify functionality.
