**Tags:** #drone-automation, #mission-planning, #task-management, #enum-handling
**Created:** 2026-01-13
**Type:** code-notes

# mission_tasks

## Summary

```
Manages drone mission tasks with air/water jets, cleaning, and spray operations.
```

## Details

> This module defines a system for organizing drone mission tasks, including initialization, execution tracking, and quality assessment. It uses `TaskType` (an `Enum`) to categorize tasks (e.g., air jet, water spray) and `MissionTask` to store positional data, duration, and progress metrics. The `update()` method simulates progress based on drone positioning, while `get_status()` returns current task state. Quality scoring combines position accuracy and completion progress.

## Key Functions

### ``TaskType` (Enum)`

Defines task types (e.g., `AIR_JET`, `CLEANING`).

### ``MissionTask.__init__()``

Initializes a task with type, position, area, and duration.

### ``MissionTask.start()``

Marks task as active and records start time.

### ``MissionTask.update()``

Updates progress based on drone position and elapsed time.

### ``MissionTask.get_status()``

Returns a dictionary with task metadata (type, position, progress).

## Usage

1. Create a `MissionTask` with `TaskType`, `target_position`, `target_area`, and `duration`.
2. Call `start()` to begin execution.
3. Periodically call `update(drone_position, dt)` to track progress.
4. Retrieve status via `get_status()`.

## Dependencies

> `numpy`
> `typing`
> `enum`
> `time`

## Related

- [[none]]

>[!INFO] Position Tolerance
> `position_tolerance` (default: 1.0m) defines acceptable proximity for task completion. Adjust for precision needs.

>[!WARNING] Simplified Coverage
> `coverage_percentage` is a placeholder—real systems should track actual area scanned via sensors.
