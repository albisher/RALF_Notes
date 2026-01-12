**Tags:** #flight-test, #drone-simulation, #api-failure, #debugging, #session-management, #gps-coordinates
**Created:** 2026-01-12
**Type:** test-reference

# 20251223-home-flight-simulation-test

## Summary

```
Test flight simulation at home location to verify drone movement and playback functionality, with critical issues in API command handling and log deduplication.
```

## Details

> This test document records a home-based flight simulation attempt for a drone system, focusing on verifying drone movement via API commands and playback of recorded flight data. The test encountered persistent issues with JavaScript error handling in log processing (`deduplicateLogs`), HTTP 500 errors during command execution, and missing motion history in session playback. The setup included Docker services, GPS configuration, and session management, but critical backend and frontend failures prevented successful flight execution.

## Key Functions

### ``/api/command``

Fails with HTTP 500; drone movement commands not processed.

### ``/api/master-controls``

Successfully sets GPS coordinates to home location.

### ``/api/sessions/create-demo``

Creates a session but lacks motion history.

### ``/api/spawn``

Spawns drone but fails to execute flight commands.

### ``deduplicateLogs` (app-data.js)`

JavaScript method not accessible in computed properties, causing log display failures.

### ``hmrs_simulation_live.py``

Backend script handling drone command processing (error-prone).

## Usage

1. Run Docker services locally.
2. Set GPS coordinates via `/api/master-controls` to home location.
3. Create a session (`/api/sessions/create-demo`) and spawn drone (`/api/spawn`).
4. Execute flight commands via API (`/api/command`) or browser UI.
5. Verify playback of motion history in session replay.

## Dependencies

> `Docker services`
> ``/api/master-controls``
> ``/api/sessions/create-demo``
> ``/api/spawn``
> ``/api/command``
> ``hmrs_simulation_live.py``
> `browser-based UI for command execution.`

## Related

- [[None]]

>[!INFO] Important Note
> The `deduplicateLogs` error persists despite moving the method to the methods section, suggesting browser caching or incorrect method invocation context in computed properties. Investigate method accessibility in frontend code.


>[!WARNING] Caution
> The `/api/command` endpoint consistently returns HTTP 500 errors, indicating a backend issue in drone command processing. Investigate `hmrs_simulation_live.py` error handling and drone readiness before sending commands.
