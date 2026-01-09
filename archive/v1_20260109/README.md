# RALF Notes

RALF Notes is a Python tool that automatically generates documentation in Markdown format for your source code files, creating a knowledge base in Obsidian.

## How it works

The script traverses the specified source directories, and for each file, it generates a detailed Obsidian note. This note includes:

- A summary of the file's purpose and functionality.
- A detailed explanation of the logic and components.
- A list of key functions or classes with their descriptions.
- Usage examples.
- A list of related files.

This process is powered by a local AI model running with Ollama.

## Project Structure

- `main.py`: The main script that orchestrates the documentation generation process.
- `config.py`: Configuration file for specifying source paths, target directories, and Ollama model settings.
- `prompts.py`: Contains the prompts used to instruct the AI model.
- `logs/`: Directory for log files.
- `To_Obsidian/`: Default output directory for the generated Obsidian notes.

## Usage

1.  **Configure the project:**
    -   Edit `config.py` to set the `SOURCE_PATHS` to the directories containing the code you want to document.
    -   Set the `TARGET_DIR` to your desired output directory.
    -   Make sure you have a local Ollama server running and the specified `MODEL_NAME` is available.
2.  **Run the script:**
    ```bash
    python main.py
    ```
