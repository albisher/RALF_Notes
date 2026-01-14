**Tags:** #automation, #web-scraping, #puppeteer, #game-dev, #world-building, #robotics-simulation
**Created:** 2026-01-13
**Type:** code-notes

# create-space-peral-world

## Summary

```
Automates creation of a custom sci-fi world and associated X-Series robots in a web-based game environment using Puppeteer.
```

## Details

> This script uses Puppeteer to automate interactions with a web application (likely a space-themed game or simulation) to:
> 1. Launch a browser, navigate to the worlds page, and capture initial screenshots.
> 2. Create a custom world named "Space Peral" with detailed descriptions of its environment.
> 3. Navigate to the newly created world and capture its details.
> 4. Automate the creation of six specialized X-Series robots (e.g., Drone, Orchestrator) with predefined roles, descriptions, and locations.
> The script employs Puppeteer’s `evaluateHandle` and `page.$` methods to dynamically locate and interact with UI elements, including buttons, inputs, and text fields.

## Key Functions

### `createSpacePeralWorld()`

Orchestrates the entire workflow of world creation and robot setup.

### `createRobot(page, name, role, description)`

Helper function to dynamically create and configure individual X-Series robots with custom attributes.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node create-space-peral-world.js`.
3. Ensure the target web application (e.g., game) is running locally on `http://localhost:5173/worlds`.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Game World Automation Scripts]]
- [[Puppeteer Automation Guide]]

>[!INFO] Important Note
> The script assumes the target application uses standard HTML/CSS selectors for UI elements. If the DOM structure changes, selectors may need adjustment.

>[!WARNING] Caution
> Running Puppeteer in non-headless mode (`--no-sandbox`) may expose security risks on certain systems. Use with caution in restricted environments.
