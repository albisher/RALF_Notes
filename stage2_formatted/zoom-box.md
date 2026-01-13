**Tags:** #3D-visualization, #zoom-control, #plotly, #asynchronous-operation, #camera-state
**Created:** 2026-01-13
**Type:** code-notes

# zoom-box

## Summary

```
Handles 3D plot zoom operations with async camera state updates and directional zoom logic.
```

## Details

> The `ZoomBox` class manages zoom functionality for 3D Plotly visualizations. It prevents concurrent zoom operations via a lock (`isApplyingZoom`) and delegates zoom logic to an API endpoint (`/api/zoom`). The `applyZoom` method sends a POST request with plot metadata, direction (`in`/`out`), and optional zoom target coordinates, then updates the camera state via `Plotly.relayout`. The `calculateZoomPoint` method computes zoom target coordinates from mouse events relative to the plot element.

## Key Functions

### ``applyZoom``

Initiates zoom via API, updates camera state, and returns updated zoom metrics.

### ``calculateZoomPoint``

Derives zoom target coordinates from mouse position relative to the plot element.

## Usage

```javascript
const zoomBox = new ZoomBox();
await zoomBox.applyZoom('myPlot', 'in', cameraState, { x: 10, y: 20 });
```
Call `applyZoom` with plot ID, zoom direction, and camera state. Optionally pass a target point.

## Dependencies

> `Plotly.js`
> `Fetch API`
> ``window.loggingBox` (custom logging utility).`

## Related

- [[Plotly]]
- [[Camera State API]]
- [[LoggingBox utility]]

>[!INFO] Preventing Overlaps
> `isApplyingZoom` flag ensures only one zoom operation runs at a time, avoiding race conditions.

>[!WARNING] API Error Handling
> Silent logging falls back to `console.error` if `loggingBox` is unavailable. Test error paths explicitly.
