**Tags:** #hash-generation, #storytelling, #deterministic-seeding, #space-time-coordinates, #narrative-structure
**Created:** 2026-01-13
**Type:** code-library

# demo-hash-generation

## Summary

```
Generates deterministic story elements using SHA-256 hashing for space-time linking in narrative systems.
```

## Details

> This script implements a `SpacePearlHashGenerator` class that creates consistent, reproducible story elements (characters, locations, plots) from input seeds. It uses SHA-256 hashing to derive deterministic outputs across multiple dimensions (personality, space coordinates, time coordinates), enabling multi-dimensional story mapping. The system links elements spatially and temporally by calculating distances and time relationships between generated entities.

## Key Functions

### `SpacePearlHashGenerator`

Core class managing hash generation and story element creation.

### ``generate_hash(seed, dimension)``

Creates deterministic hashes for story components.

### ``hash_to_coordinates(hash_value)``

Converts hash prefixes to 3D spatial coordinates.

### ``hash_to_time_coordinates(hash_value)``

Extracts time components (year, month, etc.) from hash.

### ``generate_character_from_hash(seed)``

Produces complete character profiles with personality traits.

### ``generate_location_from_hash(seed)``

Creates locations with spatial and temporal attributes.

### ``generate_story_from_hash(seed)``

Builds full stories with interconnected characters/locations.

### ``link_space_time(story_data)``

Computes spatial and temporal relationships between story elements.

### `_hash_to_traits(hash_value)`

Maps hash segments to personality traits (e.g., "Brave", "Wise").

### `_hash_to_motivation(hash_value)`

Derives character motivations from hash.

### `_hash_to_conflict(hash_value)`

Extracts character arcs/conflicts.

### `_calculate_distance(coords)`

Computes Euclidean distance between 3D coordinates.

### `_calculate_time_difference(time_coords)`

Evaluates temporal differences between entities.

## Usage

```python
generator = SpacePearlHashGenerator()
character = generator.generate_character_from_hash("seed_value")
story = generator.generate_story_from_hash("seed_value")
linked_story = generator.link_space_time(story)
```

## Dependencies

> ``hashlib``
> ``json``
> ``datetime``
> ``typing` (standard Python libraries)`

## Related

- [[Space Pearl Framework]]
- [[Narrative Generation Patterns]]

>[!INFO] Deterministic Outputs
> All generated elements (characters, locations, plots) will produce identical outputs for the same seed, enabling reproducible stories across runs.

>[!WARNING] Hash Collisions
> SHA-256 collisions are astronomically unlikely, but extremely long seeds may still risk minor variations in derived attributes.
