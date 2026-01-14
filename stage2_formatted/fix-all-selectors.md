**Tags:** #CSS-selector-fix, #Web-scraping, #JavaScript, #DOM-manipulation, #Playwright
**Created:** 2026-01-13
**Type:** code-notes

# fix-all-selectors

## Summary

```
Automates conversion of `:has-text` selectors to Playwright’s `evaluateHandle` for dynamic element matching.
```

## Details

> This script reads a JavaScript file containing `:has-text` selectors (e.g., `element:has-text("text")`), rewrites them into `page.evaluateHandle` calls that dynamically query elements by text content. It handles both single and multiple `:has-text` selectors by:
> 1. Parsing the original selector pattern (e.g., `const x = await page.$('div:has-text("foo")')`).
> 2. Replacing it with a `page.evaluateHandle` block that:
>    - Extracts the selector (e.g., `'div'`) and cleaned text (e.g., `"foo"`).
>    - Uses `document.querySelectorAll` to fetch matching elements.
>    - Filters elements by `textContent.includes()`.
> 3. Compares modified content with the original; if changed, writes the updated file.

## Key Functions

### ``fixSelectors(filePath)``

Core function that processes a file, applies fixes, and logs results.

### `Input`

File path with `:has-text` selectors.

### `Output`

Updated file (if changes detected) or `false` on failure.

### ``fixScript()``

Entry point that targets a predefined script (`scripts/create-space-peral-world.js`).

## Usage

1. Call `fixSelectors(path)` with a file path containing `:has-text` selectors.
2. Example: `fixSelectors('scripts/my-script.js')`.
3. For auto-fix: Uncomment/modify `scriptToFix` and run the script.

## Dependencies

> ``fs``
> ``page` (Playwright’s Puppeteer/Chromium API)`
> ``regex` (built-in).`

## Related

- [[Playwright documentation on `evaluateHandle`]]
- [[CSS `:has-text` selector limitations]]

>[!INFO] Dynamic Matching Limitation
> `:has-text` is not natively supported in Playwright; this script emulates it via `evaluateHandle`. For complex cases, consider using `page.locator()` with `textContains()` instead.


>[!WARNING] Text Matching Sensitivity
> `textContent.includes()` is case-sensitive and partial. For exact matches, use `textContent === cleanText` (requires escaping special regex chars).
