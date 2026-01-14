**Tags:** #deterministic-generation, #hash-based, #heightmap-processing, #world-generation, #utilities-box
**Created:** 2026-01-13
**Type:** code-notes

# hash_based_heightmap_utils_box

## Summary

```
A utility box for deterministic hash-based operations in heightmap generation systems.
```

## Details

> This module provides reusable hash-based functions for generating, assigning heights, and selecting peaks from a base hash in a world-type heightmap generator. It relies on a `HashGeneratorMasterBox` for core hashing logic, ensuring consistency across operations. The class handles three primary operations: generating cell-specific hashes, converting hashes to height values within a specified range, and deterministically selecting peak cell indices based on a base hash.

## Key Functions

### `HashBasedHeightmapUtilsBox`

Main utility class encapsulating all hash-based heightmap operations.

### `execute`

Routes input operations to appropriate methods (`hash_for_cell`, `assign_height_from_hash`, `select_peaks_from_hash`).

### `hash_for_cell`

Combines a base hash and cell ID to generate a SHA-256 hash for the cell.

### `assign_height_from_hash`

Maps a cell hash to a height value within a given min/max range using a fallback linear interpolation if the primary method fails.

### `select_peaks_from_hash`

Deterministically selects peak cell indices by generating hashes for each peak attempt and deriving indices from them.

## Usage

1. Initialize `HashBasedHeightmapUtilsBox` and attach it to a heightmap generator pipeline.
2. Call `execute` with an operation type (`"hash_for_cell"`, `"assign_height_from_hash"`, or `"select_peaks_from_hash"`) and relevant parameters.
3. Retrieve results (e.g., `{"hash": "..."}`, `{"height": 1.23}`, or `{"peak_indices": [1, 3, 7]}`).

## Dependencies

> ``HashGeneratorMasterBox``
> ``Box``
> ``BoxInput``
> ``BoxOutput` (from `..core.box_interface` and `.hash_generator_master_box`).`

## Related

- [[`HashGeneratorMasterBox`]]
- [[`Box`]]
- [[`BoxInput`]]
- [[`BoxOutput`]]

>[!INFO] Fallback Mechanism
> If the `HashGeneratorMasterBox` fails, the code uses a direct SHA-256 hash or linear interpolation for `assign_height_from_hash`/`select_peaks_from_hash`, ensuring robustness.

>[!WARNING] Precision Limits
> `assign_height_from_hash` truncates the hash to 16 hex digits for integer conversion, risking precision loss if the hash is shorter. Always validate hash length before truncation.
