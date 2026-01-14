**Tags:** #architecture, #map-generation, #procedural-generation, #vue-components
**Created:** 2026-01-13
**Type:** architecture-diagram

# map-generator-architecture

## Summary

```
Designs a modular system for generating and integrating procedural maps with climate, biomes, and city placements.
```

## Details

> This architecture defines a **box-based workflow** for generating a map using Vue.js components. The system begins with user inputs in `MapGeneratorPage.vue`, which feeds parameters into `MapGenerationOrchestratorBox`. This orchestrator delegates tasks to specialized boxes: `HeightmapGenerationBox` creates terrain data, `BiomeAssignmentBox` assigns biome types based on terrain, and `CityPlacementBox` places cities. The `MapAssemblyBox` merges these components into a structured Azgaar-format map. Finally, `MapStoryIntegrationBox` links generated cities to a story system via `CardsAPIBox`, `TimelinesAPIBox`, and `WorldsAPIBox`, producing location cards and event timelines. The diagram also outlines dependencies between boxes and the final map’s data structure, including coordinates, vertices, and biome definitions.

## Key Functions

### `MapGeneratorPage.vue`

UI wrapper for user inputs (seed, dimensions, settings).

### `MapGenerationOrchestratorBox`

Central coordinator for map generation workflow.

### `HeightmapGenerationBox`

Produces a `Float32Array` heightmap from inputs.

### `BiomeAssignmentBox`

Maps terrain cells to biome indices using height data.

### `CityPlacementBox`

Places cities based on biome/terrain criteria.

### `MapAssemblyBox`

Combines heightmap, biomes, and cities into Azgaar-format output.

### `MapStoryIntegrationBox`

Converts cities into location cards and timeline events.

### `MapPreview.vue`

Visualizes the rendered map via `MapRenderBox`.

### `CardsAPIBox`

Handles location card creation for story integration.

### `TimelinesAPIBox`

Links events to coordinates in the story system.

## Usage

1. Users input parameters in `MapGeneratorForm.vue`.
2. The orchestrator triggers specialized boxes (`HeightmapGenerationBox`, `BiomeAssignmentBox`, etc.).
3. Assembled map data is rendered in `MapPreview.vue` and exported as Azgaar format.
4. Story integration via `MapStoryIntegrationBox` generates location cards and timeline events.

## Dependencies

> `Vue.js (frontend framework)`
> `Azgaar map format (output structure)`
> `custom procedural generation libraries (heightmap/biome algorithms)`
> `API wrappers for story integration (`CardsAPI``
> ``TimelinesAPI`).`

## Related

- [[Procedural-Generation-Guide]]
- [[Azgaar-Map-Format-Spec]]
- [[Vue-Component-Library]]

>[!INFO] **Modularity**
> Each box operates independently, allowing easy swapping of algorithms (e.g., replace heightmap generation with a noise-based method).

>[!WARNING] **Data Validation**
> The `MapAssemblyBox` must validate inputs (e.g., biome indices must match predefined lists) to avoid runtime errors.

>[!INFO] **Story Integration**
> Coordinates from the map must align with the story system’s coordinate system (e.g., lat/lon) to ensure accurate linking.
