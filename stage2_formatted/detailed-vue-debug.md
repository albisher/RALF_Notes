**Tags:** #Vue.js, #Puppeteer, #Automated Testing, #Frontend Debugging, #Web Scraping
**Created:** 2026-01-13
**Type:** code-notes

# detailed-vue-debug

## Summary

```
Debugs a Vue.js application by inspecting its state, components, and UI elements using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless Chrome instance and interact with a Vue.js application running on `localhost:8443`. It performs detailed debugging by:
> 1. Launching Chrome with custom options to bypass security restrictions.
> 2. Navigating to the login page and inspecting Vue.js runtime state (e.g., `Vue`, `VueApp`, `router`).
> 3. Evaluating the DOM to detect Vue components (using `data-v-` attributes) and analyzing their structure.
> 4. Checking for Vue-related errors in the browser console.
> 5. Identifying login-related UI elements and form components.
> 6. Capturing a screenshot of the page for visual inspection.
> 
> The script logs all findings to the console and handles errors gracefully.

## Key Functions

### ``runTest()``

Orchestrates the entire debugging workflow, including browser launch, page navigation, and DOM inspection.

### ``page.evaluate()` callbacks`

Extract Vue app state, router details, and UI element metadata via JavaScript execution in the browser context.

### ``page.on('console', ...)` and `page.on('pageerror', ...)``

Capture browser console logs and errors for debugging.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node detailed-vue-debug.js`.
3. Ensure the Vue app is running on `localhost:8443` (adjust `baseUrl` if needed).

## Dependencies

> `puppeteer`
> `Google Chrome (bundled in the script).`

## Related

- [[Vue]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> The script requires Chrome to be installed and accessible at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. If Chrome is not found, Puppeteer will fail to launch.

>[!WARNING] Caution
> Running Chrome in `--disable-web-security` mode may expose the application to security risks. Use only in controlled environments for debugging.
