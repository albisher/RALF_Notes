**Tags:** #real-time-communication, #multi-container-architecture, #socketio, #flask, #docker, #nginx, #drone-swarm, #web-sockets
**Created:** 2026-01-13
**Type:** code-notes

# socketio-multi-container-implementation

## Summary

```
Implements Socket.IO for real-time drone swarm control using a multi-container Docker architecture to replace HTTP polling.
```

## Details

> This implementation addresses a drone swarm control system by migrating from HTTP polling to Socket.IO for low-latency, scalable real-time communication. The solution splits the application into three containers: a Flask-based backend with Socket.IO, an Nginx frontend for static assets, and a PostgreSQL database. Socket.IO enables bidirectional real-time event handling between clients and the backend, reducing latency from 1000ms to <50ms and improving bandwidth efficiency by ~330x. The architecture decouples frontend/backend, enabling independent scaling and easier updates.

## Key Functions

### ``hmrs_simulation_live.py``

Flask-SocketIO server handling drone commands, status updates, and periodic broadcasts.

### ``app-data.js``

Frontend Socket.IO client managing real-time event listeners for status, drone positions, visualization, and logs.

### ``sendCommand()``

Fallback mechanism using Socket.IO first, then HTTP if disconnected.

### ``docker/nginx.conf``

Nginx config proxying WebSocket traffic and static assets, with compression and caching.

## Usage

1. Deploy containers with `docker-compose` (backend, frontend, database).
2. Configure `nginx.conf` to proxy `/socket.io/*` and `/api/*` to the backend.
3. Initialize Socket.IO in frontend (`app-data.js`) and run Flask backend (`hmrs_simulation_live.py`).
4. Replace HTTP polling with Socket.IO events in the frontend.

## Dependencies

> `flask-socketio`
> `nginx`
> `PostgreSQL`
> `Docker`
> `Flask (backend)`
> `Nginx (frontend)`

## Related

- [[doc]]
- [[Dockerfile]]
- [[Dockerfile]]

>[!INFO] **Real-Time Fallback**
> Socket.IO prioritizes real-time communication, but HTTP polling acts as a graceful fallback (5s interval) if the connection drops.

>[!WARNING] **WebSocket Latency**
> Latency spikes may occur if the backend fails to broadcast updates promptly; monitor periodic update intervals (e.g., 0.04s for status).
