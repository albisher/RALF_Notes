**Tags:** #i18n-testing, #puppeteer, #vue-internals, #debugging, #internet-research
**Created:** 2026-01-13
**Type:** code-test

# i18n-debug-test

## Summary

```
Debugs i18n functionality in a Vue.js application using Puppeteer to inspect errors and validate translations.
```

## Details

> This script uses Puppeteer to launch a browser instance with Chrome headless disabled, then interacts with a local Vue.js application running on `localhost:8443`. It captures JavaScript errors, checks for the existence of Vue’s i18n translation functions (`$t`), and evaluates Vue compilation errors. The test also logs i18n-related issues, screenshots the UI, and ensures proper error handling. The `page.evaluate()` method runs checks inside the browser context to detect missing or broken i18n components.

## Key Functions

### ``runTest()``

Orchestrates the entire test workflow, including browser launch, navigation, error checks, and cleanup.

### ``page.on('console', msg => ...)``

Logs browser console messages (e.g., warnings, errors) for debugging.

### ``page.evaluate()` (i18nTest)`

Validates i18n availability by checking `$t` function and `__VUE_I18N__` global, with error handling.

### ``page.evaluate()` (vueErrors)`

Scans console.error logs for Vue-specific compilation errors.

### ``page.screenshot()``

Captures a full-page screenshot for visual debugging.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node i18n-debug-test.js`.
3. Ensure the target Vue app is running on `localhost:8443` with i18n enabled.
4. Check logs for errors, i18n issues, or Vue compilation problems.

## Dependencies

> `puppeteer`
> `Chrome browser (bundled via `/Applications/Google Chrome.app`).`

## Related

- [[Vue i18n documentation]]
- [[Puppeteer debugging guide]]
- [[Vue]]
- [[i18n troubleshooting]]

>[!INFO] Important Note
> The script uses Chrome’s bundled executable path (`/Applications/Google Chrome.app`), which may fail on non-Mac systems. Replace with a local Chrome binary (e.g., `executablePath: '/usr/bin/chrome'`).

>[!WARNING] Caution
> Headless mode is disabled (`headless: false`) for debugging. Ensure the target app is not running in production mode with security restrictions.
