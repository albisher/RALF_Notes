**Tags:** #vue-composable, #map-generation, #box-orchestration, #asynchronous-operations, #error-handling
**Created:** 2026-01-13
**Type:** code-notes

# useMapGeneration

## Summary

```
A Vue.js composable for generating map data using box-based terrain and heightmap generation systems.
```

## Details

> This composable provides asynchronous map generation functionality through a `boxOrchestrator` instance. It supports terrain generation, heightmap creation for Voronoi cells, and cell hashing/peak selection. The system includes fallback mechanisms for error cases and state tracking for generation progress. It uses a modular approach with external generators (`WorldTypeTerrainGeneratorBox`, `WorldTypeHeightmapGeneratorBox`) and utility functions (`HashBasedHeightmapUtils`).
> 
> Key logic involves:
> 1. Validating the `boxOrchestrator` before execution.
> 2. Handling default values for optional parameters (e.g., `width`, `height`).
> 3. Implementing error logging via a `logger` utility.
> 4. Managing state (`generatingMap`, `mapGenerationError`) to track operations.
> 5. Fallback logic for missing orchestrator dependencies.

## Key Functions

### ``generateMap``

Creates terrain data for a world using box-based generation.

### ``generateHeightmap``

Produces height values for Voronoi cells based on cell centers.

### ``hashForCell``

Generates a hash for a cell using either the orchestrator or a simple fallback.

### ``selectPeaksFromHash``

Selects peak indices from a hash-based representation.

### ``simpleHash``

Private fallback hash function (not imported).

## Usage

```javascript
import { useMapGeneration } from 'composables/useMapGeneration';

const { generateMap, generateHeightmap, hashForCell, selectPeaksFromHash } = useMapGeneration(boxOrchestrator);

// Example usage:
const mapData = await generateMap('world123', 'planet', { width: 256 });
const heights = await generateHeightmap('world123', 'planet', [{ i: 0, p: [10, 10] }]);
```

## Dependencies

> ``vue``
> ``logger` (from `../utils/logger.js`)`
> ``simpleHash`/`simplePeakSelection` (internal fallbacks).`

## Related

- [[`Box Orchestration System`]]
- [[`World Generation Utilities`]]
- [[`Logger Module`]]

>[!INFO] Error Handling
> The composable logs errors via `logger.error` and provides fallback mechanisms (e.g., `simpleHash`) when the orchestrator fails. Always check `mapGenerationError` for failure states.


>[!WARNING] State Management
> `generatingMap` is set to `true` during operations to prevent concurrent executions. Ensure UI components handle this state to avoid UI glitches.
