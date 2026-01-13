# Feedback: Link Management System Proposal

**Date:** January 13, 2026
**Topic:** WikiLink Validation and Refinement

## Problem Statement
The current system allows the LLM to generate "Related" links freely. This leads to several issues:
1.  **Broken Links:** The LLM might guess a filename (e.g., `[[AuthModule]]`) that doesn't match the actual generated file (e.g., `authentication.md`).
2.  **"None" Links:** Sometimes the LLM outputs `[[None]]` or `[[none]]` despite prompt instructions.
3.  **Inconsistent Naming:** Links might include extensions (`[[file.py]]`) whereas the system generates `.md` files.

## Proposed Solution: Link Management System (Phase 10)

Introduce a post-processing step similar to the Tag Refinement System.

### Key Features

1.  **Validation:**
    - Verify that every `[[link]]` points to an existing file in the documentation folder.
    - Flag links that point to nowhere.

2.  **Smart Resolution:**
    - If a link is broken, try to find the intended target.
    - **Extension Stripping:** `[[file.py]]` -> match `file.md`.
    - **Fuzzy Matching:** Use string similarity to find the closest valid filename.

3.  **Cleanup:**
    - Automatically remove links that are explicitly "none".
    - Remove self-references (linking to the file itself).

4.  **Reporting:**
    - Identify **Orphan Files**: Documentation files that are not linked to by any other file. This helps identify isolated parts of the codebase.

### Integration

-   **CLI:** New `links` command group (`analyze`, `fix`).
-   **Pipeline:** Optionally integrate a "link check" step at the end of `generate` (Stage 3).

### Expected Impact
-   **High quality navigation:** Users can trust that clicking a link works.
-   **Better graph view:** The Obsidian graph view will be cleaner and more accurate.
-   **Professional polish:** Eliminates "hallucinated" links.

## Next Steps
-   Approve `roadmap/12-link-management-system.md`.
-   Begin implementation of `ralf_notes/linking/` module.
