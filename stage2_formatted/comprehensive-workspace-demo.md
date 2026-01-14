**Tags:** #automation, #web-scraping, #puppeteer, #browser-automation, #workspace-demo, #interactive-ui-testing
**Created:** 2026-01-13
**Type:** code-notes

# comprehensive-workspace-demo

## Summary

```
Automates interaction with a fictional "ملاحم (Malahim)" writing workspace application using Puppeteer to simulate user actions, configure context, and capture screenshots.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local web application (`http://localhost:5173`), and automate interactions with its Writer Workspace. It handles navigation, context setup (world, time, location), and character asset creation while logging progress and capturing screenshots at each step. The demo includes error handling for missing UI elements and fallback navigation paths.
> 
> The workflow follows sequential steps:
> 1. **Loads the application** and takes a screenshot.
> 2. **Navigates to the Writer Workspace** (either via link or direct URL).
> 3. **Sets up the World Context** by selecting a world from a dropdown.
> 4. **Configures the Time Period** (e.g., "Future").
> 5. **Sets the Location** (e.g., "Neo-Tokyo, Sector 7").
> 6. **Creates a Character Asset** by clicking a "+" button, filling in details, and capturing the dialog screenshot.

## Key Functions

### `comprehensiveWorkspaceDemo`

Orchestrates the full automation workflow.

### `takeScreenshot`

Captures a full-page screenshot with timestamped filename.

### `worldSelectors`

Handles world selection logic (if dropdown exists).

### `timeSelectors`

Manages time period configuration.

### `locationInputs`

Fills location fields dynamically.

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node comprehensive-workspace-demo.js`.
3. Ensure the app (`http://localhost:5173`) is running before execution.
4. Customize selectors (e.g., `a[href="/workspace"]`) if the UI structure changes.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-automation-guide]]
- [[web-app-interaction-patterns]]

>[!INFO] Important Note
> The script assumes the UI selectors (`a[href="/workspace"]`, `input[placeholder*="location"]`) match the target application. Adjust selectors if the app’s HTML structure differs.

>[!WARNING] Caution
> Disabling security flags (`--disable-web-security`) may expose the browser to security risks. Use only in controlled environments for testing.
