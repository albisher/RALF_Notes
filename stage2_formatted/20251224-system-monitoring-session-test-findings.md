**Tags:** #system-monitoring, #container-restart, #session-management, #vue-router, #debugging
**Created:** 2026-01-12
**Type:** test-reference

# system-monitoring-session-test-findings

## Summary

```
Test findings for verifying system monitoring page functionality after container restart and drone session operations.
```

## Details

> This document records a test session evaluating the system monitoring page’s ability to display session data, system status, and synchronization after a container restart and drone session interactions. The test confirmed container health, session creation, simulation progression, and UI responsiveness but identified routing and conditional rendering issues in the monitoring page.

## Key Functions

### ``docker-compose down/up -d``

Managed container lifecycle.

### ``New Session` button`

Created session with timestamp format `YYYYMMDDHHMM`.

### ``Start` button`

Initiated simulation time incrementation.

### ``Spawn` modal`

Displayed drone configurations (RGB, IR, Thermal, Polarization, LiDAR).

### `System Monitoring Page (`#/sm/`)`

Expected to show system status but rendered simulation interface instead.

### `Vue Router`

Likely failed to switch views based on URL hash.

## Usage

To reproduce:
1. Restart containers via `docker-compose down/up -d`.
2. Navigate to `http://localhost:5007/#/sm/` and verify monitoring page loads correctly.
3. Test session creation, simulation, and drone spawning to isolate monitoring-specific issues.

## Dependencies

> `Docker Compose`
> `Vue.js router`
> `backend services (`hmrs-backend``
> ``hmrs-session-db`)`
> `frontend UI components.`

## Related

- [[`20251224-container-restart-log`]]
- [[`20251224-simulation-test-results`]]

>[!INFO] Routing Issue
> The URL hash (`#/sm/`) should trigger a state change (`currentView = 'system-monitoring'`) in Vue Router, but the page still renders the simulation view. Check router configuration and component lifecycle hooks.

>[!WARNING] Conditional Rendering
> The `v-if` condition (`v-if="currentView === 'system-monitoring'"`) may not execute due to incorrect state updates. Verify router middleware or component logic for view transitions.
