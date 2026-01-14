**Tags:** #WebSockets, #Real-time, #Backend-Frontend, #Flask-SocketIO, #Socket.IO, #Pinia, #Live-Previews, #Collaborative-Editing
**Created:** 2026-01-13
**Type:** documentation-research

# task_025

## Summary

```
Implements WebSocket-based real-time updates for collaborative editing and live previews using Flask-SocketIO and socket.io-client.
```

## Details

> This task outlines the implementation of a WebSocket-based system to enable real-time synchronization across multiple clients. The backend integrates Flask-SocketIO to handle WebSocket connections and emit events when resources (e.g., world elements) are updated. The frontend uses `socket.io-client` to connect to the backend, listen for updates, and trigger UI/Pinia store reactions. The system ensures bidirectional communication, allowing clients to see live changes without page refreshes.

## Key Functions

### `Flask-SocketIO Integration`

Sets up WebSocket support in a Flask application for real-time communication.

### `Event Emitters`

Backend logic to broadcast updates (e.g., character name changes) to connected clients via `socketio.emit()`.

### `socket.io-client Setup`

Frontend connection to the WebSocket server with event listeners for reactive UI updates.

### `Pinia Store Updates`

Frontend state management to reflect real-time changes dynamically.

## Usage

1. **Backend Setup**:
   - Install `Flask-SocketIO` and configure the Flask app with `socketio.run()`.
   - Implement event emitters in backend routes (e.g., on `save`/`update` actions).
   - Broadcast updates to connected clients using `socketio.emit()`.

2. **Frontend Setup**:
   - Install `socket.io-client` and connect to the backend WebSocket URL.
   - Set up event listeners (e.g., `socket.on('update')`) to trigger UI/Pinia store updates.
   - Example: Listen for `update` events and call `piniaStore.updateState()`.

3. **Testing**:
   - Open multiple browser windows, edit data in one, and verify real-time sync in others.

## Dependencies

> `Flask`
> `Flask-SocketIO`
> `socket.io-client`
> `Pinia (frontend state management).`

## Related

- [[Task 025]]
- [[Task 025]]
- [[Task 025.3: Frontend Socket]]

>[!INFO] Important Note
> Ensure CORS is configured in the backend to allow frontend connections from different origins. Use `socketio.CORS_ALLOW_ALL_ORIGINS = True` (or equivalent) if testing locally.

>[!WARNING] Caution
> Avoid hardcoding WebSocket URLs in production. Use environment variables (e.g., `process.env.WS_URL`) for dynamic backend URLs.
