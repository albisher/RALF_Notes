**Tags:** #deterministic-generation, #hash-based-selection, #planet-data-generation, #randomized-characteristics, #data-structures
**Created:** 2026-01-13
**Type:** code-library

# planets

## Summary

```
Generates randomized planet data using deterministic hash-based selection for consistency and reproducibility.
```

## Details

> This script reads predefined lists of planet attributes (e.g., types, colors, surface features) from text files and uses cryptographic hashing to deterministically select values. It combines these selections with numeric ranges derived from hashes to produce unique, reproducible planet descriptions. The system includes a structured JSON output for planet metadata, including visual, physical, and contextual properties.

## Key Functions

### `read_list_from_file(filename)`

Loads a list of items from a text file in a designated directory.

### `hash_input(input_str)`

Generates a SHA-256 hash of an input string for deterministic selection.

### `derive_int_from_hash(input_hash, salt, max_value)`

Converts a hash into a pseudo-random integer within a specified range.

### `select_from_list(input_hash, salt, item_list, list_name)`

Randomly selects an item from a list based on the hash and salt.

### `generate_name(input_hash, salt, type_name, color, number)`

Creates a formatted planet name using abbreviated type/color and a numeric suffix.

### `assign_number(input_hash, salt, min_value, max_value)`

Assigns a number within a given range using hash-based derivation.

### `generate_planet_description(input_hash)`

Orchestrates the full planet description generation, combining selected attributes and numeric values into a structured JSON output.

### `main()`

Entry point for command-line execution (currently incomplete).

## Usage

1. Place text files (`planet_types.txt`, `surface_features.txt`, etc.) in the `PlanetsLists` subdirectory.
2. Run the script with a seed input (e.g., `python planets.py "seed_input"`).
3. The script will generate a planet description based on the input hash, producing a JSON-formatted output with deterministic properties.

## Dependencies

> ``hashlib``
> ``os``
> ``random``
> ``json``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[None]]

>[!INFO] Important Note
> The script relies on deterministic hashing (`hashlib.sha256`) to ensure reproducibility. Changing the input hash or salt alters the generated values, allowing for controlled variation.

>[!WARNING] Caution
> If text files in `PlanetsLists` are missing or corrupted, the script defaults to `"Unknown"` for missing attributes. Ensure all required files exist for accurate results.
