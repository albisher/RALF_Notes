**Tags:** #deterministic-coordinates, #hash-based-generation, #geographic-coordinates, #box-pattern, #world-map
**Created:** 2026-01-13
**Type:** code-notes

# location_box

## Summary

```
Generates deterministic geographic coordinates from a hash or seed string using a modular box system.
```

## Details

> The `LocationBox` class converts a provided hash or seed into latitude/longitude coordinates via deterministic hashing. It relies on `HashGeneratorMasterBox` to derive floating-point values from the input hash, scaling them to valid geographic ranges (-90/+90 for latitude, -180/+180 for longitude). The box supports fallback from a seed string if no hash is provided, and includes directional indicators (N/S/E/W) for readability. Error handling ensures robustness against invalid inputs or hash derivation failures.

## Key Functions

### ``execute(input_data)``

Orchestrates the full coordinate generation pipeline, validating inputs and delegating to `HashGeneratorMasterBox` for float derivation.

### ``__init__()``

Initializes the box with a `HashGeneratorMasterBox` instance and sets metadata (name/description).

### ``derive_float_from_hash()`** (underlying call)`

Converts a hash+salt into a float value (used for latitude/longitude).

## Usage

1. Pass a `BoxInput` containing `input_hash` or `location_seed`.
2. If `location_seed` is provided, it generates a hash internally before processing.
3. Returns a `BoxOutput` with:
   - `location_hash` (input hash)
   - `coordinates` (dict: `latitude`, `longitude`)
   - `location_data` (formatted strings + cardinal directions).

## Dependencies

> ``..core.box_interface``
> ``..generators.hash_generator_master_box``
> ``coordinate.py` (external deterministic coordinate logic)`

## Related

- [[`coordinate]]
- [[`HashGeneratorMasterBox`]]
- [[`Box` interface documentation]]

>[!INFO] Input Validation
> The box first checks for required `input_hash` or `location_seed` before proceeding. If neither is provided, it returns an error immediately.

>[!WARNING] Precision Truncation
> Coordinates are rounded to 6 decimal places, which may lose precision for high-accuracy applications. Consider preserving raw float values if sub-millimeter precision is needed.
