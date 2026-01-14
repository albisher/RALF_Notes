**Tags:** #world-generation, #map-testing, #data-visualization, #statistics-discrepancy, #test-summary
**Created:** 2026-01-13
**Type:** test-reference

# TEST_RESULTS_SUMMARY

## Summary

```
Document summarizing test results for a world type map generator, highlighting discrepancies between statistical and visual outputs.
```

## Details

> This file documents a test run for a **World Type Map Generation** system, evaluating different map types (Planet, Galaxy) with metrics like cell count, land/water distribution, and generation time. The test reveals a persistent **statistics-visual rendering mismatch** (e.g., 100% land stats but blue-dominated visuals), alongside minor issues like authentication interruptions and schema errors. The system is incomplete, with pending tests for 6 additional world types (e.g., Cloud World, Solar System).

## Key Functions

### ``generateFullMap``

Handles map generation logic, previously had a null-width/height bug.

### ``WORLD_EXPECTATIONS``

Defines target metrics (e.g., land ratio, clustering) for validation.

### `Statistics Calculation`

Computes land/water ratios but diverges from visual rendering.

## Usage

Tested via a web interface (`localhost:5174`), using provided URLs to generate and inspect maps. Remaining tests require manual execution via URLs listed.

## Dependencies

> ``WORLD_EXPECTATIONS` (internal config)`
> `authentication service (intermittent issues)`
> `rendering engine (visual discrepancies).`

## Related

- [[WORLD_EXPECTATIONS]]
- [[Map Rendering Documentation]]
- [[Authentication Logs]]

>[!INFO] **Critical Discrepancy**
> The system’s **statistics (100% land) and visuals (blue-dominated)** conflict, indicating a bug in land/water classification logic. Investigate height thresholds or rendering thresholds.

>[!WARNING] **Authentication Risk**
> Intermittent timeouts suggest session instability. Refresh login or implement retry logic to avoid dropped connections during long runs.
