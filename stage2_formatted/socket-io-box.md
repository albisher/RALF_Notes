**Tags:** #Socket.IO, #EventManagement, #Reconnection, #WebSocket, #Client-Server
**Created:** 2026-01-13
**Type:** code-notes

# socket-io-box

## Summary

```
Manages Socket.IO connection and event handling with reconnection logic.
```

## Details

> `SocketIOBox` is a class designed to handle all Socket.IO communication, adhering to a single responsibility principle. It manages connection state, event handlers, reconnection logic, and logging. The class initializes a Socket.IO connection with configurable reconnection parameters and emits internal events upon connection/disconnection. It uses a `Map` to store event handlers and tracks reconnection attempts and delays.

## Key Functions

### ``constructor()``

Initializes Socket.IOBox with default values for connection state, reconnection logic, and event handlers.

### ``initialize(url)``

Establishes a Socket.IO connection to a specified URL (defaults to current origin) with configurable transport options (websocket/polling), reconnection settings, and timeout.

### ``connect` event`

Resets reconnection attempts and logs connection success.

### ``disconnect` event`

Handles disconnection (logs if unintentional) and does not trigger further reconnection attempts.

## Usage

1. Instantiate `SocketIOBox`:
   ```javascript
   const socketBox = new SocketIOBox();
   ```
2. Call `initialize(url)` to connect:
   ```javascript
   socketBox.initialize('https://example.com/socket.io');
   ```
3. Register event handlers via `eventHandlers` Map:
   ```javascript
   socketBox.eventHandlers.set('customEvent', (data) => { ... });
   ```
4. Emit internal events (e.g., `socket-connected`) to trigger logic.

## Dependencies

> ``socket.io` (client library)`
> ``window.loggingBox` (optional logging utility)`
> ``window.location` (for URL resolution).`

## Related

- [[Socket]]
- [[Reconnection Strategies Guide]]

>[!INFO] Important Note
> The `maxReconnectAttempts` is set to `Infinity`, allowing unlimited reconnection attempts. Adjust this if strict limits are needed.

>[!WARNING] Caution
> If `window.loggingBox` is unavailable, console logs will be used instead. Ensure logging is properly implemented for debugging.
