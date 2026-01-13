**Tags:** #BuildingManagement, #APIService, #OOP, #DependencyInjection, #HTTPClient
**Created:** 2026-01-13
**Type:** code-notes

# BuildingService

## Summary

```
Manages building-related business logic via HTTP API communication.
```

## Details

> `BuildingService` is a class-based service implementing **Single Responsibility Principle** to handle all building operations. It uses **APIBox** (an HTTP client) for communication and follows **OOP principles** with dependency injection. The service provides methods to fetch, spawn, save, delete, and retrieve buildings via asynchronous HTTP requests. Error handling is centralized with consistent logging and re-throwing of errors.

## Key Functions

### ``constructor(apiBox)``

Initializes the service with an injected `APIBox` instance, validating its presence.

### ``getAllBuildings()``

Asynchronously retrieves a list of all buildings from the API.

### ``spawnRandomBuilding(config)``

Generates a new building with configurable dimensions, position, and attributes.

### ``saveBuilding(building)``

Persists a building’s configuration to the backend.

### ``deleteAllBuildings()``

Removes all buildings from the system.

### ``getBuildingById(buildingId)``

Fetches a specific building by its ID (not explicitly listed in the snippet but implied by naming conventions).

## Usage

1. Inject an `APIBox` instance into `BuildingService` during construction.
2. Call methods like `getAllBuildings()`, `spawnRandomBuilding()`, or `saveBuilding()` to interact with buildings.
3. Handle errors via `try/catch` blocks, as all methods propagate errors.

## Dependencies

> `APIBox (`../../boxes/generic/APIBox.js`)`

## Related

- [[APIBox Documentation]]
- [[Universal Programming Skills Guide]]

>[!INFO] Dependency Injection
> Mandatory `APIBox` instance must be provided; failure throws an error.

>[!WARNING] Error Handling
> All methods log errors internally but re-throw them for caller control. Avoid silent failures.
