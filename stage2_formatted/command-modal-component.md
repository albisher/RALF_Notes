**Tags:** #VueJS, #UI-Component, #Drone-Control, #Modal-Dialog, #Reactivity, #Form-Handling
**Created:** 2026-01-13
**Type:** code-notes

# command-modal-component

## Summary

```
A Vue.js-based modal component for sending drone commands via a dynamic form interface.
```

## Details

> `CommandModalComponent` is a Vue.js template-based component that renders a modal dialog for selecting a drone and specifying a command type (move, hover, follow). It uses reactive state (`localCommandForm`) to conditionally display form fields based on the selected command type. The component emits events (`close`) to manage visibility and handles dynamic drone selection and form validation via `v-model` bindings and conditional rendering (`v-if`). The `useCurrentPosition` method suggests using the current coordinates for a "Move To" command.

## Key Functions

### ``onCommandTypeChange``

Updates form fields dynamically based on the selected command type.

### ``useCurrentPosition``

Sets default coordinates (X, Y, Z) for a "Move To" command using the current values in `localCommandForm`.

## Usage

1. Import and use the component in a Vue app:
   ```html
   <CommandModalComponent @close="handleClose" ref="modal" />
   ```
2. Provide drones data via `drones` prop:
   ```js
   this.drones = [{ name: "Drone1", type: "quadrotor" }];
   ```
3. Trigger the modal via a button or event:
   ```js
   this.$refs.modal.show = true;
   ```
4. Handle emitted commands (e.g., `move_to` with coordinates) in parent logic.

## Dependencies

> `Vue.js (with `v-model``
> ``v-if``
> ``@click.self``
> ``@emit`)`
> `Vuex/Pinia (implicitly for drone data/dispatch).`

## Related

- [[drone-command-handler]]
- [[vue-modal-template]]

>[!INFO] Dynamic Field Rendering
> The component conditionally renders fields (e.g., `move_to` inputs) based on `localCommandForm.type`, ensuring only relevant inputs are displayed.

>[!WARNING] State Management
> Ensure parent logic updates `localCommandForm` correctly to avoid stale data or validation errors. The `useCurrentPosition` button assumes `localCommandForm.droneName` exists.
