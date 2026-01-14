**Tags:** #debugging, #ui-testing, #puppeteer, #automation, #frontend-testing
**Created:** 2026-01-13
**Type:** code-notes

# debug-ui-check

## Summary

```
Automated UI debugging script using Puppeteer to inspect and validate frontend interactions.
```

## Details

> This script uses Puppeteer to launch a browser in non-headless mode for interactive debugging. It logs console/network activity, captures screenshots, and evaluates DOM elements across multiple UI states (login, post-login). The script dynamically identifies form fields, buttons, and page components to verify UI structure and functionality.

## Key Functions

### `runDebugUICheck`

Orchestrates the full debugging workflow (login → elements page).

### `CheckHelper.takeScreenshot`

Captures page snapshots with relative paths.

### `page.evaluate()`

Executes JavaScript in the browser context to inspect DOM structure.

### `page.goto()`

Navigates to configured frontend URLs with timeout handling.

## Usage

1. Install dependencies (`npm install puppeteer chalk`).
2. Configure `./config` with frontend URLs and Puppeteer options.
3. Run script (`node debug-ui-check.js`).
4. Use `console.log` outputs and screenshots for debugging insights.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local ./config)`
> `utils/check-helper`

## Related

- [[Debug UI Check Config]]
- [[Puppeteer Test Reference]]

>[!INFO] Important Note
> The script intentionally runs in `headless: false` for visual debugging. Ensure the frontend is accessible at `config.urls.frontend`.

>[!WARNING] Caution
> Avoid hardcoding credentials in the script. The placeholder values (`user@spacepearl.com`, `password123`) are illustrative; replace with actual test data. Network delays may occur during page navigation.
