**Tags:** #automated-testing, #puppeteer, #web-scraping, #hash-generation, #dialog-interaction, #ui-testing
**Created:** 2026-01-13
**Type:** code-test

# test-enhanced-hash-details

## Summary

```
Automated UI test for enhanced hash details panel using Puppeteer to verify character creation workflow with hash-based generation.
```

## Details

> This script automates a browser session to test a web application’s character creation workflow, specifically focusing on the enhanced hash details panel. It launches a headless browser, navigates to a world detail page, and verifies interactions with the "Add Character" button. After opening a dialog, it selects hash-based generation, inputs a seed, and checks if the enhanced hash details panel appears. The test captures screenshots at critical steps for validation.
> 
> The workflow includes login, navigation, and interaction with UI elements (buttons, dialogs, and inputs) to simulate user actions. It uses Puppeteer’s `evaluateHandle` to locate dynamic elements and `jsonValue()` to confirm their existence before triggering actions.

## Key Functions

### `testEnhancedHashDetails`

Orchestrates the entire automated test sequence, including browser setup, navigation, and UI interaction validation.

### `puppeteer.launch`

Configures and launches a headless Chrome browser with security and performance optimizations.

### `page.evaluateHandle`

Dynamically locates and interacts with elements (e.g., buttons, inputs, dialogs) using JavaScript in the browser context.

### `page.screenshot`

Captures screenshots of UI states (e.g., dialogs, panels) for verification.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-enhanced-hash-details.js`.
3. Ensure the target application (`https://localhost:8443`) is accessible and the UI supports the expected interactions (e.g., login, hash-based character creation).

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the target application uses a multi-language UI (e.g., Arabic/English buttons). Adjust selectors (e.g., `textContent.includes`) if the UI changes.
>

>[!WARNING] Caution
> Headless browser flags (`--no-sandbox`, `--disable-web-security`) may bypass security checks. Use cautiously in production environments. The `ignoreHTTPSErrors` flag disables SSL validation—only for testing local/self-signed certs.
