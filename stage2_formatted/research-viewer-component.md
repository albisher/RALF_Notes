**Tags:** #VueJS, #Markdown, #UI-Component, #ResearchViewer, #Reactivity, #ConditionalRendering
**Created:** 2026-01-13
**Type:** code-notes

# research-viewer-component

## Summary

```
Displays markdown-formatted research documents with loading/error states and a close button.
```

## Details

> This Vue.js component renders a research document viewer that dynamically displays markdown content when a `selectedResearch` prop is provided. It handles conditional rendering for loading states, errors, and empty states. The component injects basic markdown styling and emits a `close-viewer` event when the close button is clicked. The `watch` directive triggers document loading when `selectedResearch` changes, ensuring content updates reactively.

## Key Functions

### ``loadResearchDocument(path)``

(Implicitly called via `watch`): Loads and processes the research document from the given path, rendering it as HTML.

### ``renderedContent``

Stores the processed markdown content for display.

### ``loading`/`error``

State variables to track document loading status and errors.

## Usage

```javascript
<ResearchViewerComponent
    :selectedResearch="researchDoc"
    @close-viewer="handleClose"
/>
```
- **Props**: `selectedResearch` (object with `title` and `path` properties).
- **Emits**: `close-viewer` (triggered when the close button is clicked).

## Dependencies

> ``vue` (for reactivity and template rendering)`
> ``vue-template-parser` (likely for markdown rendering`
> `though not explicitly imported in snippet).`

## Related

- [[research-document-parser]]
- [[markdown-stylesheet-injector]]

>[!WARNING] Missing Implementation
> The `loadResearchDocument` method is referenced but not defined in the snippet. It should fetch the document from `path` (likely a URL or file path) and parse it into HTML.
> **Fix**: Implement a function like:
> ```javascript
> async loadResearchDocument(path) {
>   this.loading = true;
>   try {
>     const response = await fetch(path);
>     const content = await response.text();
>     this.renderedContent = this.parseMarkdown(content); // Assume a parser exists
>   } catch (err) {
>     this.error = err.message;
>   } finally {
>     this.loading = false;
>   }
> }
> ```

>[!INFO] Styling Note
> The component uses inline styles for consistency but could benefit from a CSS module or global stylesheet for maintainability.
