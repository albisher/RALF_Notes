**Tags:** #UI/UX, #FeedbackTracking, #IterationManagement, #DesignSystem, #ComponentBasedArchitecture
**Created:** 2026-01-13
**Type:** documentation-research

# FEEDBACK_TRACKING

## Summary

```
Tracks UI/UX feedback and design iterations for a card-based timeline system, focusing on visual layout, workflow stages, and component-based architecture improvements.
```

## Details

> This file documents iterative feedback for a **card-based timeline UI system**, evolving from Iteration 04 through 07. It emphasizes **user interface refinements**, **color schemes**, and **component reuse** while maintaining consistency with prior design choices. The process includes **timeline improvements**, **world management systems**, and **responsive layout adjustments** for better usability. Architectural decisions focus on modular components and standardized styling (e.g., color schemas) to ensure maintainability.

## Key Functions

### `Feedback Tracking`

Logs user preferences, design changes, and iteration decisions.

### `Timeline Card System`

Manages side/primary timelines, card selection, and visual feedback.

### `World Management`

Handles world conventions, time systems, and rules via a settings dialog.

### `Workflow Stages`

Dynamically updates UI columns based on selected stage (e.g., Generate, Link, Story).

### `CardViewer UI`

Production-ready card viewer (`cardview.html`) with embedded functionality.

### `Color Schema`

Centralized style documentation (`styles/color-schema.html`) for consistency.

## Usage

1. **Iteration Review**: Compare feedback across iterations (e.g., 04→05 vs. 06→07) to identify trends.
2. **Component Testing**: Use `cardview.html` for prototyping with embedded mode (`?embedded=true`).
3. **Architecture**: Apply component-based design (e.g., reusable boxes) and color schemas to new features.
4. **Documentation**: Reference `README.md` and `CARDVIEWER_DOCUMENTATION.md` for implementation details.

## Dependencies

> ``ui-explorations/cardview-iterations/``
> ``ui-explorations/``
> ``box-components.js``
> ``styles/color-schema.html``
> `Obsidian notes for related design docs.`

## Related

- [[README]]
- [[design-systems]]
- [[`FEEDBACK_TRACKING`]]
- [[`UI_COMPONENTS`]]

>[!INFO] **Critical Version**
> The **`cardview.html`** (Iteration 6) is the stable production UI—all future iterations should embed this version. Avoid hardcoding changes unless explicitly approved by feedback iterations.

>[!WARNING] **World Dialog Caution**
> World-related settings (e.g., time systems) were moved to a **settings dialog** (Iteration 6) to prevent clutter. Ensure new features integrate here, not as standalone UI elements.
