**Tags:** #modular-architecture, #world-simulation, #enhancement-system, #box-based-design, #high-fidelity-visualization, #terrain-generation, #biome-simulation, #physics-based-rendering
**Created:** 2026-01-13
**Type:** documentation

# ENHANCEMENT_BOXES_ARCHITECTURE

## Summary

```
Documentation of a modular box-based enhancement system for high-fidelity world simulation, defining how different world types (planet, galaxy, space station) utilize specific enhancement boxes.
```

## Details

> This architecture implements a **modular box system** where each enhancement (e.g., erosion, tectonic simulation) is encapsulated in reusable Python boxes. The system dynamically selects and executes boxes based on the user-defined `world_type`, ensuring only relevant enhancements are applied. The core principle is **type-specific optimization**, where each world type (e.g., planet, galaxy) uses a curated set of boxes tailored to its needs. The execution order is strictly defined to maintain logical dependencies—for example, erosion runs after heightmap generation but before biome assignment.

## Key Functions

### `WorldTypeBoxSelector`

Maps world types to their respective box sets and enforces execution order.

### `HydraulicErosionBox`

Simulates water flow and erosion for river systems (applies to Planet/Moon with water).

### `TectonicPlateSimulationBox`

Models mountain formation via tectonic plate interactions (Planet-only).

### `MoistureCalculatorBox`

Computes moisture distribution for biome classification (Planet-only).

### `HillshadingBox`

Adds visual depth via lighting calculations (Planet/Moon/Asteroid).

### `LloydsRelaxationBox`

Smooths Voronoi-based terrain by relocating points to centroids (Planet/Space Station/Ship/Cloud World).

## Usage

1. **Initialize**: Load `WorldTypeBoxSelector` with a `world_type` (e.g., `"planet"`).
2. **Execute**: Call selector to fetch and run the appropriate box chain in order.
3. **Integrate**: Hook boxes into the simulation pipeline (e.g., post-heightmap generation for erosion).
4. **Render**: Use `HillshadingBox` outputs in rendering layers (e.g., `WorldMap2D.vue`).

## Dependencies

> ``numpy``
> ``scipy``
> ``pyproj``
> ``matplotlib` (for numerical computations`
> `geospatial math`
> `and visualization utilities).`

## Related

- [[WorldTypeBiomeCalculator]]
- [[SimplexNoiseGenerator]]
- [[VoronoiDiagramGenerator]]

>[!INFO] Execution Order Matters
> Boxes must follow the predefined sequence (e.g., `SimplexNoise` → `LloydsRelaxation` → `TectonicPlateSimulation`). Violating this breaks logical dependencies (e.g., erosion cannot run before height changes).

>[!WARNING] World-Type Locking
> Some boxes (e.g., `GalaxyPointCloud`) are **world-type exclusive**. Incorrectly applying them to a planet will produce visual artifacts or errors. Always validate `world_type` before execution.
