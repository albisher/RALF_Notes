**Tags:** #StateManagement, #VueJS, #3DVisualization, #PlotManagement, #CameraControl
**Created:** 2026-01-13
**Type:** code-notes

# VisualizationState

## Summary

```
Manages visualization and plotting state for a 3D/2D application, including camera, zoom, and data tracking.
```

## Details

> `VisualizationState` is a class that encapsulates all state related to visualization, plots, camera controls, and zoom functionality. It follows a single-responsibility principle, focusing solely on managing visualization data, plot initialization, camera states, zoom mechanics, and time-travel history. The class provides default state initialization via `getDefaultState()` and integrates with Vue.js via `data()`. It includes methods for initializing plot containers (`plot3DBox`, `plot2DBox`, `zoomBox`) and handles throttled updates for plots.
> 
> Key components include:
> - **Plot Management**: Tracks initialized plots, update intervals, and throttling.
> - **Camera & Tracking**: Stores camera states per plot and manages tracked objects.
> - **Zoom Logic**: Implements zoom functionality with a flag to prevent feedback loops.
> - **Time Travel**: Supports historical data storage for time-based simulations.
> - **Modal & Filtering**: Manages details modals and log filters for interactive elements.

## Key Functions

### ``getDefaultState()``

Returns a default state object for visualization components.

### ``data()``

Vue.js-compatible method returning the default state.

### ``initializePlotBoxes()``

Sets up plot containers (`plot3DBox`, `plot2DBox`, `zoomBox`) globally and in the Vue instance.

## Usage

1. Initialize the state by calling `VisualizationState.getDefaultState()` to get a default object.
2. Use `VisualizationState.data()` in a Vue component to inject the state into Vue’s reactivity system.
3. Call `initializePlotBoxes()` with Vue instance and plot container references to bind the state to plot elements.
4. Update plot data via state properties (e.g., `visualizationData`) and trigger updates with throttled intervals.

## Dependencies

> `Vue.js (for reactivity)`
> `WebGL/Three.js (for 3D rendering)`
> `and custom plot-related classes (`Plot3DBox``
> ``Plot2DBox``
> ``ZoomBox`).`

## Related

- [[VisualizationStateUsage]]
- [[Plot3DBox]]
- [[ZoomBox]]

>[!INFO] State Throttling
> Plot updates are throttled to `200ms` via `plotUpdateThrottle` to avoid excessive rendering. Adjust this value if performance degrades.

>[!WARNING] Global Window References
> Plot boxes (`plot3DBox`, `plot2DBox`) are exposed globally via `window` in `initializePlotBoxes()`. Avoid unintended global pollution by scoping these references if possible.
