**Tags:** #statistical-analysis, #world-generation, #visual-rendering, #validation-failure, #data-mismatch, #height-thresholds, #map-validation
**Created:** 2026-01-13
**Type:** documentation

# ANALYSIS_AND_COMPARISON

## Summary

```
Analyzes discrepancies between generated world types and expected statistical/visual criteria, highlighting critical failures in land ratio, clustering, geometry, and background color rendering.
```

## Details

> This document compares four world types (Planet, Galaxy, Cloud World, Space Station) against predefined `WORLD_EXPECTATIONS`, revealing systematic failures in statistical accuracy, visual representation, and background color application. All tested maps exhibit 100% land statistics despite varying expected ratios, with visuals showing empty blue/green backgrounds instead of intended patterns (e.g., spirals for galaxies). Root causes include misaligned height thresholds for land classification, incorrect rendering logic, and improper data flow between generators and viewers.

## Key Functions

### ``map_generator.py``

Generates world data but misclassifies all cells as "land" due to flawed height thresholds.

### ``MapValidationBox``

Calculates statistics but does not align with visual rendering thresholds.

### ``WorldMap2D.vue``

Renders maps as empty backgrounds due to incorrect data processing or zoom issues.

### ``WORLD_EXPECTATIONS``

Defines target metrics (land ratio, clustering, geometry, background color) for validation.

## Usage

To resolve issues:
1. **Adjust thresholds**: Modify height classification in `map_generator.py` (e.g., increase threshold from 0.0 to 0.2).
2. **Validate rendering**: Inspect `WorldMap2D.vue` for data-passing errors or zoom-level mismatches.
3. **Debug colors**: Verify background color logic in rendering pipelines (e.g., `WorldMap2D.vue` or `MapValidationBox`).

## Dependencies

> ``map_generator.py``
> ``MapValidationBox``
> ``WorldMap2D.vue``
> ``WORLD_EXPECTATIONS` (internal data structure)`
> `statistical libraries (e.g.`
> `NumPy/Pandas for analysis).`

## Related

- [[`WORLD_EXPECTATIONS]]
- [[`MapValidationGuide]]
- [[`RenderingDebugLog]]

>[!INFO] Critical Threshold Issue
> The `height_threshold` in `map_generator.py` (likely set to `0.0`) forces all cells to classify as "land," overriding expected ratios. Increasing this threshold (e.g., `0.2`) should align statistics with visuals.

>[!WARNING] Visual Data Silo
> Separation between statistical calculations (`MapValidationBox`) and rendering (`WorldMap2D.vue`) may cause mismatches. Ensure both systems use identical data formats (e.g., cell height values).

>[!INFO] Background Color Override
> The blue background in all maps suggests a color override in the rendering layer. Check for hardcoded colors in `WorldMap2D.vue` or `MapValidationBox` logic.
