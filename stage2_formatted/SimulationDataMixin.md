**Tags:** #HTTP-polling, #OOP-mixin, #fallback-logic, #realtime-data, #API-communication, #session-management
**Created:** 2026-01-13
**Type:** code-notes

# SimulationDataMixin

## Summary

```
Handles HTTP-based simulation data fetching as a fallback when Socket.IO is unavailable, updating simulation status via API calls.
```

## Details

> `SimulationDataMixin` implements a **mixin pattern** to reuse HTTP-based simulation data fetching logic. It delegates API calls to `window.apiCommunicationBox` and updates simulation state properties (`running`, `simTime`, etc.) from server responses. The mixin includes logic to:
> - **Silently skip** failed requests (e.g., when the server is between sessions).
> - **Highlight target buildings** in OSM views if `osmIntegrationBox` is available.
> - **Track maximum simulation time** (`maxSimTime`) and update `currentTime` conditionally (e.g., during recording or time travel).
> - **Log errors** (excluding fetch-specific errors) via `loggingBox` or `console.debug`.

## Key Functions

### ``updateStatus()``

Asynchronously fetches realtime simulation data via HTTP polling, updates internal state, and triggers UI/phase system reactions.

## Usage

1. Attach this mixin to an object (e.g., `const sim = new SimulationData(); sim.__proto__ = SimulationDataMixin`).
2. Call `sim.updateStatus()` to trigger HTTP polling and state updates.
3. Ensure `apiCommunicationBox` exists (e.g., via `window.apiCommunicationBox = new APICommunicationBox()`).

## Dependencies

> ``window.apiCommunicationBox``
> ``window.osmIntegrationBox``
> ``window.loggingBox``

## Related

- [[APICommunicationBox]]
- [[Socket]]

>[!INFO] Critical Fallback
> This function **explicitly avoids Socket.IO**, relying solely on HTTP polling. If Socket.IO is unavailable, it gracefully degrades to HTTP-only updates.

>[!WARNING] Silent Skips
> Failed requests (e.g., server downtime) are **silently skipped** to prevent UI crashes. Debug logs are logged only if `loggingBox` is available.
