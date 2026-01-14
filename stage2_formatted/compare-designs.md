**Tags:** #visual-design, #comparison-tool, #puppeteer, #vuejs, #html-css, #automated-testing
**Created:** 2026-01-13
**Type:** code-notes

# compare-designs

## Summary

```
Automates visual design comparison between a static HTML sample and a running Vue.js web application.
```

## Details

> This script uses Puppeteer to capture screenshots of both a predefined HTML template and a live Vue.js application across multiple pages. It generates a structured comparison report highlighting key visual elements like color schemes, layout, typography, and interactive components. The workflow involves launching a browser, taking screenshots of the HTML sample and each page of the webapp, then generating a markdown report with visual comparison guidelines.

## Key Functions

### `compareDesigns()`

Orchestrates the entire comparison workflow, including browser launch, screenshot capture, and report generation.

### `puppeteer.launch()`

Initializes a headless browser with custom viewport settings.

### `page.goto()`

Navigates to HTML/URL endpoints for screenshot capture.

### `page.screenshot()`

Captures full-page screenshots at specified paths.

### `fs.writeFileSync()`

Writes the generated comparison report to a markdown file.

## Usage

1. Save the script as `compare-designs.js`.
2. Ensure:
   - `sample01.html` exists in the `./preparation` folder.
   - The Vue.js app runs on `http://localhost:5173`.
3. Execute via Node.js: `node compare-designs.js`.
4. Review the generated `comparison-report.md` and screenshots in the root folder.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Visual Design Guidelines]]
- [[Vue]]

>[!INFO] Important Note
> The script assumes the Vue app is fully loaded before taking screenshots. Use `waitForTimeout()` to account for dynamic content (e.g., 2000ms for HTML, 3000ms for Vue).

>[!WARNING] Caution
> Avoid running this in production. Puppeteer in headless mode (`headless: false`) may expose browser internals. Use `headless: true` for CI/CD environments.
