**Tags:** #automation, #web-scraping, #puppeteer, #ui-testing, #workspace-demo
**Created:** 2026-01-13
**Type:** code-notes

# robust-workspace-demo

## Summary

```
Automated Puppeteer demo for testing and validating a writing workspace application (e.g., "ملاحم").
```

## Details

> This script uses Puppeteer to automate interactions with a local web application (likely a writing workspace) hosted on `http://localhost:5173`. It follows a structured demo workflow:
> 1. **Headless Browser Launch**: Starts a headless Chrome instance with strict security and performance settings.
> 2. **Navigation & Screenshots**: Loads the app, navigates to the workspace, and captures screenshots at key steps.
> 3. **Dynamic Checks**: Validates the presence of UI components (panels, cards, inputs) via `page.evaluate()`.
> 4. **Contextual Setup**: Interacts with dropdowns (world selection, time period, location) to configure the workspace environment.
> 
> The demo includes error handling for Puppeteer/Page events and logs progress via `console.log`.

## Key Functions

### `robustWorkspaceDemo`

Orchestrates the full demo workflow.

### `takeScreenshot`

Captures full-page screenshots with timestamps and error handling.

### `page.on('error')/**page.on('console')`

Monitors and logs Puppeteer/Puppeteer errors.

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node robust-workspace-demo.js`.
3. Ensure the target app (`http://localhost:5173`) is running.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the target app uses class names like `.left-panel`, `.writing-card`, etc. Adjust selectors if the UI structure differs.

>[!WARNING] Caution
> Headless mode with `--disable-web-security` may expose the browser to security risks. Use cautiously in production environments.
