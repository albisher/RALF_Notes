**Tags:** #automation, #web-scraping, #puppeteer, #story-writing, #web-interaction
**Created:** 2026-01-13
**Type:** code-notes

# space-peral-session-5-story

## Summary

```
Automates the process of navigating a web application, writing a predefined story, and saving it as an asset using Puppeteer.
```

## Details

> This script uses Puppeteer to automate interactions with a web application (likely a space-themed or simulation platform) to:
> 1. Launch a browser, load the application, and take screenshots at each step.
> 2. Navigate to a workspace and write a structured story about a fictional scenario involving robotic exploration of a planet (Space Peral).
> 3. Save the story by clicking a "Save" button (or a translatable "Save" button in another language).
> 4. Capture screenshots of the story writing and saving process.
> 
> The script dynamically searches for UI elements (like textareas and buttons) to interact with, ensuring adaptability to minor UI changes. It includes error handling for missing elements and logs progress via console.

## Key Functions

### `createSpacePeralStory`

Orchestrates the full workflow of loading, writing, and saving a story.

### `takeScreenshot`

Captures a screenshot of the current page with a timestamped filename.

### `createScreenshotsDirectory`

Ensures the `screenshots` directory exists before saving images.

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node space-peral-session-5-story`.
3. Ensure the web app is running locally at `http://localhost:5173` for the script to interact with.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Space Peral Web App Documentation]]
- [[Puppeteer Automation Guide]]

>[!INFO] Important Note
> The script assumes the web app has a `<textarea>` element for story writing and a button with "Save" or "حفظ" text. If the UI changes, the script may fail. Consider adding more robust selectors (e.g., `id`, `class`) for dynamic elements.


>[!WARNING] Caution
> Running Puppeteer in headless mode (`--headless: false`) may expose the browser to potential security risks. Use `--no-sandbox` and `--disable-setuid-sandbox` only in trusted environments. Always validate the target URL and UI structure before execution.
