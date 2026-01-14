**Tags:** #ui-testing, #map-generation, #frontend-backend-integration, #verification-report, #world-generation
**Created:** 2026-01-13
**Type:** documentation

# map_generation_ui_verification_20251206

## Summary

```
Manual UI verification report for map generation functionality, detailing frontend/backend integration, test worlds, and verification steps for customizable map creation.
```

## Details

> This document serves as a verification guide for the map generation system, which combines frontend UI components (`GenerateStage.vue`, `MapGeneratorForm.vue`) with backend services (`map-generator/api.py`, `map_generator.py`). The process requires manual UI testing across three predefined test worlds (Clouds, Galaxy, Random General) to validate map generation, parameter handling, progress tracking, and preview functionality. The workflow includes generating descriptive inputs, triggering map generation via API endpoints (`/api/maps/generate`), and verifying UI responses such as parameter forms, progress indicators, and saved map previews.

## Key Functions

### ``GenerateStage.vue``

Displays the main map generation UI tab with dropdowns and controls.

### ``MapGeneratorForm.vue``

Handles dynamic parameter generation from user input (e.g., hash text) and renders the form for manual review.

### ``MapGeneratorControls.vue``

Manages the "Generate Map" button and progress tracking.

### ``MapPreview.vue``

Visualizes the generated map data in real-time.

### ``services/map-generator/api.py``

Backend API endpoint (`/api/maps/generate`) for initiating map generation jobs.

### ``services/map-generator/engine/map_generator.py``

Core logic for generating map data (voronoi, heightmaps, biomes).

### ``backend/boxes/api/generation_bp.py``

API box for handling generation requests and status polling.

### ``backend/boxes/generators/map_generator_box.py``

Manages job queues and map generation workflows.

## Usage

1. **Setup**: Install dependencies and run the backend (`backend/`) and frontend (`frontend/`) servers.
2. **Test Worlds**: Create three worlds (Clouds, Galaxy, Random General) via the frontend UI.
3. **Manual Testing**:
   - Navigate to the `/generate` tab in the frontend.
   - Select a world and input descriptive text in the hash field.
   - Click "Generate" to trigger parameter generation, then "Generate Map" to start the process.
   - Verify UI elements (progress bars, parameter forms) and backend responses (API status polling).

## Dependencies

> ``vue``
> ``axios``
> ``fastapi``
> ``python-multiprocessing``
> ``numpy` (for map generation algorithms)`
> ``react-router-dom` (for frontend routing).`

## Related

- [[Map Generation API Design]]
- [[Frontend UI Component Specs]]
- [[Backend Service Integration Guide]]

>[!INFO] Important Note
> **World Context Matters**: The world type (e.g., "Clouds World") influences map generation parameters (e.g., seed values, biome distributions). Test each world type separately to ensure compatibility with custom inputs.
>

>[!WARNING] Caution
> **API Rate Limits**: Excessive map generation requests may trigger backend throttling. Monitor job queues (`/api/maps/status/{job_id}`) for errors or timeouts during testing.
