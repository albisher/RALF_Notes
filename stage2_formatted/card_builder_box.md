**Tags:** #data_processing, #card_generation, #hash_aggregation, #duplicate_detection
**Created:** 2026-01-13
**Type:** documentation

# card_builder_box

## Summary

```
Constructs a unified card entity from aggregated liked hash results for database storage.
```

## Details

> This `CardBuilderBox` class processes input data containing multiple hash references (e.g., from user likes) and merges them into a cohesive card structure. It validates required fields (`card_type`, `card_name`) and supports fallback via `combined_entity_data`. The logic prioritizes merging data by type (e.g., `personality`, `location_hash`) while preserving optional metadata like coordinates or timestamps. A SHA-256-based uniqueness signature ensures duplicate detection by excluding the card name (allowing "twins").

## Key Functions

### ``execute(input_data`

BoxInput)`**: Orchestrates card construction from input fields, validating requirements and combining hash references into a structured `card_data` dictionary.

### ``_generate_uniqueness_signature(card_data`

Dict)`**: Computes a cryptographic hash of core fields (excluding `card_name`) to detect duplicates across cards with identical metadata.

## Usage

1. Pass `BoxInput` with:
   - Required: `card_type`, `card_name`, `liked_hash_references` (or `combined_entity_data`).
   - Optional: Additional metadata (e.g., `location_hash`, `coordinates`).
2. Output: `BoxOutput` containing `card_data` (ready for DB) and `uniqueness_signature`.

## Dependencies

> ``..core.box_interface``
> ``logging``
> ``hashlib` (standard library)`

## Related

- [[`core]]
- [[`duplicate_detection`]]

>[!INFO] Key Fields Exclusion
> The uniqueness signature omits `card_name` to allow cards with identical metadata but different names (e.g., "Alice’s Sword" vs. "Sword of Alice").

>[!WARNING] Error Handling
> Silent failures (e.g., malformed `liked_hash_references`) log via `logger.error` and return `success=False`.
