**Tags:** #world-building, #narrative-management, #database-design, #ui/ux-enhancement, #flexible-architecture
**Created:** 2026-01-13
**Type:** planning-document

# DEVELOPMENT_ROADMAP

## Summary

```
Roadmap outlines transitioning a space-themed app into a flexible story world builder supporting diverse world types, characters, and ecosystems with missing features identified for phased implementation.
```

## Details

> This document details a **2019 vision** for expanding a space-themed application into a **comprehensive story world builder**, focusing on modular enhancements. The current system is restricted to "Space Peral" worlds, requiring a **database schema update** to support hierarchical world types (e.g., universes, solar systems) and metadata storage. The UI must be redesigned to allow dynamic world selection and configuration. Missing features include **time period classification**, **transportation systems**, and **AI-driven image generation**, prioritized for Phase 1. The roadmap emphasizes **flexibility** over rigid constraints while addressing gaps in **character/soul separation**, **creature ecosystems**, and **map generation**.

## Key Functions

### `World Type Enum Expansion`

Extends `World.world_type` to include `universe`, `solar_system`, `imaginary`, etc.

### `Hierarchical World Storage`

Adds `parent_world_id` for nested world structures (e.g., planet under solar system).

### `Dynamic UI Selection`

Modifies `CreateWorldModal` to support world type and metadata input.

### `Celestial Object Tracking`

Stores weather/environmental data via `celestial_objects` JSONB field.

### `Story Time Period Classification`

Introduces metadata tags for historical/futuristic events in timelines.

## Usage

1. **Phase 1**: Implement database schema and UI changes to enable world flexibility.
2. **Phase 2**: Add time period classification and transportation systems.
3. **Phase 3**: Integrate AI image generation and creature/plant ecosystems.

## Dependencies

> `PostgreSQL (JSONB support)`
> `Vue.js (UI components)`
> `Node.js/Backend framework (database schema updates).`

## Related

- [[15]]
- [[Backend Database Schema]]
- [[UI Component Library]]

>[!INFO] **World Hierarchy Limitation**
> Current `parent_world_id` design assumes a tree structure; future iterations may need graph-based relationships for complex universes.

>[!WARNING] **JSONB Risks**
> Overuse of JSONB may impact query performance; optimize with indexed fields for large-scale worlds.

>[!INFO] **UI Prioritization**
> Dynamic world selection must balance usability with technical complexity; test with end-users for feedback.
