**Tags:** #state_machine, #mission_control, #scan_plan_execute_verify, #enum, #time_tracking
**Created:** 2026-01-13
**Type:** code-notes

# mission_state_machine_box

## Summary

```
Manages a Scan-Plan-Execute-Verify state machine for mission operations, tracking transitions and durations.
```

## Details

> This code implements a state machine for a mission system following the Scan-Plan-Execute-Verify workflow. It uses an `Enum` to define mission phases (`SCAN`, `PLAN`, `EXECUTE`, `VERIFY`) and enforces valid transitions between them. The `MissionStateMachineBox` class tracks phase durations, records transitions in a history log, and validates transitions based on predefined rules (e.g., `SCAN` must precede `PLAN`). Time tracking is used to measure phase execution durations.

## Key Functions

### ``MissionPhase``

Defines mission phases as an `Enum` for structured state representation.

### ``MissionStateMachineBox.__init__()``

Initializes the state machine with default `SCAN` phase and starts tracking time.

### ``transition_to_phase()``

Handles state transitions, validates them, logs history, and returns transition metadata.

### ``_validate_transition()``

Private method enforcing valid transitions (e.g., `PLAN` only after `SCAN`).

## Usage

1. Instantiate `MissionStateMachineBox()` to start.
2. Call `transition_to_phase(new_phase)` with a valid `MissionPhase` and optional reason.
3. Check `current_phase` and `phase_history` for state tracking.

## Dependencies

> ``enum``
> ``typing``
> ``time``

## Related

- [[none]]

>[!INFO] Important Note
> The `_validate_transition()` method enforces strict rules (e.g., `VERIFY` can only transition to `SCAN` or `EXECUTE`). Violations return `valid=False`.

>[!WARNING] Caution
> Time-based transitions (e.g., `SCAN` → `PLAN`) assume phase completion is time-based; ensure logic aligns with actual mission criteria.
