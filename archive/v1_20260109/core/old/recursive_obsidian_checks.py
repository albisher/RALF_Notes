import os
import time
from datetime import datetime
from ollama import Client

# --- Configuration ---
SOURCE_PATHS = [
    '/Users/amac/Documents/code/WindowCleanner/'
]

TARGET_DIR = '/Users/amac/Library/CloudStorage/GoogleDrive-abalbisher@gmail.com/My Drive/ObsidianVault/Swarm_Project'

# 1. NEW: Preferred Start Time (24-hour format, e.g., "02:00" for 2 AM)
PREFERRED_START_TIME = "09:03"

# 2. NEW: Overwrite setting
# Set to False to skip files already documented (Avoids duplicate API calls)
OVERWRITE_EXISTING = False 

# 3. NEW: Context window configuration
# Set the approximate number of lines you want the model to see.
# The script will calculate the appropriate context window size (num_ctx).
APPROX_LINES_FOR_FULL_CONTEXT = 1000 
# A rough estimate. 10 is a generous value for average line length.
TOKENS_PER_LINE_ESTIMATE = 10

# Ollama configuration
OLLAMA_HOST = 'http://127.0.0.1:11434'
MODEL_NAME = 'ministral-3:3b'         # Edge-optimized, stable on Mac Mini M4 (~3GB VRAM)
MAX_CTX = 16384                      # Set via: ollama run ministral-3:3b --num_ctx 16384
CHUNK_SIZE = 6000                    # ~400 lines/chunk - excellent balance for speed/memory

# --- High Context Options ---
# num_ctx is now calculated based on your line preference
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2
}

client = Client(host=OLLAMA_HOST)


# System prompt to teach the AI Obsidian syntax and help documentation
SYSTEM_PROMPT = """
You are an expert technical writer specializing in Obsidian documentation. Without duplications.
Your task is to analyze files (all in code path or in vault) and generate high-quality Obsidian Markdown files without duplicates.
For every file I give you, you must:
1. Check if the file has a YAML frontmatter with 'tags', 'created', and 'type'.
2. Use proper Markdown headers (H1 for file name, H2 for summary, etc.).
3. Include a 'Related' section using Obsidian double-bracket links (e.g., [[wikilinks]]).
4. Summarize the logic, identify key functions, and explain the purpose of the code.
5. Suggest tags based on the content (e.g., #python #logic #setup).
6. Ensure the tone is professional and helpful.
7. Use Obsidian's callouts '> [!INFO]' where appropriate to highlight key takeaways.

remember that you are an expert technical writer specializing in Obsidian documentation. Your task is to analyze files (all in code path or in vault) and generate high‑quality Obsidian Markdown notes without duplicates.

## Core instructions

1. YAML frontmatter should be present and valid:
   tags: #tag1, #tag2, #tag3
   created: {{date}}
   type: documentation, research, code notes, etc.


2. Proper Markdown structure must be present:
   H1: file name (without extension)
   H2: Summary
   H2: Details
   H2: Key Functions
   H2: Usage
   H2: Related

3. In the **Related** section, include Obsidian-style links to other notes when they are mentioned or clearly implied, using `[[wikilinks]]`.

4. Make sure that summerization is present and valid:
    Explain the main purpose of the file.
    Describe the overall logic and data flow.
    List and briefly explain key functions, classes, and important variables.
    Mention any external dependencies, frameworks, or APIs used.
    Have summerization content be in between ```` and ```

5. Suggest tags must be present and valid:
    Infer relevant tags from the content (for example: #python, #javascript, #api, #testing, #cli, #database).
    use most relevant to the text in the file you are creating (example #drone, #sensor, #idea, #implemented, #simulation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design
    Put them in the `tags` in the frontmatter and optionally repeat them at the bottom of the note if useful.

6. Tone and style must be professional and helpful:
    Use a professional, concise, and helpful tone.
    Prefer short paragraphs and bullet lists for clarity.

7. Obsidian callouts:
   Use callouts to highlight key information, such as:
     '>[!INFO]'
     '>' Key takeaway or important behavior of this module.
   Use them sparingly for the most important points (e.g., core responsibilities, side effects, or gotchas).[1]

8. Link otherfiles must be present and valid:
   Link other files in the vault using Obsidian double-bracket links (e.g., [[wikilinks]]).

## Output format

For each file (all in path folders and subfolders) input, output a single complete Obsidian document that:
    Starts with YAML frontmatter as described above.[2]
    Contains clear explanations of purpose, logic, and key elements of the code.  
    Includes a **Related** section with `[[wikilinks]]` linking to other files.  
    Includes at least one `>[!INFO]` callout if there is a meaningful takeaway to highlight.

Never output anything else than the requested.
Never ask questions or make assumptions.
Never write your thinking to the file and make sure it is not there
If file is corrupted then find it and readonly from '/Users/amac/Documents/code/WindowCleanner/' or sub folders. then correct the destination corrupted file.
If you can not do it then do not do any thing with the file
"""

REVIEW_SYSTEM_PROMPT = """
You are an expert technical editor reviewing an existing piece of Obsidian documentation.
Your goal is to improve its structure, clarity, and interconnectedness.

Core instructions:
    1.  **Analyze Existing Content**: Review the provided files in the path folders and subfolders.
    2.  **Correct Structure**: Ensure it follows the proper structure (H1, H2 sections, YAML frontmatter).
    3.  **Enhance Tags**: Add any missing, relevant tags to the `tags` array in the frontmatter.
    4.  **Add More Links**: Scrutinize the text and add more `[[wikilinks]]` where appropriate to improve knowledge discovery. Do not remove existing links.
    5.  **Improve Clarity**: Refine the language for clarity and conciseness without changing the core meaning.
    6.  **Maintain Content**: Do NOT summarize or remove existing information. Your role is to enhance, not to shorten.
    7.  **Never output anything else than the requested.** Never ask questions or make assumptions.

## Core instructions

1. YAML frontmatter should be present and valid:
   tags: #tag1, #tag2, #tag3
   created: {{date}}
   type: documentation, research, code notes, etc.


2. Proper Markdown structure must be present:
   H1: file name (without extension)
   H2: Summary
   H2: Details
   H2: Key Functions
   H2: Usage
   H2: Related

3. In the **Related** section, include Obsidian-style links to other notes when they are mentioned or clearly implied, using `[[wikilinks]]`.

4. Make sure that summerization is present and valid:
    Explain the main purpose of the file.
    Describe the overall logic and data flow.
    List and briefly explain key functions, classes, and important variables.
    Mention any external dependencies, frameworks, or APIs used.
    Have summerization content be in between ```` and ```

5. Suggest tags must be present and valid:
    Infer relevant tags from the content (for example: #python, #javascript, #api, #testing, #cli, #database).
    use most relevant to the text in the file you are creating (example #drone, #sensor, #idea, #implemented, #simulation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design, #architecture, #implementation, #testing, #debugging, #optimization, #performance, #security, #maintenance, #documentation, #research, #development, #design
    Put them in the `tags` array in the frontmatter and optionally repeat them at the bottom of the note if useful.

6. Tone and style must be professional and helpful:
    Use a professional, concise, and helpful tone.
    Prefer short paragraphs and bullet lists for clarity.

7. Obsidian callouts:
   Use callouts to highlight key information, such as:
     '>[!INFO]'
     '>' Key takeaway or important behavior of this module.
   Use them sparingly for the most important points (e.g., core responsibilities, side effects, or gotchas).[1]

8. Link otherfiles must be present and valid:
   Link other files in the vault using Obsidian double-bracket links (e.g., [[wikilinks]]).

Return the FULL, corrected, and enhanced document.
Never output anything else than the requested.
Never ask questions or make assumptions.
Never write your thinking to the file and make sure it is not there, remove any thinking parts.
If file is corrupted then find it and readonly from '/Users/amac/Documents/code/WindowCleanner/' or sub folders. then correct the destination corrupted file.
If you can not do it then do not do any thing with the file
"""

def review_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        return f"Error reading file: {e}"

    final_prompt = (
        "Please review and enhance this Obsidian note according to your instructions. "
        f"Return the full, corrected markdown content:\n\n{raw_content}"
    )
    
    response = client.generate(
        model=MODEL_NAME,
        system=REVIEW_SYSTEM_PROMPT,
        prompt=final_prompt,
        options=OPTIONS
    )
    return response['response']

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_all_files(paths):
    """Recursively finds all files in folders and subfolders."""
    valid_extensions = ('.py', '.txt', '.md', '.sh')
    # Per your requirements: keep venv in the list to skip processing it
    skip_dirs = {'__pycache__', '.git', 'venv', '.obsidian', '.venv'}
    files_to_process = []

    for base_path in paths:
        if not os.path.exists(base_path):
            print(f"Warning: Path not found {base_path}")
            continue
            
        for root, dirs, files in os.walk(base_path):
            # This applies the skip_dirs to subfolders recursively
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            for file in files:
                if file.endswith(valid_extensions):
                    if file not in {'recursive_obsidian_checks.py', 'obsidian_generator.py', 'debug_output.txt', 'prompt1.txt'}:
                        files_to_process.append(os.path.join(root, file))
    return files_to_process

def wait_until_start_time(target_time_str):
    """Pauses the script until the PREFERRED_START_TIME."""
    print(f"Waiting until {target_time_str} to begin night-time tasks...")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == target_time_str:
            print(f"It is {now}. Starting execution.")
            break
        time.sleep(30) # Check every 30 seconds

def recursive_summarize(content, chunk_size=100000):
    """
    chunk_size=100000 characters is roughly 2500-3000 lines.
    If a file is smaller than this, it processes in one shot.
    If larger, it uses the MIT 'Recursive' method.
    """
    if len(content) <= chunk_size:
        return content

    print(f"Content length ({len(content)}) exceeds chunk size. Applying recursive decomposition...")
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"  Processing chunk {i+1}/{len(chunks)}...")
        prompt = f"Summarize this code/text snippet for documentation purposes:\n\n{chunk}"
        # We pass OPTIONS here to ensure chunk processing has enough memory
        response = client.generate(model=MODEL_NAME, prompt=prompt, options=OPTIONS)
        summaries.append(response['response'])
    
    combined = "\n\n".join(summaries)
    return recursive_summarize(combined, chunk_size)

def generate_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        return f"Error reading file: {e}"

    file_name = os.path.basename(file_path)
    # Apply recursive summary first
    processed_content = recursive_summarize(raw_content)
    
    final_prompt = (
        f"Create a full Obsidian documentation file for '{file_name}' "
        f"based on this analyzed content:\n\n{processed_content}"
    )
    
    # Final generation with the high-context OPTIONS
    response = client.generate(
        model=MODEL_NAME,
        system=SYSTEM_PROMPT,
        prompt=final_prompt,
        options=OPTIONS
    )
    return response['response']

def main():
    # If you run this manually, it will wait until the night
    # wait_until_start_time(PREFERRED_START_TIME)
    
    ensure_dir(TARGET_DIR)
    all_files = get_all_files(SOURCE_PATHS)
    revisit_list = [] # List for files to be reviewed
    
    print(f"Found {len(all_files)} files. Starting Pass 1: Documenting new files...")

    # --- PASS 1: Process new files ---
    for file_path in all_files:
        if os.path.basename(file_path) == "obsidian_recursive_generator.py":
            continue

        # --- NEW: Logic to preserve directory structure ---
        # Find which source root this file belongs to
        src_root = next((root for root in SOURCE_PATHS if file_path.startswith(root)), None)
        
        if not src_root:
            print(f"Warning: Could not determine source root for {file_path}. Skipping.")
            continue

        # Calculate relative path and construct target path
        relative_path = os.path.relpath(file_path, src_root)
        target_path = os.path.join(TARGET_DIR, relative_path)
        
        # Ensure the target directory exists
        target_sub_dir = os.path.dirname(target_path)
        ensure_dir(target_sub_dir)

        # Use a cleaner filename for the .md file
        base_name, _ = os.path.splitext(os.path.basename(target_path))
        target_path = os.path.join(target_sub_dir, f"{base_name}.md")
        
        # --- End of new path logic ---

        if os.path.exists(target_path):
            if not OVERWRITE_EXISTING:
                revisit_list.append(target_path) # Add to revisit list
            else:
                # Process and overwrite if OVERWRITE_EXISTING is True
                print(f"\n--- [{datetime.now().isoformat()}] Documenting (Overwrite): {relative_path} ---")
                doc_md = generate_obsidian_doc(file_path)
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(doc_md)
                print(f"Saved: {target_path}")
        else:
            # File does not exist, so create it
            print(f"\n--- [{datetime.now().isoformat()}] Documenting (New): {relative_path} ---")
            doc_md = generate_obsidian_doc(file_path)
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(doc_md)
            print(f"Saved: {target_path}")

    # --- PASS 2: Review existing files ---
    print(f"\n--- Pass 1 complete. Starting Pass 2: Reviewing {len(revisit_list)} existing files... ---")
    for file_path in revisit_list:
        print(f"\n--- [{datetime.now().isoformat()}] Reviewing: {os.path.basename(file_path)} ---")
        reviewed_md = review_obsidian_doc(file_path) 
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(reviewed_md)
        print(f"Updated: {file_path}")
    
    print("\nAll tasks complete.")

if __name__ == "__main__":
    main()