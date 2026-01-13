**Tags:** #ui-verification, #ml-scenario, #automation-testing, #swarm-intelligence, #web-interface
**Created:** 2026-01-13
**Type:** documentation-research

# 0003-ml-scenario-ui-verification

## Summary

```
Documentation summarizing ML scenario UI verification workflow, including UI components, scenario categorization, and automated testing setup.
```

## Details

> This file outlines the verification process for the ML Scenario UI, which includes a web interface for managing and tracking 15 ML scenarios extracted from HMRS research. The system categorizes scenarios into components (Scout, Overseer, Coordination, System-wide) and provides a status-tracking dashboard. The verification script automates UI checks via screenshots, ensuring elements like the header, statistics bar, and scenario filters function correctly. The UI server runs on port 5006, accessible via `http://localhost:5006`, and includes REST API endpoints for programmatic interaction.

## Key Functions

### ``ml_scenario_manager.py``

Manages ML scenarios with status tracking, JSON persistence, and filtering.

### ``ml_scenario_ui.py``

Provides a web UI with gradient design, scenario grids, and action buttons (Start/Pause/Complete).

### ``verify_ml_scenario_ui.py``

Automates UI verification via screenshots, connectivity checks, and API testing.

### ``scout_component` scenarios`

Focus on point cloud/polarization analysis (e.g., Obstacle Detection, Crack Detection).

### ``overseer_component` scenarios`

Specialized tasks like Bird Detection via YOLOv8.

## Usage

1. **Start Server**: Run `python ml_scenario_ui.py` in the `simulation` directory.
2. **Access UI**: Open `http://localhost:5006` in a browser.
3. **Verify UI**: Use `verify_ml_scenario_ui.py` to capture screenshots and validate UI elements.
4. **API Testing**: Use `curl` commands to test endpoints (e.g., `http://localhost:5006/api/scenarios`).

## Dependencies

> `Python libraries (e.g.`
> `Flask for UI server`
> `Selenium/Pytest for automated testing)`
> `HMRS research data`
> `and external ML models (e.g.`
> `YOLOv8).`

## Related

- [[0002-ml-scenario-ui]]
- [[0003-ml-scenario-ui-verification]]

>[!INFO] **Scenario Categorization**
> Scenarios are grouped into **Scout** (6), **Overseer** (2), **Coordination** (3), and **System-wide** (1) components for modular management.

>[!WARNING] **Server Dependency**
> Ensure the UI server is running before testing UI elements. Port 5006 conflicts may occur if another service uses it.
