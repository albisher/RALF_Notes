**Tags:** #automation, #web-scraping, #puppeteer, #testing, #interactive-ui, #api-interaction
**Created:** 2026-01-13
**Type:** code-notes

# final-working-demo

## Summary

```
Automated UI testing and demo workflow for a web application using Puppeteer to interact with a dashboard and workspace.
```

## Details

> This script automates interactions with a web application (likely a game or simulation platform) by:
> 1. Launching a headless browser with Puppeteer to simulate user actions.
> 2. Capturing console logs, network requests (API calls), and responses for debugging.
> 3. Taking screenshots at key steps to document the workflow.
> 4. Navigating through the UI to create a world, fill metadata, and verify creation.
> 5. Interacting with a workspace textarea to input story content.
> 
> The workflow follows a structured sequence: dashboard navigation, world creation, verification, workspace access, and content input.

## Key Functions

### `finalWorkingDemo`

Orchestrates the entire automated demo workflow.

### `takeScreenshot`

Captures a screenshot at specified steps with timestamped filenames.

### `page.on('console')`

Logs browser console messages for debugging.

### `page.on('request')/**page.on('response')`

Monitors and logs API interactions.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run the script (`node final-working-demo.js`).
3. Ensure the target application (`http://localhost:5173`) is running.
4. Modify selectors (e.g., `data-testid`) if the UI structure changes.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> This script assumes the target application uses `data-testid` attributes for form inputs (e.g., `world-name-input`). If selectors fail, adjust the XPath queries or debug with browser dev tools.

>[!WARNING] Caution
> Running Puppeteer in headless mode with `--disable-web-security` may expose the browser to security risks. Use cautiously in production environments. Always validate API endpoints and network requests in a controlled environment.
