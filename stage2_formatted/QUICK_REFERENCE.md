**Tags:** #quick-reference, #drone-simulation, #api-reference, #docker, #simulation-tools
**Created:** 2026-01-12
**Type:** code-notes

# QUICK_REFERENCE

## Summary

```
Quick reference card for managing drone simulations, building generation, and system status via Docker and API commands.
```

## Details

> This quick reference card provides a concise guide for launching, monitoring, and controlling a drone simulation system using Docker containers and REST APIs. It includes commands for starting services, spawning drones (scout, overseer, logistics), sending commands (move, hover, land), generating buildings, and managing GPS coordinates. The system relies on Docker Compose for container orchestration and a backend API for drone and building management.

## Key Functions

### ``docker compose -f docker/docker-compose.yml up -d``

Starts all Docker containers in detached mode.

### ``curl http`

//localhost:5007/api/health`**: Checks backend health status.

### ``docker compose ps``

Lists running container statuses.

### ``curl http`

//localhost:5007/api/buildings/random`**: Generates a random building with specified parameters.

### ``curl -X POST http`

//localhost:5007/api/spawn`**: Spawns drones (scout, overseer, logistics) via API.

### ``curl -X POST http`

//localhost:5007/api/command`**: Sends drone commands (move, hover, land, scan).

### ``curl http`

//localhost:5007/api/buildings/list`**: Lists all generated buildings.

## Usage

1. **Start System**: Run Docker Compose commands to launch containers and check health.
2. **Spawn Drones**: Use API calls or web interface to deploy drones with specific roles.
3. **Send Commands**: Issue drone commands via API to control movement, hover, or land.
4. **Buildings**: Generate buildings via API or scan them using scout drones.
5. **GPS/Location**: Set or retrieve GPS coordinates via API.

## Dependencies

> `Docker Desktop`
> `Docker Compose`
> `backend API server (presumably running on port 5007).`

## Related

- [[Dockerfile]]
- [[docker-compose]]
- [[backend-api-docs]]
- [[simulation-environment-setup]]

>[!INFO] Important Note
> Ensure Docker Desktop is running before executing Docker commands. The simulation uses localhost:5007, so network access must allow traffic to this port.

>[!WARNING] Caution
> Avoid sending conflicting commands to the same drone simultaneously. The system may buffer commands, leading to unintended drone behavior if not managed properly. Always verify drone names match expected IDs.
