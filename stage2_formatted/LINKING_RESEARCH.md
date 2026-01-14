**Tags:** #visual-linking, #knowledge-graph, #interactive-ui, #world-building, #timeline-navigation, #mind-mapping, #data-visualization, #ui-ux-patterns, #card-based-system
**Created:** 2026-01-13
**Type:** research

# LINKING_RESEARCH

## Summary

```
Explores modern linking methods for a space-themed world-building application emphasizing timeline-first navigation and visual relationship visualization.
```

## Details

> This document analyzes existing and emerging linking patterns for a card-based system focused on linking cards by type (characters, locations, events) across time and space. It evaluates three primary approaches: **bi-directional visual connectors**, **brushing and linking**, and **graph/network views**, comparing their strengths and limitations. The research emphasizes integrating these methods with existing visual language (color coding, timeline, map) to enhance navigation and storytelling.

## Key Functions

### `Executive Summary`

Highlights key findings on combining visual connectors, brushing, and graph views for effective linking.

### `Current State Analysis`

Documents existing UI components (e.g., `link-box.js`, timeline/map integration) and their limitations.

### `Modern Linking Patterns`

Describes detailed implementations of visual connectors, brushing, and graph/network views with visual examples.

### `Recommended Approaches`

Suggests prioritizing brushing and graph views for scalability and context awareness.

### `Visual Concepts`

Defines visual treatments (e.g., color-coded lines, node sizes) for relationships.

### `Implementation Strategy`

Outlines phased integration of linking features into the existing workflow.

## Usage

To apply this research:
1. **Analyze existing UI** (e.g., `link-box.js`) to identify gaps in visual linking.
2. **Implement brushing** in timeline/map views to highlight related cards/locations.
3. **Add graph/network view** as a dedicated panel for visualizing the knowledge network.
4. **Enhance link stage** with visual connectors for drag-and-drop creation.
5. **Standardize visual treatments** (e.g., color-coded lines) across all views.

## Dependencies

> `Obsidian graph view framework`
> `Scrintal/FigJam-inspired drag-and-drop libraries`
> `spatial/timeline visualization libraries (e.g.`
> `D3.js)`
> `custom UI components (`link-box.js`).`

## Related

- [[Space Peral World-Building UI Explorations]]
- [[Knowledge Graph Implementation Guide]]
- [[UX Patterns for Interactive Dashboards]]

>[!INFO] Key Insight
> Prioritize **brushing and graph views** for passive discovery and network visualization, as they align best with timeline-first navigation while minimizing UI clutter.

>[!WARNING] Scalability Risk
> Overuse of visual connectors may lead to clutter; implement constraints (e.g., line thickness based on connection strength) to manage complexity.

>[!INFO] Existing Strengths
> Leverage your established color coding and timeline/map integration to reinforce linking visuals (e.g., use entity colors for lines in graph view).

>[!WARNING] Context Awareness
> Ensure brushing highlights maintain consistency across views (e.g., same color for linked cards/locations) to avoid cognitive dissonance.

>[!INFO] Timeline-Spatial Tradeoff
> Balance timeline-first navigation with spatial context by dynamically adjusting graph/network layouts (e.g., force-directed vs. manual) based on user focus.
