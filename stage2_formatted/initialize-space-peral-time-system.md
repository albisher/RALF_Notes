**Tags:** #automation, #web-scraping, #puppeteer, #time-system, #api-integration
**Created:** 2026-01-13
**Type:** code-notes

# initialize-space-peral-time-system

## Summary

```
Automates browser initialization and API-based setup of a custom time system for a virtual world named "Space Peral."
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a workspace, and interact with a web application to configure a custom time system for the "Space Peral" world. It dynamically selects the world, retrieves its ID, and initializes a time system with a 30-hour day cycle and custom time periods. The script also handles creation of the world if it does not exist and tests time advancement via API calls.

## Key Functions

### `initializeSpacePeralTimeSystem`

Orchestrates the entire process of launching a browser, navigating to the workspace, selecting the "Space Peral" world, and initializing the time system via API.

### ``page.evaluate` for world API calls`

Executes JavaScript in the browser context to interact with backend APIs (e.g., fetching/create worlds and time systems).

### `Time system configuration`

Defines a custom time structure (e.g., 30-hour days, 10 months/year) and time periods (Dawn, Morning, etc.) for the "Space Peral" world.

## Usage

1. Install Puppeteer (`npm install puppeteer`).
2. Ensure the local web app is running on `http://localhost:5173/workspace`.
3. Store an `auth_token` in `localStorage` for API authentication.
4. Run the script to initialize the "Space Peral" world and its time system.

## Dependencies

> `puppeteer`
> `fetch (built-in browser API)`
> `localStorage (browser API)`
> ``mdi-weather-*` icons (likely a frontend icon library).`

## Related

- [[Space Peral API Documentation]]
- [[Puppeteer Browser Automation Guide]]

>[!INFO] Important Note
> The script assumes the backend API endpoints (`/api/worlds`, `/api/worlds/{id}/time-system`, etc.) are accessible and properly configured. If the world does not exist, it creates it dynamically.

>[!WARNING] Caution
> Running Puppeteer in non-headless mode (`--no-sandbox`) may expose security risks if not used in a controlled environment. Ensure proper sandboxing is handled elsewhere.
