**Tags:** #visual-programming, #block-based, #mission-creation, #swarm-robotics, #ui-component
**Created:** 2026-01-13
**Type:** code-notes

# visual-swarm-programmer-component

## Summary

```
Block-based visual programming interface for mission creation in a swarm robotics system.
```

## Details

> This component implements a drag-and-drop visual programming environment where users can design mission sequences for swarm robots. The UI includes categorized blocks for movement, control, and formations, allowing users to assemble logic visually. The template renders a header with controls (clear, generate, save) and a palette of draggable blocks. The component is designed for Phase 3 of a swarm-robotics project, marked as low priority but intended for future enhancement.

## Key Functions

### `dragStart`

Handles drag events for block categorization (e.g., 'move_to', 'hover', 'follow').

### `clearBlocks`

Clears the current visual program.

### `generateCode`

Converts the visual program into executable mission logic.

### `saveMission`

Saves the constructed mission sequence.

## Usage

1. Import the component into a Vue.js application.
2. Use the template to render the UI with draggable blocks.
3. Drag blocks from the palette to the workspace to build mission logic.
4. Use buttons to clear, generate, or save the mission.

## Dependencies

> `Vue.js (for reactivity and event handling)`
> `Vuex or Pinia (likely for state management of the program blocks)`
> `possibly custom swarm-robotics logic libraries.`

## Related

- [[visual-programming-blocks]]
- [[swarm-robotics-mission-planner]]

>[!INFO] Missing Closing Tag
> The template string for the `template` property is incomplete and lacks a closing `</div>` for the `blocks-palette` section, which could cause rendering errors.

>[!WARNING] Event Handler Naming
> The `dragstart` handler is defined inconsistently (e.g., `dragStart` vs. `dragstart` in the template). Ensure all event handlers use the same naming convention to avoid runtime errors.
