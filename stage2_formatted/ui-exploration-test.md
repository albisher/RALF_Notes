**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-exploration, #frontend-analysis
**Created:** 2026-01-13
**Type:** code-notes

# ui-exploration-test

## Summary

```
Automated UI exploration script using Puppeteer to analyze and log character creation elements in a web application.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local web application (running on `localhost:5173`), and systematically inspect UI elements. It captures screenshots, extracts page metadata (e.g., title), and evaluates elements like links, buttons, inputs, and textareas. The script filters and logs elements related to character creation, create/generate actions, and form inputs, providing structured output for further analysis.
> 
> The script dynamically creates a timestamped directory for screenshots and logs UI findings to the console. It includes error handling for missing directories and ensures elements are only logged if they are visually present (`visible` check).

## Key Functions

### `exploreUI`

Orchestrates the entire UI exploration workflow, including browser launch, navigation, screenshot capture, and element analysis.

### ``page.goto()``

Navigates to the target URL with configurable wait and timeout settings.

### ``page.evaluate()``

Executes JavaScript in the context of the page to extract dynamic UI elements (links, buttons, inputs, textareas).

### ``page.screenshot()``

Captures a full-page screenshot with timestamped naming.

### `Element filtering logic`

Filters elements based on keywords like "character," "create," or "generate" for targeted analysis.

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node ui-exploration-test`.
3. Configure `puppeteer.launch()` options (e.g., headless mode) as needed.
4. Modify the target URL (`http://localhost:5173`) to match the application being tested.

## Dependencies

> `puppeteer`
> `path`
> `fs`

## Related

- [[Character Creation UI Analysis Report]]
- [[Puppeteer Documentation]]

>[!INFO] Important Note
> The script logs all found UI elements, including those not directly related to character creation, for completeness. To refine results, adjust the filtering logic in `characterElements` or `createElements` filters.

>[!WARNING] Caution
> Running in non-headless mode (`headless: false`) may cause browser extensions or other processes to interfere. Use `--disable-gpu` and other flags to mitigate GPU-related issues in production environments.
