**Tags:** #Puppeteer, #JavaScript, #Automation, #WebTesting, #TimeoutFix
**Created:** 2026-01-13
**Type:** code-notes

# fix-puppeteer-timeout

## Summary

```
Automates replacement of `page.waitForTimeout` with `setTimeout` in Puppeteer scripts to enforce proper timeouts.
```

## Details

> This script reads Puppeteer scripts, detects instances of `await page.waitForTimeout(duration)`, and replaces them with a `setTimeout`-based promise. It ensures backward compatibility while enforcing explicit timeouts. The tool checks two predefined scripts for modifications and logs results.

## Key Functions

### `fixWaitForTimeout(filePath)`

Reads a file, replaces `waitForTimeout` with `setTimeout`, and writes changes if modifications occur.

### `scriptsToFix`

Array of script paths to process for fixes.

## Usage

1. Run the script directly in a Node.js environment.
2. It processes two hardcoded scripts (`create-space-peral-world.js`, `initialize-space-peral-time-system.js`).
3. Outputs success/error logs and counts fixed files.

## Dependencies

> ``fs``
> ``path` (Node.js built-ins)`

## Related

- [[Puppeteer Best Practices]]
- [[Node]]

>[!INFO] Important Note
> This script only modifies files if `waitForTimeout` appears as `await page.waitForTimeout(duration)`. Non-async contexts (e.g., `page.waitForTimeout()` without `await`) are unaffected.

>[!WARNING] Caution
> Manual review is recommended for files modified by this script, as replacements are literal and may alter intended logic.
