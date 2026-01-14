**Tags:** #automation, #web-testing, #puppeteer, #dark-mode, #visual-testing
**Created:** 2026-01-13
**Type:** code-test

# dark-mode-visual-test

## Summary

```
Automated dark mode visual testing script using Puppeteer to verify theme toggling functionality.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a Vue.js application running locally, and test dark mode functionality. It logs the initial state, toggles the theme, verifies changes, and captures screenshots of each state. The test checks if the dark mode toggle correctly switches between light/dark themes, validates visual consistency across elements, and ensures the toggle cycles back to the original state.

## Key Functions

### `testDarkModeVisual`

Orchestrates the entire testing workflow, including browser launch, navigation, theme toggling, and screenshot capture.

### `page.goto()`

Navigates to the application URL with network idle wait.

### `page.waitForSelector()`

Waits for Vue app root element (`#app`) to load.

### `page.evaluate()`

Executes JavaScript in the context of the page to check theme/class states and background colors.

### `page.screenshot()`

Captures full-page screenshots at each state (initial, toggled, final).

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node dark-mode-visual-test.js`.
3. Ensure the target application (Vue.js) is running locally at `https://localhost:8443`.
4. The script will:
   - Log progress and errors.
   - Save screenshots to `screenshots/` folder.
   - Output console logs for verification.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Visual Regression Testing Guide]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script assumes the target app uses Vue.js with a class `dark` for dark mode and `.v-navigation-drawer`/`.v-main` for visual checks. Adjust selectors if the app uses different class names.

>[!WARNING] Caution
> Running in headless mode (`--headless: false`) may cause UI inconsistencies if the app relies on browser-specific features. Test in a controlled environment.
