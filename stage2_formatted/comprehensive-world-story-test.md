**Tags:** #automated-testing, #web-scraping, #puppeteer, #sci-fi-world-builder, #interdimensional-testing
**Created:** 2026-01-13
**Type:** code-test

# comprehensive-world-story-test

## Summary

```
Automated Puppeteer test suite for creating and verifying a sci-fi world with assets in a web application.
```

## Details

> This script uses Puppeteer to automate interactions with a web application (running on `localhost:5173`) for testing a comprehensive sci-fi world creation workflow. It configures a test world (`Nexus Prime - The Cosmic Convergence`) and predefined assets (buildings, characters, plants, and animals) with detailed descriptions. The test handles login, navigation, form submissions, and screenshots at each step to document interactions. It employs robust error handling for element existence and waits for navigation completion.
> 
> The code organizes test data into structured objects (`testWorld`, `testAssets`) and systematically navigates through UI elements using selectors with fallback options. It captures screenshots at critical stages to verify UI behavior and logs progress via console output.

## Key Functions

### `takeScreenshot(page, name)`

Captures full-page screenshots with timestamps for debugging.

### `waitForElement(page, selector, timeout)`

Safely waits for DOM elements to appear with timeout handling.

### `login(page)`

Authenticates via email/password and verifies login state.

### `createWorld(page)`

Creates a new world with predefined metadata (name, description, genre, theme).

### `addAssets(page)`

Iterates through predefined assets, adding each to the world’s elements collection.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Update `BASE_URL` to match your application’s host.
3. Run the script (`node comprehensive-world-story-test.js`).
4. Verify screenshots in `screenshots/comprehensive-world-story/` and logs in `reports/`.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Test World Creation UI Design]]
- [[Puppeteer Best Practices Guide]]

>[!INFO] Important Note
> The script uses hardcoded credentials (`test@example.com`, `testpassword123`) for login. In production, replace these with environment variables or a secure credential manager.

>[!WARNING] Caution
> The `waitForTimeout` calls are simplistic and may not account for dynamic UI delays. For reliability, replace with `page.waitForFunction()` or `page.waitForSelector()` with explicit conditions.
