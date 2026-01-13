**Tags:** #machine-learning, #dream-scenario, #flight-control, #random-generator, #enum, #numpy
**Created:** 2026-01-13
**Type:** code-notes

# scenario_generator

## Summary

```
Generates randomized flight control scenarios for machine learning training.
```

## Details

> This script defines a `ScenarioGenerator` class that creates varied flight scenarios for testing autonomous systems. It uses `numpy` and `random` to produce dynamic targets with adjustable parameters like distance, altitude, and motor states. The `ScenarioType` enum categorizes different scenario types, such as random position adjustments or motor failure simulations. The generator initializes with fixed base and building positions and allows customization of success criteria (e.g., max distance error, max time).

## Key Functions

### ``generate_random_position_scenario()``

Creates a scenario where the drone must fly to a randomly generated position within constrained bounds (3–20m distance, 1–10m altitude).

### ``generate_random_motor_scenario()``

Simulates motor variability by setting random initial thrust values (0.2–0.8) while targeting a hover position 5m above the base.

## Usage

```python
# Initialize with fixed positions
generator = ScenarioGenerator([0, 0, 0], [10, 10, 0])

# Generate a random position scenario
scenario = generator.generate_random_position_scenario()
print(scenario)
```

## Dependencies

> `numpy`
> `random`
> `typing`
> `enum`

## Related

- [[None]]

>[!INFO] Parameter Adjustments
> Reduced default distances (3–20m) and altitudes (1–10m) make scenarios easier for initial training, but can be expanded for harder challenges.

>[!WARNING] Hardcoded Values
> `max_distance` (100m) and `min_altitude` (0.5m) are static; consider dynamic adjustments based on system capabilities.
