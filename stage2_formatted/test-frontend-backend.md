**Tags:** #automated-testing, #frontend-backend-integration, #puppeteer, #web-scraping, #api-testing
**Created:** 2026-01-13
**Type:** test-reference

# test-frontend-backend

## Summary

```
Automated frontend-backend integration test using Puppeteer to validate API connectivity and data display.
```

## Details

> This script uses Puppeteer to launch a browser headless, load a frontend application (presumably a React/Vue app running on `localhost:5173`), and perform several checks:
> 1. Verifies the frontend loads successfully by checking the page title.
> 2. Monitors network activity for API calls (e.g., `/api/` endpoints).
> 3. Analyzes rendered page content for expected UI elements (e.g., world statistics, demo worlds).
> 4. Manually triggers a direct API call via `page.evaluate()` to fetch `/api/worlds` and validates the response.
> 
> The test logs each step’s outcome (success/failure) and handles browser cleanup gracefully.

## Key Functions

### ``testFrontendBackend()``

Orchestrates the entire integration test workflow.

### ``puppeteer.launch()``

Configures and starts a headless browser with security/performance tweaks.

### ``page.goto()``

Loads the frontend application with timeout and wait-for logic.

### ``page.on('request')``

Captures and logs API requests (e.g., `/api/` endpoints).

### ``page.evaluate()``

Executes JavaScript in the context of the rendered page to:

### ``browser.close()``

Ensures proper cleanup after tests.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-frontend-backend.js`.
3. Expected frontend app to be running on `http://localhost:5173` with a backend API (e.g., `/api/worlds`).
4. The test logs results to `console` and exits on errors.

## Dependencies

> `puppeteer`
> `Node.js runtime.`

## Related

- [[None]]

>[!INFO] Important Note
> This script assumes the frontend is a React/Vue app (common with `vite`/`webpack`). Adjust `page.goto()` URL if the app uses a different port (e.g., `http://localhost:3000`).
>

>[!WARNING] Caution
> Disable `--disable-web-security` only for local development. In production, this bypasses CORS and security headers, risking vulnerabilities. Use only in controlled environments.
