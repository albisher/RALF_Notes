**Tags:** #throttling, #debouncing, #polling-optimization, #api-performance, #server-load-reduction, #interval-management
**Created:** 2026-01-12
**Type:** code-notes

# app-data.js

## Summary

```
Fixes excessive `/api/data` polling by implementing interval cleanup, throttling, and increased polling intervals to reduce server load.
```

## Details

> The code fixes multiple rapid requests to `/api/data` by:
> 1. **Clearing existing intervals** in `startPlotUpdates()` to prevent duplicate intervals.
> 2. **Adding request throttling** in `updatePlots()` to enforce a minimum delay (200ms) between updates.
> 3. **Increasing the polling interval** from 100ms to 200ms, reducing requests from 10/s to 5/s.

## Key Functions

### ``startPlotUpdates()``

Clears previous intervals and sets a new 200ms polling interval.

### ``updatePlots()``

Implements throttling to prevent rapid successive calls.

### ``lastPlotUpdateTime``

Tracks the last update timestamp for throttling logic.

## Usage

Call `startPlotUpdates()` to begin periodic updates. The throttling and cleanup ensure smooth operation without excessive API calls.

## Dependencies

> ``setInterval``
> ``clearInterval``
> ``Date.now()` (built-in JS functions).`

## Related

- [[app-data]]
- [[server-performance-best-practices]]

>[!INFO] **Interval Cleanup Critical**
> Clearing existing intervals (`clearInterval`) prevents duplicate polling if `startPlotUpdates()` is called multiple times.

>[!WARNING] **Throttling Overrides Interval**
> The throttling logic (`plotUpdateThrottle`) ensures API calls respect the minimum delay, even if the interval fires more frequently.
