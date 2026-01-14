**Tags:** #statistical-validation, #map-generation, #world-building, #data-analysis, #pillar-based-validation, #BFS-algorithm, #retries-and-fallbacks
**Created:** 2026-01-13
**Type:** documentation

# MAP_VALIDATION_SYSTEM

## Summary

```
Validates map data using statistical and topological checks to ensure generated maps conform to expected world types via three analytical pillars.
```

## Details

> The **Map Validation System** employs **statistical signature validation** to assess map integrity without visual inspection. It evaluates three pillars:
> 1. **Mass Check (Histogram)** – Measures land/empty space distribution via height thresholds.
> 2. **Clustering Check (Topology)** – Uses BFS to determine landmass connectivity (e.g., continents vs. noise).
> 3. **Geometry Check (Spatial)** – Analyzes spatial patterns (e.g., spiral, ring, or bimodal distributions).
> 
> World types define thresholds for each pillar (e.g., *Water World* requires 95% low cells, while *Pangea* demands high clustering). The system integrates into map generation pipelines, retrying failed attempts up to 3 times before allowing invalid maps.

## Key Functions

### ``check_ratio(values, threshold, min_percent, max_percent)``

Validates cell distribution against thresholds.

### ``execute()``

Orchestrates the full validation workflow in `MapValidationBox`.

### ``_build_expectations()``

Populates `WORLD_EXPECTATIONS` with type-specific rules.

### ``_pillar_a_mass_check()``

Computes land/empty ratio via histogram.

### ``_pillar_b_clustering_check()``

Detects landmass clusters via BFS.

### ``_pillar_c_geometry_check()``

Evaluates spatial patterns (e.g., center bias, ring uniformity).

## Usage

1. **Automatic Integration**: Called post-map assembly in `map_generator.py` (step 7).
2. **Standalone Use**: Instantiate `MapValidationBox` with `BoxInput` containing `world_type`, `cells`, and `heights`.
3. **API Endpoint**: `POST /api/generation/validation` returns `valid`/`signature_score` and pillar results.

## Dependencies

> ``backend/boxes/core/box_interface``
> ``backend/boxes/generators/map_validation_box``
> ``services/map-generator/engine/map_generator``
> ``numpy` (for statistical operations)`
> ``networkx` (for BFS-based clustering).`

## Related

- [[`MAP_GENERATION_PIPELINE`]]
- [[`STATISTICAL_SIGNATURES`]]
- [[`TOPOLOGY_ALGORITHMS`]]

>[!INFO] Retry Logic
> If validation fails, the system modifies the seed and retries up to `max_retries` (default: 3). This prevents invalid maps from passing silently.

>[!WARNING] Configurable Thresholds
> `min_percent`/`max_percent` and `signature_score` (e.g., >0.7) are tunable. Adjust for stricter/lenient validation.
