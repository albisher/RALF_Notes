**Tags:** #drone_learning, #progressive_learning, #flight_simulation, #enum_management, #numerical_evaluation
**Created:** 2026-01-13
**Type:** code-notes

# learning_curve

## Summary

```
A structured system for tracking and evaluating drone flight learning progress through progressively difficult scenarios.
```

## Details

> This code implements a **Small Dreams Learning Curve System**, designed to guide users through drone flight training by organizing scenarios in ascending difficulty levels (Beginner → Expert). The system tracks performance metrics (attempts, success rate, time/position errors) per scenario and aggregates progress across all attempts. Flight scenarios are evaluated using Euclidean distance and time thresholds defined in `success_criteria`, while the `LearningCurve` class manages scenario progression, completion tracking, and overall learning analytics.
> 
> The `ScenarioDifficulty` enum categorizes difficulty levels, and `FlightScenario` objects store scenario-specific data (name, target position, success thresholds). The `LearningCurve` class initializes predefined scenarios and tracks performance metrics dynamically.

## Key Functions

### ``ScenarioDifficulty``

Enum defining difficulty tiers (BEGINNER, INTERMEDIATE, ADVanced, EXPERT).

### ``FlightScenario``

- `__init__`: Initializes a scenario with name, difficulty, target position, and success criteria.

### ``evaluate``

Computes success status and metrics (error, time) for a given flight attempt.

### ``LearningCurve``

- `__init__`: Sets up the system, initializes empty scenario lists, and loads predefined scenarios.

### ``_initialize_scenarios``

(Private) Populates `scenarios` list with structured flight tasks (e.g., hover, altitude control).

### ``evaluate``

(Inherited) Tracks performance metrics (attempts, successes, best times/errors).

## Usage

1. **Initialize**: Create an instance of `LearningCurve` to start tracking.
2. **Add Scenarios**: Define custom scenarios via `FlightScenario` (e.g., `scenario = FlightScenario("Hover", ScenarioDifficulty.BEGINNER, ...)`).
3. **Evaluate Attempts**: Call `scenario.evaluate(final_position, time_taken)` to assess performance.
4. **Progress Tracking**: Use `LearningCurve.total_attempts`/`total_successes` to monitor overall progress.

## Dependencies

> `numpy`
> `typing`
> `enum (Python standard libraries)`
> `time (for timing metrics).`

## Related

- [[DroneFlightSimulator (likely contains drone-specific logic)]]
- [[ProgressTrackingSystem (for broader analytics).]]

>[!INFO] Scenario Initialization
> The `_initialize_scenarios()` method hardcodes a small set of predefined scenarios. To extend, override this method or add scenarios dynamically via `LearningCurve.scenarios.append()`.

>[!WARNING] Success Criteria Hardcoding
> `max_distance` and `max_time` defaults (0.5m, 60s) may need adjustment for specific training goals. Customize `success_criteria` per scenario.
