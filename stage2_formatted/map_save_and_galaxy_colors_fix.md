**Tags:** #map-save, #galaxy-colors, #event-handling, #world-type-detection, #color-mapping, #ui-component, #backend-integration
**Created:** 2026-01-13
**Type:** code-fix

# map_save_and_galaxy_colors_fix

## Summary

```
Fixes issues with map save reloading and galaxy-specific color rendering in a game UI system.
```

## Details

> This code file addresses two critical bugs: **1)** Map save updates not triggering reloads in `WorldMap2D`/`TopTimelineMap` components due to missing worldId validation, and **2)** Galaxy maps incorrectly displaying planet biome colors (e.g., green land/blue water) instead of galaxy-themed colors (void space, nebula, star clusters). The fix involves:
> - **Event handler validation** to ensure correct world reloads post-save.
> - **Dynamic color mapping** in `MapRenderBox` based on detected `world_type` (e.g., `void`, `nebula`), with fallback logic for legacy planet biomes.
> - **Backend integration** in `map_generator.py` to store `world_type` in map metadata.

## Key Functions

### ``handleMapUploaded``

Validates `worldId` before reloading map data.

### ``worldType detection``

Checks `mapData.info.world_type`, `world_context.world_type`, or `mapData.world_type` for galaxy/space color logic.

### ``_adjustColorBrightness()``

Modifies color intensity based on height/energy for galaxy regions.

### ``MapRenderBox` color palette`

Galaxy-specific colors (`void`, `nebula`, `star_cluster`) vs. planet colors.

## Usage

1. **Save Fix**: After saving a map, the UI now checks `event.detail.worldId` against `props.worldId` to reload only relevant maps.
2. **Color Fix**: Galaxy maps render with space-themed colors if `world_type` (e.g., `"galaxy"`) is detected in map metadata. Planet biomes retain legacy colors as fallback.

## Dependencies

> ``ui-beta/src/components/common/WorldMap2D.vue``
> ``ui-beta/src/components/common/TopTimelineMap.vue``
> ``ui-beta/src/boxes/common/map_render_box.js``
> ``services/map-generator/engine/map_generator.py``
> `React/Vue.js event system.`

## Related

- [[`map_generator]]
- [[`WorldMap2D]]
- [[`map_render_box]]

>[!INFO] **World Type Fallback**
> If `world_type` is missing, the code defaults to checking `world_context.world_type` or `mapData.world_type` for galaxy detection. This ensures backward compatibility.

>[!WARNING] **Biome Name Mismatch**
> Planet biomes (e.g., `"sea"`) in galaxy maps will still render with galaxy colors due to the fallback logic. Future work could standardize biome names per world type.
