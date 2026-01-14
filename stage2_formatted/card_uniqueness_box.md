**Tags:** #data-validation, #card-system, #duplication-prevention, #twin-detection, #location-time-check
**Created:** 2026-01-13
**Type:** documentation

# card_uniqueness_box

## Summary

```
Validates card uniqueness to prevent duplicates while allowing near-duplicates (twins) based on field differences.
```

## Details

> This box checks whether a new card is unique or a duplicate by comparing its `uniqueness_signature` against existing cards. It distinguishes between exact duplicates (same name and signature) and twins (same signature but differing name/personality). The logic also accounts for location/time constraints, ensuring duplicates only occur at identical coordinates/timestamps. Error handling logs failures while returning structured validation results.

## Key Functions

### `CardUniquenessBox`

Core class implementing uniqueness validation logic.

### `execute()`

Processes input data to determine uniqueness, duplicates, or twins.

### `matching_cards`

List of cards with identical signatures (potential duplicates).

### `exact_duplicates`

Cards matching both signature and name.

### `twins`

Cards matching signature but differing in name/personality.

## Usage

1. Pass `uniqueness_signature`, `card_name`, and optional `existing_cards` (list of dictionaries with `uniquenessSignature`, `cardName`, `location_hash`, `time_hash`).
2. Retrieve results: `is_unique`, `is_duplicate`, `is_twin`, and matching cards.
3. Use `success` flag to validate operation.

## Dependencies

> ``..core.box_interface``
> ``logging` (Python standard library)`

## Related

- [[Card System Architecture]]
- [[Duplicate Prevention Guide]]

>[!INFO] Field Normalization
> Cards may use either `uniquenessSignature` or `uniqueness_signature` (case-insensitive). Similarly, `cardName`/`card_name` and `locationHash`/`location_hash` are treated identically.

>[!WARNING] Location/Time Sensitivity
> If `location_hash`/`time_hash` are provided, twins must share identical coordinates/timestamps to be considered duplicates. Omit these if location/time is irrelevant.
