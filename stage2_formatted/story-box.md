**Tags:** #UI-Component, #Storytelling-Tool, #Rich-Text-Editor, #Data-Display, #Modular-Design
**Created:** 2026-01-13
**Type:** code-library

# story-box

## Summary

```
A modular UI library for organizing and editing narrative elements in a story structure with timeline, narrative editing, and control panels.
```

## Details

> This library (`StoryBox`) provides reusable components for building interactive story editing interfaces. It consolidates story narrative functionality from `boxes.js` and extends it with rich-text editing capabilities. The design separates the story into three columns:
> 1. **Left Column (Story Timeline)**: Displays non-chronological story elements as clickable cards.
> 2. **Middle Column (Story Narrative Editor)**: Renders rich-text content with formatting options (bold, italic, etc.) and integrates with a base narrative editor.
> 3. **Right Column (Story Controls)**: Manages actions like generating content from the timeline, adding/removing cards, and exporting/previewing stories.
> 
> Each component returns a structured object with props (e.g., `selectedElement`, `onEdit`) and CSS classes for styling. The `storyElement` and `relatedCardsList` components leverage external `UIBoxes` utilities for card rendering.

## Key Functions

### `storyTimeline`

Creates a non-chronological timeline of story elements with reordering and selection support.

### `storyNarrativeEditor`

Extends a base narrative editor with rich-text formatting and editor-specific props.

### `storyControls`

Provides action buttons for timeline-driven story generation, card management, and preview/export.

### `storyElement`

Renders a single story element (e.g., a card) with visual feedback for selection.

### `relatedCardsList`

Displays related cards (e.g., references) and allows adding them to the story.

## Usage

1. Import `StoryBox` and export it for modular use in a story editor application.
2. Instantiate components via `StoryBox.storyTimeline()`, `StoryBox.storyNarrativeEditor()`, etc., passing required props (e.g., `storyElements`, `selectedElement`).
3. Customize styling via `classes` prop and handle events (e.g., `onEdit`, `onSelect`) for interactivity.

## Dependencies

> `UIBoxes (for base narrative and card rendering)`
> `React-like DOM components (for rendering UI elements).`

## Related

- [[UIBoxes]]
- [[boxes]]
- [[React-like DOM components]]

>[!INFO] Base Dependency Check
> If `UIBoxes` is not available, `storyNarrativeEditor` and `relatedCardsList` fall back gracefully by returning `null` or empty arrays, ensuring no runtime errors.

>[!WARNING] Class Concatenation
> The `classes` array uses `.filter(Boolean)` to avoid empty strings, but manual class management is required for dynamic styling—overlapping classes may need explicit handling.
