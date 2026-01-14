**Tags:** #event-handling, #vuejs, #timeline-filtering, #non-intrusive-ui, #event-prevention, #user-experience
**Created:** 2026-01-13
**Type:** code-notes

# TIMELINE_FILTERING_ENHANCEMENT

## Summary

```
Enhances timeline filtering in a Vue.js application to enable global, non-intrusive filtering across stages without triggering unintended navigation.
```

## Details

> This enhancement modifies the `TopTimeline` component to act as a global filter, allowing users to interact with a timeline slider, markers, or time scale selector while remaining on their current stage. The implementation prevents event bubbling and stage navigation by using `stopPropagation()` and selectively emitting events, ensuring only filtering actions occur. The `WorkflowPage` component updates content filters based on user interactions, maintaining the current stage in the URL.

## Key Functions

### ``onClick` (TopTimeline.vue)`

Detects interactive elements and prevents stage switching by returning early for filtered actions.

### ``startDrag` (TopTimeline.vue)`

Uses `stopPropagation()` to prevent event bubbling during slider drags.

### ``selectMarker` (TopTimeline.vue)`

Emits filtered events (`marker-selected`, `time-filter-changed`) without triggering a stage switch.

### ``handleTimelinePositionChange` (WorkflowPage.vue)`

Updates card filters based on slider or marker interactions.

### ``handleTimelineFilterChange` (WorkflowPage.vue)`

Applies filters to content when markers are clicked.

### ``handleTimeScaleChange` (TopTimeline.vue)`

Adjusts timeline view without triggering stage navigation.

## Usage

1. **Drag Slider**: Adjusts the timeline filter by year without switching stages.
2. **Click Markers**: Filters content to a specific event year/marker without navigation.
3. **Change Time Scale**: Adjusts the timeline view (e.g., Days → Years) without altering the current stage.
4. **Click Empty Timeline**: Deliberately navigates to the Timeline stage (only for background clicks).

## Dependencies

> `Vue.js (3.x)`
> `Vuex (for state management if applicable)`
> `custom Vue components (`TopTimeline.vue``
> ``WorkflowPage.vue`).`

## Related

- [[Vue]]
- [[Non-Intrusive UI Patterns]]
- [[Event Propagation Best Practices]]

>[!INFO] Event Prevention Strategy
> The use of `stopPropagation()` ensures that interactive elements (sliders, markers) do not trigger unintended parent handlers, like stage navigation. This is critical for maintaining the non-intrusive nature of the filter.

>[!WARNING] Background Click Navigation
> Users must explicitly click empty timeline areas to navigate to the Timeline stage. Misclicking interactive elements will only filter content, not switch stages.
