**Tags:** #UI-Testing, #Puppeteer, #Frontend-Validation, #CSS-Padding-Check
**Created:** 2026-01-13
**Type:** code-notes

# quick-padding-check

## Summary

```
Automated UI validation script to verify and log padding properties of a `<main>` element in a dashboard.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local dashboard (`localhost:8443/dashboard`), and inspect the `<main>` element’s computed padding values (top, left, right, bottom). It checks for CSS classes (`p-6`, `main-content-padding`) and compares padding against expected non-zero values. After validation, it saves a full-page screenshot for record-keeping. The script handles errors gracefully and ensures the browser is closed in a `finally` block.

## Key Functions

### ``quickPaddingCheck()``

Orchestrates the entire test workflow (browser launch, navigation, inspection, and cleanup).

### ``puppeteer.launch()``

Configures a non-headless browser with security/performance flags.

### ``page.evaluate()``

Extracts computed styles and class checks from the `<main>` element.

### ``page.screenshot()``

Captures a full-page screenshot for debugging.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node quick-padding-check.js`.
3. Ensure the dashboard is accessible at `https://localhost:8443/dashboard` before execution.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[UI-Validation-Guide]]
- [[Puppeteer-Test-Cases]]

>[!INFO] Important Note
> The script assumes the `<main>` element exists and is the target for padding checks. If the element is dynamically loaded, adjust `waitForTimeout` or use `page.waitForSelector('main')` before evaluation.

>[!WARNING] Caution
> Avoid running this in production without proper sandboxing (e.g., `--disable-dev-shm-usage` may cause issues on some systems). Test in a controlled environment first.
