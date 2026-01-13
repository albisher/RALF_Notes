**Tags:** #Plotly, #2D-plot, #BestPractices, #Validation, #OSM, #DataCaching
**Created:** 2026-01-13
**Type:** code-notes

# plot-2d-box

## Summary

```
Handles 2D plot initialization and validation for Plotly, enforcing best practices and caching OSM vector data.
```

## Details

> This class manages 2D plot rendering for Plotly, ensuring single responsibility for top/front/side views. It tracks Plotly command logs, enforces timing constraints (e.g., 50ms minimum between updates), and caches OSM vector data (roads/ways) to optimize performance. The `validateCommandBestPractice` method checks if commands (like `initPlot` or `updatePlot`) comply with best practices, logging violations (e.g., repeated `initPlot` calls) with severity levels.

## Key Functions

### ``constructor()``

Initializes tracking structures for Plotly commands, best practices, OSM caching, and pending updates.

### ``validateCommandBestPractice(commandType, plotId, params)``

Validates command compliance with best practices (e.g., enforces max calls for `initPlot` or update frequency thresholds).

## Usage

1. Instantiate `Plot2DBox` to manage plot lifecycle.
2. Call `validateCommandBestPractice()` before Plotly commands to check compliance.
3. Use `this.osmVectorCache` to cache OSM data for reuse.

## Dependencies

> `Plotly library (implicitly used for rendering)`
> `OSM vector data (cached via `this.osmVectorCache`).`

## Related

- [[Plotly documentation]]
- [[Best practices for Plotly updates]]

>[!INFO] Best Practice Enforcement
> Enforces timing thresholds (e.g., 50ms min between updates) to maintain smooth rendering (20 FPS max). Repeated `initPlot` calls are flagged if exceeding 1 call per minute.

>[!WARNING] Cache Invalidation Risk
> If `osmVectorCache` timestamps are not refreshed, stale data may persist. Ensure `cacheKey`/`timestamp` updates match data changes.
