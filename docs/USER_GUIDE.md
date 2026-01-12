# RALF Note User Guide

Welcome to the RALF Note User Guide! This document will walk you through everything you need to know to get the most out of RALF Note, an AI-powered documentation generator for your code.

---

## 🚀 1. Introduction to RALF Note

RALF Note (Recursive AI-powered Learning Framework for Obsidian Documentation) transforms your code into structured, Obsidian-ready markdown notes with a single command. It leverages local Large Language Models (LLMs) via Ollama to provide fast, intelligent, and private documentation generation.

### Key Features:
-   **Fast & Efficient:** Single LLM call per file, significantly reducing processing time.
-   **Structured Output:** Generates consistent markdown with predefined sections (Summary, Key Functions, Dependencies, etc.).
-   **Rich CLI:** Intuitive command-line interface powered by Typer and Rich for beautiful terminal output.
-   **Configurable:** Customize models, paths, and behavior via a simple configuration file or CLI options.
-   **Robust:** Includes features like rate limiting, retry mechanisms, and comprehensive logging for reliable operation.
-   **Local & Private:** Keeps your code and data on your machine by using local LLMs.

---

## 📦 2. Installation

Before you can use RALF Note, you need to set up your environment.

### Prerequisites:
-   **Python 3.9+:** Ensure you have a compatible Python version installed. You can download it from [python.org](https://www.python.org/).
-   **Ollama:** RALF Note relies on [Ollama](https://ollama.ai/) to run local Large Language Models.
    1.  **Download & Install Ollama:** Follow the instructions on the [Ollama website](https://ollama.ai/download).
    2.  **Start Ollama Server:** After installation, ensure the Ollama server is running in the background. You can usually start it from your applications or by running `ollama serve` in your terminal.
    3.  **Pull an LLM:** RALF Note defaults to `ministral-3:3b`. You need to pull this model (or another compatible model) into Ollama:
        ```bash
        ollama pull ministral-3:3b
        ```

### Installing RALF Note:

You can install RALF Note directly from its GitHub repository:

```bash
pip install git+https://github.com/albisher/RALF_Notes.git
```

*(Installation via PyPI coming soon)*

---

## ⚙️ 3. First-Time Setup & Configuration

After installation, the first step is to configure RALF Note.

### 3.1. Interactive Setup Wizard (`ralf-notes init`)

The easiest way to get started is by running the interactive setup wizard:

```bash
ralf-notes init
```

This command will:
1.  **Create a configuration file:** `~/.ralf-notes/config.json` (or update it if it already exists).
2.  **Prompt for essential settings:**
    -   **Source Paths:** Directories containing your code files. RALF Note will scan these for documentation.
    -   **Target Directory:** Where the final Obsidian markdown notes will be saved.
    -   **Stage 1 Raw Output Directory:** Intermediate directory for raw LLM responses.
    -   **Stage 2 Initial Formatted Directory:** Intermediate directory for parsed and formatted LLM responses before finalization.
    -   **Stage 3 Review Needed Directory:** Directory for notes that fail final validation or require manual review.
    -   **Ollama Model Name:** The name of the LLM you want to use (e.g., `ministral-3:3b`).
3.  **Validate paths:** It will check if provided paths exist and are writable, guiding you to correct any issues.

### 3.2. Manual Configuration (`ralf-notes init --set-*`)

You can also manage individual configuration settings directly from the command line:

-   **Show Current Configuration:**
    ```bash
    ralf-notes init --show
    ```

-   **Add a Source Path:**
    ```bash
    ralf-notes init --add-source /path/to/my/code_repo
    ```

-   **Remove a Source Path:**
    ```bash
    ralf-notes init --remove-source /path/to/old_code
    ```

-   **Set Output Directories:**
    ```bash
    ralf-notes init --set-target ~/ObsidianVault/CodeNotes
    ralf-notes init --set-stage1-raw-output ./ralf_raw_output
    ralf-notes init --set-initial-formatted ./ralf_formatted
    ralf-notes init --set-review-needed ./ralf_review
    ```

-   **Set Ollama Model:**
    ```bash
    ralf-notes init --set-model qwen2.5:14b
    ```

-   **Set LLM Parameters (Advanced):**
    ```bash
    ralf-notes init --set-temperature 0.5   # Controls randomness (0.0-2.0)
    ralf-notes init --set-num-ctx 8192      # Context window size for LLM
    ralf-notes init --set-chunk-size 100000 # Max characters per chunk for large files
    ralf-notes init --set-max-content-length 8000 # Max content sent to LLM for full generation
    ralf-notes init --set-max-chunk-summary-length 4000 # Max content for chunk summaries
    ```

-   **Rate Limiting & Retries:**
    ```bash
    ralf-notes init --set-request-delay-seconds 0.1 # Delay between LLM calls (seconds)
    ralf-notes init --set-request-timeout-seconds 60 # Max time for one LLM call (seconds)
    ralf-notes init --set-retry-attempts 5         # Number of retries on LLM failure
    ```

-   **Logging Configuration:**
    ```bash
    ralf-notes init --set-log-level DEBUG          # Set verbosity: DEBUG, INFO, WARNING, ERROR, CRITICAL
    ralf-notes init --set-log-file /var/log/ralf-notes.log # Custom log file path (defaults to ~/.ralf-notes/ralf-notes.log)
    ```

-   **Reset Configuration:**
    ```bash
    ralf-notes init --reset # Resets all settings to default
    ```

### 3.3. Configuration File (`~/.ralf-notes/config.json`)

All settings are stored in a JSON file, typically located at `~/.ralf-notes/config.json`. You can edit this file directly if you prefer, but be careful with JSON syntax.

Example `config.json`:
```json
{
  "source_paths": ["/Users/myuser/projects/my_project"],
  "target_dir": "/Users/myuser/ObsidianVault/CodeNotes",
  "stage1_raw_output_dir": "./stage1_raw",
  "initial_formatted_dir": "./stage2_formatted",
  "review_needed_dir": "./review_needed",
  "model_name": "ministral-3:3b",
  "ollama_host": "http://127.0.0.1:11434",
  "temperature": 0.1,
  "num_ctx": 10000,
  "chunk_size": 100000,
  "max_content_length": 8000,
  "max_chunk_summary_length": 4000,
  "request_delay_seconds": 0.05,
  "request_timeout_seconds": 90,
  "retry_attempts": 3,
  "log_level": "INFO",
  "log_file": null
}
```

---

## 🤖 4. Generating Documentation

RALF Note uses a 3-stage pipeline to generate documentation:

1.  **Stage 1: Raw Content Generation (`ralf-notes generate-raw`)**
    -   Scans your source files.
    -   Feeds file content to the LLM (Ollama).
    -   Receives raw structured text output from the LLM.
    -   Saves this raw output to the configured `stage1_raw_output_dir`.

2.  **Stage 2: Initial Formatting (`ralf-notes format-initial`)**
    -   Reads the raw structured text files from Stage 1.
    -   Parses the structured text into a programmatic data structure.
    -   Formats this data into initial Obsidian markdown notes.
    -   Saves these notes to the configured `initial_formatted_dir`.

3.  **Stage 3: Validation, Filtering & Finalization (`ralf-notes finalize`)**
    -   Reads the initially formatted markdown notes from Stage 2.
    -   (Optional) Performs validation checks on the note content (e.g., ensuring all required sections are present).
    -   Moves valid notes to your final `target_dir`.
    -   Moves notes requiring review to your `review_needed_dir`.

### 4.1. Full Pipeline (Recommended)

To run all three stages sequentially with a single command:

```bash
ralf-notes generate
```

You can customize this process with various options:

-   **Specify Source Path (overrides config):**
    ```bash
    ralf-notes generate /path/to/my/project
    ```
-   **Custom Output Directories (overrides config):**
    ```bash
    ralf-notes generate --raw-output ./my_raw --formatted-output ./my_formatted --output ~/ObsidianVault/FinalNotes --review-output ./my_review
    ```
-   **Dry Run (preview changes without writing files):**
    ```bash
    ralf-notes generate --dry-run
    ```
-   **Overwrite Existing Files:**
    ```bash
    ralf-notes generate --overwrite
    ```
-   **Quiet Mode (minimal terminal output):**
    ```bash
    ralf-notes generate --quiet
    ```
-   **Override Model on the Fly:**
    ```bash
    ralf-notes generate --model mistral:7b
    ```
-   **Override Rate Limiting on the Fly:**
    ```bash
    ralf-notes generate --delay 0.2 --timeout 90 --retries 5
    ```

### 4.2. Running Stages Individually

You can also run each stage independently for more control or debugging:

#### Stage 1: Generate Raw Output
```bash
ralf-notes generate-raw [SOURCE_PATH] [--output <RAW_OUTPUT_DIR>] [--model <MODEL_NAME>] [--quiet]
```
-   `[SOURCE_PATH]`: Optional. Overrides configured source paths.
-   `--output`: Optional. Overrides configured raw output directory.
-   `--model`: Optional. Overrides configured model name.
-   `--quiet`: Suppresses verbose terminal output.

#### Stage 2: Initial Formatting
```bash
ralf-notes format-initial [RAW_INPUT_PATH] [--output <FORMATTED_OUTPUT_DIR>] [--model <MODEL_NAME>] [--dry-run] [--overwrite] [--quiet]
```
-   `[RAW_INPUT_PATH]`: Optional. Overrides configured raw output directory as input.
-   `--output`: Optional. Overrides configured initial formatted directory.
-   `--model`: Optional. Overrides configured model name (for pipeline initialization).
-   `--dry-run`: Prevents writing formatted files.
-   `--overwrite`: Overwrites existing formatted files.
-   `--quiet`: Suppresses verbose terminal output.

#### Stage 3: Finalization
```bash
ralf-notes finalize [FORMATTED_INPUT_PATH] [--output <FINAL_OUTPUT_DIR>] [--review-output <REVIEW_DIR>] [--dry-run] [--overwrite] [--quiet]
```
-   `[FORMATTED_INPUT_PATH]`: Optional. Overrides configured initial formatted directory as input.
-   `--output`: Optional. Overrides configured final target directory.
-   `--review-output`: Optional. Overrides configured review needed directory.
-   `--dry-run`: Prevents moving files.
-   `--overwrite`: Overwrites existing files in the final target directory.
-   `--quiet`: Suppresses verbose terminal output.

---

## 👀 5. Monitoring & Health Checks

### 5.1. Check System Health

Verify your Ollama connection and model availability:

```bash
ralf-notes check-health
```
This command will report any issues with your Ollama setup and suggest fixes.

### 5.2. Logging

RALF Note utilizes a comprehensive logging system. By default, logs are written to `~/.ralf-notes/ralf-notes.log` and also displayed in the terminal (unless `--quiet` mode is active).

-   **Default Log File:** `~/.ralf-notes/ralf-notes.log`
-   **Configuring Log Level:** You can adjust the verbosity of logs (DEBUG, INFO, WARNING, ERROR, CRITICAL) via:
    ```bash
    ralf-notes init --set-log-level DEBUG
    ```
-   **Custom Log File:** Specify a different path for log output:
    ```bash
    ralf-notes init --set-log-file /path/to/my/custom.log
    ```

---

## 💡 6. Best Practices

-   **Start Small:** Begin by processing a single file or a small directory to fine-tune your settings and observe the output.
-   **Use `--dry-run`:** Always use `--dry-run` with `generate` or `format-initial` when experimenting to see the expected output without modifying files.
-   **Review Output:** Regularly check the generated notes, especially those moved to the `review_needed` directory, to ensure quality and LLM adherence.
-   **Optimize LLM Parameters:** Experiment with `temperature`, `num_ctx`, and `chunk_size` for your specific model and code. The auto-tuning system (Phase 7) will help automate this.
-   **Monitor Performance:** Keep an eye on the summary results after generation to track `Time` and `Speed`.
-   **Consult Troubleshooting:** If you encounter unexpected behavior, refer to the [Troubleshooting Guide](TROUBLESHOOTING.md).

---

## 🎯 7. What's Next (Auto-Tuning)

RALF Note includes an experimental auto-tuning system designed to find optimal LLM parameters for your specific hardware and chosen model. This feature will be accessible via a dedicated `ralf-notes tune` command (coming soon).

The auto-tuning process benchmarks various `num_ctx`, `chunk_size`, and other parameters to recommend the most efficient settings balancing speed, quality, and resource usage.

---

## 📚 8. Output Format Reference

Each generated file follows a structured markdown format compatible with Obsidian:

```markdown
---
tags: #python, #documentation, #automation
created: 2026-01-09
type: code-notes
---

# filename

## Summary
High-level purpose in 1-2 sentences

## Details
Detailed explanation of logic and architecture

## Key Functions
### `function_name`
Description with signature and return value

## Usage
How to use this code

## Dependencies
Required libraries and modules

## Related
- [[Related File 1]]
- [[Related File 2]]

> [!INFO]- Key Insight
> Important information highlighted in callouts
```

---

## ❓ 9. Frequently Asked Questions (FAQ)

*(To be populated based on user feedback)*

---

**RALF Note v2.0 - Transforming code into knowledge, one file at a time.** 📚✨
