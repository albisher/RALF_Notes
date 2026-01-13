**Tags:** #drone-automation, #3d-flight-patterns, #simulation, #figure-8, #butterfly-flight
**Created:** 2026-01-13
**Type:** code-notes

# butterfly-session-created

## Summary

```
Generates a 3D figure-8 (butterfly) flight pattern for drone simulation with parametric waypoints.
```

## Details

> This script creates a **butterfly session** using a figure-8 trajectory in 3D space, defined by parametric equations for smooth motion. The session includes a center point, horizontal/vertical radii, and height oscillation, producing 50 waypoints for drone navigation. The session stores motion history and building data, with pending fixes for drone movement and replay functionality.

## Key Functions

### ``create_butterfly_session.py``

Orchestrates session generation with parametric equations.

### ``motion_history.json``

Logs drone positions during flight.

### ``buildings.json``

Stores static building data for spatial context.

## Usage

1. Run in terminal:
   ```bash
   cd simulation && python create_butterfly_session.py
   ```
2. Replay via UI after server restart:
   - Navigate to `http://localhost:5007`, select session, and load replay.

## Dependencies

> ``simulation` (local directory)`
> ``json` (for file handling)`
> ``numpy`/`math` (for parametric calculations).`

## Related

- [[motion-history-replay-fixes]]
- [[all-issues-fixed-summary]]

>[!INFO] **Pending Fixes**
> Server restart required to apply path corrections for smooth replay.

>[!WARNING] **Drone Movement**
> Current implementation has minimal drone movement; adjust wait times or simulation duration for full effect.
