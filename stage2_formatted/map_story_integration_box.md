**Tags:** #world-building, #game-dev, #data-integration, #location-management, #api-box
**Created:** 2026-01-13
**Type:** code-notes

# map_story_integration_box

## Summary

```
Generates location cards from map data and links story events to map coordinates for a game/world system.
```

## Details

> This module (`MapStoryIntegrationBox`) extends a `Box` class to integrate map data with a story/world system. It processes map-generated cities, converts their coordinates into lat/lon, and creates location cards via a `CardsAPIBox`. The system also links story events to map locations by finding the nearest city within a specified radius. The implementation includes error handling for missing inputs and failed card creation, with detailed logging for debugging.
> 
> The `_executeInternal` method routes operations (`createLocationCards`, `linkEventsToMap`, `syncCoordinates`) to their respective private handlers. The `_createLocationCards` method validates inputs, processes each city, and delegates card creation to `CardsAPIBox`. The `_linkEventsToMap` method checks event coordinates against map cities to establish spatial relationships.

## Key Functions

### ``MapStoryIntegrationBox``

Core class extending `Box` to handle map-story integration.

### ``_executeInternal``

Dispatches operations to private methods with error handling.

### ``_createLocationCards``

Processes map cities into location cards with metadata.

### ``_linkEventsToMap``

Finds nearest cities for events within a radius.

### ``_mapToLatLon``

(Incomplete) Converts map coordinates to lat/lon (placeholder function).

### ``_findNearestCity``

(Incomplete) Logic to determine closest city for event proximity checks.

## Usage

1. Instantiate `MapStoryIntegrationBox` and call `execute()` with an input object containing:
   - `operation`: `'createLocationCards'`, `'linkEventsToMap'`, or `'syncCoordinates'`.
   - Relevant parameters (e.g., `mapData`, `events`, `worldId`).
2. Example:
   ```js
   const box = new MapStoryIntegrationBox();
   const input = new BoxInput({
       operation: 'createLocationCards',
       mapData: { cities: [...] },
       worldId: '123'
   });
   const result = await box.execute(input);
   ```

## Dependencies

> ``../core/box_interface.js``
> ``../api/cards_api_box.js``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory``
> ``CardsAPIBox``

## Related

- [[Game World Data Integration Guide]]
- [[CardsAPI Documentation]]

>[!INFO] Missing `_findNearestCity` Implementation
> The `_linkEventsToMap` method references an incomplete `_findNearestCity` function. This logic must be implemented to compare event coordinates against map cities (e.g., using Euclidean distance).

>[!WARNING] Error Handling for `CardsAPIBox`
> Failed card creation is logged but does not retry or propagate errors to the caller. Consider adding retry logic or validation for `CardsAPIBox` failures.
