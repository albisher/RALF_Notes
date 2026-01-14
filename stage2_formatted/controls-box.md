**Tags:** #React-UI-Components, #Utility-Functions, #Component-Creation, #Frontend-Development
**Created:** 2026-01-13
**Type:** code-notes

# controls-box

## Summary

```
A utility object consolidating reusable UI control components for a web application.
```

## Details

> This `ControlsBox` object provides modular, reusable React-like UI components for common interactive elements. Each function returns an object with properties defining component state, event handlers, and class names for styling. Components include buttons, inputs, selectors, and filtering logic, designed for modular integration into larger applications.
> 
> The `timeScaleSelector` is highlighted as the primary implementation for time-based scaling, replacing potential duplicates in another file.

## Key Functions

### `likeButton`

Creates a like/dislike button with state (`isLiked`) and counter (`count`).

### `commentField`

Generates a text input field with `value`, `onChange`, and `onSave` handlers.

### `actionButton`

Builds a styled button with `label`, `onClick`, `variant` (primary/secondary/danger/success), and optional `icon`.

### `selector`

Implements a dropdown/select component with `options`, `selectedValue`, and `onChange`.

### `checkboxGroup`

Creates a group of checkboxes with `options`, `selectedValues`, and `label`.

### `searchInput`

Designs a searchable input with `value`, `onChange`, and `placeholder`.

### `filterPanel`

Handles dynamic filtering with `filters`, `onFilterChange`, and `onClear`.

### `sortControls`

Manages sorting logic with `sortBy`, `sortOrder`, and predefined `options`.

### `timeScaleSelector`

Provides time-based selection (e.g., day/week/month/year) with `currentScale` and `onScaleChange`.

## Usage

1. Import `ControlsBox` in a React component:
   ```javascript
   import ControlsBox from './controls-box';
   ```
2. Use any component by passing required props:
   ```javascript
   const LikeButton = ControlsBox.likeButton(true, 42, () => console.log('Liked!'));
   ```
3. Apply classes via `classes` property for styling.

## Dependencies

> `None (pure utility functions; no external libraries required).`

## Related

- [[controls-box]]
- [[boxes.js (if `timeScaleSelector` is duplicated elsewhere).]]

>[!INFO] **Modularity**
> Components are stateless and designed for direct integration into React components. Override `classes` for custom styling.

>[!WARNING] **Default Values**
> Some props (e.g., `variant`, `placeholder`) default to values (e.g., `'primary'`), but passing `null` or empty strings may break rendering. Always validate inputs.
