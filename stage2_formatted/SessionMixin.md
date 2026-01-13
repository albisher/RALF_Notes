**Tags:** #Vue, #Mixin, #SessionManagement, #Replay, #APIIntegration, #OOP, #ReusableComponent
**Created:** 2026-01-13
**Type:** code-notes

# SessionMixin

## Summary

```
Provides session management functionality via a Vue.js mixin for component reuse.
```

## Details

> `SessionMixin` implements a Vue.js mixin to handle session-related operations (loading, selecting) using a `SessionService`. It follows the mixin pattern for code reuse, encapsulating session state (`sessions`, `selectedReplaySession`, etc.) and methods (`loadSessions`, `selectSession`). The mixin initializes a `SessionService` with a global API endpoint (`apiCommunicationBox`/`apiBox`) and logs session actions via `loggingBox`. It includes error handling for missing dependencies.

## Key Functions

### ``loadSessions()``

Asynchronously fetches and stores all available sessions from `SessionService`.

### ``selectSession(sessionId)``

Attempts to select a session by ID, updates internal state (e.g., `sessionDetails`), and triggers status changes if `this.status` exists.

### ``created()``

Initializes `sessionService` with the global API endpoint if available; otherwise, logs an error.

## Usage

1. Import and use in a Vue component:
   ```javascript
   export default {
       mixins: [SessionMixin],
       // Component logic...
   };
   ```
2. Call `loadSessions()` to populate `this.sessions`.
3. Call `selectSession(sessionId)` to activate a session.

## Dependencies

> ``SessionService` (imported from `../services/SessionService.js`)`
> ``window.apiCommunicationBox`/`window.apiBox``
> ``window.loggingBox` (optional logging).`

## Related

- [[SessionService]]
- [[APIBox Integration Guide]]

>[!INFO] Initialization Check
> If `window.apiCommunicationBox`/`window.apiBox` is missing, `sessionService` remains `null`, and `loadSessions()` will log an error.

>[!WARNING] Missing SessionService
> If `SessionService` fails to initialize, `loadSessions()` defaults to an empty array and logs an error. Ensure the service is properly injected before calling methods.
