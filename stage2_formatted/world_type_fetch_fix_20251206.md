**Tags:** #api-fetch, #data-validation, #default-values, #parameter-injection
**Created:** 2026-01-14
**Type:** code-fix

# world_type_fetch_fix_20251206

## Summary

```
Fixes missing `world_type` and `world_description` parameters in API request body for map generation service.
```

## Details

> The fix ensures `world_type` and `world_description` are properly included in the fetch request body by:
> 1. Adding default values in destructured parameters (`'Planet'` and `''`).
> 2. Including these fields in the JSON payload sent to the API endpoint.
> 3. Updating the input schema to enforce these defaults. The root issue was that these parameters were defined in `params` but never passed to the fetch request body, causing an invalid request.

## Key Functions

### ``map_generator_service_box.js` fetch logic`

Handles API request body construction for map generation.

### ``world_type`/`world_description` defaults`

Ensures consistent defaults (`'Planet'` and empty string) for missing inputs.

## Usage

1. The fix automatically integrates into existing map generation workflows.
2. No manual changes required—defaults are applied during parameter parsing.

## Dependencies

> ``ui-beta/src/boxes/maps/map_generator_service_box.js``
> ``services/map-generator/api.py` (API endpoint validation).`

## Related

- [[api]]
- [[map_generator_service_box]]

>[!INFO] **API Compatibility**
> The fix aligns with the expected schema in `services/map-generator/api.py` (lines 61-62), ensuring backward compatibility with existing endpoints.

>[!WARNING] **Default Overrides**
> If `world_type`/`world_description` are explicitly set to non-default values, they will override the defaults. Test edge cases where these fields are empty or invalid.
