**Tags:** #session, #replay, #drone, #testing, #api, #ui, #verification, #data, #motion_history, #curl, #python
**Created:** 2026-01-13
**Type:** test-reference

# replayable-session-created

## Summary

```
Records successful creation of a replayable session with drone motion data for playback verification.
```

## Details

> This document confirms the successful generation of a replayable session (`202512141338-ReplayTest`) containing motion history for two drones (`scout-1` and `scout-2`), each with 2 position updates. The session includes metadata like session ID, creation timestamp, and associated files (e.g., `motion_history.json`). Verification via API endpoints (`/api/sessions` and `/api/sessions/{id}/replay`) confirms `replay_available: True` and drone data integrity. The session is ready for playback testing via a local UI (`http://localhost:5007`).

## Key Functions

### ``create_replayable_session.py``

Script that generates the replayable session structure and data files.

### ``motion_history.json``

Stores drone position updates (e.g., `scout-1` and `scout-2` entries).

### ``simulation_summary.json``

Contains metadata like session ID, creation time, and drone counts.

## Usage

1. **Verify via API**:
   ```bash
   curl -s "http://localhost:5007/api/sessions" | grep "202512141338-ReplayTest"
   ```
   ```bash
   curl -s "http://localhost:5007/api/sessions/202512141338-ReplayTest/replay" | python -c "import sys, json; d=json.load(sys.stdin); print('Replay available:', d.get('replay_available')); print('Drones:', len(d.get('motion_history', {})))".
   ```
2. **Test Playback**:
   - Access UI at `http://localhost:5007`, search for `ReplayTest`, and load the session.

## Dependencies

> `- Python (`curl``
> ``python3`)`
> `local UI server (`http://localhost:5007`)`
> `drone simulation backend.`

## Related

- [[ui-playback-solution]]
- [[ui-verification-final-report]]

>[!INFO] **Session Verification**
> Verify the session exists via API endpoints (`/api/sessions` and `/replay`). The expected output confirms `replay_available: True` and drone motion history integrity.

>[!WARNING] **UI Dependency**
> Ensure the UI server (`http://localhost:5007`) is running before testing playback. Session selection requires the UI dropdown functionality.
