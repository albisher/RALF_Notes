**Tags:** #ui-playback, #session-management, #motion-history, #debugging, #workaround
**Created:** 2026-01-13
**Type:** documentation

# ui-playback-solution

## Summary

```
Documentation outlining a UI playback solution for sessions with missing motion history data, including root causes, test procedures, and workarounds.
```

## Details

> This document explains why the session `202512131946-Quadcopter` fails playback due to an empty `motion_history.json` file. The root cause is that no drone movements were recorded during the session. The solution identifies working sessions with motion history and provides steps to test playback via the UI, including API verification. It also details how to create a session with motion history by spawning and moving drones.

## Key Functions

### ``Load Replay for Selected Session``

Functionality to load and display drone motion history in the UI.

### ``Create Demo Session``

UI action to initiate a new session for testing.

### ``API Endpoint (curl test)``

Verifies playback availability via `/api/sessions/{session_id}/replay`.

## Usage

1. **Test Playback**: Use sessions like `202512131422` to verify playback works.
2. **Create New Session**: Spawn drones, move them, and complete the session to generate motion history.
3. **API Verification**: Run the provided `curl` command to check replay availability programmatically.

## Dependencies

> `- UI framework (e.g.`
> `React/Django frontend for `http://localhost:5007`).
- Session management backend (handles `/api/sessions` endpoints).
- Motion history storage (JSON files or database for `motion_history.json`).`

## Related

- [[ui-session-management]]
- [[motion-history-backend]]

>[!INFO] Important Note
> The UI replay feature is functional; the issue lies in the absence of motion history data for the problematic session. Ensure drones are spawned and moved to populate `motion_history.json`.


>[!WARNING] Caution
> Empty `motion_history.json` files indicate no drone activity. Always verify session logs or manually check drone movement before playback.
