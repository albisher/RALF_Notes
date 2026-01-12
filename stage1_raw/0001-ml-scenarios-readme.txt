### FILENAME
ml-scenarios-readme

### TAGS
#machine-learning, #scenario-management, #ui-system, #research-tracking, #hmsr, #automation, #web-interface, #data-extraction, #json-storage

### TYPE
documentation

### SUMMARY
Documentation for an ML scenario selection system extracting and managing 12 HMRS research-based scenarios via a web UI and API.

### DETAILS
This README outlines a **machine learning scenario management system** designed to extract, organize, and track 12 predefined ML scenarios from HMRS research. The system provides a **user-friendly web UI** for browsing, selecting, and monitoring scenarios, alongside a **REST API** for programmatic access. Scenarios are stored persistently in JSON format, enabling easy updates and verification.

The system categorizes scenarios into groups (e.g., Scout, Overseer, Coordination) and allows filtering by status or component. Users can manually or automatically verify functionality via a dedicated verification script.

### KEY_FUNCTIONS
- **`ml_scenario_ui.py`**: Runs the web UI server (port 5006) for scenario management.
- **`verify_ml_scenario_ui.py`**: Executes automated UI verification checks.
- **REST API**: Enables programmatic scenario selection and status updates.
- **JSON Storage**: Persists scenario data for offline or batch processing.

### DEPENDENCIES
Python libraries (likely including Flask for UI, requests for API interactions, and JSON handling).

### USAGE
1. **Installation**: Navigate to the `simulation` directory and run `ml_scenario_ui.py`.
2. **Access UI**: Open `http://localhost:5006` in a browser.
3. **Select Scenarios**: Click "Start" on desired scenarios to begin tracking.
4. **Verify**: Run `verify_ml_scenario_ui.py` for automated checks or manually inspect UI functionality.

### RELATED
[[0002-ml-scenario-ui.md]], [[none]]

### CALLOUTS
>[!INFO]- **Categorization**
> Scenarios are grouped logically (e.g., Scout, Coordination) for intuitive navigation. Each group contains specific ML tasks (e.g., obstacle detection, predictive maintenance).
>[!WARNING]- **Localhost Dependency**
> The UI runs on `localhost:5006`. Ensure no conflicts exist with other services on this port.