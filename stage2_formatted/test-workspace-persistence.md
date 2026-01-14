**Tags:** #puppeteer, #web-testing, #workspace-persistence, #automated-testing, #frontend-validation
**Created:** 2026-01-13
**Type:** code-test

# test-workspace-persistence

## Summary

```
Tests if a workspace application retains state after page refresh using Puppeteer.
```

## Details

> This script automates testing for workspace persistence by verifying if UI elements (world selector, time period dropdown, and writing content) retain functionality and state after a page refresh. It launches a headless browser, navigates to a workspace page, performs initial checks, interacts with UI components (e.g., selecting a world, choosing a time period, typing into a textarea), and then refreshes the page to confirm persistence of the selected state. Screenshots are captured at key stages for visual validation.

## Key Functions

### `testWorkspacePersistence`

Orchestrates the entire persistence test workflow, including browser launch, UI interactions, and refresh validation.

### `puppeteer.launch`

Configures and starts a headless Chrome browser with security and performance optimizations.

### `page.goto`

Navigates to the workspace URL with timeout and DOM content loading checks.

### `page.evaluate`

Extracts dynamic content (e.g., body text) for validation checks.

### `page.select`

Manages dropdown selections (e.g., world or time period).

### `page.type`

Simulates typing in a textarea for content persistence testing.

### `page.reload`

Simulates a page refresh to test state retention.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-workspace-persistence.js`.
3. Ensure the target workspace is accessible at `http://localhost:5173/workspace`.
4. Verify screenshots are saved in `checks/screenshots/` for debugging.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Test-Workspace-UI-Elements]]
- [[Puppeteer-Configuration-Guide]]

>[!INFO] Important Note
> The script assumes the workspace UI has a `<select>` element for world selection, a `<button>` for time period selection, and a `<textarea>` for writing content. Adjust selectors if the target application differs.

>[!WARNING] Caution
> Running in headless mode with `--disable-web-security` may expose the browser to security risks. Use only in controlled environments for testing.
