**Tags:** #time-generation, #hash-based, #temporal-analysis, #lifecycle-stage, #probabilistic-modelling
**Created:** 2026-01-13
**Type:** code-box

# time_box

## Summary

```
Generates time-related metadata (temporal zones, phases, lifecycle stages) from a hash input using predefined lists and probabilistic calculations.
```

## Details

> This `TimeBox` class processes input hashes to derive structured temporal metadata. It leverages a `HashGeneratorMasterBox` to derive values from the input hash via predefined salts (e.g., `"temporal_zone"`, `"time_phase"`). The system first validates the input hash or seed, then maps it to thematic categories (e.g., "Dawn Era" for temporal zones, "Formation" for time phases) using deterministic lists. Probabilistic values (e.g., existence probability) and multi-dimensional coordinates (e.g., `temporal_x`, `temporal_y`) are derived via floating-point hashing. Granularity (default: "day") influences the output precision.

## Key Functions

### ``execute(input_data)``

Orchestrates the entire workflow: validates input, generates hash if needed, and retrieves temporal metadata (zone, phase, stage, coordinates, probability).

### ``HashGeneratorMasterBox``

External dependency used for hash-based value derivation (e.g., selecting from lists or deriving floats).

### ``Box` (parent class)`

Provides core box interface (e.g., `BoxInput`, `BoxOutput` handling).

## Usage

1. Pass a `BoxInput` containing:
   - `input_hash` (required) or `time_seed` (optional).
   - Optional: `granularity` (e.g., `"month"`).
2. Output includes:
   - `time_hash`: Original input hash.
   - `temporal_zone`: Thematic era (e.g., "Prime Era").
   - `time_phase`: Evolutionary stage (e.g., "Formation").
   - `lifecycle_stage`: Growth/decline phase (e.g., "Growth").
   - `temporal_coordinates`: 4D probabilistic values.
   - `existence_probability`: Float (0.0–1.0).

## Dependencies

> ``..core.box_interface``
> ``..generators.hash_generator_master_box``
> ``time_existence.py` (implicitly referenced for temporal logic).`

## Related

- [[`time_existence]]
- [[`HashGeneratorMasterBox`]]

>[!INFO] Input Validation
> If neither `input_hash` nor `time_seed` is provided, the box fails with an error. Seed-based hashing is conditional on `time_seed`.

>[!WARNING] Fallback Defaults
> Missing hash results default to `"Prime Era"` (temporal zone) or `0.5` (probability), risking ambiguity for debugging. Explicit error handling is recommended for production use.
