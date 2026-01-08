# --- Configuration ---
# Choose a source directory to process the code files
# You can add multiple source directories to the list.
# For example, to process the current directory and a 'src' subdirectory:
# SOURCE_PATHS = ['./', 'src/']
SOURCE_PATHS = ['/Users/']

# Choose a target directory to save the Obsidian notes
TARGET_DIR = 'To_Obsidian/'

PREFERRED_START_TIME = "08:03"
OVERWRITE_EXISTING = False 

APPROX_LINES_FOR_FULL_CONTEXT = 500  # Ministral-3:3b handles ~16K tokens effectively on M4
TOKENS_PER_LINE_ESTIMATE = 15        # Standard: code ~10-12, text ~15-20 tokens/line

# --- High Context Options ---
# num_ctx is now calculated based on your line preference
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": "30m"  # Keep model loaded for 30 minutes
}

# Ollama configuration
OLLAMA_HOST = 'http://127.0.0.1:11434'
MODEL_NAME = 'ministral-3:3b'         # Edge-optimized, stable on Mac Mini M4 (~3GB VRAM)

# Optimized for Ministral-3:3b (128K native context, 16K practical limit)
CHUNK_SIZE = 6000                    # ~400 lines/chunk - excellent balance for speed/memory
MAX_CTX = 16384                      # Set via: ollama run ministral-3:3b --num_ctx 16384
