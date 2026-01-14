**Tags:** #deterministic-generation, #hash-based-selection, #solar-system-creation, #procedural-content
**Created:** 2026-01-13
**Type:** code-library

# solar_systems

## Summary

```
Generates procedurally created solar systems using deterministic hash-based selection for consistency and randomness control.
```

## Details

> This script defines a modular system for generating solar systems with configurable attributes. It loads predefined lists (e.g., system types, planetary arrangements) from text files and uses cryptographic hashing to deterministically select values. The core logic involves:
> 1. Reading static lists (e.g., `system_types.txt`) to populate attributes like system type or stability.
> 2. Applying SHA-256 hashing to derive deterministic indices for selecting items from these lists.
> 3. Combining hash-derived values with numeric ranges (e.g., planet count, system diameter) to produce realistic solar system properties.
> 4. Combining selected attributes into a structured JSON description, including visual and orbital dynamics metadata.
> 
> The script ensures reproducibility by using salts (e.g., `"type"`, `"name"`) to control selection variability while maintaining consistency across runs.

## Key Functions

### ``read_list_from_file(filename)``

Loads a text file into a list of strings, stripping whitespace.

### ``hash_input(input_str)``

Generates a SHA-256 hash for deterministic selection.

### ``derive_int_from_hash(input_hash, salt, max_value)``

Maps a hash to an integer within a specified range.

### ``select_from_list(input_hash, salt, item_list, list_name)``

Picks an item from a list based on hash-derived index.

### ``generate_name(input_hash, salt, type_name, arrangement, number)``

Creates a short, hash-derived name for the system.

### ``assign_number(input_hash, salt, min_value, max_value)``

Randomly assigns an integer within a range.

### ``assign_float(input_hash, salt, min_value, max_value, precision)``

Randomly assigns a float within a range.

### ``generate_solar_system_description(input_hash)``

Orchestrates the full system generation, combining attributes into a structured output.

## Usage

1. Place text files (`system_types.txt`, `planetary_arrangements.txt`, etc.) in `SolarSystemsLists/` to define system attributes.
2. Call `generate_solar_system_description(input_hash)` with a seed (e.g., a string) to produce a deterministic solar system description.
3. Example:
   ```python
   description = generate_solar_system_description("seed_string")
   print(description)
   ```
4. Output is a JSON object with keys like `"Solar System Image Description"` and `"System Characteristics"`.

## Dependencies

> ``hashlib``
> ``os``
> ``random``
> ``json``
> ``typing.Dict``
> ``typing.Any``

## Related

- [[`solar_system_generation_guide]]
- [[`procedural-worldbuilding]]

>[!INFO] Input Hash Importance
> The `input_hash` parameter seeds the entire generation process. Changing it produces a different system, ensuring reproducibility across runs.

>[!WARNING] File Dependency
> Missing or malformed text files (e.g., `system_types.txt`) will default to `"Unknown"` for that attribute. Ensure all files exist in `SolarSystemsLists/`.
