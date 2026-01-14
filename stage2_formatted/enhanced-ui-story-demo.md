**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #storytelling-platform, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-notes

# enhanced-ui-story-demo

## Summary

```
Automates UI testing for a story creation demo application, capturing screenshots and interacting with form fields to validate UI behavior.
```

## Details

> This script uses Puppeteer to automate interactions with a local web application (running on `http://localhost:5173`) for a story creation demo. It defines predefined story data (world, characters, and elements) and interacts with the UI to populate a story creation form. The script captures screenshots at key steps, logs interactions, and handles element waits and errors gracefully. The configuration includes a directory for storing screenshots (`screenshots/story-creation-demo`).
> 
> The core logic involves:
> 1. **Initialization**: Setting up a Puppeteer browser instance, ensuring the screenshots directory exists, and defining story data.
> 2. **UI Interaction Functions**: Functions like `fillFormField`, `selectDropdownOption`, and `clickButton` handle dynamic form inputs and selections.
> 3. **Step-by-Step Demonstration**: Functions like `demonstrateDashboard` and `demonstrateWorldsPage` guide the script through UI navigation and form filling, capturing screenshots at each stage.
> 4. **Error Handling**: Basic error handling for element waits and form interactions, logging failures for debugging.

## Key Functions

### ``takeScreenshot(page, name, description)``

Captures a screenshot of the current page and saves it to the `screenshots` directory.

### ``waitForElement(page, selector, timeout)``

Waits for an element to be present on the page with a specified timeout.

### ``fillFormField(page, selector, value, description)``

Fills a form field with a given value and logs the action.

### ``selectDropdownOption(page, selector, value, description)``

Selects an option from a dropdown menu.

### ``clickButton(page, selector, description)``

Clicks a button on the page.

### ``demonstrateDashboard(page)``

Navigates to the dashboard, logs dashboard elements, and captures an initial screenshot.

### ``demonstrateWorldsPage(page)``

Navigates to the worlds page, locates and clicks the "Add World" button, and captures the dialog screenshot.

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node enhanced-ui-story-demo.js`.
3. Ensure the web application is running locally at `http://localhost:5173`.
4. The script will automatically:
   - Create a `screenshots/story-creation-demo` directory.
   - Navigate through the UI, fill the story creation form with predefined data.
   - Capture screenshots at each step.
   - Log interactions and errors.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[none]]

>[!INFO] Important Note
> This script assumes the UI elements (e.g., buttons, inputs) have either `data-testid` attributes or text content matching the expected keywords ("Add World," "Create World," etc.). If the selectors are dynamic or change frequently, the script may fail to locate elements.


>[!WARNING] Caution
> The script uses `page.waitForTimeout` for delays, which can be unreliable for dynamic page loads. Consider replacing these with more robust waits (e.g., `page.waitForSelector`) if the application relies on asynchronous loading. Also, ensure the `BASE_URL` and form selectors match the actual application UI.
