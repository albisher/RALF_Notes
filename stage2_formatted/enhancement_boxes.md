**Tags:** #geospatial-simulation, #environmental-modelling, #procedural-generation, #frontend-wrapper, #api-integration
**Created:** 2026-01-13
**Type:** code-notes

# enhancement_boxes

## Summary

```
Frontend wrappers for high-fidelity world simulation enhancements, enabling dynamic terrain and climate calculations via API calls.
```

## Details

> This file defines frontend wrappers (`Box` subclasses) for geospatial and environmental simulation enhancements. Each class (`HydraulicErosionBox`, `TectonicPlateSimulationBox`, etc.) extends a base `Box` class, encapsulating asynchronous API interactions to compute features like river systems, tectonic plate movements, moisture distribution, hillshading, and habitability scores. The `execute()` method validates the operation type and processes input data (e.g., `world_hash`, `heights`) through an `APIClient` to fetch results, returning structured success/error responses.

## Key Functions

### `HydraulicErosionBox.execute`

Applies erosion logic via API to generate rivers and terrain degradation.

### `TectonicPlateSimulationBox.execute`

Simulates plate tectonics, returning plate boundaries and modified heightmaps.

### `MoistureCalculatorBox.execute`

Computes moisture patterns (e.g., Whittaker Diagram) based on wind and terrain data.

### `HillshadingBox.execute`

Calculates 3D lighting effects (e.g., sun angles) for visual rendering.

### `HabitabilityScoringBox.execute`

Evaluates cell suitability for cities using terrain/environmental metrics.

## Usage

1. Instantiate a `Box` subclass (e.g., `new HydraulicErosionBox()`).
2. Call `execute(operation, inputData)` with a valid operation (e.g., `'apply_erosion'`) and required fields (e.g., `world_hash`, `heights`).
3. Handle the returned `{ success, data/error }` object to integrate results into a map generation pipeline.

## Dependencies

> ``../core/box_interface.js``
> ``../../services/api-client.js``

## Related

- [[World Generation Pipeline]]
- [[API Service Documentation]]

>[!INFO] Input Validation
> All `execute()` methods reject unsupported operations (e.g., `'apply_erosion'` vs. `'unknown_operation'`).

>[!WARNING] Default Values
> Missing optional params (e.g., `erosion_rate`) default to `0.01` or `10000`, which may bias results. Explicitly pass all fields for accuracy.
