**Tags:** #test_document, #world_generation, #procedural_worlds, #validation, #obsidian_wikilink
**Created:** 2026-01-13
**Type:** test-reference

# WORLD_TYPES_TO_TEST

## Summary

```
Document outlining test cases for procedural world generation types, including expected visual and statistical outcomes.
```

## Details

> This file defines a checklist for testing different world types (e.g., Planet, Galaxy, Space Station) in a procedural generation system. It specifies test URLs, expected visual characteristics, and screenshot requirements. The document references predefined expectations from `WORLD_EXPECTATIONS` for validation, with pending entries awaiting further criteria.

## Key Functions

### `WORLD_EXPECTATIONS`

Defines statistical and visual benchmarks for each world type.

### `Map Validation Box`

Provides expected results for visual and density metrics.

### `Test URL Generator`

Constructs dynamic test links for each world type (e.g., `http://localhost:5174/#map-generator?hash=ew&worldType=[TYPE]&mapType=full`).

## Usage

1. Navigate to the generated URL for each world type.
2. Observe and screenshot the rendered map after ~30-60 seconds.
3. Compare visuals against expected metrics (e.g., land density, clustering).
4. Update `WORLD_EXPECTATIONS` if discrepancies are found.

## Dependencies

> ``WORLD_EXPECTATIONS` (internal data structure)`
> `procedural generation engine (e.g.`
> `React/Next.js frontend)`
> `screenshot tool (e.g.`
> `Puppeteer or browser extension).`

## Related

- [[WORLD_EXPECTATIONS]]
- [[MapValidationBox]]
- [[Procedural Generation Guide]]

>[!INFO] Test URL Construction
> Replace `[TYPE]` with the current world type (e.g., `Planet`) and ensure `hash=ew` matches the input hash for consistency.

>[!WARNING] Pending Types
> **Galaxy, Cloud World, Space Station, Space Ship, Asteroid, Moon** require updated expectations before testing. Verify `WORLD_EXPECTATIONS` updates before proceeding.
