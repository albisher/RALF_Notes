# Roadmap: Phase 11 - File Organization System

**Feature:** `ralf-notes organize` (and pipeline integration)
**Purpose:** Clean up filenames and organize documents into meaningful folder structures.
**Status:** Planned
**Date:** January 2026

---

## 🎯 Goal

Transform the flat or messy output directory into a clean, structured knowledge base.
1.  **Remove Artifacts:** Strip sorting numbers (`001-`, `12_`) from filenames.
2.  **Structure:** Move files into subfolders based on their content type or source origin.

## 📦 Components

### 1. Name Sanitizer
**Responsibility:** Clean up filenames.
**Logic:**
-   Regex strip: `^\d+[-_.]*` (Removes `01-`, `0002_`, `1.`)
-   Case normalization: Option for `lower` or `keep`.
-   Space handling: Replace spaces with `-` (kebab-case) or `_` (snake_case).

### 2. Folder Strategist
**Responsibility:** Determine the destination folder for a file.
**Strategies:**
-   **`mirror` (Default):** Replicates the relative path of the source file.
    -   Source: `project/core/auth.py` -> Target: `docs/core/auth.md`
-   **`type`:** Uses the `TYPE` metadata field from generation.
    -   Type: `API Reference` -> Target: `docs/API Reference/filename.md`
-   **`tag`:** Uses the first primary tag.
    -   Tag: `#database` -> Target: `docs/database/filename.md`
-   **`flat`:** Keeps everything in root (current behavior).

### 3. File Mover
**Responsibility:** Safely move files to their calculated destinations.
-   Handles collisions (e.g., if `01-test.md` and `02-test.md` both become `test.md`).
-   Updates internal links if necessary (Phase 10 integration).

## 🎮 CLI Integration

### `ralf-notes organize`
Stand-alone command to organize an existing directory.
```bash
ralf-notes organize [TARGET_DIR] --strategy [mirror|type|tag] --clean-names
```

### Pipeline Integration
Add configuration options to `generate` command to perform this automatically during Stage 3 (Finalize).
```json
{
  "organize_strategy": "type",
  "clean_filenames": true
}
```

## 📝 Implementation Plan

1.  **Create `ralf_notes/organization/` module.**
2.  **Implement `NameSanitizer` class.**
3.  **Implement `FolderStrategist` class.**
4.  **Integrate into `finalize` step.**
5.  **Add `organize` CLI command.**

---

This phase ensures that the "physical" structure of the files matches the high quality of their content.
