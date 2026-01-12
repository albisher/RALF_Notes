# Feedback: Two-Phase Documentation Process Proposal

**Date:** 2026-01-10
**Author:** Gemini CLI Agent
**Context:** Proposal for refactoring the RALF Notes documentation generation pipeline into two distinct phases, as requested by the user.

---

## 🚀 Proposal: Two-Phase Documentation Pipeline

### 💡 Vision
To decouple raw content generation from final formatting and refinement, allowing for efficient content capture and iterative improvement towards Obsidian-ready notes.

### Phase 1: Raw Content Generation (Focus: Correct Content)

**Goal:** Generate raw, unformatted LLM output for each source file and store it in a designated "raw output" directory. This phase prioritizes capturing the correct information without concern for final presentation.

**Steps:**

1.  **Define a new "Raw Output" directory in configuration:**
    *   Add a new configurable setting, e.g., `raw_output_dir`, to `ConfigManager`.
    *   This directory will serve as the temporary storage for raw LLM responses.

2.  **Modify `DocumentPipeline` (or create a new `RawContentGenerator`):**
    *   Bypass the `TextParser` and `NoteFormatter` in this phase.
    *   The `StructuredTextGenerator` will directly write its raw string output to a file within the `raw_output_dir`.
    *   Filename in `raw_output_dir` should correspond to the source file (e.g., `source_file.py` -> `source_file.txt` in raw_output_dir).

3.  **Update `ralf-notes generate` command:**
    *   Introduce an option (e.g., `--raw-only`) or a new subcommand (e.g., `ralf-notes generate-raw`) to trigger this phase.
    *   When this option is active, the process will:
        *   Read source files.
        *   Call the LLM via `StructuredTextGenerator`.
        *   Write the *raw string response* directly to `raw_output_dir`.
        *   Skip parsing and formatting.

4.  **Error Handling (Phase 1):** Focus on LLM API errors or connectivity issues. Content quality issues (e.g., missing sections) will be addressed in Phase 2.

### Phase 2: Formatted Notes Generation & Refinement (Focus: Tidy Notes & Obsidian Style)

**Goal:** Take the raw content generated in Phase 1, process it through the app's parsing and formatting logic, and potentially refine it further to produce polished Obsidian notes.

**Steps:**

1.  **Define a new command (e.g., `ralf-notes tidy-notes` or `ralf-notes format-raw`):**
    *   This command will take the `raw_output_dir` (from config) as its source.
    *   It will also take the final `target_dir` (from config) for the formatted notes.

2.  **Modify `DocumentPipeline` (or adapt it for Phase 2):**
    *   Read files from `raw_output_dir`.
    *   Pass the raw content through the `TextParser` to extract structured data.
    *   Pass the parsed data through the `NoteFormatter` to create Obsidian markdown.
    *   Write the final markdown to the `target_dir`.

3.  **Introduce an optional "Refinement Loop" (Ralf Loop):**
    *   Within Phase 2, if desired, add a mechanism to re-engage the LLM with the *parsed data* or *initial markdown* from Phase 1/early Phase 2.
    *   This "Ralf Loop" could be triggered by specific flags (e.g., `--refine-style`, `--check-obsidian-style`).
    *   The LLM in this loop would be prompted to:
        *   Review the formatted markdown against Obsidian style guides (e.g., `/Users/amac/Documents/code/RALF_Notes/docs/Obsidian.md`).
        *   Suggest improvements or directly reformat sections for better Obsidian compatibility (e.g., using specific callout types, table formatting, image embeds).
        *   This could involve an iterative process where the LLM reviews, suggests, and applies changes.

4.  **Obsidian Style Checks:**
    *   Integrate logic within Phase 2 (especially in the "Refinement Loop") to explicitly check against Obsidian best practices and style guidelines from `/Users/amac/Documents/code/RALF_Notes/docs/Obsidian.md`.
    *   This could involve a "linter" like functionality that assesses the generated Markdown for adherence to Obsidian's specific syntax and conventions.

---

## 📝 Next Steps (for Implementation)

1.  **Update `ConfigManager`:** Add `raw_output_dir` setting.
2.  **Modify `StructuredTextGenerator`:** Add method to directly write raw LLM output to a file.
3.  **Modify `cli.py`:** Add new subcommand/options for `generate-raw` and `format-raw` (or `tidy-notes`).
4.  **Adapt `DocumentPipeline`:** Ensure it can handle both raw output generation (Phase 1) and raw output processing (Phase 2).
5.  **Develop Refinement Logic (Optional but Recommended):** Implement the "Ralf Loop" for iterative LLM-driven formatting and style adherence.
6.  **Create Obsidian Style Checker:** Develop validation based on `docs/Obsidian.md`.

---
