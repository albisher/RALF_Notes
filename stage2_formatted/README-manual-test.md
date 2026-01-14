**Tags:** #manual-test, #ui-testing, #world-creation, #automated-script, #space-simulation
**Created:** 2026-01-13
**Type:** documentation

# README-manual-test

## Summary

```
Manual UI test guide for creating a complete Space Peral world via browser-based automation.
```

## Details

> This document provides step-by-step instructions for executing a JavaScript-based manual UI test script to generate a fully functional Space Peral world, including robots, flora, fauna, buildings, and a narrative. The process leverages the application’s UI interface and backend APIs to automate asset creation, ensuring consistency across the simulation environment. The script is designed to be executed in a browser console, requiring the application to be fully operational and Docker containers running.

## Key Functions

### `manual-ui-test.js`

Executes automated UI actions to create world elements (robots, plants, animals, buildings, and a story).

### `Space Peral World Creation Script`

Orchestrates the generation of all assets using hash-based identifiers.

### `Story Writing Module`

Populates the narrative with predefined lore about the landing event.

## Usage

1. Navigate to `http://localhost:5173` in a modern browser.
2. Open DevTools (`F12` or `Right-click > Inspect`).
3. Paste the contents of `manual-ui-test.js` into the **Console** tab.
4. Execute the script and monitor progress in the console.
5. Verify results by checking the workspace and story output.

## Dependencies

> `browser-devtools (Chrome/Firefox)`
> `Node.js runtime (for script execution)`
> `Space Peral backend API`
> `Docker containers (for backend services).`

## Related

- [[Space Peral Documentation]]
- [[Backend API Reference]]
- [[Docker Setup Guide]]

>[!INFO] Important Note
> The script relies on **text-based selectors**—ensure UI elements match the expected labels (e.g., "dashboard," "workspace"). Language mode (Arabic/English) may affect selectors.
>

>[!WARNING] Caution
> If the backend API fails, assets may not persist. Check the **Network tab** for errors and ensure the backend is running (`http://localhost:5173/api`). Delays are included to handle API responses.
