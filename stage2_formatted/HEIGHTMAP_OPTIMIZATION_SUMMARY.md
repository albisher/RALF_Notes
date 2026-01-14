**Tags:** #optimization, #hash-based, #deterministic, #map-generation, #performance-improvement, #algorithm-design
**Created:** 2026-01-13
**Type:** research-summary

# HEIGHTMAP_OPTIMIZATION_SUMMARY

## Summary

```
Explores hash-based optimization for heightmap generation, improving speed and maintaining deterministic relationships between map types.
```

## Details

> This document outlines research on optimizing heightmap generation using hash functions to replace random number generation, reducing complexity from O(n*m) queue propagation to distance-based calculations. The approach maintains deterministic outputs by deriving seeds from a unified `world_hash`, enabling related map variations (e.g., heightmaps, cities) to share a base hash while producing mathematically consistent outputs. The strategy targets a 10-20x single-threaded and 40-160x multi-threaded speedup by eliminating random sampling and propagating queues.

## Key Functions

### ``HashBasedHeightmapUtils.hash_for_cell()``

Generates a hash for a specific cell using a base hash and cell ID.

### ``HashBasedHeightmapUtils.assign_height_from_hash()``

Maps a hash-derived value to a height within a specified range.

### ``HashBasedHeightmapUtils.select_peaks_from_hash()``

Deterministically selects peak positions for heightmap generation.

### ``WorldTypeHeightmapGenerator``

Uses hash-based methods to generate heightmaps, replacing random sampling with distance-based and hash-derived calculations.

### ``generate_world_hash()``

Creates a base hash for world context (name, type, user_id).

### ``generate_related_hash()``

Produces related map-specific hashes (e.g., "heightmap", "cities") from a base hash.

## Usage

1. **Phase 1**: Integrate `world_hash` into `MapGenerator.generate()` and fallback to `input_hash` if unavailable.
2. **Phase 2**: Replace random calls in `WorldTypeHeightmapGenerator` with `HashBasedHeightmapUtils` methods.
3. **Phase 3**: Replace static seeds (e.g., `"seed-height"`) with `generate_related_hash(world_hash, "heightmap")` for consistency.
4. **Testing**: Validate determinism, performance, and related map relationships via tests.

## Dependencies

> ``random` (legacy fallback)`
> ``hashlib` (for hash generation)`
> ``math` (for distance calculations)`
> ``typing` (for type hints)`
> ``services.map-generator.engine` (core generator modules).`

## Related

- [[HEIGHTMAP_OPTIMIZATION_RESEARCH]]
- [[HASH_BASED_RELATED_MAP_GENERATION]]

>[!INFO] **Deterministic Outputs**
> Hash-based generation ensures identical inputs produce identical outputs, critical for reproducibility in procedural generation.

>[!WARNING] **Backward Compatibility**
> Fallback to `input_hash` preserves existing behavior during transition phases. Ensure backward compatibility testing for legacy systems.
