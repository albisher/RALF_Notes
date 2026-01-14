**Tags:** #deprecated, #robot-data, #space-peral, #autonomous-systems, #data-file
**Created:** 2026-01-13
**Type:** code-notes

# cards-data

## Summary

```
Deprecated auto-generated robot data file for Space Peral’s early X-Series robots, structured for reference and future removal.
```

## Details

> This file contains metadata for early Space Peral robots (X1–X4), originally auto-generated from documentation. Each entry includes details like ID, name, type, description, and visual attributes. The data is deprecated and should be fetched dynamically via the database API instead, with filtering for the "Space Peral" world. The file is retained for legacy reference but will be phased out in future updates.

## Key Functions

### ``CARDS_DATA``

Array of robot entries with structured metadata.

### ``robot-X1001``

Drone unit for aerial surveying (X-Series).

### ``robot-X2001``

Orchestrator for task coordination and resource management.

### ``robot-X3001``

Resource finder for mineral/water detection.

### ``robot-X4001``

Agriculture unit for crop cultivation (radiation/soil challenges).

## Usage

To load cards dynamically:
1. Use `BoxOrchestrator` with `CardsAPIBox` to fetch filtered data.
2. Apply `world_id` filter for "Space Peral."
3. Refer to `cardview.html` for implementation examples.

## Dependencies

> ``BoxOrchestrator``
> ``CardsAPIBox``
> ``cardview.html` (external API/database components).`

## Related

- [[Space Peral API Documentation]]
- [[Robot Naming Conventions]]
- [[Future Deprecation Policy]]

>[!INFO] Critical Dependency Warning
> This file is **not production-ready**. Always fetch data via the database API for consistency.

>[!WARNING] Data Integrity Risk
> Some entries (e.g., `X3`) mention operational limitations (e.g., 30-hour cycle issues) that may require validation in real-world use.
