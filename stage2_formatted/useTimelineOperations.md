**Tags:** #Vue.js, #Composable, #Timeline, #State Management, #API Integration
**Created:** 2026-01-13
**Type:** code-notes

# useTimelineOperations

## Summary

```
Manages timeline data operations, state, and UI interactions for a timeline visualization system.
```

## Details

> This composable handles fetching, processing, and state management of timeline events from an external `boxOrchestrator` API. It initializes reactive state variables like `timelineNodes` (stores parsed events) and `topTimelineMarkers` (used for visual positioning). The logic includes asynchronous API calls to retrieve events, parse dates, and compute positions for timeline rendering. Error handling and fallback logic ensure robustness when data parsing fails.

## Key Functions

### `loadTimelineEvents`

Fetches timeline data from `boxOrchestrator`, processes events into structured nodes, and initializes `timelineNodes` and `topTimelineMarkers`.

### `generateTopTimelineMarkers`

Parses dates from `timelineNodes`, calculates date ranges, and computes positions for markers using `TimelinePositionBox` (with fallbacks for error cases).

### ``timelineNodes``

Ref storing parsed timeline events with metadata (ID, name, date, coordinates, etc.).

### ``topTimelinePosition``

Tracks the top position of the timeline (default: 40).

### ``timeScale``

Current time scale setting (e.g., 'month').

## Usage

1. Import and call `useTimelineOperations` with a `boxOrchestrator` and `currentWorldId`.
2. Use `timelineNodes` to render timeline items in a Vue component.
3. Call `loadTimelineEvents()` to refresh data (e.g., on component mount or user action).
4. Manually trigger `generateTopTimelineMarkers()` if `timelineNodes` changes dynamically.

## Dependencies

> ``vue``
> ``boxOrchestrator``
> ``logger` (from `../utils/logger.js`)`
> ``DateParsingBox``
> ``TimelinePositionBox`.`

## Related

- [[Vue]]
- [[Box Orchestrator API Documentation]]

>[!INFO] Missing `dateRange` Calculation
> The `generateTopTimelineMarkers` function incorrectly references `dateRange` before it is defined. The line should use `maxDate.getTime() - minDate.getTime()` instead of `dateRan` (likely a typo).

>[!WARNING] Hardcoded Fallback Year
> The fallback year value `20485` is arbitrary and may cause misalignment in timeline rendering. Consider validating or dynamically deriving this value from the API or user input.
