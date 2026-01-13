**Tags:** #bash-script, #ml-ui, #server-startup, #python, #localhost
**Created:** 2026-01-13
**Type:** code-notes

# start_ml_scenario_ui

## Summary

```
Script to launch an ML scenario UI server on port 5006.
```

## Details

> This Bash script automates the startup of an ML Scenario UI server by navigating to the script’s directory and executing a Python application (`ml_scenario_ui.py`). It prints a progress message, the assigned port (5006), and the local URL (`http://localhost:5006`) to inform users of the server’s availability.

## Key Functions

### ``cd "$(dirname "$0")"``

Changes directory to the script’s location for relative path resolution.

### ``python ml_scenario_ui.py``

Executes the Python server entry point.

## Usage

1. Save the script as `start_ml_scenario_ui`.
2. Run it in the same directory as `ml_scenario_ui.py`:
   ```bash
   ./start_ml_scenario_ui
   ```
3. Access the UI at `http://localhost:5006`.

## Dependencies

> `python3`
> `ml_scenario_ui.py (local Python script)`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure `ml_scenario_ui.py` is in the same directory and executable Python is available.

>[!WARNING] Caution
> Avoid running multiple instances—port 5006 may conflict with existing services.
