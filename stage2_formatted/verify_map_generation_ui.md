**Tags:** #automated-testing, #puppeteer, #ui-testing, #map-generation, #world-creation, #javascript, #web-scraping
**Created:** 2026-01-13
**Type:** test-reference

# verify_map_generation_ui

## Summary

```
Automated UI verification script for map generation in a game or application, testing world creation and map generation workflows via Puppeteer.
```

## Details

> This script uses Puppeteer to automate interactions with a web application (running on `localhost:5174`) for verifying map generation functionality. It creates test worlds with customizable data (name, description, and type) and captures screenshots to validate UI behavior. The workflow includes:
> 1. **World Creation**: Fills a modal form with provided `worldData` (name, description, type) and submits it.
> 2. **Map Generation Testing**: Navigates to a generate tab, selects the created world, and verifies map generation UI elements.
> 3. **Screenshots**: Captures UI states at critical steps (e.g., form submission, modal closing) for debugging/validation.
> 
> The script handles dynamic elements (e.g., selects, modals) via JavaScript evaluation and waits for elements to appear/become interactive.

## Key Functions

### ``takeScreenshot(page, name)``

Saves a full-page screenshot to `screenshots/map-generation-verification` with a timestamped filename.

### ``waitForElement(page, selector, timeout)``

Polls for an element to appear within a timeout, returning `true` if found.

### ``createWorld(page, worldData)``

- Clicks the "Create World" button, fills a modal with `worldData`, and submits it.

### ``testMapGeneration(page, worldName, hashInput)``

- Navigates to the generate tab, selects the world via JavaScript, and captures screenshots.

### `Note`

`hashInput` is unused in the snippet but appears in the function signature.

## Usage

1. **Setup**:
   - Install dependencies: `npm install puppeteer`.
   - Ensure the target app runs on `http://localhost:5174` (adjust `BASE_URL` if needed).
   - Create a `screenshots/map-generation-verification` directory (script auto-creates it).

2. **Run**:
   ```javascript
   const puppeteer = require('puppeteer');
   const script = require('./verify_map_generation_ui');

   async function runTest() {
       const browser = await puppeteer.launch();
       const page = await browser.newPage();
       await page.goto('http://localhost:5174');

       // Example world data
       const worldData = { name: "TestWorld", description: "A test world", world_type: "random" };
       await script.createWorld(page, worldData);
       await script.testMapGeneration(page, worldData.name);
       await browser.close();
   }
   runTest();
   ```

## Dependencies

> ``puppeteer``
> ``path``
> ``fs` (Node.js built-ins)`
> ``node:console` (for logging).`

## Related

- [[Application UI Documentation]]
- [[Puppeteer Test Framework Guide]]
- [[Map Generation Algorithm Specifications]]

>[!INFO] Dynamic Selector Handling
> The script uses JavaScript evaluation (`page.evaluateHandle`) to locate and interact with dropdowns (`select` elements) dynamically, which may fail if the UI structure changes. Prefer stable selectors (e.g., `class` or `id`) for robustness.


>[!WARNING] Timeout Risks
> Explicit delays (`setTimeout`) are used to handle UI lag, but aggressive delays may cause flaky tests. Adjust timeouts based on app performance (e.g., reduce `5000ms` for fast apps).
