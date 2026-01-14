**Tags:** #automated-testing, #web-scraping, #puppeteer, #element-interaction, #api-integration
**Created:** 2026-01-13
**Type:** code-test

# test-element-deletion

## Summary

```
Tests deletion functionality of web elements using Puppeteer to interact with a local elements page.
```

## Details

> This script automates the process of locating, clicking, and confirming deletion of elements on a web page hosted locally at `https://localhost:8443/elements`. It uses Puppeteer to launch a headless browser, navigate to the page, and interact with elements by identifying delete buttons, triggering deletion, and capturing screenshots at each step. The script logs the number of elements and delete buttons found, checks for confirmation dialogs, and records network requests related to deletion attempts.

## Key Functions

### `testElementDeletion`

Orchestrates the entire deletion test workflow, including browser setup, element interaction, and screenshot capture.

### `puppeteer.launch`

Launches a Puppeteer browser instance with security and performance optimizations.

### `page.evaluateHandle`

Executes JavaScript in the context of the page to dynamically find and interact with delete buttons.

### `page.goto`

Navigates to the target URL with configurable wait and timeout settings.

### `page.screenshot`

Captures screenshots at predefined stages (pre-deletion, post-click, post-deletion).

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Ensure the target web page (`https://localhost:8443/elements`) is accessible.
3. Run the script: `node test-element-deletion.js`.
4. Verify screenshots and logs in the `checks/screenshots` directory for visual confirmation of deletion steps.

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the target page contains elements with `element-card` or similar classes and delete buttons with text/HTML containing "Delete," "حذف," or "mdi-delete" icons. Adjust selectors if the UI differs.
>

>[!WARNING] Caution
> Running in headless mode with `--disable-web-security` and `--ignore-ssl-errors` may expose the browser to security risks if misconfigured. Use only in trusted environments. Ensure the local server (`localhost:8443`) is secure and properly authenticated.
