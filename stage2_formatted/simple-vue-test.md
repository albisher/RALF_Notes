**Tags:** #automated-testing, #vue-testing, #puppeteer, #web-automation, #frontend-validation
**Created:** 2026-01-13
**Type:** code-test

# simple-vue-test

## Summary

```
Automates Vue.js application testing using Puppeteer to validate Vue availability, component rendering, and UI integrity.
```

## Details

> This script uses Puppeteer to launch a headless Chrome instance, interact with a Vue.js application running on `localhost:8443`, and perform basic validation checks. It evaluates whether Vue is properly loaded, checks for Vue components (`[data-v-]` attributes), verifies the presence of the `#app` element, and captures text content. The test logs results and saves a screenshot of the rendered page. The browser is closed automatically after execution.

## Key Functions

### ``SimpleVueTest.runTest()``

Orchestrates the entire test workflow, including browser launch, page navigation, and validation checks.

### ``page.evaluate()``

Executes JavaScript in the browser context to inspect Vue availability, component structure, and content.

### ``page.screenshot()``

Captures a full-page screenshot for visual verification.

## Usage

1. Install dependencies (`npm install puppeteer`).
2. Run the script (`node simple-vue-test.js`).
3. Ensure the Vue app is running on `localhost:8443` before execution.

## Dependencies

> `puppeteer`
> `Google Chrome (custom executable path provided).`

## Related

- [[Vue]]
- [[Puppeteer API reference]]

>[!INFO] Important Note
> The script uses a custom Chrome executable path (`/Applications/Google Chrome.app`) and disables security features (`--ignore-web-security`, `--disable-dev-shm-usage`) for testing. Avoid running this in production environments.

>[!WARNING] Caution
> The `waitUntil: 'networkidle2'` and `timeout` settings may fail if the server is slow or unresponsive. Adjust values if tests hang.
