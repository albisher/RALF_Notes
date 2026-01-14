**Tags:** #map-processing, #world-save, #backend-integration, #secure-storage, #json-processing
**Created:** 2026-01-13
**Type:** code-box

# map_save_to_world_box

## Summary

```
Handles saving generated maps to a world for visualization via a 2D world map system, processing and uploading map data securely.
```

## Details

> This box processes raw map data, checks for pre-existing derived metadata (e.g., coordinates, dimensions), and uploads it to a backend API. If the map lacks derived metadata, it delegates processing to a `MapProcessBox` before conversion to JSON. The processed map is then formatted into a file, attached via `FormData`, and sent to `/api/maps/upload` with authentication via a stored token. Error handling covers missing fields, processing failures, and authentication issues.

## Key Functions

### ``MapSaveToWorldBox``

Core class extending `Box` to manage map-to-world saving workflow.

### ``_executeInternal``

Handles the execution logic, validating inputs, processing maps, and uploading to the backend.

### ``MapProcessBox``

External dependency for map metadata derivation (instantiated in constructor).

## Usage

1. Initialize the box with `new MapSaveToWorldBox()`.
2. Call `execute()` with an input object containing `mapData`, `worldId`, and optional `worldName`.
3. The box returns a `BoxOutput` with success/error status and metadata (e.g., `map_path`).

## Dependencies

> ``../core/box_interface.js``
> ``./map_process_box.js``
> ``../../services/env.js``
> ``../../utils/secure-storage.js``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory``
> ``FormData``
> ``Blob``
> ``File``
> ``fetch`.`

## Related

- [[MapProcessBox]]
- [[WorldMap2D]]
- [[upload`]]

>[!INFO] DerivedInfo Check
> If `mapData.derivedInfo` already contains `mapOriginX`, `mapOriginY`, `mapNativeWidth`, and `mapNativeHeight`, the map is skipped for reprocessing to avoid redundant steps.


>[!WARNING] Authentication Risk
> The box relies on `secureStorage` for token retrieval. If `auth_token` or `localStorage` fails, the box returns an error. Ensure secure storage is implemented correctly to prevent token exposure.
