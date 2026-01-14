**Tags:** #data-validation, #json-validation, #map-data, #structural-checks
**Created:** 2026-01-13
**Type:** documentation

# validate_map_json

## Summary

```
Validates the structure and data types of a map JSON file to ensure correctness for map rendering or processing.
```

## Details

> This script performs a comprehensive validation of a `map.json` file by checking:
> 1. **Top-level structure** (root must be a dictionary with required keys: `info`, `settings`, `mapCoordinates`, `pack`).
> 2. **Nested blocks** (`info`, `pack`) for correct key types (e.g., `info.width` must be numeric).
> 3. **Critical fields** like `pack.cells` and `pack.vertices` for proper list/dict formats and coordinate validation.
> The script gracefully handles missing or malformed data while flagging errors with severity levels (INFO, ERROR, CRITICAL).

## Key Functions

### `validate_map_json(file_path)`

Main function to validate the entire JSON file.

### `check_type(data, key, expected_type, path)`

Validates if a key exists and matches the expected type.

### `check_list_item_type(data_list, expected_type, path)`

Ensures all items in a list conform to the expected type.

### `print_feedback(message, level)`

Helper to log validation feedback with severity.

## Usage

1. Call `validate_map_json(file_path)` with the path to the `.json` file.
2. The script prints validation results in real-time, returning `True`/`False` based on success.
3. Critical failures (e.g., missing root keys) exit early; partial checks continue if possible.

## Dependencies

> `json`
> `sys`
> `os`

## Related

- [[None]]

>[!INFO] Important Note
> The script prioritizes critical fields (`cells`, `vertices`) but allows optional checks (e.g., `info.seed`). Adjust `required_pack_keys` to match your schema’s strictness.


>[!WARNING] Caution
> Empty lists (e.g., `pack.cells`) are accepted but may cause rendering issues. Validate empty lists explicitly if needed.
