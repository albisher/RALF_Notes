**Tags:** #ui-verification, #master-controls, #frontend, #api-integration, #configuration
**Created:** 2026-01-13
**Type:** documentation

# ui-verification-master-controls

## Summary

```
Verifies UI components and backend integration for master controls dashboard in a geospatial application.
```

## Details

> This document confirms the completion of UI verification for a master controls panel, ensuring all interactive elements (e.g., GPS mode selector, building selection, weather settings) and backend APIs (e.g., `master-controls`, `weather`) are functional. The verification includes frontend components (Vue.js, CSS), backend API endpoints, and configuration management for dynamic features like drone brands and time restrictions.

## Key Functions

### ``verify_master_controls_ui.py``

Script that runs UI and backend checks.

### ``onGpsModeChange()``

Updates UI based on GPS mode selection (simulation/current/custom).

### ``getCurrentLocation()``

Retrieves user’s real-time coordinates via browser API.

### ``loadMapData()``

Fetches 3D building data from an API endpoint (`map-data`).

### ``toggleBuildingSelection()``

Enables/disables multi-select for buildings.

### ``updateSelectedBuildings()``

Dynamically updates the list of selected buildings.

### ``getDroneBrands()``

Loads drone brand models from an API (`drone-brands`).

### ``saveMasterControls()``

Persists configuration to `integration_config.json`.

### ``loadMasterControls()``

Restores saved settings from storage.

## Usage

1. **Setup**: Install dependencies (`requests`, `pytz`) and configure `integration_config.json`.
2. **Verification**: Run `verify_master_controls_ui.py` to validate UI/back-end compatibility.
3. **Testing**: Use the UI to interact with features (e.g., select buildings, adjust weather settings).
4. **API Testing**: Call endpoints like `master-controls` or `weather` via tools like Postman.

## Dependencies

> ``requests` (2.32.3)`
> ``pytz` (2025.2)`
> `Vue.js framework (assumed for frontend)`
> `backend API endpoints (custom).`

## Related

- [[ui-verification-master-controls]]
- [[backend-api-docs]]
- [[frontend-component-guidelines]]

>[!INFO] Important Note
> The `verify_master_controls_ui.py` script automates UI checks but requires manual API key updates in `integration_config.json` for live testing.

>[!WARNING] Caution
> Disabling `GPS mode` to "custom" may break real-time location updates if coordinates are not manually set. Test edge cases (e.g., invalid timezone inputs).
