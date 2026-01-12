**Tags:** #drone-coordination, #automated-workflow, #building-cleaning, #mission-planning, #HMRS, #kuwait-city, #weather-api, #docker-simulation
**Created:** 2026-01-12
**Type:** code-notes

# WindowCleaningMissionWorkflow

## Summary

```
End-to-end automated workflow for cleaning 500+ windows on a 30-story office building using coordinated HMRS drone fleet.
```

## Details

> This document outlines a mission workflow for cleaning exterior windows of a 120m (30-story) building in Kuwait City using four specialized HMRS drone types. The system integrates drone coordination, weather checks, and building data loading via API calls. The workflow is divided into phases: pre-mission setup (GPS, base position, building data), real-time drone operations (mapping, cleaning, fluid resupply), and post-mission validation. Weather conditions from OpenWeatherMap API influence flight safety decisions.

## Key Functions

### ``docker compose -f docker/docker-compose.yml up -d``

Launches HMRS simulation environment.

### ``curl http`

//localhost:5007/api/health`**: Verifies system operational status.

### ``curl -X POST http`

//localhost:5007/api/master-controls/gps`**: Sets mission GPS coordinates (Kuwait City).

### ``curl -X POST http`

//localhost:5007/api/buildings/load`**: Loads building CAD data (or generates synthetic model).

### ``curl http`

//localhost:5007/api/weather/current`**: Checks real-time weather for flight safety.

### `HMRS Drone Fleet Roles`

- **Scout Drone**: Pre-mission mapping/planning.

### `Worker Drone (Climber)`

Attaches to building for cleaning.

### `Tanker-Mule Drone`

Resupplies cleaning fluid.

### `Tanker-Lifeline Drone`

Provides continuous power via tether.

### `Overseer Drone`

Monitors quality/safety.

## Usage

1. **Initialize**: Run Docker Compose to start simulation.
2. **Set Location**: Configure GPS coordinates and base truck position.
3. **Load Building**: Use existing CAD or generate synthetic data.
4. **Check Weather**: Validate flight safety before deployment.
5. **Execute Mission**: Deploy drone fleet in coordinated phases (mapping → cleaning → resupply → inspection).

## Dependencies

> `Docker Compose`
> `OpenWeatherMap API`
> `HMRS drone simulation framework`
> `REST API endpoints (`/api/health``
> ``/api/master-controls/*``
> ``/api/buildings/*``
> ``/api/weather/current`).`

## Related

- [[HMRS_Drone_Specs]]
- [[Kuwait_City_Weather_Profiles]]
- [[Building_CAD_Modeling_Guide]]

>[!INFO] Critical Weather Check
> **Always verify `flight_safe` flag** from `/api/weather/current` before drone deployment. Wind speed >10 m/s or adverse conditions halt operations.

>[!WARNING] GPS Accuracy
> **Coordinate precision** (e.g., ±0.001°) is critical for drone path planning. Errors in `latitude/longitude` cause misalignment with building coordinates.

>[!INFO] Drone Tether Management
> **Tanker-Lifeline Drone** must maintain a 50m tether buffer to prevent power failures during cleaning. Overstretch risks drone detachment.

>[!WARNING] Building Complexity
> **Non-rectangular windows** (e.g., arched, curved) require manual override in `/api/buildings/random` to avoid collision detection failures.
