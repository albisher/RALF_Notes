**Tags:** #automated-testing, #puppeteer, #web-scraping, #space-simulation, #robotics-scenario
**Created:** 2026-01-13
**Type:** code-test

# comprehensive-space-peral-world-test

## Summary

```
Automated test suite for creating and verifying a complete "Space Peral World" in a web-based simulation environment, including robots, ecosystems, and structures.
```

## Details

> This script uses Puppeteer to automate interactions with a web application simulating a sci-fi space world. It sequentially creates a world, populates it with X-Series robots, custom robots, plants/animals, buildings, and a narrative, then verifies the setup. The test logs each step, captures screenshots, and handles errors gracefully. The world is designed with a blue sun, robotic inhabitants, and unique biomes.

## Key Functions

### `comprehensiveSpacePeralWorldTest`

Orchestrates the full test workflow, including navigation, creation, and verification steps.

### `createSpacePeralWorld`

Creates the base world with a name, description, and genre (e.g., sci-fi).

### `createXSeriesRobots`

Deploys predefined X-Series robots (e.g., X1, X2) using a reusable `createRobot` helper.

### `createRobot`

Generic function to instantiate a robot with a name, role, and seed (placeholder for future customization).

### `createNewRobots`

Creates custom robots (e.g., CylGre-Exp01, SphWhi-Ana02) with unspecified logic.

### `createPlantsAndAnimals`

Populates the world with flora/fauna (e.g., "reddish rocks," "purplish vegetation").

### `createBuildings`

Adds structures like "Pod Houses" to simulate settlement.

### `createSpacePeralStory`

Implements narrative elements (e.g., story creation in the world).

### `finalVerification`

Validates the completed world setup.

## Usage

1. Run the script to launch a browser, navigate to the target application, and execute the automated workflow.
2. Ensure the application is running locally at `http://localhost:5173`.
3. The script creates a `screenshots` directory to store visual logs of each step.
4. Handle errors gracefully (e.g., browser crashes, missing elements) via `try/catch`.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Space Peral World Documentation]]
- [[Puppeteer Test Framework Guide]]

>[!INFO] Important Note
> The script assumes the target application uses specific selectors (e.g., `a[href="/workspace"]`, `button:has-text("Create World")`). If selectors change, update the code accordingly.

>[!WARNING] Caution
> Running in headless mode (`--headless: false`) may expose the browser to potential security risks. Use `--no-sandbox` only in trusted environments. Always clean up the `screenshots` directory after execution.
