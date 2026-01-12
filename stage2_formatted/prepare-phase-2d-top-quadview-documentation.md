**Tags:** #documentation, #backend-api, #gps-coordinates, #simulation, #2d-top-view, #quadview, #api-endpoint, #gps-generation
**Created:** 2026-01-12
**Type:** documentation

# prepare-phase-2d-top-quadview-documentation

## Summary

```
Documentation for the backend frontend interaction to prepare a 2D top quadview area by fetching and processing GPS location data.
```

## Details

> This document outlines the workflow for the **prepare phase** of a 2D top quadview simulation, detailing how GPS coordinates are sourced from a backend API and processed in the frontend. The backend stores location data in memory via a class (`HMRSSimulationLive`) and generates random coordinates from a predefined list of cities in the Middle East/North Africa region if not already set. The frontend fetches this data via a `/api/prepare` GET request and updates master controls with the retrieved coordinates.

## Key Functions

### ``/api/prepare` endpoint`

Handles fetching or generating GPS coordinates based on flags (`force_random`).

### ``set_base_gps` method** (in `HMRSSimulationLive`)`

Stores latitude, longitude, and random flag in memory.

### ``prepareScene()` function** (in `frontend/app-data.js`)`

Initiates the API call and updates frontend controls with GPS data.

### `City list generation logic`

Randomly selects a city from a predefined MENA list (~40 cities) with a small offset (~5km).

## Usage

1. **Backend Setup**:
   - Initialize `HMRSSimulationLive` with `base_latitude` and `base_longitude` set to `None`.
   - Call `/api/prepare` with `force_random=true` to generate random GPS coordinates or `false` to return stored values.

2. **Frontend Integration**:
   - Call `prepareScene()` in the frontend to fetch and update master controls with GPS data.
   - Ensure `fetch` is available to make API requests.

## Dependencies

> `- `simulation/hmrs_simulation_live.py` (backend logic for GPS storage/generation)
- `frontend/app-data.js` (frontend interaction with API response)
- External libraries: `fetch` (for API calls)`
> ``json` (for parsing responses)`

## Related

- [[hmrs_simulation_live]]
- [[app-data]]

>[!INFO] Important Note
> The backend uses **in-memory storage** for GPS coordinates, meaning data is lost on restart unless explicitly saved elsewhere. Ensure persistence logic is implemented if long-term storage is required.

>[!WARNING] Caution
> Hardcoded city list (`hmrs_simulation_live.py`) may need updates if new cities are added or existing ones are deprecated. Test with default fallback (Kuwait City) to avoid runtime errors.
