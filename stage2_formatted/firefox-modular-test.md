**Tags:** #web-testing, #puppeteer, #firefox-browser, #modular-testing, #frontend-validation
**Created:** 2026-01-13
**Type:** code-notes

# firefox-modular-test

## Summary

```
Automated modular test suite for verifying a web application's frontend functionality using Puppeteer with Firefox.
```

## Details

> This script automates Firefox-based testing of a web application hosted locally (port 8443) by validating UI elements, content loading, navigation, and error handling. It uses Puppeteer to launch Firefox in headless mode, interact with the page, and execute 11 validation tests via page methods and JavaScript `evaluate()` calls. The test suite logs results for each check, including element existence, content loading, and structural integrity.

## Key Functions

### `firefoxModularTest`

Orchestrates the entire test workflow, including browser launch, page navigation, and test execution.

### `page.on('console')`

Captures and logs all console messages (including errors) for debugging.

### `page.evaluate()`

Executes arbitrary JavaScript in the page context to inspect DOM elements dynamically.

### `page.goto()`

Navigates to the target URL with configurable wait and timeout settings.

## Usage

1. Install Puppeteer: `npm install puppeteer`
2. Run the script: `node firefox-modular-test.js`
3. Ensure the target application (localhost:8443) is running before execution.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Web Application UI Specifications]]
- [[Puppeteer Testing Framework Guide]]

>[!INFO] Important Note
> This script assumes the target application uses IDs (`#sidebar-container`, `#page-content`) and classes (`.nav-link`, `.nav-group-header`) for consistent testing. Adjust selectors if the application structure differs.

>[!WARNING] Caution
> The `--no-sandbox` and `--ignore-ssl-errors` flags disable security protections. Use only in trusted environments. Headless mode (`'new'`) may not work in all environments; test with visible browser first.
