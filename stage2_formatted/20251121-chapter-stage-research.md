**Tags:** #user-interface, #content-management, #card-based-system, #writing-assist, #multi-page-documentation
**Created:** 2026-01-13
**Type:** documentation-research

# 20251121-chapter-stage-research

## Summary

```
Research document outlining Chapter stage features for a card-based writing system, focusing on card selection, chapter organization, and page creation workflows.
```

## Details

> This document analyzes the **Chapter Stage** of a digital writing platform, detailing how users can organize content by selecting cards (e.g., characters, locations) and structuring them into multi-page chapters. The system leverages a hierarchical card model (Story → Chapters → Pages) where chapters are stored as cards of type 'chapter' and pages as 'page' cards linked via `metadata.chapter_id`. Core functionality includes filtering, multi-select card browsing, and rich text editing for pages, while metadata like `combined_entity_data` and `notes` enables deep integration of card attributes (e.g., personality traits, coordinates) into chapter content.
> 
> The design emphasizes modular panels for **chapter metadata**, **card selection**, **notes**, and **pages management**, with optional writing prompts to guide narrative development. Dependencies include the Card model (JSONB fields like `combined_entity_data`, `image_url`) and external libraries for filtering/searching cards.

## Key Functions

### `Chapter Information Panel`

Manage chapter metadata (title, status, notes) and navigation.

### `Card Selection & Reference Panel`

Filterable card browser with multi-select, preview cards, and quick actions (e.g., "Start Writing").

### `Chapter Notes Panel`

Free-form and structured notes for chapter-level planning and research.

### `Pages Management Panel`

Create/edit/delete pages, preview content, and link to selected cards.

### `Writing Assistant Panel`

Dynamic prompts and references based on selected cards (e.g., personality traits, location details).

## Usage

1. **Select Cards**: Use the Card Browser to filter/search and multi-select cards relevant to the chapter.
2. **Create Chapter**: Assign a title/description and add chapter-level notes.
3. **Write Pages**: Use the Pages Management to create pages, referencing selected cards via a reference panel.
4. **Expand Notes**: Add chapter-specific notes or card-specific insights (e.g., "Character’s backstory").
5. **Use Assistant**: Trigger prompts for scene ideas or plot development based on card relationships.

## Dependencies

> `Card model (JSONB fields: `card_name``
> ``card_type``
> ``combined_entity_data``
> ``notes``
> ``image_url``
> ``coordinates`)`
> `Obsidian/Confluence-like search/filtering libraries`
> `Rich Text Editor (e.g.`
> `Slate.js)`
> `Map Integration (e.g.`
> `Leaflet)`
> `Auto-save utilities.`

## Related

- [[Card Model Documentation]]
- [[Story Stage Research]]
- [[Writing Assistant Prototypes]]
- [[Obsidian Card System Guide]]

>[!INFO] **Card Metadata Depth**
> The `combined_entity_data` (JSONB) field merges diverse attributes (e.g., personality, powers) into a unified reference for writing. Example: A character’s `powers` array could auto-suggest dialogue or conflict scenarios.

>[!WARNING] **Data Integrity Risks**
> Manual card selection may lead to inconsistencies if `metadata.chapter_id` isn’t updated during page creation. Validate links between pages and chapters post-save.

>[!INFO] **Collaborative Workflow**
> The system assumes multi-user editing; ensure `is_reference`/`is_story_element` flags are set correctly to avoid conflicts in shared chapters.

>[!WARNING] **Performance for Large Card Sets**
> Filtering/searching all cards (e.g., 10,000+) could slow down the browser. Implement caching or lazy-loading for card previews.
