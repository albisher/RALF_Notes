**Tags:** #procedural-generation, #map-creation, #voronoi-diagram, #noise-based-terrain, #biome-assignment, #browser-automation, #api-integration, #javascript-backend, #python-backend
**Created:** 2026-01-13
**Type:** research

# SUMMARY

## Summary

```
Explores Azgaar’s map generation methodology to replicate its random map creation in a custom application, detailing technical approaches and implementation phases.
```

## Details

> This document analyzes Azgaar’s Fantasy Map Generator, which employs a **Voronoi diagram-based approach** combined with **Perlin/Simplex noise for terrain elevation**, followed by biome assignment, river generation, and additional features like states, cities, and roads. The research identifies two primary implementation strategies: **browser automation** (using Playwright/Puppeteer to fetch and process Azgaar’s exported JSON) and a **native implementation** (directly generating maps using libraries like `scipy.spatial.Voronoi` and `noise`). The existing system already supports Azgaar’s JSON format, simplifying integration. The plan is divided into **Phase 1 (1–2 weeks)** for quick integration via automation and **Phase 2 (4–6 weeks)** for a scalable native solution.

## Key Functions

### ``process_map_data.py``

Converts Azgaar’s JSON output into internal map structures.

### ``map_generation_research.md``

Detailed technical breakdown of Azgaar’s algorithm.

### ``implementation_plan.md``

Step-by-step roadmap for both phases.

### ``browser_automation_example.py``

Script to automate Azgaar’s map generation via Playwright.

### ``native_generation_example.py``

Example of implementing Voronoi/Perlin noise-based generation.

### ``MapGeneratorBox` (Phase 1)`

Core backend component for map generation.

### ``api/map_generation_bp.py``

REST API endpoint for generating maps.

### ``useMapGeneration.js``

Frontend composable for UI integration.

### ``MapGenerator.vue``

Vue.js component for visualizing/managing maps.

## Usage

1. **For Phase 1 (Browser Automation)**:
   - Use `research/code_examples/browser_automation_example.py` to automate Azgaar’s map generation.
   - Call the `/api/maps/generate` endpoint with parameters (`seed`, `width`, `height`, `template`).
   - Process the exported JSON via `process_map_data.py`.

2. **For Phase 2 (Native Implementation)**:
   - Implement Voronoi diagram generation using `scipy.spatial.Voronoi`.
   - Apply Perlin noise for heightmaps via the `noise` library.
   - Assign biomes based on height/temperature/precipitation.
   - Export maps in Azgaar-compatible JSON format.

## Dependencies

> `Playwright`
> `Puppeteer (for browser automation)`
> ``scipy``
> ``numpy``
> ``noise``
> ``shapely` (for native implementation)`
> ``python-playwright` (optional for Playwright in Python).`

## Related

- [[`map_generation_research]]
- [[`implementation_plan]]
- [[README]]

>[!INFO] Key Tradeoff
> Browser automation (Phase 1) is faster but relies on an external service (Azgaar). Native implementation (Phase 2) offers full control but requires more development effort.

>[!WARNING] External Dependency Risk
> If Azgaar’s website changes its URL structure or export format, browser automation may break. Validate JSON consistency with `process_map_data.py` during testing.

>[!INFO] Existing System Compatibility
> The backend’s `process_map_data.py` and map visualization components are pre-configured for Azgaar’s JSON schema, reducing integration complexity.
