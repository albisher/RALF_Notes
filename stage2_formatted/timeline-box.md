**Tags:** #timeline-component, #UI-component, #event-management, #data-visualization, #interactive-UI
**Created:** 2026-01-13
**Type:** code-library

# timeline-box

## Summary

```
A modular timeline box system for rendering, interacting, and managing event nodes across three columns: detailed timeline, map visualization, and controls.
```

## Details

> `TimelineBox` is a utility object that consolidates three primary components for timeline visualization:
> 1. **Detailed Timeline View** renders individual nodes using `UIBoxes.timelineNode()`, highlighting the selected node via callback-driven selection.
> 2. **Map Visualization** maps timeline nodes as markers using `UIBoxes.timelineMarker()`, supporting 2D/3D map modes via `mapMode`.
> 3. **Timeline Controls** aggregates actions (add/edit/delete) for event management.
> 4. **Event Form** provides a reusable form for creating/editing events with fields like `name`, `date`, and `keyYear`.
> 
> The system abstracts UI rendering logic, delegating node/marker creation to `UIBoxes` (a dependency) while exposing callbacks for interactivity (e.g., `onSelect`, `onNodeClick`).

## Key Functions

### `detailedTimelineView`

Creates a left-column timeline with node rendering and selection logic.

### `mapVisualization`

Generates map markers from timeline nodes, configurable by `mapMode`.

### `timelineControls`

Centralizes event management callbacks (add/edit/delete).

### `timelineEventForm`

Returns a form structure for event editing with predefined fields.

### `module.exports`

Exports the object for Node.js compatibility.

## Usage

1. Import `TimelineBox` and call its methods:
   ```js
   const { detailedTimelineView, mapVisualization } = TimelineBox;
   const nodes = [...];
   const selectedNode = nodes[0];
   const result = detailedTimelineView(nodes, selectedNode, (node) => console.log(node));
   ```
2. Use returned objects (`result.timelineNodes`) to render components with `UIBoxes`-compatible wrappers.

## Dependencies

> ``UIBoxes` (for `timelineNode`/`timelineMarker` implementations)`
> ``module.exports` (Node.js compatibility).`

## Related

- [[boxes]]
- [[UIBoxes (core UI utilities for timeline rendering).]]

>[!INFO] Fallback Handling
> If `UIBoxes` is undefined, the system falls back to raw `timelineNodes`/`timelineMarkers` without UI rendering.

>[!WARNING] Callback Dependency
> All interactive functions (e.g., `onSelect`) must be provided to enable event handling. Missing callbacks may render UI elements inert.
