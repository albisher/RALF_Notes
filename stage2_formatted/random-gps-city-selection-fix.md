**Tags:** #gps, #random-selection, #arab-gulf, #middle-east, #north-africa, #api-fix, #data-filtering, #region-restriction
**Created:** 2026-01-12
**Type:** code-fix

# random-gps-city-selection-fix

## Summary

```
Fixed random GPS city selection to ensure varied regional focus on Arab Gulf, Middle East, and North Africa.
```

## Details

> This fix modifies the `/api/prepare` endpoint to enforce random city generation when the "Random" preset is selected, ensuring uniqueness and regional specificity. It refines the city database to prioritize Arab Gulf, Middle East, and North Africa regions by removing irrelevant cities and expanding relevant ones. The backend logic now checks for a `force_random` parameter to dynamically trigger new random location generation, even if GPS coordinates are already set.

## Key Functions

### ``/api/prepare``

Modified to include `force_random` parameter logic.

### ``force_random` parameter`

Determines whether to generate a new random city regardless of existing GPS settings.

### `City list filtering`

Updated to exclude non-MENA cities and add expanded MENA cities.

## Usage

1. Call `/api/prepare?force_random=true` in the frontend when selecting "Random" preset.
2. Backend checks `force_random` and generates a new random city if true, regardless of existing GPS data.
3. City selection now strictly adheres to Arab Gulf, Middle East, and North Africa regions.

## Dependencies

> `Python (Flask/FastAPI)`
> `JavaScript (frontend fetch API)`
> `external city database (customized for MENA focus).`

## Related

- [[random-gps-generation-original]]
- [[arab-gulf-city-list]]
- [[api-endpoint-documentation]]

>[!INFO] Important Note
> The `force_random` parameter must be explicitly passed (`?force_random=true`) to trigger a new random city selection. Without it, existing GPS coordinates override random generation.

>[!WARNING] Caution
> Ensure the updated city list is synced with the backend database to avoid inconsistencies between frontend and backend city selections.
