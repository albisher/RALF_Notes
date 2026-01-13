**Tags:** #VueJS, #Plotly, #3DVisualization, #SimulationUI, #InteractivePlot, #DataVisualization, #TimeSlider, #Component
**Created:** 2026-01-13
**Type:** code-notes

# visualization-view-component

## Summary

```
A Vue.js component for rendering interactive 2D/3D data visualizations with time-based controls for simulation views.
```

## Details

> This component (`VisualizationViewComponent`) serves as the main UI for displaying simulation data through a quad-view arrangement (2D Top/Front/Side and 3D Isometric) using Plotly.js. It includes a time slider for dynamic time travel, status indicators for recording/paused states, and a unified legend dynamically populated with active simulation entities (e.g., drones). The template uses Vue’s reactivity to emit events (e.g., `time-slider-change`, `exit-time-travel`) for parent components to handle interactions.
> 
> The component’s template is split into three main sections:
> 1. **Time Slider**: Adjusts simulation time via a range input, with live/pause buttons tied to `timeTravelMode` and `status.running`.
> 2. **Viewport Grid**: Contains four Plotly plots (2D views + 3D) rendered in distinct containers (`plot-top`, `plot-front`, etc.).
> 3. **Legend**: Dynamically renders drone spawns via a `v-for` loop (incomplete snippet shown).

## Key Functions

### ``formatTime()``

Formats numerical time values into human-readable strings (e.g., "HH:MM:SS").

### ``currentView === 'list'``

Conditional rendering logic for the time slider and grid (likely tied to a parent component’s state).

### ``@input` event handlers`

Emits time updates and mode changes to parent components.

### ``v-for` loop (incomplete)`

Dynamically renders legend items (e.g., drone icons/legends) based on `currentView` data.

## Usage

1. **Mounting**: Include in a parent Vue component via `<VisualizationViewComponent />`.
2. **Props**: Pass props like `currentView`, `currentTime`, `maxSimTime`, `status`, and `timeTravelMode`.
3. **Events**: Listen for emitted events (e.g., `time-slider-change`) to update parent logic.
4. **Plotly Integration**: Ensure Plotly charts are initialized in `id="plot-top"`, `id="plot-front"`, etc., with data provided via props.

## Dependencies

> `Plotly.js (for rendering interactive charts)`
> `Vue.js (for reactivity and templating)`
> `Vuex/Pinia (likely for state management of `currentTime``
> ``maxSimTime``
> ``status``
> `etc.).`

## Related

- [[visualization-data-provider]]
- [[time-slider-component]]
- [[simulation-status-manager]]

>[!INFO] Time Slider Logic
> The slider’s `maxSimTime` defaults to `100` if not provided, but should dynamically reflect the simulation’s actual duration. Ensure `maxSimTime` is passed as a prop to avoid hardcoded values.

>[!WARNING] Plotly Initialization
> Missing initialization code for Plotly charts (e.g., `Plotly.newPlot()`) in the template. The `id` attributes (`plot-top`, etc.) must be paired with data objects passed via props to render visualizations.
