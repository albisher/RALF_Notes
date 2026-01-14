**Tags:** #automation, #web-scraping, #puppeteer, #data-validation, #game-dev, #dashboard-check
**Created:** 2026-01-13
**Type:** code-notes

# simple-data-check

## Summary

```
Automated data validation script for a game application dashboard, checking world/character counts and demo world presence via Puppeteer.
```

## Details

> This script uses Puppeteer to automate browser interactions with a local game application (likely a Voxel Engine or similar) to verify:
> 1. Dashboard content (world count, character count, element count)
> 2. Presence of demo worlds (e.g., *Cyberpunk Neo-Tokyo 2087*)
> 3. Character availability (e.g., *Cyber-Samurai Kaito*, *Mr. Ha Bee*)
> 
> The script follows a multi-step workflow:
> - Launches a headless browser with Puppeteer
> - Navigates through dashboard, worlds, and characters pages
> - Extracts and validates text content using regex and substring checks
> - Returns structured validation results via JSON

## Key Functions

### ``simpleDataCheck()``

Main async function orchestrating the entire validation workflow.

### ``puppeteer.launch()``

Configures browser launch with security-disabling flags (for testing).

### ``page.goto()``

Navigates to each page endpoint with timeout handling.

### ``page.evaluate()``

Extracts full page text content for analysis.

### `Regex patterns`

Extracts numeric values from Arabic/English text (e.g., `Total Worlds`).

## Usage

1. Install dependencies: `npm install puppeteer`
2. Run script: `node simple-data-check.js`
3. Modify `localhost:5173` to target your application URL
4. Adjust regex patterns if game displays content differently

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[Game Application Dashboard Documentation]]
- [[Puppeteer Best Practices Guide]]

>[!WARNING] Caution
> **Security Note**: Disables sandboxing (`--no-sandbox`) and web security (`--disable-web-security`) for testing only. Use in controlled environments.
> **Headless Mode**: Runs in headless mode (`headless: true`) to avoid GUI output.
