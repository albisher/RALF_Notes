**Tags:** #automated-testing, #vuejs, #puppeteer, #frontend-validation, #vue-testing
**Created:** 2026-01-13
**Type:** code-notes

# vue-app-comprehensive-test

## Summary

```
Automated Vue.js application validation using Puppeteer to verify rendering, components, and UI elements.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a Vue.js application running on `localhost:8443`, and perform a comprehensive validation check. It verifies the presence of Vue’s root container (`#app`), checks for Vuetify components, CSS classes (Tailwind, custom scrollbars, sidebar), router view, console errors, and loading states. The test also captures a screenshot and logs the page title. The browser is properly closed in a `finally` block to ensure cleanup.

## Key Functions

### ``vueAppComprehensiveTest()``

Orchestrates the entire test workflow, including browser launch, navigation, and validation checks.

### ``page.evaluate()``

Executes JavaScript in the browser context to inspect DOM elements dynamically.

### ``page.waitForSelector()``

Waits for a specific DOM selector to appear before proceeding.

### ``page.screenshot()``

Captures a full-page screenshot for debugging.

### ``process.on('unhandledRejection')``

Handles unhandled promise rejections gracefully.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node vue-app-comprehensive-test.js`.
3. Ensure the Vue app is running on `localhost:8443` before execution.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Vue]]
- [[Puppeteer Documentation]]
- [[Automated UI Testing Best Practices]]

>[!INFO] Important Note
> This script assumes the Vue app is hosted on `localhost:8443`. Adjust the URL if the app runs on a different port or domain.

>[!WARNING] Caution
> Headless mode (`--no-sandbox`) may not work in all environments (e.g., Docker containers). Use `--headless: none` for debugging if issues arise.
