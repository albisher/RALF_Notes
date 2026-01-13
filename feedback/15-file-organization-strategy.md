# Feedback: File Naming and Organization Strategy

**Date:** January 13, 2026
**Topic:** Improving File Naming and Folder Structure for Generated Documentation

## Problem
Currently, RALF Notes generates documentation in a relatively flat structure (or mirrors source paths exactly).
1.  **Numbering Artifacts:** Input files often contain ordering prefixes (e.g., `0001-overview.md`, `01-intro.md`) which clutter the filename and become irrelevant as the knowledge base grows.
2.  **Flatness/Clutter:** As the number of files grows (hundreds/thousands), navigating a single directory becomes difficult.
3.  **Context Loss:** Without folder grouping, it's harder to see which documents relate to specific modules or topics at a glance.

## Research & Best Practices

### 1. File Naming
-   **Semantic Naming:** Filenames should describe contents, not order.
-   **Kebab-case:** `user-authentication.md` is preferred over `UserAuthentication.md` or `user_authentication.md` in web/URL-friendly contexts, though Obsidian handles spaces well. Kebab-case is generally safest.
-   **Remove Prefixes:** Ordinal prefixes (`001-`) make sense for a linear book, but not for a networked knowledge base (digital garden).
    -   *Recommendation:* Strip regex pattern `^\d+[-_.]+` from filenames.

### 2. Folder Organization Strategies
There are two main approaches to organizing code documentation:

#### A. Source Mirroring (Structural)
Replicate the directory structure of the source code.
-   **Pros:** Predictable, easy to find "code buddy" file, distinct namespaces.
-   **Cons:** Doesn't group cross-cutting concerns (e.g., "Architecture" docs might be scattered).
-   **Example:** `src/auth/login.py` -> `docs/src/auth/login.md`.

#### B. Topic/Tag-based Grouping (Semantic)
Group files based on their content type or tags.
-   **Pros:** Great for high-level browsing (e.g., all `API` docs together).
-   **Cons:** Can be ambiguous (file belongs to multiple tags).
-   **Example:** Tags: `#api`, `#auth` -> `docs/API/Auth/login.md`.

## Proposal: "Organization System" (Phase 11)

We should introduce a flexible organization step in the pipeline (or a standalone command `ralf-notes organize`).

### Features

1.  **Name Sanitizer:**
    -   Automatically strips numeric prefixes (`01-`, `0001_`).
    -   Normalizes to kebab-case (optional but recommended).

2.  **Smart Grouping:**
    -   **Default:** "Smart Mirror". Use source path but map to target.
    -   **Option:** "Semantic Folders". Use the `TYPE` field from the structured text (e.g., `Architecture`, `API`, `Guide`) to create top-level folders.

3.  **Implementation:**
    -   Add `clean_filename` method to `DocumentPipeline`.
    -   Allow configuring a `folder_strategy` in `config.json`.

## Conclusion
Adopting **Name Sanitization** (removing numbers) and **Semantic Folder Grouping** (based on `TYPE` or Source Path) will significantly improve the "shelf appeal" of the generated vault.
