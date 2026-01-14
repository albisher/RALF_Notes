**Tags:** #debugging, #web-scraping, #puppeteer, #login-page, #automated-testing, #frontend-analysis
**Created:** 2026-01-13
**Type:** code-notes

# debug-login-page

## Summary

```
Debugs and inspects a login page using Puppeteer to analyze UI structure, errors, and visibility.
```

## Details

> This script uses Puppeteer to launch a browser with Chrome headless disabled, inspect the login page at `localhost:8443/login`, and perform several checks:
> 1. **Basic UI Validation**: Verifies the existence of the `#app` element and logs its content length.
> 2. **Dynamic Element Detection**: Evaluates all visible DOM elements (using `offsetWidth/offsetHeight`) and logs their tags, text, and classes.
> 3. **Error Handling**: Checks for JavaScript errors via `window.console.error` and logs them.
> 4. **Visual Inspection**: Captures a full-page screenshot for debugging purposes.
> The script includes error handling, console logging for debugging, and cleanup of the browser instance.

## Key Functions

### ``DebugLoginPage``

Class encapsulating the login page debugging logic.

### ``constructor()``

Initializes the base URL (`https://localhost:8443`).

### ``runTest()``

Core method that:

### ``page.on('console', ...)``

Logs browser console messages.

### ``page.on('pageerror', ...)``

Logs page-level errors.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node debug-login-page.js`.
3. Ensure the target login page (`localhost:8443/login`) is accessible.

## Dependencies

> `puppeteer`
> `Chrome browser (bundled via `--executablePath`).`

## Related

- [[Debugging Framework Notes]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script uses Chrome’s `--disable-web-security` and `--ignore-ssl-errors` flags, which may expose the page to security risks in production. Use only in controlled environments.

>[!WARNING] Caution
> The `page.evaluate()` call for visible elements (`document.querySelectorAll('*')`) is computationally expensive. Limit its scope if debugging large pages.
