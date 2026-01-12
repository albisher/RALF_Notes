**Tags:** #CSS, #UI-Design, #Layout-Fix, #Flexbox, #Horizontal-Stacking, #Simulation-Page
**Created:** 2026-01-12
**Type:** code-notes

# simulation/frontend/styles/layout.css

## Summary

```
Fixes vertical stacking in a UI simulation page by implementing horizontal flex layout and refining sidebar/content area styling.
```

## Details

> The fix addresses a layout issue where UI elements (sidebar, content area, and logs sidebar) were vertically stacked in a narrow left column, leaving unused horizontal space. The solution involves:
> 1. Applying `display: flex` with `flex-direction: row` to `.simulation-page` to enable horizontal arrangement.
> 2. Adjusting `.content-area` to use flexbox internally (`flex-direction: column`) while allowing it to expand horizontally (`flex: 1`).
> 3. Standardizing the right sidebar (logs) with fixed width (`25%`) and gradient background for consistency with the left sidebar.

## Key Functions

### ``.simulation-page``

Horizontal flex container wrapping all UI components.

### ``.content-area``

Middle section that expands horizontally (`flex: 1`) and stacks visualizations vertically.

### ``.right-sidebar``

Right-aligned logs sidebar with scrollable content and gradient styling.

## Usage

Apply these CSS rules to `simulation/frontend/styles/layout.css` to enable horizontal layout in the simulation page. Ensure the parent container (`.simulation-page`) has `width: 100%` and `height: 100%` to respect the layout.

## Dependencies

> `- None (pure CSS modifications).`

## Related

- [[ (Obsidian wikilink to parent styles directory)]]

>[!INFO] Critical Flexbox Property
> `flex: 1` on `.content-area` forces it to take remaining space, but `min-width: 0` prevents overflow issues when content shrinks below its natural size.

>[!WARNING] WebKit Scrollbar Fix
> Custom scrollbar styling for `.right-sidebar` requires `-webkit-` prefixes (e.g., `::-webkit-scrollbar`). Cross-browser compatibility may need additional vendor prefixes.
