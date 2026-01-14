**Tags:** #CSS, #CSSVariables, #UI/UXImprovement, #Centralization, #HardcodedColorRemoval, #BorderRadiusStandardization, #GenerateStageFixes
**Created:** 2026-01-13
**Type:** documentation

# css-variables-centralization-20251121

## Summary

```
Centralized CSS variables and eliminated hardcoded styles in the Generate stage to improve maintainability and consistency.
```

## Details

> This document details a CSS refactoring effort to replace hardcoded colors and inconsistent border-radius values in the Generate stage of a UI application. The project centralized all CSS variables into a dedicated `color-scheme.css` file, ensuring consistent theming across the application. It replaced 25 instances of hardcoded values with CSS variables, improving reusability and reducing duplication. The changes were verified to ensure no breaking changes and full compliance with the centralized style system.

## Key Functions

### `color-scheme.css`

Defines reusable CSS variables for colors, borders, shadows, and overlays.

### `generate-stage.css`

Applies Generate stage-specific styles using centralized variables.

### `generated-content.css`

Manages styles for dynamically generated UI content.

### `common.css`

Contains shared styles for reusable UI components.

### `workflow.css`

Handles styles for workflow-specific elements (e.g., timelines).

## Usage

1. **Add CSS Variables**: Define new variables in `color-scheme.css` for consistent theming.
2. **Replace Hardcoded Values**: Use CSS variables (`var(--variable-name)`) in other CSS files instead of direct color/value declarations.
3. **Verify Consistency**: Check all files in `ui-beta/src/styles/` for compliance with centralized styles.
4. **Test Overrides**: Ensure intended overrides (e.g., dark/light theme buttons) work as expected.

## Dependencies

> ``ui-beta/src/styles/``
> `CSS modules`
> `CSS preprocessor (e.g.`
> `Sass/SCSS)`
> `Linter (e.g.`
> `Stylelint).`

## Related

- [[CSS Best Practices Guide]]
- [[UX Testing Report 20251121]]
- [[CSS Variable Documentation]]

>[!INFO] Intentional Overrides
> Button styles in `common.css` and `generate-stage.css` intentionally duplicate definitions to support dark/light theme variations. Overrides are applied via CSS specificity or inheritance rules.

>[!WARNING] Timeline Exceptions
> Hardcoded colors in `workflow.css` remain for timeline-specific visuals (e.g., markers, labels). These are non-Generate-stage concerns and are intentionally excluded from the refactor.
