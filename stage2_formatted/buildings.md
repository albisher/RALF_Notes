**Tags:** #deterministic-generation, #building-attributes, #hash-based-selection, #data-structures
**Created:** 2026-01-13
**Type:** code-library

# buildings

## Summary

```
Generates deterministic building descriptions using hashed inputs and predefined lists of attributes.
```

## Details

> This script reads predefined lists of building attributes (e.g., materials, styles, functions) from text files and uses cryptographic hashing to deterministically select attributes and generate a building name. It processes user input via SHA-256 hashing to derive random-like selections from these lists, ensuring reproducibility. The `generate_building_description` function constructs a structured JSON-like output with visual, general, and pod-specific details.

## Key Functions

### `read_list_from_file`

Loads lists from text files stored in `BuildingsLists`.

### `hash_input`

Generates SHA-256 hashes for deterministic selection.

### `derive_int_from_hash`

Converts hash segments into integers for range-based selection.

### `select_from_list`

Picks items from lists based on hash-derived indices.

### `assign_number`

Assigns numbers within a specified range deterministically.

### `clean_for_name`

Standardizes text for naming (e.g., capitalization, trimming).

### `generate_building_name`

Combines cleaned style and a number to form a building name.

### `generate_building_description`

Orchestrates the full description generation using all attributes.

## Usage

1. Place text files (e.g., `BuildingMaterials.txt`) in a `BuildingsLists` subdirectory.
2. Run the script and input any text to generate a building description.
3. The script outputs a structured description (e.g., name, style, structural details) based on hashed inputs.

## Dependencies

> ``hashlib``
> ``os``
> ``re``

## Related

- [[None]]

>[!INFO] Important Note
> The script relies on deterministic hashing (`hashlib.sha256`) to ensure identical inputs produce identical outputs, making it reproducible. User input must be non-empty; empty inputs default to "Building."

>[!WARNING] Caution
> If `BuildingsLists` directory or required files are missing, the script will print an error and return empty lists for attributes. Ensure all files exist before execution.
