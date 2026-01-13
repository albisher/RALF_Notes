**Tags:** #simulation, #time-management, #threading, #debugging, #fix
**Created:** 2026-01-13
**Type:** code-notes

# 0016-sim-time-fix

## Summary

```
Fixes simulation time (`sim_time`) stuck at 0.0s by restructuring loop logic, improving thread handling, and adding verification checks.
```

## Details

> The issue involved a simulation thread (`run_simulation_thread()`) where `sim_time` remained at 0.0s due to improper loop structure and thread synchronization. The root cause was misplaced code after exception handling, preventing iterative execution. The fix restructured the loop to ensure continuous execution, added proper thread initialization checks, and enhanced error handling with debug outputs to verify `sim_time` progression.

## Key Functions

### ``run_simulation_thread()``

Main simulation loop with exception handling and thread management.

### ``sim_time``

Simulation clock variable that must increment continuously for correct position tracking.

### `Thread verification checks`

Ensures thread remains active and logs initial state.

## Usage

Apply the fixes in `hmrs_simulation_live.py` by:
1. Restructuring loop-dependent logic inside the `try` block.
2. Adding debug prints to verify `sim_time` progression.
3. Running the verification script (`verify_time_based_data.py`) to confirm fixes.

## Dependencies

> ``hmrs_simulation_live.py``
> ``verify_time_based_data.py` (external script for testing).`

## Related

- [[`verify_time_based_data]]
- [[0007-time-based-data-verification.md`.]]

>[!INFO] Critical Loop Fix
> Ensure all loop-dependent operations (e.g., scouting logic, progress updates) execute inside the `try` block to maintain continuous iteration.

>[!WARNING] Thread Initialization
> Verify `self.running` flag is set before starting the thread; otherwise, the simulation may exit prematurely.
