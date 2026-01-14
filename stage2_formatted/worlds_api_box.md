**Tags:** #API, #World Management, #Validation, #Sequential Processing, #Data Transformation
**Created:** 2026-01-13
**Type:** code-notes

# worlds_api_box

## Summary

```
Manages world-related API operations with input validation and structured execution for a game or simulation system.
```

## Details

> This `WorldsAPIBox` class extends a base `Box` class to handle all world-related API interactions, including listing, retrieving, creating, deleting, and updating world data. It integrates a `ValidationBox` to enforce parameter validation before processing each operation. The class supports operations like `list`, `get`, `create`, `delete`, `updateTimeSystem`, `updateInfo`, and `updateRules`, with conditional validation rules applied based on the requested operation. The `_executeInternal` method routes requests to the underlying `apiClient` while ensuring proper input validation and error handling.

## Key Functions

### `constructor(apiClient)`

Initializes the box with an API client and validation logic.

### `_executeInternal(inputData)`

Orchestrates API operations, validates inputs, and processes results based on the operation type.

### `list()`

Returns a list of all worlds via the API client.

### `get(params.world_id)`

Retrieves a world by its ID after validating `world_id`.

### `create(params.world_data)`

Creates a new world with validated `world_data`.

### `delete(params.world_id)`

Deletes a world by its ID after validating `world_id`.

### `updateTimeSystem(params)`

Updates a world’s time system (e.g., day/year cycles) with validation for `world_id` and `time_system`.

### `updateInfo(params)`

Updates world metadata (e.g., name, description) via a PUT request.

### `updateRules(params)`

Applies custom rules to a world after validating `world_id` and `rules`.

## Usage

1. Instantiate `WorldsAPIBox` with an `apiClient` (e.g., a fetch-based HTTP client).
2. Call `_executeInternal` with an input object containing:
   - `operation`: String (e.g., `'get'`, `'updateTimeSystem'`).
   - Optional parameters (e.g., `world_id`, `world_data`).
3. Handle the returned `BoxOutput` (success/error status + result).

## Dependencies

> ``../core/box_interface.js` (Base `Box` class)`
> ``../common/validation_box.js` (Validation logic)`
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`.`

## Related

- [[Worlds API Client]]
- [[Validation Rules Documentation]]

>[!INFO] Input Validation
> Validation rules dynamically adjust based on the operation (e.g., `get` requires `world_id`, `create` requires `world_data`). Missing or invalid inputs trigger early rejection via `ValidationBox`.

>[!WARNING] Time System Conversion
> Time system updates (e.g., `updateTimeSystem`) convert camelCase properties (e.g., `hoursPerDay`) to snake_case (`hours_per_day`) for backend compatibility. Inconsistent naming may cause errors.
