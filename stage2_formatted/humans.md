**Tags:** #deterministic-generation, #human-attributes, #hash-based-selection, #data-structures
**Created:** 2026-01-13
**Type:** code-library

# humans

## Summary

```
Generates deterministic human attributes and descriptions using cryptographic hashing and predefined lists.
```

## Details

> This script defines a library for generating human-like attributes (e.g., name, height, hair color) deterministically via SHA-256 hashing. It loads predefined lists (e.g., `body_types.txt`, `hair_colors.txt`) from a directory (`HumansLists`) and uses a salted hash to select random-looking attributes deterministically. The `assign_height()` function maps a category to a probabilistic height range, while `generate_name()` combines cleaned input strings (e.g., hair/eye colors) into a pseudo-random name. The `get_latest_generation_code()` function retrieves a generation code from a linked directory, likely for versioning or compatibility with other modules (e.g., robot reproduction).

## Key Functions

### ``read_list_from_file(filename)``

Safely reads a text file into a list of strings.

### ``hash_input(input_str)``

Generates a SHA-256 hash for deterministic selection.

### ``derive_int_from_hash(input_hash, salt, max_value)``

Converts a hash segment into a pseudo-random integer within a range.

### ``select_from_list(input_hash, salt, item_list, list_name)``

Randomly selects an item from a list based on the hash and salt.

### ``assign_age(input_hash, salt, min_age=18, max_age=80)``

Assigns a deterministic age within a specified range.

### ``assign_height(input_hash, salt, height_category)``

Maps a height category to a probabilistic height range (cm/feet).

### ``clean_for_name(text)``

Normalizes text (e.g., removes spaces, capitalizes parts) for name generation.

### ``generate_name(input_hash, salt, hair_color, eye_color, number)``

Combines cleaned attributes into a deterministic name.

### ``generate_distinguishing_marks(input_hash, salt)``

Selects a random distinguishing feature.

### ``get_latest_generation_code()``

Extracts a generation code from a linked file (e.g., `YearsHistory.txt`).

### ``generate_human_description(input_hash)``

Orchestrates the full deterministic description generation (partial implementation shown).

## Usage

1. Ensure `HumansLists` and `human_data` directories exist with required text files (e.g., `body_types.txt`).
2. Call `generate_human_description(input_hash)` to produce a deterministic human profile. Example:
   ```python
   hash_input = hashlib.sha256(b"user_input").hexdigest()
   description = generate_human_description(hash_input)
   ```
3. Customize lists (e.g., `height_categories`) or extend functions (e.g., add more name templates).

## Dependencies

> ``hashlib``
> ``os``
> ``re``
> ``json` (standard Python libraries).`

## Related

- [[HumansLists]]
- [[YearsHistory]]
- [[Deterministic Generation Framework]]

>[!INFO] Directory Structure
> Ensure `HumansLists` and `human_data` are absolute paths in `BASE_DIR`. Missing files (e.g., `body_types.txt`) trigger warnings/errors.

>[!WARNING] Hash Collisions
> SHA-256 collisions are theoretically possible but unlikely for short inputs. For critical applications, validate derived values (e.g., height ranges).

>[!INFO] Default Generation Code
> `get_latest_generation_code()` defaults to `"SPQ8"` if `YearsHistory.txt` is missing. Override this for version control.
