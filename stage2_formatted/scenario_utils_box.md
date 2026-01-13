**Tags:** #randomization, #generative, #simulation, #physics, #object-configuration
**Created:** 2026-01-13
**Type:** code-notes

# scenario_utils_box

## Summary

```
Generates random object configurations for simulation scenarios with spacing constraints.
```

## Details

> The `ScenarioUtilsBox` class provides utilities to create randomized object configurations (e.g., cubes, spheres, cylinders) within specified bounds while enforcing minimum spacing between objects. It uses NumPy and Python’s `random` module for probabilistic sampling. The class initializes with an optional random seed for reproducibility and handles placement logic with a maximum retry limit (`max_attempts`) to avoid infinite loops.

## Key Functions

### ``__init__(self, random_seed`

Optional[int] = None)`**: Initializes the box with reproducibility control via a seed.

### ``generate_random_objects(self, ...)``

Core method generating configurations with:

### `Random shape selection (default`

`['cube', 'sphere', 'cylinder']`).

## Usage

```python
utils = ScenarioUtilsBox(random_seed=42)  # Set reproducibility
configs = utils.generate_random_objects(
    num_objects=10,
    area_bounds=(-100, 100, -100, 100),
    size_ranges={"cube": (5.0, 20.0)}  # Customize size ranges
)
```

## Dependencies

> `numpy`
> `typing`
> `random`

## Related

- [[None]]

>[!INFO] Rejection Sampling
> The method uses a loop (`max_attempts=100`) to place objects only if they meet spacing constraints, reducing collisions.

>[!WARNING] Edge Cases
> If `area_bounds` are too small or `min_spacing` is unrealistic, the loop may fail silently (no error raised).
