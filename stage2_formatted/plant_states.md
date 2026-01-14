**Tags:** #botanical_states, #plant_health, #state_management
**Created:** 2026-01-13
**Type:** code-notes

# plant_states

## Summary

```
Defines discrete plant growth and condition states for state-based tracking.
```

## Details

> This file enumerates qualitative states representing a plant’s lifecycle and health, such as growth phases (flowering, fruiting) and degradation (wilted, dead). States like `healthy` and `harvested` denote functional or harvested conditions, while `wilted`/`dead` indicate decline. Used likely in a system tracking plant progression or condition assessment.

## Key Functions

### `state_lookup`

Maps string inputs (e.g., `"flowering"`) to state identifiers for validation.

### `state_validation`

Ensures input matches predefined states (e.g., rejects `"rotten"`).

## Usage

1. Import the list as a set or frozen set for validation:
   ```python
   from plant_states import STATE_LIST
   if state not in STATE_LIST:
       raise ValueError("Invalid state")
   ```
2. Use for conditional logic (e.g., `if state == "harvested"`).

## Related

- [[plant_state_transitions]]
- [[plant_health_metrics]]

>[!INFO] State Ordering
> States may implicitly imply progression (e.g., `healthy` → `flowering` → `harvested`). Custom logic needed for non-sequential transitions.

>[!WARNING] Case Sensitivity
> Inputs like `"Wilted"` will fail validation unless normalized (e.g., lowercase). Always enforce exact matches.
