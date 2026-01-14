**Tags:** #randomized_generation, #procedural_content, #hash_based_selection, #narrative_descriptors
**Created:** 2026-01-13
**Type:** code-notes

# giants

## Summary

```
Generates randomized giant descriptions using hash-based selection from predefined lists.
```

## Details

> This script reads predefined lists of giant attributes (e.g., types, skin colors) from a file and uses cryptographic hashing to derive randomized selections. It processes user input (or a provided hash) to generate a structured JSON output describing a giant’s appearance, temperament, and lore. The logic involves hashing input data, deriving indices from salts, and mapping those to random attributes from predefined lists.

## Key Functions

### `read_list_from_file(filename)`

Loads a text file containing comma-separated or space-separated items into a list.

### `hash_input(input_str)`

Computes SHA-256 hash of input text for deterministic randomness.

### `derive_int_from_hash(input_hash, salt, max_value)`

Extracts an integer from a hash segment, scaled modulo `max_value` for bounded randomness.

### `select_from_list(input_hash, salt, item_list)`

Randomly selects an item from a list using the derived index.

### `generate_giant_description(input_hash)`

Orchestrates the full description generation by combining selected attributes into a structured JSON output.

## Usage

1. Run the script with an optional input hash (`python giants.py <hash>`) or provide text interactively.
2. The script outputs a JSON description of a randomized giant, including visual traits, temperament, and lore.
3. Predefined lists (`giant_types.txt`) must exist in the `GiantsLists` subdirectory.

## Dependencies

> ``hashlib``
> ``os``
> ``json``
> ``argparse``

## Related

- [[None]]

>[!INFO] Important Note
> The script relies on `giant_types.txt` to be present in the `GiantsLists` directory. If missing, it defaults to empty lists, resulting in "Unknown" responses for attributes.

>[!WARNING] Caution
> Hash collisions may produce duplicate descriptions. For uniqueness, consider adding a secondary salt or hashing step.
