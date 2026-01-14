**Tags:** #automated-testing, #puppeteer, #web-automation, #story-verification, #frontend-validation
**Created:** 2026-01-13
**Type:** code-test

# simple-story-verification

## Summary

```
Automates verification of a story creation workspace UI and functionality using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a browser, interact with a local web application (running on `http://localhost:5173/workspace`), and validate the presence of key layout elements, writing functionality, and interactive buttons. It captures screenshots at multiple stages (empty workspace, post-input, and final state) and logs results for debugging. The verification includes checking for:
> - Panel visibility (left, center, right)
> - Text editor presence
> - Button accessibility (Save Story, Create Story Asset)
> - Manual typing and button-click interactions.

## Key Functions

### `simpleStoryVerification()`

Orchestrates the entire verification workflow, including browser launch, UI checks, interactions, and cleanup.

### `layoutCheck`

Evaluates DOM elements for basic layout validation via `page.evaluate()`.

### `Writing functionality test`

Types predefined content into a textarea and captures the state.

### `Button interaction tests`

Clicks "Save Story" and "Create Story Asset" buttons with delays.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node simple-story-verification.js`.
3. Ensure the target workspace (e.g., a Next.js app) is running locally on `http://localhost:5173/workspace`.
4. Verify screenshots are saved in `./screenshots/` for debugging.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Next]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> The script logs detailed console output for each step, including success/failure of UI elements and interactions. Screenshots are saved to `./screenshots/` with timestamps for auditing.

>[!WARNING] Caution
> Avoid running this in production without proper sandboxing (e.g., `--disable-setuid-sandbox` may not be secure for all environments). The script assumes the target app is accessible on `localhost:5173`.
