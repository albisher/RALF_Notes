**Tags:** #drone-simulation, #visualization, #headless-browser, #web-scraping, #api-integration
**Created:** 2026-01-13
**Type:** code-notes

# generate_visualization_screenshot

## Summary

```
Generates a screenshot of a drone simulation UI by controlling drones and capturing the rendered output.
```

## Details

> This script automates the process of creating a visual representation of an HMRS (Hypothetical Multi-Robot Simulation) by:
> 1. Sending movement commands via an API to drones to create visible paths.
> 2. Waiting for the simulation to render drone paths and building detections.
> 3. Using Selenium in headless mode to navigate to the simulation UI, trigger a quad view, and capture a screenshot.
> 
> The script relies on a local API (`http://localhost:5007`) to interact with drones and the simulation UI.

## Key Functions

### `send_command(drone_name, target)`

Sends a movement command to a drone via HTTP POST to `/api/command`.

### `take_screenshot()`

Initializes a headless Chrome driver, navigates to the simulation URL, triggers the quad view, and saves a screenshot to `simulation_output/hmrs_simulation_screenshot.png`.

### `main()`

Orchestrates the entire workflow: checks simulation health, verifies API connectivity, and initiates the screenshot process.

## Usage

1. Ensure the HMRS simulation is running and accessible at `http://localhost:5007`.
2. Run the script to:
   - Send drone movement commands (if needed).
   - Capture the simulation UI in quad view mode.
   - Save the screenshot to `simulation_output/`.
3. Modify `BASE_URL` or `screenshot_path` if the simulation runs on a different host/port.

## Dependencies

> `requests`
> `selenium`
> `time`
> `json`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the simulation UI contains a **"Quad View"** button. If the button’s name/location differs, update the XPath in `take_screenshot()`.

>[!WARNING] Caution
> Headless Chrome may fail if the simulation UI relies on dynamic JavaScript rendering. Increase `time.sleep()` values if plots fail to render. Avoid running this in environments with restricted network access.
