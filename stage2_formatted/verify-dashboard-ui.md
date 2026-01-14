**Tags:** #automated-testing, #ui-verification, #puppeteer, #frontend-validation, #dashboard-check
**Created:** 2026-01-13
**Type:** test-reference

# verify-dashboard-ui

## Summary

```
Automated UI verification script for a dashboard application using Puppeteer to validate dashboard content, navigation, and error conditions.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local web application (running on `http://localhost:5173`), and systematically verify the dashboard UI. It captures screenshots at key stages, checks for specific UI elements (e.g., statistics cards, character/world listings), and logs console/network activity. The workflow includes validation of dashboard content, character/world pages, and error handling.

## Key Functions

### `verifyDashboardUI`

Orchestrates the entire UI verification process, including browser launch, navigation, UI checks, and screenshot capture.

### `puppeteer.launch`

Configures and starts a browser instance with debugging enabled.

### `page.goto`

Navigates to the application URL with network idle wait.

### `page.waitForSelector`

Ensures dashboard content loads before proceeding.

### `page.evaluate`

Extracts text content from dynamically rendered elements (e.g., stat cards).

### `page.screenshot`

Captures full-page screenshots at critical points.

### `page.click`

Simulates user navigation to characters/worlds pages.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node verify-dashboard-ui.js`.
3. Ensure the application is running locally at `http://localhost:5173`.
4. Outputs:
   - Console logs for verification steps.
   - Screenshots saved to `checks/screenshots/`.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Dashboard UI Design Spec]]
- [[Application API Documentation]]

>[!INFO] Important Note
> The script uses `--no-sandbox` and other flags for debugging, which may not be secure in production. Disable these in production environments.

>[!WARNING] Caution
> Network requests and console logs are logged via `page.evaluate()`, which may expose sensitive data if not sanitized. Validate `networkRequests`/`consoleLogs` before use in production.
