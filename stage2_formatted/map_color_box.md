**Tags:** #color-palette, #world-generation, #game-design, #visual-styling, #procedural-generation
**Created:** 2026-01-13
**Type:** code-notes

# map_color_box

## Summary

```
Assigns dynamic colors to map cells based on world type and height for visual representation.
```

## Details

> This module (`MapColorBox`) extends a base `Box` class to define a system for generating color gradients and backgrounds for map cells across various world types. It initializes predefined color palettes for each world type (e.g., Terrestrial, Space, Exotic) and provides methods to retrieve colors for specific operations like height-based gradients or background colors. The `_buildColorPalettes()` method constructs a structured object mapping world types to their respective background colors (`bg`) and gradient ramps (`ramp`), which define transitions between colors (e.g., deep water to land). The `_normalizeWorldType()` method standardizes input world type names to match keys in the palette object.

## Key Functions

### ``constructor()``

Initializes the `MapColorBox` with a versioned configuration and precomputes color palettes for all supported world types.

### ``_buildColorPalettes()``

Private method that populates the `WORLD_COLOR_PALETTES` object with color schemes for each world type.

### ``_normalizeWorldType(worldType)``

Converts input world type strings (e.g., "Mars" or "terran") into a standardized key (e.g., "Mars") for palette lookup.

## Usage

1. **Instantiation**: Create an instance of `MapColorBox` to access predefined color palettes.
2. **Color Retrieval**: Use methods like `get_color_for_height` or `get_background_color` (not explicitly implemented here) to fetch colors based on input parameters (e.g., `worldType`, `height`).
3. **Input Validation**: The constructor validates input schema (e.g., `worldType` must be a string) via `inputSchema`.

## Dependencies

> ``../core/box_interface.js` (Box class and related utilities like `BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`).`

## Related

- [[Space Pearl Team Documentation: Box System]]
- [[Procedural World Generation Guide]]

>[!INFO] Palette Design
> Color ramps are designed to reflect environmental realism (e.g., deep water → land gradients) or thematic cohesion (e.g., cyberpunk cities use neon pink/green). The `bg` value sets the base color for map backgrounds.

>[!WARNING] Normalization Edge Cases
> `_normalizeWorldType()` defaults to "Planet" if input is empty or invalid. Override this behavior for custom world types by extending the method or adding additional checks.
