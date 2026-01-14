**Tags:** #UI-Testing, #Automation, #Space-Simulation, #World-Builder, #Robotics
**Created:** 2026-01-13
**Type:** code-notes

# manual-ui-test

## Summary

```
Manual UI test script for creating a sci-fi world with robotic elements in a browser-based space simulation environment.
```

## Details

> This script automates the creation of a customizable "Space Peral" world in a web-based application, including world properties, robotic inhabitants, ecosystems, and narrative elements. It uses browser console automation to interact with UI elements like buttons, inputs, and textareas, with delays to account for asynchronous rendering. The script handles multilingual UI elements (English and Arabic) and relies on placeholder-based selectors for dynamic UI components.

## Key Functions

### `waitForElement`

Asynchronously waits for an element to appear within a timeout period.

### `findButtonByText`

Locates a button by checking its text content (supports partial matches).

### `findInputByPlaceholder`

Finds an input field by its placeholder text.

### `findTextareaByPlaceholder`

Finds a textarea by its placeholder text.

### `createSpacePeralWorld`

Orchestrates the full workflow of creating a world, robots, plants, buildings, and narrative content.

### `createXSeriesRobots`

Creates a predefined list of X-Series robots with distinct roles and seeds.

### `createRobot`

Abstract function to instantiate a single robot with configurable attributes.

### `createPlantsAndAnimals** (assumed)`

Likely handles ecosystem creation (not fully implemented in snippet).

### `createBuildings** (assumed)`

Likely handles architectural elements (not fully implemented).

### `writeStory** (assumed)`

Likely handles narrative content input (not fully implemented).

### `saveEverything** (assumed)`

Likely handles saving all created elements (not fully implemented).

## Usage

1. Open browser console at `http://localhost:5173`.
2. Paste and run the script.
3. The script will:
   - Authenticate (simulated with delay).
   - Create a world named "Space Peral" with a detailed description.
   - Generate X-Series robots with predefined roles.
   - (Assumed) Create plants/animals, buildings, and narrative content.
   - Save all elements to workspace.

## Dependencies

> ``document.querySelector``
> ``setTimeout``
> ``Event` (built-in browser APIs)`
> `no external libraries.`

## Related

- [[Space-Simulation-Documentation]]
- [[UI-Automation-Guide]]
- [[X-Series-Robot-Specs]]

>[!INFO] Important Note
> The script assumes the UI structure matches expected selectors (e.g., `input[name="name"]` or `textarea[placeholder="description"]`). If the UI changes, selectors may need updates.
>

>[!WARNING] Caution
> Delays (`setTimeout`) are used for asynchronous operations. Overly long delays may cause UI freezes. Adjust timing based on actual application performance.

>[!WARNING] Caution
> Assumed helper functions (`createPlantsAndAnimals`, `writeStory`, `saveEverything`) are not implemented in this snippet. These must be defined or integrated separately.

>[!INFO] Multilingual Support
> The script checks for both English (`Create World`) and Arabic (`إنشاء عالم`) button text dynamically. Ensure UI supports these translations.
