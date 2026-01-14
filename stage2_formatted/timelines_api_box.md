**Tags:** #API, #Timeline, #Box, #CRUD, #Asynchronous
**Created:** 2026-01-13
**Type:** code-notes

# timelines_api_box

## Summary

```
Manages timeline operations via an API wrapper for a modular system.
```

## Details

> This `TimelinesAPIBox` class extends a base `Box` component to handle all CRUD (Create, Read, Update, Delete) operations for timelines and events. It acts as an intermediary between a user-facing API and an underlying `apiClient`, validating inputs, routing requests, and formatting responses. The class supports operations like listing, retrieving, creating, updating, and deleting timelines and events, with optional parameters like `world_id`, `timeline_id`, and `event_id`. The `_executeInternal` method processes requests based on the specified `operation`, delegating calls to the `apiClient` and wrapping results in a standardized `BoxOutput` format. Error handling is centralized, converting external API errors into consistent `BoxErrorCode` and `BoxErrorCategory` responses.

## Key Functions

### ``constructor(apiClient)``

Initializes the box with an API client and configures metadata (version, dependencies, supported operations).

### ``_executeInternal(inputData)``

Core method that routes operations to the `apiClient` and returns structured results or errors.

### ``list()``

Retrieves timelines by `world_id` and `timeline_type`.

### ``get()``

Fetches a specific timeline by `timeline_id`.

### ``getEvents()``

Lists all events for a world (simplified as a `list` call with `include_events=true`).

### ``create()``

Creates a new timeline with `timeline_data`.

### ``update()``

Modifies an existing timeline via `timeline_id` and `update_data`.

### ``delete()``

Removes a timeline by `timeline_id`.

### ``createEvent()``

Adds an event to a timeline using `timeline_id` and `event_data`.

### ``updateEvent()``

Edits an event via `timeline_id`, `event_id`, and `update_data`.

### ``deleteEvent()``

Removes an event by `timeline_id` and `event_id`.

## Usage

1. Instantiate `TimelinesAPIBox` with an `apiClient`:
   ```js
   const box = new TimelinesAPIBox(apiClient);
   ```
2. Call operations via `_executeInternal` with an input object containing:
   - `operation` (e.g., `'create'`).
   - Required parameters (e.g., `timeline_id`, `world_id`).
   - Optional parameters (e.g., `include_events`, `event_data`).
3. Handle responses: Success returns `{ operation, result }`; errors return structured `BoxOutput.error`.

## Dependencies

> ``../core/box_interface.js` (provides `Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`)`
> ``apiClient.timelines` (external API client for timeline operations)`
> ``apiClient.timelines.events` (external API client for event operations).`

## Related

- [[Space Peral Team Architecture]]
- [[Box Interface Documentation]]

>[!INFO] Input Validation
> The `inputSchema` enforces required fields (e.g., `operation`) and data types (e.g., `world_id` as a string). Missing/invalid data triggers `BoxErrorCategory.VALIDATION`.

>[!WARNING] Parallelism Limitation
> `supportsParallel: false` prevents concurrent operations, which may impact performance for batch requests. Ensure sequential calls if needed.
