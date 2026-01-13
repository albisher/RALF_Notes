# Roadmap: Phase 10 - Link Management System

**Feature:** `ralf-notes links analyze` and `ralf-notes links apply`
**Purpose:** Ensure all wikilinks in generated documentation point to valid files, eliminating broken references and "hallucinations".
**Status:** Planned
**Date:** January 2026

---

## 🎯 Goal

Enhance the quality of generated documentation by validating, sanitizing, and fixing wikilinks. The system currently generates links based on the LLM's understanding, which can lead to:
- Broken links (linking to non-existent files)
- "None" links (linking to "none" or placeholder text)
- Orphan files (files that are never linked to)
- Ambiguous links (multiple files with similar names)

**Lesson Learned from Tags:** We must enforce strict sanitization rules (no "none", no weird characters) and provide a clear "schema" report of what actually exists in the system.

## 📦 Components

### 1. Link Collector
**Responsibility:** Scan the **entire body** of all markdown files (recursively) to extract every wikilink `[[...]]`.
**Output:** 
- `all_links`: Map of `{source_file: [list_of_outgoing_links]}`.
- `file_index`: Set of all valid filenames in the target directory (e.g., `{'auth.md', 'utils.md'}`).

### 2. Link Validator & Sanitizer
**Responsibility:** 
- **Sanitize:** Filter out invalid links immediately (e.g., `[[none]]`, `[[null]]`, empty links).
- **Validate:** Check if `[[link]]` matches a file in `file_index`.
- **Logic:**
    - Exact match check (`[[filename]]` -> `filename.md` exists?)
    - Case-insensitive check (Obsidian is often case-insensitive).

### 3. Link Resolver (Fuzzy Matching)
**Responsibility:** Attempt to find the correct target for broken links.
**Strategies:**
- **Extension mismatch:** Link `[[utils.py]]` -> Target `utils.md`
- **Path mismatch:** Link `[[core/utils]]` -> Target `utils.md`
- **Fuzzy name match:** Link `[[auth]]` -> Target `authentication.md` (using Levenshtein distance or similar).

### 4. Link Refiner (The "Replacer")
**Responsibility:** Apply fixes to the markdown files based on the refinement guide.
**Actions:**
- Replace broken links with resolved targets.
- Remove invalid/none links entirely.
- Generate a comprehensive report (`applied_links.md`).

## 🎮 CLI Commands

### `ralf-notes links analyze`
- Scans the directory.
- Reports:
    - Total links found.
    - Number of broken links.
    - Number of "none" links to be removed.
    - List of orphan files (files with 0 incoming links).
- Generates `link_refinement_guide.json` proposing fixes:
  ```json
  {
    "fixes": [
      {"file": "doc1.md", "old": "[[auth]]", "new": "[[authentication]]"},
      {"file": "doc2.md", "old": "[[none]]", "new": null} 
    ]
  }
  ```

### `ralf-notes links apply`
- Defaults to reading `link_refinement_guide.json`.
- Applies fixes to files (with backup).
- **Report (`applied_links.md`):** 
    - Lists all **active, valid links** in the system (the "Link Schema").
    - Lists all **orphan files** (helps identifying disconnected documentation).

## 📝 Implementation Plan

1.  **Create `ralf_notes/linking/` module.**
2.  **Implement `LinkCollector`:** Regex-based scanning of full file content.
3.  **Implement `LinkResolver`:** Logic for mapping broken links to existing files.
4.  **Implement `LinkRefiner`:** Logic to text-replace links in files.
5.  **Add CLI commands to `ralf_notes/cli.py`** (`analyze`, `apply`).
6.  **Add tests:** Ensure fuzzy matching and replacement don't break valid content.

---

This phase will significantly improve the navigability and cohesiveness of the generated knowledge base, creating a truly connected "Obsidian Graph".
