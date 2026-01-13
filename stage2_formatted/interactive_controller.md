**Tags:** #drone-simulation, #real-time-control, #interactive-ui, #event-driven, #callback-based
**Created:** 2026-01-13
**Type:** code-notes

# interactive_controller

## Summary

```
Manages real-time drone control via keyboard/mouse/web inputs with event-driven callbacks.
```

## Details

> The `InteractiveController` class handles drone simulation control logic, including command queuing, mode switching, and worker selection. It supports manual, auto, and learning control modes and processes user events via callbacks. The `INTERACTIVE_HTML_CONTROLS` snippet defines a web-based UI for selecting control modes and workers, though it is incomplete (missing closing `</div>` and JavaScript logic).
> 
> Key components include:
> - A command queue (`commands_queue`) for pending drone actions.
> - Callback registration (`register_callback`) for event handling (e.g., mode changes).
> - Worker selection and control mode switching (`select_worker`, `set_control_mode`).

## Key Functions

### ``register_callback(event`

str, callback: Callable)`**: Associates an event (e.g., `mode_changed`) with a function to execute when triggered.

### ``send_command(worker_id`

int, command: Dict)`**: Adds a drone command to the queue with metadata (timestamp, worker ID).

### ``get_pending_commands()``

Retrieves and clears all queued commands.

### ``set_control_mode(mode`

str)`**: Updates the control mode (manual/auto/learning) and triggers callbacks.

### ``select_worker(worker_id`

int)`**: Designates a worker for manual control and notifies via callbacks.

## Usage

1. Initialize `InteractiveController()` to start the system.
2. Register callbacks for events (e.g., `register_callback("mode_changed", lambda: print("Mode changed"))`).
3. Use `send_command()` to dispatch drone actions (e.g., `send_command(1, {"action": "move"})`).
4. Access status via `get_status()` (e.g., `status = controller.get_status()`).
5. For web UI, integrate `INTERACTIVE_HTML_CONTROLS` into a frontend (requires JavaScript to implement `setControlMode`/`selectWorker`).

## Dependencies

> `numpy`
> `typing (Python standard library)`
> `time (Python standard library)`

## Related

- [[drone_simulation_core]]
- [[event_system_implementation]]

>[!INFO] Event-Driven Design
> The controller relies on callbacks for dynamic updates (e.g., mode changes or worker selections). Missing a callback registration may cause silent failures.

>[!WARNING] Incomplete UI
> `INTERACTIVE_HTML_CONTROLS` lacks closing tags and JavaScript logic. Ensure frontend integration completes these components to avoid broken controls.
