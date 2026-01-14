**Tags:** #automation, #web-scraping, #puppeteer, #robotics, #ui-testing, #seed-based-generation, #visual-logging
**Created:** 2026-01-13
**Type:** code-notes

# space-peral-session-2-robots

## Summary

```
Automates creation of X-Series robots via UI interaction using Puppeteer for browser automation.
```

## Details

> This script automates the creation of 11 X-Series robots (e.g., drones, orchestrators) in a web application by:
> 1. Launching a browser, navigating to the workspace, and capturing screenshots at each step.
> 2. Iterating through predefined robot configurations (name, role, seed) to:
>    - Locate and click the "Create" button.
>    - Select "character" type and "hash-based" generation mode.
>    - Input a seed value for each robot.
>    - Generate and confirm creation via UI interactions.
> 3. Includes error handling, screenshot logging, and cleanup of browser resources.

## Key Functions

### `createXSeriesRobots`

Orchestrates the full automation workflow.

### `takeScreenshot`

Captures page snapshots with timestamps for debugging/validation.

### `robot creation loop`

Dynamically handles each robot’s UI interaction sequence.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run script (`node space-peral-session-2-robots.js`).
3. Ensure the target web app (running on `http://localhost:5173`) is accessible.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Space Peral UI Architecture]]
- [[Robotics Workflow Design]]

>[!INFO] Important Note
> The script assumes the UI elements (e.g., buttons, selects) match the expected selectors. Adjust selectors if the target app’s UI changes.

>[!WARNING] Caution
> Headless mode is disabled (`--no-sandbox` is used for security). Avoid running in production without proper sandboxing.
