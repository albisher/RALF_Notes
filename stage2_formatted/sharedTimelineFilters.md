**Tags:** #Vue, #Reactive-State, #Timeline-Filtering, #Proximity-Sorting, #State-Management
**Created:** 2026-01-13
**Type:** code-notes

# sharedTimelineFilters

## Summary

```
Manages shared reactive state for timeline filters across multiple Vue.js components.
```

## Details

> This module implements a centralized reactive state (`sharedTimelineFilters`) for timeline proximity and year-based filtering. It uses Vue’s `reactive` API to maintain state that all connected components (e.g., Card, Timeline, Story) can access. The state includes:
> - `timelinePosition` (0–100) for proximity-based sorting.
> - `timelineYear` for year selection.
> - `timelineYearMarkers` for distance calculations.
> - `timelineMarkerId` for tracking selected markers.
> 
> The `updateSharedTimelineFilters` function updates individual filter values, while `clearSharedTimelineFilters` resets all fields to `null`.

## Key Functions

### ``sharedTimelineFilters``

Reactive object storing all filter configurations.

### ``updateSharedTimelineFilters(filters)``

Conditionally updates filter values from an input object.

### ``clearSharedTimelineFilters()``

Resets all filter fields to `null`.

## Usage

1. Import `sharedTimelineFilters` and `updateSharedTimelineFilters` in components needing shared filters.
2. Call `updateSharedTimelineFilters({ timelinePosition: 50 })` to set proximity filters.
3. Call `clearSharedTimelineFilters()` to reset all filters.

## Dependencies

> ``vue``
> ``@vue/reactive``

## Related

- [[Vue State Management Patterns]]
- [[Proximity Filtering Implementation]]

>[!INFO] Reactive Updates
> Changes to `sharedTimelineFilters` trigger Vue’s reactivity system, ensuring all subscribed components update automatically.

>[!WARNING] Null Safety
> Resetting filters to `null` may break dependent logic if filters are expected to remain populated. Validate state before use.
