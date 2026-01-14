**Tags:** #procedural-generation, #space-simulation, #hash-based-algorithms, #astronautics
**Created:** 2026-01-13
**Type:** code-library

# other_world_types

## Summary

```
Generates procedural layouts for space structures (space stations, ships, asteroids) using deterministic hashing and modular noise.
```

## Details

> This module implements deterministic algorithms to generate spatial layouts for "other worlds" (space stations, ships, asteroids) based on a base hash input. It uses modular grid-based approaches for stations and ships, and noise-based irregular shapes for asteroids. Each structure assigns "deck levels" (0.0–1.0) to represent functional zones (e.g., core systems, habitation, docking) via hash-derived probabilities. The `generate_noise_fast()` function (not shown) is called for asteroid generation, which adds organic irregularity.

## Key Functions

### `generate_space_station_fast`

Creates a modular grid-based space station layout with configurable width/height, using a base hash to determine module types (habitation, industrial, core, etc.) and their deck levels.

### `generate_space_ship_fast`

Produces a segmented ship layout with horizontal sections (bow, crew, cargo, engine, core), where each section’s deck levels vary based on its position and type.

### `generate_asteroid_fast`

Generates an irregular asteroid surface using noise-based distance calculations from a central point, with crater generation via additional hashing.

## Usage

```python
# Example: Generate a space station layout
station_map = generate_space_station_fast("seed123456", width=300, height=200)

# Example: Generate a ship layout
ship_map = generate_space_ship_fast("ship_seed", width=400, height=100)

# Example: Generate an asteroid layout
asteroid_map = generate_asteroid_fast("asteroid_seed", width=250, height=250)
```
Customize `width`/`height` and provide a base hash string for reproducibility.

## Dependencies

> `numpy`
> `hashlib`
> `math`

## Related

- [[OTHER_WORLD_TYPES_RESEARCH]]
- [[PROCEDURAL_GEN_ALGORITHMS]]

>[!INFO] **Hash-Dependent Reproducibility**
> The base hash determines module placement, section types, and crater positions, ensuring deterministic generation across runs.

>[!WARNING] **Noise Dependency**
> Asteroid generation relies on an external `generate_noise_fast()` function (not shown). If this function changes, asteroid shapes may vary unpredictably.
