**Tags:** #automated-testing, #web-development, #puppeteer, #tailwind-css, #debugging
**Created:** 2026-01-13
**Type:** code-test

# tailwind-debug-test

## Summary

```
Automated Tailwind CSS debugging tool using Puppeteer to inspect and validate Tailwind utility classes.
```

## Details

> This script uses Puppeteer to launch a browser, log in to a local application (running on `localhost:8443`), and perform Tailwind CSS debugging. It evaluates the page to detect:
> - Loaded stylesheets (including cross-origin)
> - `<style>` tags containing Tailwind directives (e.g., `@tailwind`)
> - `<link>` tags referencing Tailwind CSS files
> - Tailwind utility classes (e.g., `.p-6`) in stylesheets
> - Computed styles of a dynamically injected `<div>` with `class="p-6"` to verify proper rendering
> - Overriding CSS rules affecting Tailwind classes on the `<main>` element.
> 
> The script logs detailed debug information, including detected stylesheets, style tags, link tags, and computed styles for validation.

## Key Functions

### ``runTest()``

Orchestrates browser launch, navigation, login, and Tailwind CSS inspection via `page.evaluate()`.

### ``page.evaluate()` callback`

Extracts and validates Tailwind-related elements (stylesheets, style tags, link tags, utility classes, and computed styles).

### `Dynamic test element`

Injects a `<div>` with `class="p-6"` to measure padding via `getComputedStyle()`.

### ``overrideRules` detection`

Checks for conflicting CSS rules overriding Tailwind classes on `<main>`.

## Usage

1. Install dependencies (`npm install puppeteer`).
2. Run the script (`node tailwind-debug-test.js`).
3. Ensure the target application (e.g., a Next.js/React app) is running locally on `localhost:8443` with credentials `test/testpass`.
4. Observe debug logs for Tailwind CSS validation results.

## Dependencies

> `puppeteer`
> `Google Chrome (hardcoded path `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`).`

## Related

- [[Next]]
- [[Puppeteer Eval Best Practices]]

>[!INFO] Important Note
> The script hardcodes Chrome’s executable path (`/Applications/Google Chrome.app`). For cross-platform compatibility, dynamically resolve Chrome’s binary path (e.g., using `child_process` or `which`).

>[!WARNING] Caution
> Avoid running this in production. It logs sensitive debug data (e.g., stylesheet paths) to the console. Use environment variables for credentials (`testCredentials`) and sanitize logs in production.
