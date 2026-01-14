**Tags:** #timeline-processing, #date-parsing, #event-handling, #api-integration, #box-module
**Created:** 2026-01-13
**Type:** code-module

# timeline_box

## Summary

```
Manages timeline stage operations, including event creation, updates, and marker generation with date parsing and positioning logic.
```

## Details

> The `TimelineBox` class extends a base `Box` component to handle timeline-related operations via an API client. It processes requests like `create`, `update`, `list`, `get`, `delete`, and `generateMarkers`. For `generateMarkers`, it validates input events, parses dates, and calculates positions using helper boxes (`DateParsingBox` and `TimelinePositionBox`). The system validates required fields (e.g., `events` array) and returns structured output with markers, including metadata like year, month, and position.

## Key Functions

### ``_executeInternal(inputData)``

Orchestrates execution of timeline operations (create/update/list/get/delete) via `TimelinesAPIBox`.

### ``_generateMarkers(params)``

Processes an array of events, parses dates, computes positions, and constructs markers with metadata.

### ``constructor(apiClient)``

Initializes dependencies (`TimelinesAPIBox`, `DateParsingBox`, `TimelinePositionBox`) and validates input/output schemas.

## Usage

1. Instantiate `TimelineBox` with an API client.
2. Call `_executeInternal` with an operation (e.g., `generateMarkers`) and event data.
3. For `generateMarkers`, pass an array of events containing `id`, `title`, `date`, and optional metadata like `is_key_year`.

## Dependencies

> ``../core/box_interface.js``
> ``../api/timelines_api_box.js``
> ``../common/date_parsing_box.js``
> ``../common/timeline_position_box.js``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`.`

## Related

- [[Space Peral API Documentation]]
- [[Box Core Module]]
- [[Date Parsing Module]]

>[!INFO] Required Fields
> Events array (`events`) is mandatory for `generateMarkers`. Missing fields (e.g., `date`) default to `null` but may cause parsing errors.

>[!WARNING] Date Parsing Fallback
> If date parsing fails, the marker’s `year/month/day` defaults to `null`. Ensure `dateStr` is valid to avoid silent failures.
