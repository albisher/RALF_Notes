# Feedback: Three-Stage Documentation Pipeline Proposal

**Date:** 2026-01-11
**Author:** Gemini CLI Agent
**Context:** Discussion on evolving the RALF Notes documentation generation pipeline to a three-stage process, including local intermediate files and explicit handling of successful and failed outputs.

---

## 💡 Vision for an Enhanced Documentation Workflow

The goal is to create a pipeline that allows for iterative processing, clear visibility into intermediate results, and robust handling of outputs that require further attention. This moves beyond a simple "generate and format" to a more sophisticated "generate, refine, and validate" approach.

---

## 🤝 User's Proposed Three Stages

Here's an interpretation of your proposed three-stage pipeline:

*   **Stage 1: Raw Content Generation (Current `ralf-notes stage-1`)**
    *   **Input:** Source files selected by the user (e.g., code files).
    *   **Process:** Call the Large Language Model (LLM) to generate raw, structured text output. This phase prioritizes speed and capturing the core information, bypassing detailed parsing and formatting.
    *   **Output:** Saves raw LLM responses to a local folder, let's call it `stage1_raw_output_dir` (e.g., `./stage1/`). These would be `.txt` files.

*   **Stage 2: Initial Formatting (Current `ralf-notes stage-2`)**
    *   **Input:** Raw structured text files from the `stage1_raw_output_dir`.
    *   **Process:** Pass the raw content through the `TextParser` to extract structured data, then through the `NoteFormatter` to create Obsidian-compatible Markdown.
    *   **Output:** Saves initially formatted Obsidian Markdown notes to a local folder, let's call it `stage2_formatted_output_dir` (e.g., `./stage2/`). These would be `.md` files.

*   **Stage 3: Validation & Filtering / Refinement**
    *   **Input:** Initially formatted Markdown notes from the `stage2_formatted_output_dir`.
    *   **Process:** This stage would perform checks (e.g., against Obsidian style guides, content completeness) and potentially trigger further LLM refinement for notes that don't meet quality standards.
    *   **Output (two types):**
        *   **`stage3p_passed_output_dir` (e.g., `./stage3p/`):** Contains notes that successfully passed validation and/or refinement. These would be moved to the user's final designated `target_dir`.
        *   **`stage3f_failed_output_dir` (e.g., `./stage3f/`):** Contains notes that failed validation or are identified as needing human review or further LLM refinement. These files are flagged for re-processing.

---

## ✨ Refined Three-Phase Pipeline (A "Better Approach" for Clarity and Testability)

Building on your proposal and aligning with the "boxes method" (clear responsibilities for each component), I suggest a refined approach that explicitly separates validation/filtering from simple output movement.

### **Phase 1: Raw Content Generation (`ralf-notes generate-raw`)**
*   **Goal:** Quickly and reliably capture the LLM's raw, structured text response.
*   **Input:** User-selected source code/text files.
*   **Process:** `StructuredTextGenerator` calls LLM, truncates large inputs for speed.
*   **Output:** Raw structured text files (`.txt`) saved to `raw_output_dir` (e.g., `./stage1/`).
*   **Testability:** Output can be easily inspected to verify LLM content without formatting noise.

### **Phase 2: Initial Formatting (`ralf-notes format-raw`)**
*   **Goal:** Convert raw structured text into Obsidian-compatible Markdown.
*   **Input:** Raw structured text files (`.txt`) from `raw_output_dir`.
*   **Process:** `TextParser` extracts data, `NoteFormatter` applies Markdown syntax.
*   **Output:** Formatted Markdown files (`.md`) saved to `initial_formatted_dir` (e.g., `./stage2/`).
*   **Testability:** Output can be checked for basic Markdown correctness and structure.

### **Phase 3: Validation, Filtering & Finalization (`ralf-notes finalize`)**
*   **Goal:** Ensure formatted notes meet quality standards, refine if necessary, and distribute to final destinations.
*   **Input:** Formatted Markdown files (`.md`) from `initial_formatted_dir`.
*   **Process:**
    1.  **Validation:** Run checks against Obsidian style guides (`docs/Obsidian.md`), content completeness, link validity, etc.
    2.  **Refinement Loop (Optional LLM Pass):** For files that don't pass initial validation or are flagged, an optional LLM pass could attempt to refine the Markdown. This might be an iterative process.
    3.  **Filtering:** Based on validation/refinement results, direct files.
*   **Output (Two main destinations):**
    *   **`final_target_dir` (Configurable, user's main Obsidian vault path):** For notes that successfully pass validation/refinement.
    *   **`review_needed_dir` (New configurable setting, e.g., `./review/`):** For notes that fail validation, require human review, or need further LLM refinement. These would remain in this folder for subsequent action.
*   **Testability:** This phase is highly testable. You can feed it known good and known bad Markdown files from Phase 2 and verify correct routing to `final_target_dir` or `review_needed_dir`.

### **Why this refined approach is "better":**

1.  **Clearer Responsibilities:** Each phase has a single, well-defined primary responsibility (generate raw, format, validate/finalize).
2.  **Explicit Intermediate States:** The `stage1_raw_output_dir` and `stage2_formatted_output_dir` (or `initial_formatted_dir`) provide clear checkpoints.
3.  **Dedicated Validation:** Phase 3 is explicitly for quality assurance and distribution, making it easier to add new validation rules or refinement steps.
4.  **Iterative Refinement:** Files in `review_needed_dir` (`stage3f`) can be easily picked up by a human or a specialized LLM tool for further processing without rerunning the initial generation.
5.  **Testability:** Each phase's output can be verified independently, and mock inputs can be provided for downstream phases.

---

## 🛠️ Implications for Implementation

To implement this refined three-phase pipeline, the following modifications would be necessary:

1.  **Update `ConfigManager` (`ralf_notes/config_manager.py`):**
    *   Add `initial_formatted_dir` (default: `./stage2/`).
    *   Add `review_needed_dir` (default: `./review/`).
    *   Add corresponding setters and validators.
    *   Rename `raw_output_dir` to `stage1_raw_output_dir` (or similar for consistency).

2.  **Modify `cli.py` (`ralf_notes/cli.py`):**
    *   Rename `stage-1` and `stage-2` commands to `generate-raw` and `format-initial` respectively (or similar descriptive names that align with phase responsibilities).
    *   Add a new command, e.g., `ralf-notes finalize`, to orchestrate Phase 3.
    *   The `finalize` command would:
        *   Take input from `initial_formatted_dir`.
        *   Perform validation (or call a new `Validator` box).
        *   Move valid files to `target_dir`.
        *   Move invalid/flagged files to `review_needed_dir`.

3.  **Introduce a new "Validator" box (`ralf_notes/core/validator.py`):**
    *   This component would take formatted Markdown as input.
    *   It would implement various checks (Obsidian style, content length, link integrity, etc.).
    *   It would return a validation result (e.g., `(is_valid: bool, issues: List[str])`).

4.  **Adapt `DocumentPipeline` / `FileProcessor`:**
    *   The `FileProcessor` would need to be enhanced to understand these new phase-specific directories and orchestrate the flow through them.
    *   The existing `DocumentPipeline` (generator -> parser -> formatter) would be specifically used in Phase 2.

5.  **LLM Refinement Logic (Optional):**
    *   If LLM refinement is desired in Phase 3, a new `Refiner` box would be needed, potentially taking Markdown, prompting an LLM for improvements, and returning refined Markdown.

---
