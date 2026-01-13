**Tags:** #machine-learning, #scenario-management, #hms-research, #dataclasses, #enums
**Created:** 2026-01-13
**Type:** code-notes

# ml_scenario_manager

## Summary

```
Manages ML scenarios for tracking, selection, and verification of ongoing research projects.
```

## Details

> The `MLScenarioManager` class loads and manages ML scenarios defined in a JSON file or initializes default scenarios from HMRS research. It uses a `ScenarioStatus` enum to track scenario lifecycle stages (e.g., `NOT_STARTED`, `IN_PROGRESS`). Each `MLScenario` is a dataclass containing metadata like ID, name, component type, tools/libraries, and status. The manager loads scenarios from a config file or defaults to predefined examples (e.g., bird detection, streak detection).

## Key Functions

### ``ScenarioStatus``

Enum defining possible ML scenario lifecycle states.

### ``MLScenario``

Dataclass representing an ML scenario with attributes like `id`, `name`, `component`, `description`, and `status`.

### ``MLScenarioManager``

- `__init__`: Initializes with a data file path, loads scenarios, or sets defaults.

### ``_initialize_default_scenarios``

Populates `scenarios` dict with predefined examples (e.g., bird detection, streak detection).

### ``load_scenarios``

(Inferred) Loads saved scenarios from JSON (not explicitly shown in snippet but implied by `self.load_scenarios()`).

## Usage

1. Initialize with a config file path (e.g., `MLScenarioManager("config/ml_scenarios.json")`).
2. Access scenarios via `self.scenarios` (keyed by `id`).
3. Extend with custom scenarios or override defaults.

## Dependencies

> `- `json``
> ``os``
> ``datetime``
> ``typing``
> ``dataclasses``
> ``enum` (Python standard libraries)
- External libraries: `YOLOv8``
> ``PyTorch``
> ``OpenCV``
> ``ROS2 perception packages``
> ``nvTorchCam` (tools referenced in scenarios)`

## Related

- [[03-bird-deterrent]]
- [[02-inspection-sensors]]

>[!INFO] Default Scenarios
> Default scenarios (e.g., `bird_detection`, `streak_detection`) are initialized if no config file exists. These mirror real-world HMRS research examples.

>[!WARNING] JSON Dependency
> The manager relies on a JSON file (`ml_scenarios.json`) for custom scenarios. Ensure the file exists or use `_initialize_default_scenarios()` to bypass.
