**Tags:** #service, #OOP, #API, #dependency-injection, #GPS, #weather, #drone-controls
**Created:** 2026-01-13
**Type:** code-notes

# MasterControlsService

## Summary

```
Manages master controls (GPS, weather, buildings, drone brands) via HTTP API with fallback defaults.
```

## Details

> `MasterControlsService` implements a class-based service using dependency injection (APIBox) to handle master controls operations. It encapsulates logic for loading/saving GPS/weather/drone configurations, with fallback defaults on failure. The service follows OOP principles, abstracting API interactions behind clear methods.

## Key Functions

### ``constructor(apiBox)``

Initializes service with required APIBox dependency.

### ``loadMasterControls()``

Asynchronously fetches master controls data from API or returns defaults.

### ``saveMasterControls(controls)``

Saves master controls configuration via POST request.

### ``fetchWeatherFromGPS(lat, lon)``

Retrieves weather data from GPS coordinates.

### ``applyWeatherSettings(weather)``

Applies weather settings to simulation.

### ``loadDroneBrands()``

Loads available drone brands (placeholder implementation).

## Usage

```javascript
const apiBox = new APIBox(); // Assume this is configured elsewhere
const service = new MasterControlsService(apiBox);
await service.loadMasterControls(); // Loads data or returns defaults
await service.saveMasterControls({ gpsMode: 'manual', ... });
```

## Dependencies

> `APIBox`

## Related

- [[APIBox Documentation]]
- [[MasterControls API Spec]]

>[!INFO] Error Handling
> All methods include try-catch blocks, returning defaults/fallbacks for `loadMasterControls` but re-throwing errors for other operations.

>[!WARNING] Fallback Defaults
> `loadMasterControls` defaults to simulation values if API fails, which may not reflect real-world state.
