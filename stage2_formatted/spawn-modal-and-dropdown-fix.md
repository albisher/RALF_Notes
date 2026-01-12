**Tags:** #bugfix, #ui-component, #modal, #dropdown, #spawn-system, #socketio, #reactive-data
**Created:** 2026-01-12
**Type:** code-notes

# spawn-modal-and-dropdown-fix

## Summary

```
Fixes issues with drone spawn modal visibility and dropdown updates after spawning.
```

## Details

> This fix addresses two critical UI/functional gaps in the drone management system: the spawn modal was invisible due to missing component registration and script loading, while the dropdown failed to reflect spawned drones due to premature Socket.IO event handling and stale data updates. The solution ensures the modal appears on spawn button clicks and properly updates the dropdown list with newly spawned drones.

## Key Functions

### ``handleQuickSpawn()``

Now opens the spawn modal instead of spawning directly.

### ``updateDrones(force)``

Added forced polling to ensure drones appear in dropdown after spawning.

### ``SpawnSelectionModalComponent``

Registered and integrated into the template for modal rendering.

### ``closeSpawnModal()``

Handles modal dismissal logic.

### ``handleSpawnFromModal(spawnData)``

Processes selected spawn configurations.

## Usage

1. **Spawn Modal**: Click the spawn button to open the modal. Select a drone type/squad/swarm and confirm to spawn.
2. **Dropdown Updates**: After spawning, drones appear in the dropdown for command selection, ensuring real-time visibility.

## Dependencies

> ``components/spawn-selection-modal-component.js``
> `Socket.IO client library`
> `Vue.js framework components (e.g.`
> ``v-if``
> ``@close`/`@spawn` directives).`

## Related

- [[spawn-system-overview]]
- [[socketio-implementation]]
- [[dropdown-component-design]]

>[!INFO] Modal Integration
> Ensure `spawn-selection-modal-component.js` is loaded in `index.html` before rendering the modal template to avoid hydration errors.

>[!WARNING] Socket.IO Timing
> If `updateDrones()` is called immediately after spawn, force `true` to bypass Socket.IO checks and refresh the drones list manually.
