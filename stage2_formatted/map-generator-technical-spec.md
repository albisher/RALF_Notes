**Tags:** #procedural-generation, #biome-algorithms, #heightmap-noise, #box-architecture, #game-mapping
**Created:** 2026-01-13
**Type:** documentation

# map-generator-technical-spec

## Summary

```
Specifies a procedural map generator using Perlin/Simplex noise for terrain and biome-based city placement via the Box architecture pattern.
```

## Details

> This document outlines a technical specification for a map generator leveraging Azgaar’s algorithms, employing the Box architecture pattern. The system uses **Perlin/Simplex noise** to create heightmaps with configurable parameters (e.g., seed, octaves, persistence), followed by **biome assignment** based on elevation, temperature, and precipitation rules. Cities are placed probabilistically using terrain scoring, prioritizing flat land near water and preferred biomes. The implementation is modularized into a `HeightmapGenerationBox`, supporting parallel execution and customizable operations.

## Key Functions

### ``generateHeightmap(width, height, seed, noiseScale, octaves, persistence)``

Creates a noise-based heightmap array.

### ``assignBiome(height, temperature, precipitation)``

Determines biome classification using predefined rules.

### ``calculateCityScore(cell, heightmap, cells)``

Scores cells for city placement based on elevation, biome, and terrain roughness.

### ``placeCities(cells, numCities, minDistance)``

Places cities by sorting cells by score and enforcing minimum distance constraints.

### ``HeightmapGenerationBox``

Core class handling noise generation, template application, and customization via Box architecture.

## Usage

1. Initialize `HeightmapGenerationBox` with Box metadata.
2. Call `_executeInternal` with an operation (`generate`, `applyTemplate`, or `customize`) and parameters.
3. Use generated heightmaps/biomes to place cities via `placeCities` and `calculateCityScore`.

## Dependencies

> ``SimplexNoise` (for procedural noise generation)`
> ``Box` architecture pattern (for modular execution)`
> `and custom utility functions (e.g.`
> ``calculateDistance``
> ``generateCityName`).`

## Related

- [[Map-Generator-Implementation]]
- [[Biome-Terrain-Database]]
- [[Box-Architecture-Guide]]

>[!INFO] **Noise Initialization**
> Ensure `SimplexNoise` is properly initialized with a seed for reproducibility. The `seed` parameter controls randomness in heightmap generation.


>[!WARNING] **Biome Fallback**
> The `assignBiome` function defaults to `'ocean'` if no matching rules are found. Override this logic if waterless biomes (e.g., desert) should be excluded entirely.
