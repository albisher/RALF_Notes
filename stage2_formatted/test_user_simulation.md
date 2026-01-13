**Tags:** #pytest, #simulation, #api-testing, #gps, #drone, #building-simulation, #hms-system
**Created:** 2026-01-13
**Type:** test-reference

# test_user_simulation

## Summary

```
Simulates a user workflow for a window cleaning mission in an HMRS system via API calls.
```

## Details

> This script automates a complete user interaction sequence for a hypothetical window cleaning mission. It mimics a user checking system health, setting GPS coordinates (Kuwait), starting a simulation, generating a building (e.g., "Dubai Tower"), and spawning a Scout drone for mapping. Each step includes status checks and error handling via HTTP responses. The workflow is designed to test the backend system’s ability to handle user commands sequentially.

## Key Functions

### `test_user_workflow()`

Orchestrates the full user interaction sequence (health check → GPS → start simulation → building creation → drone spawn).

### `print_section(title)`

Helper function to format section headers in the output.

## Usage

1. Run the script directly to execute the simulated workflow.
2. Verify API responses for each step (success/failure).
3. Useful for validating backend endpoints (`/api/health`, `/api/master-controls/gps`, etc.).

## Dependencies

> `requests`
> `time`
> `json`

## Related

- [[HMRS_API_DOCS]]
- [[HMRS_SYSTEM_ARCHITECTURE]]

>[!INFO] Important Note
> This script assumes the backend (`http://localhost:5007`) is running and accessible. If the system is down, the workflow will exit early.

>[!WARNING] Caution
> Hardcoded coordinates (e.g., Kuwait GPS) may not reflect real-world accuracy. Adjust values if testing in different locations.
