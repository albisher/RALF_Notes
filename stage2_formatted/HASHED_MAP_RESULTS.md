**Tags:** #world-generation, #hash-based, #procedural-worlds, #biome-simulation, #procedural-maps
**Created:** 2026-01-13
**Type:** documentation

# HASHED_MAP_RESULTS

## Summary

```
Generates deterministic procedural world maps using hash-based inputs for fantasy, cloud, and cosmic environments.
```

## Details

> This document outlines a system for generating procedurally defined world maps via hash-based inputs. It uses deterministic parameters derived from input strings to produce consistent world configurations (e.g., cloud worlds, galaxies, or diverse planets). The system applies biome, elevation, and city distribution rules to generate maps with specified resolutions, ensuring reproducibility. The API request body mirrors the generated parameters, allowing seamless integration with a map generator service.

## Key Functions

### `Hash-to-Parameters Mapping`

Converts input strings into deterministic world configurations (e.g., `floating clouds` → `cloud_world`).

### `Biome Simulation`

Applies precipitation and temperature rules to define climate zones (e.g., `0.35` precipitation for cloud worlds).

### `City Placement Logic`

Distributes cities based on water/terrain preferences and minimum distance constraints (e.g., `20 cities` with `prefer_water` enabled).

### `Resolution Handling`

Supports `high`/`ultra` resolutions, adjusting generation time (e.g., `15-120s` for ultra).

### `Seed-Based Reproducibility`

Uses truncated hash prefixes (e.g., `"a4580c8d55c99353"`) to ensure identical outputs for identical inputs.

## Usage

1. Provide an input string (e.g., `"floating cloud platforms"`).
2. Generate a deterministic hash (e.g., `a4580c8d55c99353`).
3. Use the generated parameters in an API request to a map generator:
   ```json
   {
     "seed": "a4580c8d55c99353",
     "resolution": "high",
     ... (other params)
   }
   ```
4. Retrieve the rendered map.

## Dependencies

> ``None` (internal procedural logic; relies on external map generator service for rendering).`

## Related

- [[Procedural World Generator API]]
- [[Biome Simulation Guide]]
- [[Hash-Based Determinism]]

>[!INFO] **Deterministic Outputs**
> Same input hash always produces identical world parameters, enabling consistent testing and sharing of generated worlds.

>[!WARNING] **Resolution Tradeoff**
> Higher resolutions (e.g., `ultra`) increase generation time; preemptively choose resolution based on project needs.

>[!INFO] **Parameter Overrides**
> Customize `city_params` (e.g., `min_distance`) or `biome_params` (e.g., `temperature`) to tailor world aesthetics.
