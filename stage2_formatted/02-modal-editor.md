**Tags:** #UI-Design, #Modal-UI, #Event-Editor, #Vue-Component, #Accessibility
**Created:** 2026-01-13
**Type:** documentation

# 02-modal-editor

## Summary

```
Design iteration for a modal-based event editor system in a timeline application, optimizing user interaction by moving the editor to an overlay.
```

## Details

> This design iteration introduces a **modal/overlay-based event editor** that appears when an event is selected, freeing the middle column for dynamic content like event relationships or visualizations. The system uses a **3-column layout** (Timeline Events, Event Preview, Timeline Settings) with the editor overlaying the timeline view. The modal ensures full focus on editing while maintaining accessibility features like focus trapping and keyboard navigation (ESC/X to close). The preview component in the middle column provides a quick summary of the selected event, with a "Click to edit" call-to-action, while the right column retains persistent settings.

## Key Functions

### ``EventEditorModal``

Vue component that renders a full-screen modal for editing events, triggered by event selection. Uses `Teleport` for overlay placement and includes close functionality via ESC or X button.

### ``EventPreview``

Displays a summary card of the selected event in the middle column, with quick actions (edit, link, create chapter) and immediate updates when the event changes.

### ``EventEditorForm``

Internal form component within the modal for editing event details (name, date, type, key year status).

### ``handleSave`/`handleDelete``

Event handlers in the modal for saving edited event data or deleting events.

### ``openEditor`/`linkToCard``

Preview component functions to trigger modal opening or card linking.

## Usage

1. **Select an Event**: Click an event in the left column to trigger a preview in the middle column.
2. **Edit via Modal**: Click the "Edit Event" button in the preview or double-click the event to open the modal.
3. **Edit in Modal**: Use the form to update event details, then save or delete.
4. **Close Modal**: Press ESC or click the X button. The preview updates automatically.

## Dependencies

> `Vue.js (for component rendering)`
> `Vue Teleport (for modal overlay)`
> `Vuex/Pinia (likely for state management of selected events)`
> `Tailwind CSS or similar CSS framework (for styling)`
> `Accessibility libraries (e.g.`
> `ARIA attributes).`

## Related

- [[Design Iteration 1: Timeline Layout]]
- [[Accessibility Guidelines for UI Components]]
- [[Mobile UI Adaptations]]

>[!INFO] **Accessibility Focus Trapping**
> The modal includes `@click.self` and `@keydown.esc` to ensure keyboard users can navigate within the modal without escaping to the body. Focus remains trapped inside the modal until explicitly closed.


>[!WARNING] **Mobile Considerations**
> Modals may disrupt mobile UX due to reduced screen real estate. For mobile, consider **bottom-sheet variants** (Variation C) or **slide-over panels** (Variation A) to maintain usability. Always test on small screens.
