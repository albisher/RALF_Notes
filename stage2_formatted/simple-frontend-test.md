**Tags:** #automated-testing, #frontend-testing, #puppeteer, #vue-js, #web-scraping
**Created:** 2026-01-13
**Type:** code-notes

# simple-frontend-test

## Summary

```
Automated frontend test script using Puppeteer to validate Vue.js application loading and structure.
```

## Details

> This script launches a headless Chrome browser with Puppeteer, navigates to a Vue.js frontend running on `localhost:5173`, and performs checks for the Vue application's presence and structure. It evaluates the DOM for Vue-specific elements (classes starting with `v-`), captures the app's content, and saves a full-page screenshot. Error handling and cleanup are managed via `try/catch`/`finally` blocks.

## Key Functions

### `testFrontend()`

Orchestrates the entire test workflow, including browser launch, navigation, DOM inspection, and cleanup.

### `page.evaluate()`

Executes JavaScript in the browser context to inspect the DOM (e.g., checking for Vue app elements).

### `page.screenshot()`

Captures a full-page screenshot of the rendered Vue app.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node simple-frontend-test.js`.
3. Ensure a Vue.js app is running locally at `http://localhost:5173`.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Vue]]
- [[Puppeteer API reference]]

>[!INFO] Important Note
> The script assumes the Vue app is hosted on `localhost:5173`. Adjust the URL if the frontend runs on a different port.

>[!WARNING] Caution
> Running Puppeteer in headless mode with `--no-sandbox` may expose security risks on non-trusted systems. Use with caution in production environments.
