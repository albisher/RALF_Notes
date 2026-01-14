**Tags:** #map-generation, #enhancement-boxes, #backend-integration, #ui-testing, #terrain-generation, #box-architecture
**Created:** 2026-01-13
**Type:** documentation

# 20251209-HONEST_ANALYSIS_REPORT

## Summary

```
Analyzes missing execution of enhancement boxes in map generation workflows, identifying bypassed backend pipelines and incomplete integration in UI preview paths.
```

## Details

> The report examines why world-type map generation lacks enhancement features despite functional backend box creation. The core issue stems from two paths: a **Quick Preview** route that skips the enhanced `map_generator.py` pipeline, and an unverified **Full Map** route that may also fail to execute enhancements. While all boxes are implemented in `map_generator.py`, the Quick Preview API endpoints (`/generation/terrain`, `/generation/cells`, `/generation/heightmap`) bypass them, resulting in flat, basic Voronoi/heightmap outputs. The Full Map route (`/api/maps/generate`) requires verification to confirm it uses the enhanced pipeline.

## Key Functions

### ``services/map-generator/engine/map_generator.py``

Core pipeline containing enhancement boxes (e.g., `HydraulicErosionBox`, `SimplexNoiseBox`).

### ``ui-beta/src/pages/MapGeneratorPage.vue``

UI component calling Quick Preview endpoints (`generateQuickPreview()`).

### ``services/map-generator/api.py``

Backend API endpoint for `/api/maps/generate` (needs verification).

### ``backend/boxes/generators/*_box.py``

Individual enhancement modules (e.g., `HillshadingBox`, `WorldTypeBoxSelector`).

## Usage

To resolve this, integrate enhancement boxes into Quick Preview endpoints (Option A/B/C) or ensure `/api/maps/generate` correctly invokes `map_generator.py`. Test both paths with enhanced features enabled.

## Dependencies

> ``services/map-generator/engine/map_generator.py``
> ``backend/boxes/generators/*``
> ``ui-beta/src/pages/MapGeneratorPage.vue``
> ``services/map-generator/api.py``

## Related

- [[20251209-map-generator-engine-analysis]]
- [[20251209-ui-test-screenshots]]

>[!INFO] Quick Preview Limitation
> The current Quick Preview route bypasses `map_generator.py`, omitting all enhancement boxes. Fixing requires either:
> - Updating endpoints to call `map_generator.py` (Option B), or
> - Adding enhancement logic to individual endpoints (Option A).
>

>[!WARNING] Silent Pipeline Failure
> The Full Map route (`/api/maps/generate`) may silently fail to execute enhancements if backend logs show no box calls. Verify logs and ensure `map_generator.py` is invoked.
