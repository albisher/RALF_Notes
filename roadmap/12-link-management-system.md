# Roadmap: Phase 10 - Link Management System

**Feature:** `ralf-notes links analyze` and `ralf-notes links fix`
**Purpose:** Ensure all wikilinks in generated documentation point to valid files.
**Status:** Planned
**Date:** January 2026

---

## 🎯 Goal

Enhance the quality of generated documentation by validating and fixing wikilinks. The system currently generates links based on the LLM's understanding, which can lead to:
- Broken links (linking to non-existent files)
- "None" links (linking to "none" or placeholder text)
- Orphan files (files that are never linked to)

## 📦 Components

### 1. Link Collector
**Responsibility:** Scan all markdown files in the target directory and extract all outgoing wikilinks.
**Output:** A map of `{source_file: [list_of_links]}`.

### 2. Link Validator
**Responsibility:** Check if each extracted link corresponds to an actual file in the `target_dir`.
**Logic:**
- Exact match check (`[[filename]]` -> `filename.md`)
- Case-insensitive check
- "None" check

### 3. Link Resolver (Fuzzy Matching)
**Responsibility:** Attempt to find the correct target for broken links.
**Strategies:**
- **Extension mismatch:** Link `[[utils.py]]` -> Target `utils.md`
- **Path mismatch:** Link `[[core/utils]]` -> Target `utils.md`
- **Fuzzy name match:** Link `[[auth]]` -> Target `authentication.md`

### 4. Link Refiner
**Responsibility:** Apply fixes to the markdown files.
**Actions:**
- Update broken links with resolved targets.
- Remove invalid/none links.
- Generate a report of orphan files.

## 🎮 CLI Commands

### `ralf-notes links analyze`
- Scans the directory.
- Reports:
    - Total links found.
    - Number of broken links.
    - Number of "none" links.
    - List of orphan files.
- Generates a `link_refinement_guide.json` (similar to tags).

### `ralf-notes links fix`
- Reads `link_refinement_guide.json`.
- Applies fixes to files (with backup).
- Reports changes made.

## 📝 Implementation Plan

1.  **Create `ralf_notes/linking/` module.**
2.  **Implement `LinkCollector` and `LinkValidator`.**
3.  **Implement `LinkResolver` with fuzzy matching.**
4.  **Implement `LinkRefiner` logic.**
5.  **Add CLI commands to `ralf_notes/cli.py`.**
6.  **Add tests.**

---

This phase will significantly improve the navigability and cohesiveness of the generated knowledge base.
