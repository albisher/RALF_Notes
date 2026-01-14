**Tags:** #procedural-generation, #hash-based, #world-building, #game-design, # procedural-maps
**Created:** 2026-01-13
**Type:** code-library

# maps

## Summary

```
Generates deterministic procedural maps using hash inputs for fantasy, space, or other world types.
```

## Details

> This code implements a procedural map generator that converts input strings (or hashes) into structured map metadata. It uses SHA-256 hashing to ensure reproducibility, categorizing world types (e.g., "Planet," "Galaxy") and deriving attributes like size, features, and resolution based on the hash and context. The system dynamically assigns map names, coordinates, heightmaps, biomes, and city parameters using deterministic logic tied to the input hash.

## Key Functions

### `hash_input`

Converts input strings into SHA-256 hex hashes for deterministic generation.

### `generate_map_description`

Orchestrates the full map generation pipeline, combining hash-derived characteristics with world context.

### `_generate_map_characteristics`

Selects size, feature, and resolution based on hash and world category.

### `_generate_map_name`

Constructs a descriptive map name from input hash or world description.

### `_generate_map_coordinates`

(Incomplete in snippet; likely generates spatial coordinates.)

### `_generate_heightmap_params`

(Incomplete; likely defines terrain parameters.)

### `_generate_biome_params`

(Incomplete; likely defines biome distributions.)

### `_generate_city_params`

(Incomplete; likely defines settlement rules.)

## Usage

1. Call `hash_input()` to generate a deterministic hash from input text.
2. Use `generate_map_description()` with the hash and world type (e.g., `"Planet"`) to produce a structured map metadata dictionary.
3. Extract attributes like `map_name`, `resolution`, or `biome_params` for further processing (e.g., rendering or asset generation).

## Dependencies

> `hashlib`
> `json`
> `typing (Python standard libraries)`

## Related

- [[Procedural-Gen-Architecture]]
- [[World-Building-Systems]]

>[!INFO] Contextual Hashing
> The code first checks if the input is already a valid hex hash (64 chars). If not, it converts descriptive text to a hash using `hashlib.sha256`, ensuring consistent results across runs.

>[!WARNING] Incomplete Helper Functions
> The snippet omits `_generate_map_coordinates`, `_generate_heightmap_params`, and `_generate_city_params`—these would need implementation to fully define spatial and thematic details. The current output only includes `map_name` and basic characteristics.
