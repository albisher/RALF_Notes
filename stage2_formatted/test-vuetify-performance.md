**Tags:** #performance-testing, #web-performance, #vuetify, #puppeteer, #network-analysis, #css-loading
**Created:** 2026-01-13
**Type:** code-test

# test-vuetify-performance

## Summary

```
Tests Vuetify component performance by analyzing network requests, rendering metrics, and CSS loading.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a local Vuetify-powered page, and collect performance metrics. It tracks network requests (filtering for Vuetify-related URLs), captures rendering timings (load time, DOM load, first paint), checks for console errors, and verifies Vuetify component and CSS presence. Error handling includes screenshot capture for debugging.

## Key Functions

### `testVuetifyPerformance`

Orchestrates the full performance test workflow.

### `networkRequests filter`

Captures Vuetify and node_modules-related HTTP requests.

### `Performance Metrics evaluation`

Extracts `loadTime`, `domContentLoaded`, `firstPaint`, and `firstContentfulPaint` via `performance.timing`.

### `Console Errors check`

Retrieves and logs any JavaScript errors via `page.evaluate()`.

### `Vuetify Component detection`

Counts elements with Vuetify class prefixes (`[class*="v-"]`).

### `CSS Loading validation`

Checks if `<link rel="stylesheet">` tags reference Vuetify or Material Design Icons (MDI).

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-vuetify-performance.js`.
3. Ensure the target page (e.g., `localhost:8443`) serves a Vuetify application.
4. Outputs:
   - Console logs with metrics.
   - Screenshots (`checks/screenshots/`) for success/error states.
   - JSON object with aggregated results.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Performance Optimization Guide for Vuetify]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script disables security features (`--disable-web-security`) for local testing. Avoid running this on production servers.

>[!WARNING] Caution
> Headless browser flags (`--no-sandbox`) may require elevated permissions on some systems. Test in a controlled environment.
