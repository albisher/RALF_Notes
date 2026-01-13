**Tags:** #mixin, #time-travel, #data-visualization, #socket-io, #event-handling
**Created:** 2026-01-13
**Type:** code-notes

# TimeTravelMixin

## Summary

```
Handles time travel functionality via a mixin pattern for scrubbing historical data in a simulation environment.
```

## Details

> `TimeTravelMixin` implements a **time travel mode** using a mixin pattern to enable playback through historical data stored in `timeHistory`. It processes slider events, finds the closest historical time point, and updates visualizations accordingly. The mixin integrates with Socket.IO updates, cancels pending live requests during time travel, and resumes normal operation when exiting mode.

## Key Functions

### `onTimeSliderChange(event)`

Triggers time travel mode on slider interaction, cancels pending updates, and updates plots for the selected time.

### `updatePlotsForTime(time)`

Locates the nearest historical data entry and applies it to plots via `updatePlotsWithData`.

### `exitTimeTravelMode()`

Resets to live mode, restores `simTime`, and resumes real-time updates.

### `jumpToTime(time)`

Programmatically sets the simulation time (incomplete snippet truncated).

## Usage

1. Attach this mixin to an object with `timeHistory` and `status.simTime`.
2. Call `onTimeSliderChange` on slider events to enter time travel mode.
3. Use `updatePlotsForTime` internally to find/render historical data.
4. Call `exitTimeTravelMode` to return to live updates.

## Dependencies

> ``timeHistory` (array of historical data entries)`
> ``updatePlotsWithData``
> ``updatePlots``
> ``status.simTime``
> `Socket.IO updates`
> ``abortController` (for canceling pending requests).`

## Related

- [[TimeHistoryStorage]]
- [[LiveUpdateHandler]]

>[!INFO] Critical Abort Handling
> Aborts pending live updates via `abortController` to prevent conflicts during time travel.

>[!WARNING] Edge Case: `timeHistory` must exist; invalid `time` values (e.g., negative) are silently ignored in `jumpToTime`.
