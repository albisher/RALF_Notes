**Tags:** #UI-component, #generation-tool, #reactive-UI, #aspect-selection, #box-components
**Created:** 2026-01-13
**Type:** code-library

# generate-box

## Summary

```
Creates modular UI components for a generative content system, enabling user interaction via selectors, checkboxes, and input controls.
```

## Details

> This code defines a utility object `GenerateBox` containing reusable UI components for a content generation system. It consolidates multiple box types (e.g., generator selector, content display) into modular functions that return structured configurations. The `generatorSelector` function provides dropdown categories (e.g., "Physical Form," "Personality") for selecting generation parameters. The `generatedContentDisplay` extends a base UI component (`UIBoxes.generatedResult`) with additional interactive controls like edit, like, and comment buttons. The `hashInput` and `aspectCheckboxes` components handle text input and checkbox-based aspect selection (e.g., physical, personality, location). Dependencies include `UIBoxes` for core generated result logic. The code exports the object for modular reuse in a Node.js environment.

## Key Functions

### `generatorSelector`

Returns a dropdown UI for selecting generation categories (e.g., "Physical Form") with predefined options.

### `generatedContentDisplay`

Displays generated content with interactive controls (edit, like, comment) while extending a base UI component.

### `generationControls`

Provides buttons for actions like liking, commenting, or attaching metadata (e.g., time/location).

### `hashInput`

Manages a text input field for user-provided hash values to trigger generation.

### `aspectCheckboxes`

Renders checkboxes for selecting aspects (e.g., "physical," "personality") dynamically.

## Usage

1. Import `GenerateBox` in a Node.js environment:
   ```javascript
   const GenerateBox = require('./generate-box');
   ```
2. Use individual functions to render components:
   ```javascript
   const generators = ['plant', 'building'];
   const selectedGenerator = 'plant';
   const component = GenerateBox.generatorSelector(generators, selectedGenerator, (gen) => console.log(gen));
   ```
3. Pass callbacks (e.g., `onSelect`, `onChange`) to handle user interactions.

## Dependencies

> ``UIBoxes` (from `boxes.js`)`
> ``module.exports` (Node.js module system).`

## Related

- [[UIBoxes]]
- [[boxes]]

>[!INFO] Dynamic Categories
> Categories like "Physical Form" or "Personality" are hardcoded but can be extended by modifying the `categories` object in `generatorSelector`.

>[!WARNING] Dependency Risk
> If `UIBoxes` is missing or malformed, `generatedContentDisplay` may fail silently due to fallback logic (`null` checks). Ensure `UIBoxes` is properly imported.
