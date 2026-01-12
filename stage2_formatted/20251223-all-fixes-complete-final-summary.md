**Tags:** #Vue, #Cesium, #Reactivity, #ErrorHandling, #DOMRendering, #FrontendFixes
**Created:** 2026-01-12
**Type:** code-notes

# simulation/frontend/boxes/osm-integ

## Summary

```
Fixes Vue container rendering issues in Cesium 2D/3D viewers and improves error handling for Vue state serialization.
```

## Details

> This snippet focuses on the `osm-integration-box.js` file, which addresses two critical frontend issues:
> 1. **Conditional Rendering Fix**: Replaced `v-if` with `v-show` for Cesium viewer containers to prevent timing issues during initialization, while adding visibility checks via computed styles.
> 2. **Error Handling**: Enhanced error logging to safely capture Vue state properties (e.g., `setupState`, `$data`) to avoid serialization failures when errors occur during command processing or DOM operations.
> 
> The fix ensures containers persist in the DOM (via `v-show`) while dynamically controlling visibility via CSS, improving robustness for dynamic UI elements like Cesium viewers.

## Key Functions

### ``isContainerVisible()``

Checks if a container is visible by verifying both `display !== 'none'` and non-zero dimensions.

### `Error logging enhancements`

Safely captures Vue state properties (e.g., `$data`) to prevent serialization errors during error handling.

## Usage

To apply this fix:
1. Replace `v-if` with `v-show` in relevant Vue components (e.g., `simulation/frontend/components/visualization-view-component.js`).
2. Implement `isContainerVisible()` logic in `osm-integration-box.js` to dynamically check container visibility.
3. Ensure error handling in `simulation/frontend/app-data.js` (e.g., `try-except` blocks) gracefully logs errors without breaking the DOM.

## Dependencies

> `- Vue.js (for reactivity and conditional rendering)
- Cesium.js (for 2D/3D viewer containers)
- Web components (e.g.`
> ``cesium-2d-top-viewer``
> ``cesium-3d-viewer`)`

## Related

- [[visualization-view-component]]
- [[app-data]]
- [[hmrs_simulation_live]]

>[!INFO] Important Note
> The fix prioritizes **DOM persistence** over immediate visibility, using `v-show` to ensure containers exist in the DOM while deferring visibility logic to CSS. This prevents "container not found" errors during initialization.


>[!WARNING] Caution
> Initialization timing may still cause minor delays if the container is hidden (`display: none`). Test edge cases where `osmViewEnabled` is dynamically toggled to ensure smooth transitions.
