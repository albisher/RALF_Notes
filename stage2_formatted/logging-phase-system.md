**Tags:** #logging, #system-state, #contextual-filtering, #phased-logging, #IoT, #automation, #real-time
**Created:** 2026-01-13
**Type:** code-notes

# logging-phase-system

## Summary

```
Manages intelligent log filtering by system operational phases for IoT/drone systems.
```

## Details

> This system defines a phased logging approach where logs are dynamically filtered based on the current operational state. Each phase (e.g., `SYSTEM_CHECK`, `BASE_STATUS`) includes:
> - **Log type priorities** (e.g., `['error', 'system']` for Phase 1).
> - **Relevant keywords** (e.g., `['connect', 'socket']` for Phase 1).
> - **Transition conditions** (e.g., `socketConnected: true` to advance to `base_status`).
> - **Phase-specific logic** to enable/disable log filtering dynamically.
> 
> The system enforces a strict sequence: Phase 1 → Phase 2 → Phase 3 → ... → Phase 5, with fallback (`WAITING_FOR_DRONES`) for missing drones.

## Key Functions

### ``phases` object`

Defines all supported phases with metadata (ID, name, keywords, conditions).

### `Dynamic filtering`

Logs are filtered by phase-specific rules (e.g., only `error`/`system` logs appear in Phase 1).

### `State transitions`

Advances to `nextPhase` (e.g., `base_status`) when conditions (e.g., `apiAvailable: true`) are met.

## Usage

1. **Initialize**: Use the `phases` object to define log rules for each phase.
2. **Filter logs**: Apply phase-specific logic to log entries (e.g., check `keywords` or `priorityLogTypes`).
3. **Trigger transitions**: Evaluate `conditions` to advance phases (e.g., `socketConnected` → `base_status`).

## Dependencies

> `None (purely structural/configuration).`

## Related

- [[logging-filtering-strategy]]
- [[IoT-system-architecture]]

>[!INFO] Phase Overlap Handling
> The `WAITING_FOR_DRONES` phase acts as a guardrail for drones. If drones are not spawned, it skips `drones_status` entirely, preventing stale log checks.

>[!WARNING] Condition Strictness
> Conditions (e.g., `apiAvailable: true`) must be met *exactly* to advance phases. Violations may stall the system (e.g., `socketConnected: false` blocks `base_status`).
