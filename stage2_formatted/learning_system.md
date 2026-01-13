**Tags:** #data-science, #simulation, #machine-learning, #knowledge-management, #exploration
**Created:** 2026-01-13
**Type:** code-notes

# learning_system

## Summary

```
A modular learning system for accumulating and refining exploration knowledge from simulation runs.
```

## Details

> This system stores and updates learned patterns from multiple simulation executions, focusing on object distributions, path effectiveness, and exploration behaviors. It uses JSON-based persistence to retain knowledge across runs, with default initialization for new systems. The design emphasizes incremental learning—each simulation contributes to broader patterns while preserving historical data.

## Key Functions

### ``__init__(self, knowledge_file="exploration_knowledge.json")``

Initializes the system with a specified JSON file for knowledge storage, loading defaults if the file doesn’t exist.

### ``_load_knowledge(self)``

Safely loads existing knowledge from the JSON file, falling back to defaults if corrupted or missing.

### ``_default_knowledge(self)``

Returns a structured empty dictionary defining the expected knowledge schema (e.g., object types, path metrics).

### ``_save_knowledge(self)``

Updates the knowledge file with timestamps and saves the current state, including error handling for file operations.

### ``learn_from_simulation(self, objects_found, waypoints_used, coverage_stats)``

Processes a completed simulation by:

## Usage

1. Initialize the system: `system = ExplorationLearningSystem("data/knowledge.json")`.
2. Call `learn_from_simulation()` after each simulation with:
   - `objects_found`: List of dictionaries (e.g., `{"type": "cube", "x": 10.5}`).
   - `waypoints_used`: List of coordinate lists (e.g., `[[10, 20], [30, 40]]`).
   - `coverage_stats`: Dictionary of metrics (e.g., `{"area": 500, "objects": 3}`).
3. The system auto-saves knowledge to the file on each update.

## Dependencies

> `numpy`
> `json`
> `os`
> `datetime`

## Related

- [[None]]

>[!INFO] Knowledge Schema
> The `_default_knowledge()` method defines a hierarchical structure for tracking:
> - **Objects**: Arrays of spawn coordinates (e.g., `{"cubes": [[x1,y1], [x2,y2]]}`).
> - **Paths**: Waypoints and their success (e.g., `{"successful_paths": [{"waypoints": [...], "objects": 2}]}`).
> - **Patterns**: Metrics like altitude/coverage (e.g., `{"effective_altitudes": [10.2, 15.5]}`).


>[!WARNING] File Corruption
> If the JSON file is corrupted or inaccessible, the system defaults to empty knowledge. Always validate file integrity before critical updates.
