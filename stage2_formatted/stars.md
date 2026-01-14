**Tags:** #deterministic-generation, #hash-based-selection, #astronomy-data, #star-naming-system
**Created:** 2026-01-13
**Type:** code-library

# stars

## Summary

```
Generates randomized star properties and names using deterministic hash-based selection for reproducibility.
```

## Details

> This script reads predefined lists of star attributes (e.g., types, colors) from text files and uses cryptographic hashing to deterministically select values. It combines these selections with numeric ranges derived from hashes to produce unique star descriptions, including names, physical properties, and visual attributes. The system ensures reproducibility by using input hashes and salts, making results consistent across runs with the same input.

## Key Functions

### `read_list_from_file`

Loads predefined lists (e.g., star types) from files in a directory.

### `hash_input`

Generates SHA-256 hashes for deterministic selection.

### `derive_int_from_hash`

Converts a hash into a random integer within a specified range.

### `select_from_list`

Picks an item from a predefined list based on hash and salt.

### `generate_name`

Creates a star name using abbreviated type/color and a numeric suffix.

### `assign_number/assign_float`

Derives numeric values (e.g., temperature, luminosity) from hashes.

### `generate_star_description`

Orchestrates the full star generation process, combining attributes and physics rules (e.g., spectral class from temperature).

## Usage

1. Place text files (`star_types.txt`, `star_colors.txt`, etc.) in a `StarsLists` subdirectory.
2. Call `generate_star_description(input_hash)` to produce a star’s name, properties, and description.
3. Use salts (e.g., `"type"`, `"name"`) to control selection granularity.

## Dependencies

> ``hashlib``
> ``os``
> ``random``
> ``json` (Python standard library modules)`

## Related

- [[None]]

>[!INFO] Input Hash Criticality
> The `input_hash` parameter seeds all selections, ensuring deterministic output. Without it, results will vary unpredictably.

>[!WARNING] File Dependency
> Missing or malformed text files (e.g., `star_types.txt`) will default to `"Unknown"` for that attribute. Validate file paths explicitly.
