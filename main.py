import os
import time
import math
import logging
import re
from datetime import datetime
from ollama import Client, ResponseError

# Import from local modules
from config import *
from prompts import *

def ensure_dir(directory):
    os.makedirs(directory, exist_ok=True)

# --- Logging Setup ---
LOG_DIR = './logs'
ensure_dir(LOG_DIR)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
LOG_FILE_PATH = os.path.join(LOG_DIR, f'obsidian_generator_{timestamp***REMOVED***.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Set overall logging level

# Clear existing handlers to prevent duplicate output if run multiple times
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

# Detailed file handler
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler for brief output
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

class ConsoleFilter(logging.Filter):
    def filter(self, record):
        return not hasattr(record, 'detailed')

console_handler.addFilter(ConsoleFilter())
logger.addHandler(console_handler)


client = Client(host=OLLAMA_HOST)

CONVERSATIONAL_STARTS = [
    "here's a", "this is", "let's look", "as an ai", "i can help", "i've extracted",
    "below is", "okay, here's", "the type is", "i would classify this as", "it is a",
    "here's a list", "the following are", "below is the", "here are the"
]

STOP_WORDS = {
    'to', 'it', 'some', 'and', 'the', 'a', 'in', 'of', 'for', 'on', 'with', 'is', 'that', 'this', 'at', 'by', 'from', 'an', 
    'or', 'as', 'but', 'not', 'your', 'my', 'we', 'you', 'i', 'he', 'she', 'they', 'them', 'us', 'our', 'their', 'which', 
    'who', 'what', 'where', 'when', 'why', 'how', 'each', 'just', 'only', 'all', 'any', 'such', 'so', 'up', 'down', 'out', 
    'off', 'then', 'there', 'here', 'now', 'will', 'would', 'could', 'should', 'can', 'may', 'might', 'must', 'has', 'have', 
    'had', 'do', 'does', 'did', 'was', 'were', 'be', 'been', 'being', 'get', 'got', 'go', 'goes', 'went', 'going', 'say', 
    'says', 'said', 'make', 'makes', 'made', 'making', 'know', 'knows', 'knew', 'knowing', 'see', 'sees', 'saw', 'seeing', 
    'take', 'takes', 'took', 'taking', 'come', 'comes', 'came', 'coming', 'want', 'wants', 'wanted', 'wanting', 'look', 
    'looks', 'looked', 'looking', 'find', 'finds', 'found', 'finding', 'give', 'gives', 'gave', 'giving', 'tell', 'tells', 
    'told', 'telling', 'work', 'works', 'worked', 'working', 'call', 'calls', 'called', 'calling', 'try', 'tries', 'tried', 
    'trying', 'ask', 'asks', 'asked', 'asking', 'need', 'needs', 'needed', 'needing', 'feel', 'feels', 'felt', 'feeling', 
    'become', 'becomes', 'became', 'becoming', 'leave', 'leaves', 'left', 'leaving', 'put', 'puts', 'put', 'putting', 
    'mean', 'means', 'meant', 'meaning', 'keep', 'keeps', 'kept', 'keeping', 'begin', 'begins', 'began', 'beginning', 
    'seem', 'seems', 'seemed', 'seeming', 'help', 'helps', 'helped', 'helping', 'talk', 'talks', 'talked', 'talking', 
    'turn', 'turns', 'turned', 'turning', 'start', 'starts', 'started', 'starting', 'show', 'shows', 'showed', 'showing', 
    'hear', 'hears', 'heard', 'hearing', 'play', 'plays', 'played', 'playing', 'run', 'runs', 'ran', 'running', 'move', 
    'moves', 'moved', 'moving', 'like', 'likes', 'liked', 'liking', 'live', 'lives', 'lived', 'living', 'believe', 
    'believes', 'believed', 'believing', 'hold', 'holds', 'held', 'holding', 'bring', 'brings', 'brought', 'bringing'
***REMOVED***

def estimate_tokens(text):
    """Rough token estimator: words * 1.3 + overhead."""
    return len(text.split()) * 1.3 + 100

def get_dynamic_count(file_size, min_count, max_count, max_count_file_size):
    """Calculates the number of tags/links based on file size."""
    if file_size >= max_count_file_size:
        return max_count
    scale_factor = file_size / max_count_file_size
    return int(min_count + (max_count - min_count) * scale_factor)

def get_summary_length(file_size, max_size=20000): # max_size for scaling
    """Calculates a desired summary length in sentences based on file size."""
    if file_size > max_size:
        return 8 # Max sentences
    return int(2 + 6 * (file_size / max_size))

def safe_generate(client, system=None, prompt=None, options=None, stream=True, prompt_type="UNKNOWN"):
    """Generate with retries and streaming support, printing prompt and response to stdout."""
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    logger.info(f"PROMPT SENT [{prompt_type***REMOVED***]")
    logger.info(f"--- PROMPT SENT [{prompt_type***REMOVED***] [{timestamp_str***REMOVED***] ---\nSYSTEM: {system***REMOVED***\nPROMPT: {prompt***REMOVED***\n", extra={'detailed': True***REMOVED***)
    
    for attempt in range(3):
        try:
            kwargs = {"model": MODEL_NAME, "prompt": prompt***REMOVED***
            if system: kwargs["system"] = system
            if options: kwargs["options"] = options
            kwargs["stream"] = stream
            
            if stream:
                stream_resp = client.generate(**kwargs)
                response = "".join(chunk['response'] for chunk in stream_resp)
                logger.info(f"RESPONSE RECEIVED [{prompt_type***REMOVED***]")
                logger.info(f"--- RESPONSE RECEIVED [{prompt_type***REMOVED***] [{timestamp_str***REMOVED***] ---\n{response***REMOVED***\n", extra={'detailed': True***REMOVED***)
                return response
            else:
                response = client.generate(**kwargs)['response']
                logger.info(f"RESPONSE RECEIVED [{prompt_type***REMOVED***]")
                logger.info(f"--- RESPONSE RECEIVED [{prompt_type***REMOVED***] [{timestamp_str***REMOVED***] ---\n{response***REMOVED***\n", extra={'detailed': True***REMOVED***)
                return response
        except (ResponseError, Exception) as e:
            logger.warning(f"Attempt {attempt+1***REMOVED*** failed: {e***REMOVED***")
            if attempt == 2:
                logger.error(f"All retries failed: {e***REMOVED***")
                raise
            time.sleep(2 ** attempt)
    return None

def validate_and_regenerate(text, validation_func, original_prompt_format_string, system_prompt, options, prompt_type, processed_content, extra_args=None):
    """
    Validates the generated text using the provided validation function. If validation fails,
    it will regenerate the text up to 3 times.
    """
    if extra_args is None:
        extra_args = {***REMOVED***

    for i in range(3):
        if validation_func(text):
            return text
        else:
            logger.warning(f"Validation failed for {prompt_type***REMOVED***. Regenerating... (Attempt {i+1***REMOVED***/3)")
            # Craft a more direct correction prompt
            correction_prompt_instruction = "The previous output was not valid and contained conversational elements or did not follow the required format. Re-generate the content STRICTLY adhering to the original instructions. Your output MUST ONLY be the requested content, with no introductory phrases, conversational filler, or questions. If the content is 'Not applicable', output only that. Do not explain or comment."
            
            # Format the original prompt string again with data
            original_prompt_reformatted = original_prompt_format_string.format(processed_content=processed_content, **extra_args)
            
            final_correction_prompt = f"{correction_prompt_instruction***REMOVED***\n\nOriginal prompt instructions:\n{original_prompt_reformatted***REMOVED***\n\nInvalid output received:\n{text***REMOVED***\n\nRe-generate now:"
            
            text = safe_generate(client, system=system_prompt, prompt=final_correction_prompt, options=options, prompt_type=f"REGENERATE_{prompt_type***REMOVED***_ATTEMPT_{i+1***REMOVED***")
    
    logger.error(f"Failed to generate valid output for {prompt_type***REMOVED*** after 3 attempts. Returning last invalid output.")
    return text # Return the last attempt, even if it's invalid

def has_no_questions(text):
    """Validation function to check for question marks and conversational filler."""
    if '?' in text:
        logger.warning(f"Question mark found in generated text: '{text***REMOVED***'")
        return False
    # Check for common conversational starts
    if any(text.lower().strip().startswith(phrase) for phrase in CONVERSATIONAL_STARTS):
        logger.warning(f"Conversational start found in generated text: '{text***REMOVED***'")
        return False
    return True

def is_summary_valid(text):
    """Validation function for summaries."""
    if '?' in text:
        logger.warning(f"Question mark found in summary: '{text***REMOVED***'")
        return False
    lines = text.strip().split('\n')
    if len(lines) > 20:
        logger.warning(f"Summary exceeds 20 lines: {len(lines)***REMOVED***")
        return False
    # Also check if it's a single paragraph (no double newlines or multiple paragraphs)
    if re.search(r'\n\s*\n', text.strip()):
        logger.warning(f"Summary contains multiple paragraphs: '{text***REMOVED***'")
        return False
    # Check for conversational filler at start
    if any(text.lower().strip().startswith(phrase) for phrase in CONVERSATIONAL_STARTS):
        logger.warning(f"Conversational start found in summary: '{text***REMOVED***'")
        return False
    return True

def clean_summary(text):
    """Removes markdown code fences, headers, frontmatter, enforces line limit, and removes questions from summary text."""
    
    lines = text.strip().split('\n')
    
    # Aggressively clean and remove opening markdown code fence line
    if lines:
        # Check for patterns like "yaml ```", "markdown ```", "```python", or just "```"
        # If the line contains a ``` and potentially leading text, remove the entire line
        if re.match(r'^\s*(.*?)\s*```(\S*|$)', lines[0]):
            lines = lines[1:] # Remove the opening fence line entirely
    
    # Check and remove closing fence (should only be ```)
    if lines and re.match(r'^\s*```', lines[-1]):
        lines = lines[:-1]
    
    # Re-join and re-split to clean up any empty lines introduced by fence removal
    text = "\n".join(lines).strip()
    lines = text.split('\n')
    cleaned_lines = []
    
    # Filter out markdown headers and frontmatter lines
    for line in lines:
        stripped_line = line.strip()
        # Skip empty lines, frontmatter, and markdown headers within the summary content
        if not stripped_line or \
           stripped_line.startswith(('tags:', 'created:', 'type:', '---')) or \
           re.match(r'^#+\s', stripped_line):
            continue
        cleaned_lines.append(line)

    # Enforce single paragraph and 20-line limit by joining all lines, then truncating
    final_summary = " ".join([line.strip() for line in cleaned_lines]).strip()
    
    # Optionally, truncate if still too long in terms of raw characters after joining
    if len(final_summary.split()) > 150: # Arbitrary word limit for very long summaries
        final_summary = " ".join(final_summary.split()[:150]) + "..."
    
    return final_summary

def is_tags_valid(text, num_tags):
    """Validation function for tags."""
    if '?' in text:
        logger.warning(f"Question mark found in tags: '{text***REMOVED***'")
        return False
    tags_conversational_starts = CONVERSATIONAL_STARTS + ["tags:", "taglist:", "list of tags:", "here are the tags:"]
    if any(text.lower().strip().startswith(phrase) for phrase in tags_conversational_starts):
        logger.warning(f"Conversational start found in tags: '{text***REMOVED***'")
        return False
    
    # Check if tags start with # and have no extra punctuation
    tags = text.strip().split()
    for tag in tags:
        if not tag.startswith('#'):
            logger.warning(f"Tag '{tag***REMOVED***' does not start with '#'")
            return False
        if re.search(r'[^\w\-வுகளை]', tag[1:]): # Allow only alphanumeric, hyphen after #
            logger.warning(f"Tag '{tag***REMOVED***' contains invalid characters")
            return False
    
    # Check if the number of tags is within reason (model might ignore num_tags exactly)
    # This validation is soft because the cleaning function will enforce the limit.
    return True


def clean_tags(text):
    """Ensures tags are correctly formatted and cleaned."""
    cleaned_text = text.strip().lower()

    # Remove conversational starts
    for phrase in CONVERSATIONAL_STARTS:
        if cleaned_text.startswith(phrase):
            cleaned_text = cleaned_text[len(phrase):].strip()

    # Remove punctuation but keep spaces for splitting
    cleaned_text = re.sub(r'[^\w\s#\-]', '', cleaned_text) # Keep alphanumeric, #, -, and spaces

    # Split by whitespace and commas, filter out empty strings
    potential_tags = [tag.strip() for tag in re.split(r'[\s,]+', cleaned_text) if tag.strip()]
    
    cleaned_tags = []
    for tag_word in potential_tags:
        # Ensure it starts with #
        if not tag_word.startswith('#'):
            tag_word = '#' + tag_word

        # Remove invalid characters from within the tag_word itself after the initial #
        tag_word = '#' + re.sub(r'[^\w\-]', '', tag_word[1:])
        
        # Filter out stop words (after removing # for comparison)
        if tag_word[1:] and tag_word[1:] not in STOP_WORDS:
            cleaned_tags.append(tag_word)
            
    # Remove duplicates and enforce 20 tag limit
    unique_tags = sorted(list(set(cleaned_tags)))
    return " ".join(unique_tags[:20])

def clean_doc_type(text):
    """Ensures doc_type is a single word."""
    # Remove any conversational filler before splitting
    text_cleaned = text.strip()
    for phrase in CONVERSATIONAL_STARTS:
        if text_cleaned.lower().startswith(phrase):
            text_cleaned = text_cleaned[len(phrase):].strip()
    
    # Ensure it's a single word and remove any punctuation
    first_word = re.sub(r'[^\w\-வுகளை]', '', text_cleaned.split()[0]).strip()
    return first_word

def clean_details(text):
    """Aggressively removes frontmatter, markdown headers, separator lines, unwanted callout titles,
    and ensures correct callout formatting for details content."""
    lines = text.strip().split('\n')
    cleaned_lines = []
    in_callout_block = False # To track if we are inside a multi-line callout block
    
    for line in lines:
        stripped_line = line.strip()

        # Check for start of a callout header
        is_callout_header = re.match(r'^\s*>\s*\[!INFO\]', stripped_line)

        # If it's a callout header
        if is_callout_header:
            in_callout_block = True
            # Clean specific unwanted callout titles (e.g., "**Bug Note**") from the callout header
            if re.match(r'^\s*>\s*\[!INFO\]\s*\*\*Bug Note\*\*', stripped_line):
                stripped_line = re.sub(r'\s*\*\*Bug Note\*\*', '', stripped_line).strip()
            cleaned_lines.append(stripped_line)
            continue

        # If we are inside a callout block
        if in_callout_block:
            if not stripped_line: # An empty line terminates the callout block
                in_callout_block = False
                cleaned_lines.append(stripped_line) # Keep the empty line as a separator
                continue
            elif not stripped_line.startswith('>'): # If a line does not start with '>' it should be prefixed
                stripped_line = '> ' + stripped_line
            cleaned_lines.append(stripped_line)
            continue
            
        # Lines outside of a callout block - apply existing general cleaning
        # Skip empty lines, frontmatter, markdown headers, and code block fences
        if not stripped_line or \
           stripped_line.startswith(('tags:', 'created:', 'type:', '---')) or \
           re.match(r'^\s*```(\S*|$)', stripped_line) or \
           re.match(r'^#+\s(Summary|Tags|Created|Type)\s*$', stripped_line) or \
           re.match(r'^#+\s', stripped_line) and len(re.findall(r'^#', stripped_line)) < 2:
            continue
        
        cleaned_lines.append(stripped_line)
        
    return "\n".join(cleaned_lines)

def clean_not_applicable(text):
    """Handles 'Not applicable' case and removes questions/conversational filler."""
    has_no_questions(text)
    
    cleaned_text = text.strip()
    # Remove common conversational starts
    for phrase in CONVERSATIONAL_STARTS:
        if cleaned_text.lower().startswith(phrase):
            cleaned_text = cleaned_text[len(phrase):].strip()

    if "not applicable" in cleaned_text.lower():
        return "Not applicable"
    return cleaned_text.replace("?", "")

def check_structure(doc_md):
    """Checks for the presence of required markdown structure."""
    required_elements = {
        "summary": "## Summary",
        "details": "## Details",
        "key_functions": "## Key Functions/Classes",
        "usage_examples": "## Usage/Examples",
        "related": "## Related",
        "callout": "> [!INFO]"
    ***REMOVED***
    
    found_elements = {key: False for key in required_elements***REMOVED***

    for key, element in required_elements.items():
        if key != "callout" and element in doc_md:
            found_elements[key] = True
            
    if re.search(r'>\s*\[!INFO\]', doc_md):
        found_elements["callout"] = True

    for key, found in found_elements.items():
        if not found:
            logger.warning(f"Structure check failed: Missing '{required_elements[key]***REMOVED***'")

def final_clean(doc_md):
    """
    A more aggressive final cleaning step to remove any lines that are not part of the expected
    markdown structure.
    """
    lines = doc_md.split('\n')
    cleaned_lines = []
    in_code_block = False
    
    # Regex to match common markdown elements
    header_re = re.compile(r'^#+\s')
    list_item_re = re.compile(r'^\s*[-*+]\s')
    frontmatter_re = re.compile(r'^(tags:|created:|type:|---)')
    callout_re = re.compile(r'^\s*>\s*\[!')
    code_block_fence_re = re.compile(r'^\s*```')

    for line in lines:
        stripped_line = line.strip()

        # Handle code blocks
        if code_block_fence_re.match(stripped_line):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
            continue
            
        if in_code_block:
            cleaned_lines.append(line)
            continue

        # Preserve empty lines for spacing
        if not stripped_line:
            cleaned_lines.append(line)
            continue

        # Check if the line matches any expected markdown element
        if (
            header_re.match(stripped_line) or
            list_item_re.match(stripped_line) or
            frontmatter_re.match(stripped_line) or
            callout_re.match(stripped_line)
        ):
            cleaned_lines.append(line)
        else:
            if cleaned_lines and (header_re.match(cleaned_lines[-1].strip()) or not cleaned_lines[-1].strip()):
                cleaned_lines.append(line)
            else:
                logger.info(f"Removing extraneous line: '{line***REMOVED***'")


    return "\n".join(cleaned_lines)


def review_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        logger.error(f"Error reading {file_path***REMOVED***: {e***REMOVED***")
        return None

    content_tokens = estimate_tokens(raw_content)
    options = {
        "num_ctx": min(content_tokens + 2048, MAX_CTX),
    ***REMOVED***
    ***REMOVED***
    
    system_prompt = f"{TECH_DOC_EDITOR_PERSONA***REMOVED***\n\n{TASK_REVIEW_AND_IMPROVE***REMOVED***\n\n{STRICT_EDITING_RULES***REMOVED***\n\n**Output ONLY the full, corrected Markdown document.**"
    final_prompt = REVIEW_PROMPT.format(raw_content=raw_content)
    response = safe_generate(client, system=system_prompt, prompt=final_prompt, options=options, prompt_type="REVIEW_PROMPT")
    return response

def get_all_files(paths):
    valid_extensions = ('.py', '.txt', '.md', '.sh')
    skip_dirs = {'__pycache__', '.git', 'venv', '.obsidian', '.venv', 'To_Obsidian'***REMOVED***
    files_to_process = []

    for base_path in paths:
        if not os.path.exists(base_path):
            logger.warning(f"Path not found: {base_path***REMOVED***")
            continue
        for root, dirs, files in os.walk(base_path):
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            for file in files:
                if file.endswith(valid_extensions) and file not in {'recursive_obsidian_checks.py', 'obsidian_generator.py', 'debug_output.txt', 'prompt1.txt', 'document2obsidian.py'***REMOVED***:
                    files_to_process.append(os.path.join(root, file))
    return files_to_process

def wait_until_start_time(target_time_str):
    logger.info(f"Waiting until {target_time_str***REMOVED***...")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == target_time_str:
            logger.info(f"Starting at {now***REMOVED***.")
            break
        time.sleep(30)

def recursive_summarize(content, chunk_size=CHUNK_SIZE):
    if len(content) <= chunk_size:
        return content

    logger.info(f"Recursive summary: {len(content)***REMOVED*** chars > {chunk_size***REMOVED***")
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    summaries = []

    for i, chunk in enumerate(chunks, 1):
        logger.info(f"  Chunk {i***REMOVED***/{len(chunks)***REMOVED***")
        content_tokens = estimate_tokens(chunk)
        options = {"num_ctx": min(content_tokens + 1024, MAX_CTX), "temperature": 0.1***REMOVED***
        prompt = RECURSIVE_SUMMARY_PROMPT.format(chunk=chunk)
        summary = safe_generate(client, system=None, prompt=prompt, options=options, prompt_type="RECURSIVE_SUMMARY_PROMPT")
        if summary:
            summaries.append(summary)
    
    combined = "\n\n".join(summaries)
    return recursive_summarize(combined, chunk_size)

def generate_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        logger.error(f"Error reading {file_path***REMOVED***: {e***REMOVED***")
        return None
    
    file_size = len(raw_content)

    file_name = os.path.basename(file_path)
    file_name_without_ext, file_ext = os.path.splitext(file_name)

    processed_content = recursive_summarize(raw_content)

    options = {
        "num_ctx": min(estimate_tokens(processed_content) + 2048, MAX_CTX),
    ***REMOVED***
    ***REMOVED***

    system_prompt = f"{EXPERT_TECH_WRITER_PERSONA***REMOVED***\n\n{TASK_ANALYZE_AND_GENERATE***REMOVED***\n\n**Output Requirements:**\n{OUTPUT_FRONTMATTER***REMOVED***\n{OUTPUT_DOCUMENT_STRUCTURE***REMOVED***\n{CONTENT_INSTRUCTIONS***REMOVED***\n{CRUCIAL_RULES***REMOVED***\n\nBegin."

    # Generate each section separately
    summary_length = get_summary_length(file_size)
    summary_prompt = SUMMARY_PROMPT.format(processed_content=processed_content, summary_length=summary_length)
    summary = safe_generate(client, system=system_prompt, prompt=summary_prompt, options=options, prompt_type="SUMMARY_PROMPT")
    summary = validate_and_regenerate(summary, is_summary_valid, SUMMARY_PROMPT, system_prompt, options, "SUMMARY_PROMPT", processed_content, {'summary_length': summary_length***REMOVED***)
    summary = clean_summary(summary)

    details_prompt = DETAILS_PROMPT.format(processed_content=processed_content)
    details = safe_generate(client, system=system_prompt, prompt=details_prompt, options=options, prompt_type="DETAILS_PROMPT")
    details = validate_and_regenerate(details, has_no_questions, DETAILS_PROMPT, system_prompt, options, "DETAILS_PROMPT", processed_content)
    details = clean_details(details)


    key_functions_prompt = KEY_FUNCTIONS_PROMPT.format(processed_content=processed_content)
    key_functions = safe_generate(client, system=system_prompt, prompt=key_functions_prompt, options=options, prompt_type="KEY_FUNCTIONS_PROMPT")
    key_functions = validate_and_regenerate(key_functions, has_no_questions, KEY_FUNCTIONS_PROMPT, system_prompt, options, "KEY_FUNCTIONS_PROMPT", processed_content)
    key_functions = clean_not_applicable(key_functions)

    usage_prompt = USAGE_PROMPT.format(processed_content=processed_content)
    usage = safe_generate(client, system=system_prompt, prompt=usage_prompt, options=options, prompt_type="USAGE_PROMPT")
    usage = validate_and_regenerate(usage, has_no_questions, USAGE_PROMPT, system_prompt, options, "USAGE_PROMPT", processed_content)
    usage = clean_not_applicable(usage)
    
    num_tags = get_dynamic_count(file_size, 5, 20, 10000)
    num_links = get_dynamic_count(file_size, 2, 30, 10000)

    related_prompt = RELATED_PROMPT.format(processed_content=processed_content, num_links=num_links)
    related = safe_generate(client, system=system_prompt, prompt=related_prompt, options=options, prompt_type="RELATED_PROMPT")
    related = validate_and_regenerate(related, has_no_questions, RELATED_PROMPT, system_prompt, options, "RELATED_PROMPT", processed_content, {'num_links': num_links***REMOVED***)
    related = clean_not_applicable(related)

    tags_prompt = TAGS_PROMPT.format(processed_content=processed_content, num_tags=num_tags)
    tags = safe_generate(client, system=system_prompt, prompt=tags_prompt, options=options, prompt_type="TAGS_PROMPT")
    tags = validate_and_regenerate(tags, lambda t: is_tags_valid(t, num_tags), TAGS_PROMPT, system_prompt, options, "TAGS_PROMPT", processed_content, {'num_tags': num_tags***REMOVED***)
    tags = clean_tags(tags)

    type_prompt = TYPE_PROMPT.format(processed_content=processed_content)
    doc_type = safe_generate(client, system=system_prompt, prompt=type_prompt, options=options, prompt_type="TYPE_PROMPT")
    doc_type = clean_doc_type(doc_type)

    # Assemble the document
    doc_md = f"""
tags: {tags if tags else '#untagged'***REMOVED***
created: {datetime.now().strftime('%Y-%m-%d')***REMOVED***
type: {doc_type if doc_type else 'documentation'***REMOVED***

---

# {file_name_without_ext***REMOVED***

## Summary
```
{summary***REMOVED***
```
"""
    # Add details section with empty lines if it contains callouts
    if details.strip(): # Only add details if not empty
        doc_md += f"""
## Details
"""
        # If details contains a callout, ensure an empty line before it
        if re.search(r'^\s*>\s*\[!INFO\]', details, re.MULTILINE):
            doc_md += f"\n{details***REMOVED***\n\n" # Add empty line before and after
        else:
            doc_md += f"{details***REMOVED***\n\n"

    doc_md += f"""
## Key Functions/Classes
{key_functions***REMOVED***

## Usage/Examples
{usage***REMOVED***

## Related
{related***REMOVED***
"""
    
    check_structure(doc_md)
    has_no_questions(doc_md)
    doc_md = final_clean(doc_md)
    
    # Post-processing to remove markdown code block wrappers
    if doc_md.startswith("```markdown\n"):
        doc_md = doc_md[len("```markdown\n"):]
        if doc_md.endswith("\n```"):
            doc_md = doc_md[:-len("\n```")]
    elif doc_md.startswith("```\n"):
        doc_md = doc_md[len("```\n"):]
        if doc_md.endswith("\n```"):
            doc_md = doc_md[:-len("\n```")]
            
    return doc_md
def main():
    # wait_until_start_time(PREFERRED_START_TIME)  # Uncomment for scheduled
    
    ensure_dir(TARGET_DIR)
    all_files = get_all_files(SOURCE_PATHS)
    logger.info(f"Found {len(all_files)***REMOVED*** files to process.")
    
    revisit_list = []

    # Pass 1: New/Overwrite files (simple counter progress)
    processed = 0
    for file_path in all_files:
        processed += 1
        logger.info(f"[Pass 1] {processed***REMOVED***/{len(all_files)***REMOVED***: {os.path.basename(file_path)***REMOVED***")

        src_root = next((root for root in SOURCE_PATHS if file_path.startswith(root)), None)
        if not src_root:
            logger.warning(f"No root for {file_path***REMOVED***")
            continue

        relative_path = os.path.relpath(file_path, src_root)
        target_path = os.path.join(TARGET_DIR, relative_path)
        target_sub_dir = os.path.dirname(target_path)
        ensure_dir(target_sub_dir)

        base_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]
        target_path = os.path.join(target_sub_dir, f"{base_name_without_ext***REMOVED***.md")
        
        if os.path.exists(target_path):
            if not OVERWRITE_EXISTING:
                revisit_list.append(target_path)
                logger.info(f"  -> Exists, queued for review")
            else:
                logger.info(f"  -> Overwriting")
                doc_md = generate_obsidian_doc(file_path)
                if doc_md:
                    with open(target_path, 'w', encoding='utf-8') as f:
                        f.write(doc_md)
                else:
                    logger.error("  -> Generation failed")
        else:
            logger.info(f"  -> New file")
            doc_md = generate_obsidian_doc(file_path)
            if doc_md:
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(doc_md)
            else:
                logger.error("  -> Generation failed")

    # Pass 2: Review
    reviewed = 0
    for file_path in revisit_list:
        reviewed += 1
        logger.info(f"[Pass 2] {reviewed***REMOVED***/{len(revisit_list)***REMOVED***: {os.path.basename(file_path)***REMOVED***")
        
        reviewed_md = review_obsidian_doc(file_path)
        if reviewed_md:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(reviewed_md)
            logger.info("  -> Reviewed OK")
        else:
            logger.error("  -> Review failed")

    logger.info("All done. Check obsidian_generator.log for details.")

if __name__ == "__main__":
    main()