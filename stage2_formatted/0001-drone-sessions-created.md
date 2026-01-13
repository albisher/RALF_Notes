**Tags:** #drone, #flight_simulation, #insect_inspired, #quadcopter, #session_log, #verification_needed
**Created:** 2026-01-13
**Type:** documentation

# 0001-drone-sessions-created

## Summary

```
Tracks drone session creation for different drone types with movement verification statuses and next steps for troubleshooting.
```

## Details

> This document records four drone sessions (Butterfly, Owl, Bee, Quadcopter) created on **2025-12-13**, noting successful session creation but pending movement verification. Each session logs drone type, ID, and location, while highlighting that **200 position updates were recorded but no movement occurred** (0.00m traveled). The Quadcopter session lacks a motion history file, suggesting incomplete data capture. Session naming follows a structured `YYYYMMDDHHMM-SessionName` format.

## Key Functions

### `Session Naming`

Generates standardized session IDs (e.g., `202512131942-Butterfly`).

### `Movement Verification`

Confirms drones receive updates but fail to execute physical movement.

### `Replay Mechanism`

Enables session replay via API or UI using session IDs.

## Usage

To replay sessions, use the provided session IDs via API (e.g., `curl` command) or navigate to the UI session dropdown. Next steps involve debugging why drones aren’t moving, checking command transmission, and verifying motion pattern execution.

## Dependencies

> `- Drone control API (`http://localhost:5007/api/sessions`)`
> `UI session selection dropdown.`

## Related

- [[Drone Movement Debugging Guide]]
- [[Flight Simulation Configuration]]

>[!INFO] Important Note
> **Session Naming**: Follow the `YYYYMMDDHHMM-SessionName` format for consistency. Example: `202512131942-Butterfly`.
>

>[!WARNING] Caution
> **Movement Issue**: Drones may not move due to missing commands, incorrect ML thrust calculations, or physics misconfigurations. Verify drone control logic before proceeding.
