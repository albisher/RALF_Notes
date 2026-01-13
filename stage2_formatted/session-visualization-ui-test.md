**Tags:** #ui-testing, #browser-automation, #visual-verification, #selenium, #plotly, #real-time-updates
**Created:** 2026-01-13
**Type:** test-reference

# session-visualization-ui-test

## Summary

```
Automated UI test verifying session, drone, and command visualization in a web application using Selenium and visual verification.
```

## Details

> This test script uses Selenium WebDriver to automate browser interactions, verifying that sessions, drones, and commands are correctly displayed and updated in a web-based visualization interface. It includes visual checks via screenshots and ensures real-time UI responsiveness, particularly in Plotly-based 3D plots. The test covers session setup, drone visualization, command execution, tab navigation, and error handling.

## Key Functions

### ``setup_session()``

Creates a session and spawns a drone for testing.

### ``load_ui_page()``

Loads the web interface using Selenium WebDriver.

### ``verify_session_display()``

Checks if session details (ID, status, sim time) are rendered.

### ``verify_drone_visualization()``

Confirms drone presence in the 3D Plotly plot.

### ``send_command_and_verify()``

Executes a command and validates UI reflection.

### ``verify_plot_updates()``

Ensures plots dynamically update with drone movement.

### ``verify_sidebar_info()``

Validates drone metadata in the sidebar.

### ``verify_tab_navigation()``

Tests switching between tabs (Simulation, Master, ML Learning).

### ``verify_real_time_updates()``

Checks UI responsiveness to live changes.

### ``verify_console_errors()``

Filters and logs critical console warnings.

## Usage

1. Run the script via `pytest` in the `simulation` directory.
2. Screenshots and results are saved in `simulation_output/session_visualization_verification/`.
3. Requires a running web server hosting the UI (e.g., Flask/Django app).

## Dependencies

> `Selenium WebDriver`
> `ChromeDriver (headless mode)`
> `Plotly`
> `pytest (for test execution)`
> ``simulation` package (likely contains backend logic for sessions/drones).`

## Related

- [[test_results]]
- [[test_selenium_browser_automation]]

>[!INFO] Important Note
> The test uses **headless Chrome** for efficiency, but ensure ChromeDriver is compatible with the browser version. If visual discrepancies occur, compare screenshots (`*.png`) with manual UI inspection.

>[!WARNING] Caution
> Non-critical console errors (e.g., minor Plotly warnings) are filtered out. Critical errors (e.g., UI crashes) trigger test failures. Always check `test_results.json` for detailed logs.
