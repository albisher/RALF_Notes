**Tags:** #code-refactoring, #box-pattern, #autonomous-exploration, #modularization, #line-count-analysis
**Created:** 2026-01-12
**Type:** code-notes

# exploration_manager_box

## Summary

```
Analyzes and documents size violations in autonomous exploration system files, focusing on refactoring to adhere to the Box Pattern (≤500 lines per file).
```

## Details

> This document examines three files (`autonomous_exploration_live.py`, `autonomous_exploration_test.py`) violating line limits while `exploration_manager_box.py` passes. It details line distribution, class/function complexity, and suggests breaking down large components into smaller, modular units (e.g., `GroundTruthLoggerBox`, `BaseStationBox`). The analysis highlights redundant code, improper imports, and integration of server logic into simulation files, emphasizing the need to decompose classes/functions and separate concerns (e.g., visualization, orchestration).

## Key Functions

### `GroundTruthLogger`

Data logging class (51 lines in `live.py`) → refactor into `GroundTruthLoggerBox`.

### `BaseStation`

Core station logic (95 lines in `live.py`) → refactor into `BaseStationBox`.

### `spawn_random_objects`

Object generation utility (89 lines in `live.py`) → refactor into `ScenarioUtilsBox`.

### `AutonomousExplorationDrone`

Main drone class (190 lines in `live.py`) → decompose via composition of smaller boxes.

### `create_3d_plot`

Visualization helper (75 lines in `live.py`) → refactor into `VisualizationBox`.

### `main()`

Orchestration logic (164 lines in `test.py`) → split into smaller functions.

### `AutonomousExplorationDrone class** (208 lines in `test.py`)`

Duplicates logic from `live.py` → extract shared utilities.

## Usage

The document provides a roadmap for refactoring by:
1. **Decomposing** large classes/functions into smaller "boxes" (e.g., `BoxPattern`).
2. **Separating concerns**: Visualization, orchestration, and server logic into distinct files.
3. **Reducing redundancy**: Extract shared logic (e.g., `spawn_random_objects`) into reusable utilities.

## Dependencies

> `- Flask/SocketIO (mixed in `live.py` simulation logic)
- External test classes (e.g.`
> ``GroundTruthLogger``
> ``BaseStation` imported from `simple_exploration_test.py`)`

## Related

- [[0002-CODE-SIZE-ANALYSIS]]
- [[Box Pattern - Refactoring Guide]]

>[!INFO] Critical Violation
> **`autonomous_exploration_live.py`** exceeds the 500-line limit by 31%, violating the Box Pattern. Refactoring is mandatory to improve modularity and maintainability.

>[!WARNING] Code Duplication
> **`autonomous_exploration_test.py`** duplicates logic from `live.py` (e.g., `GroundTruthLogger`, `create_3d_plot`). Extract shared utilities to avoid redundancy.

>[!INFO] Server-Simulation Split
> **Flask/SocketIO integration** in `live.py` should be moved to a separate server file to avoid coupling simulation logic with I/O handling.
