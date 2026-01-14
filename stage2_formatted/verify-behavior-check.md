**Tags:** #automated-testing, #frontend-verification, #puppeteer, #behavior-check, #ui-testing
**Created:** 2026-01-13
**Type:** code-notes

# verify-behavior-check

## Summary

```
Automated UI behavior verification script using Puppeteer to test frontend pages (main, login, elements) for structural and functional correctness.
```

## Details

> This script uses Puppeteer to launch a browser in non-headless mode for debugging, then verifies three key frontend pages:
> 1. **Main Page**: Checks for UI elements (navigation, sidebar, content) and captures a screenshot.
> 2. **Login Page**: Validates form structure (email/password inputs, buttons) and screenshots.
> 3. **Elements Page**: Tests selectors, input fields, and generate buttons, also capturing screenshots.
> 
> The script logs console/network activity, evaluates DOM content via `page.evaluate()`, and records results via a helper class (`CheckHelper`). It relies on a `config` object for URLs, timeouts, and screenshot paths.

## Key Functions

### ``runVerifyBehaviorCheck()``

Orchestrates the entire verification workflow.

### ``CheckHelper.addResult()``

Records test outcomes (pass/fail/info) with metadata.

### ``CheckHelper.takeScreenshot()``

Captures page snapshots and returns success status.

### ``page.evaluate()``

Extracts DOM data (titles, inputs, buttons) dynamically.

## Usage

1. Install dependencies (`npm install puppeteer chalk`).
2. Configure `config.js` with frontend URLs and timeouts.
3. Run script: `node verify-behavior-check.js`.
4. Debug in non-headless mode (`headless: false`) for visual inspection.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`

## Related

- [[Frontend Configuration]]
- [[Puppeteer Test Suite]]

>[!INFO] Debugging Tip
> Ensure `config.puppeteer` includes `slowMo: 500` for deliberate delays if debugging is slow.

>[!WARNING] Resource Warning
> Non-headless mode (`headless: false`) consumes significant memory; close the browser manually after testing.
