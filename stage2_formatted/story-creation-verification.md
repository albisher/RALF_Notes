**Tags:** #automation, #web-scraping, #puppeteer, #storytelling, #ui-testing
**Created:** 2026-01-13
**Type:** code-notes

# story-creation-verification

## Summary

```
Automated UI verification for a digital storytelling workspace using Puppeteer to check layout, component visibility, and basic functionality.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local workspace application (likely a frontend running on `http://localhost:5173/workspace`), and perform automated UI checks. It captures the initial layout, verifies the presence of key UI elements (panels, cards, buttons), and tests basic story creation workflows (e.g., selecting a world and writing content). The script includes conditional logic for dynamic elements like dropdowns and text inputs, with placeholder content for testing the writing editor.
> 
> The workflow begins with launching Puppeteer in a non-headless mode with security/performance flags disabled, then sets a full-screen viewport and navigates to the workspace. After taking a screenshot, it evaluates the DOM to check visibility of predefined UI components (e.g., `.left-panel`, `.writing-editor`). For interactive elements like buttons or dropdowns, it attempts to trigger actions (e.g., clicking a world option or typing into the editor).

## Key Functions

### `storyCreationVerification`

Orchestrates the entire workflow: browser launch, navigation, UI checks, and basic functionality tests.

### `puppeteer.launch`

Configures and starts a browser instance with customizable settings.

### `page.evaluate()`

Executes JavaScript in the browser context to inspect DOM elements and their visibility.

### `page.goto()`

Navigates to the workspace URL with network idle and timeout settings.

### `page.screenshot()`

Captures the page state as an image for verification.

### `page.$() and page.$$()`

Selects and iterates over DOM elements dynamically.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node story-creation-verification.js`.
3. Ensure the workspace application is running locally on `http://localhost:5173/workspace`.
4. The script logs progress and outputs layout visibility results to the console.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[None]]

>[!INFO] Important Note
> This script assumes the workspace UI follows a predictable structure with classes like `.left-panel`, `.writing-editor`, etc. If the actual UI differs, adjust the selectors in `page.evaluate()` accordingly.

>[!WARNING] Caution
> Running Puppeteer in headless mode with `--no-sandbox` and other disabled security flags may expose the system to potential security risks. Use only in controlled environments.
