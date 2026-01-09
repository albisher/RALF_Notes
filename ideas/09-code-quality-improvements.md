# Code Quality Improvements

Analysis of current code with recommendations for better maintainability.

## Issues Found

### 1. Magic Numbers (Scattered Throughout)

**Problem:** Hardcoded numbers without explanation

#### main.py:208
```python
if len(final_summary.split()) > 150:  # Why 150?
    final_summary = " ".join(final_summary.split()[:150]) + "..."
```

**Fix:** Move to constants
```python
# At top of file
MAX_SUMMARY_WORDS = 150  # Maximum words in summary to prevent bloat

def clean_summary(text):
    # ...
    if len(final_summary.split()) > MAX_SUMMARY_WORDS:
        final_summary = " ".join(final_summary.split()[:MAX_SUMMARY_WORDS]) + "..."
```

#### main.py:82-94 (get_dynamic_count, get_summary_length)
```python
def get_dynamic_count(file_size, min_count, max_count, max_count_file_size):
    if file_size >= max_count_file_size:  # 10000 hardcoded at call sites
        return max_count
```

**Fix:** Define file size thresholds
```python
# config.py
FILE_SIZE_THRESHOLDS = {
    'small': 2000,
    'medium': 10000,
    'large': 50000
}

TAG_COUNTS = {
    'min': 5,
    'max': 20
}
```

---

### 2. Deep Nesting (main.py:295-339)

**Problem:** `clean_details()` has 4 levels of nesting

```python
def clean_details(text):
    for line in lines:
        if is_callout_header:
            if in_callout_block:
                if not stripped_line:
                    # 4 levels deep!
```

**Fix:** Extract callout processing
```python
def process_callout_line(line, in_callout_block):
    """Process a single line within a callout block"""
    stripped = line.strip()

    if not stripped:
        return stripped, False  # End callout block

    if not stripped.startswith('>'):
        stripped = '> ' + stripped

    return stripped, True  # Continue callout block

def clean_details(text):
    lines = text.strip().split('\n')
    cleaned_lines = []
    in_callout_block = False

    for line in lines:
        stripped_line = line.strip()

        # Check for callout header
        if re.match(r'^\s*>\[!INFO\]', stripped_line):
            in_callout_block = True
            # Remove unwanted titles
            stripped_line = re.sub(r'\s*\*\*Bug Note\*\*', '', stripped_line).strip()
            cleaned_lines.append(stripped_line)
            continue

        # Process callout content
        if in_callout_block:
            processed, in_callout_block = process_callout_line(line, in_callout_block)
            cleaned_lines.append(processed)
            continue

        # Regular line processing
        if should_skip_line(stripped_line):
            continue

        cleaned_lines.append(stripped_line)

    return "\n".join(cleaned_lines)

def should_skip_line(line):
    """Check if line should be skipped in details"""
    if not line:
        return True
    if line.startswith(('tags:', 'created:', 'type:', '---')):
        return True
    if re.match(r'^\s*```(\S*|$)', line):
        return True
    if re.match(r'^#+\s(Summary|Tags|Created|Type)\s*$', line):
        return True
    return False
```

---

### 3. Global Client (main.py:50)

**Problem:** Mutable global state

```python
client = Client(host=OLLAMA_HOST)  # Global
```

**Fix:** Dependency injection
```python
class OllamaClient:
    """Wrapper for Ollama client with connection management"""

    def __init__(self, host=OLLAMA_HOST):
        self.host = host
        self.client = Client(host=host)

    def generate(self, **kwargs):
        """Delegate to underlying client"""
        return self.client.generate(**kwargs)

    def list(self):
        """List available models"""
        return self.client.list()

    def show(self, model_name):
        """Show model details"""
        return self.client.show(model_name)

# Usage
def main():
    ollama = OllamaClient()

    if not validate_model_availability(ollama):
        return

    warmup_model(ollama)
    # ... pass ollama to functions
```

---

### 4. Broad Exception Handling (main.py:120-124)

**Problem:** Catches everything

```python
except (ResponseError, Exception) as e:  # Too broad!
```

**Fix:** Specific exception handling
```python
except ResponseError as e:
    # Known API error
    logger.warning(f"Ollama API error: {e}")
    if attempt == 2:
        raise
except ConnectionError as e:
    # Connection issue
    logger.warning(f"Connection error: {e}")
    time.sleep(2 ** attempt)
except TimeoutError as e:
    # Timeout
    logger.warning(f"Timeout: {e}")
    time.sleep(2 ** attempt)
except Exception as e:
    # Unexpected error - log and re-raise
    logger.error(f"Unexpected error: {type(e).__name__}: {e}")
    raise
```

---

### 5. No Input Validation (main.py:459)

**Problem:** Assumes file is valid

```python
def generate_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
```

**Fix:** Validate inputs
```python
def validate_file_for_processing(file_path):
    """Validate file before processing"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"Not a file: {file_path}")

    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Cannot read file: {file_path}")

    # Check if file is too large
    file_size = os.path.getsize(file_path)
    if file_size > 10 * 1024 * 1024:  # 10MB
        raise ValueError(f"File too large ({file_size} bytes): {file_path}")

    # Try to read as UTF-8
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(100)  # Read first 100 bytes to validate
    except UnicodeDecodeError:
        raise ValueError(f"File is not valid UTF-8: {file_path}")

def generate_obsidian_doc(file_path):
    # Validate first
    validate_file_for_processing(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
```

---

### 6. Hardcoded File Extensions (main.py:415)

**Problem:** Not configurable

```python
valid_extensions = ('.py', '.txt', '.md', '.sh')  # Should be in config
```

**Fix:** Move to config.py
```python
# config.py
VALID_EXTENSIONS = ('.py', '.txt', '.md', '.sh', '.js', '.ts', '.yaml', '.json')

# main.py
def get_all_files(paths):
    valid_extensions = VALID_EXTENSIONS  # From config
    # ...
```

---

### 7. No Type Hints

**Problem:** Functions lack type information

```python
def estimate_tokens(text):  # What type is text? What returns?
    return len(text.split()) * 1.3 + 100
```

**Fix:** Add type hints
```python
def estimate_tokens(text: str, content_type: str = 'auto') -> int:
    """
    Estimate token count for text.

    Args:
        text: Content to estimate
        content_type: 'code', 'prose', or 'auto'

    Returns:
        Estimated token count
    """
    if not text:
        return 0
    # ...
```

---

### 8. Recursive Summarization Without Memoization

**Problem:** May re-process same chunks

**Fix:** Add caching
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def summarize_chunk_cached(chunk_hash: str, chunk: str, content_type: str) -> str:
    """Cached chunk summarization"""
    # ... summarization logic
    pass

def recursive_summarize(content, chunk_size=CHUNK_SIZE, content_type='auto'):
    if len(content) <= chunk_size:
        return content

    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    summaries = []

    for chunk in chunks:
        chunk_hash = hashlib.md5(chunk.encode()).hexdigest()
        summary = summarize_chunk_cached(chunk_hash, chunk, content_type)
        summaries.append(summary)

    combined = "\n\n".join(summaries)
    return recursive_summarize(combined, chunk_size, content_type)
```

---

## Recommended File Structure

Split large `main.py` (680 lines) into modules:

```
RALF_Notes/
├── config.py               # Configuration
├── main.py                 # Entry point, orchestration
├── models/
│   ├── __init__.py
│   ├── ollama_client.py    # OllamaClient class
│   └── model_manager.py    # Model detection, warmup
├── generators/
│   ├── __init__.py
│   ├── document_generator.py  # generate_obsidian_doc
│   └── section_generator.py   # Section-specific generation
├── validators/
│   ├── __init__.py
│   └── content_validators.py  # Validation functions
├── cleaners/
│   ├── __init__.py
│   └── content_cleaners.py     # Cleaning functions
├── utils/
│   ├── __init__.py
│   ├── token_estimator.py
│   ├── file_utils.py
│   └── logger.py
└── prompts.py              # Prompts (unchanged)
```

---

## Priority Fixes

### High Priority (Do First):
1. Move magic numbers to config constants
2. Add type hints to public functions
3. Extract nested logic (clean_details)
4. Add input validation

### Medium Priority:
5. Split main.py into modules
6. Improve exception handling
7. Add memoization to recursive_summarize

### Low Priority (Nice to Have):
8. Dependency injection for client
9. Comprehensive unit tests
10. Documentation strings

---

## Testing Strategy

Add unit tests for cleaning functions:

```python
# tests/test_cleaners.py
import pytest
from cleaners.content_cleaners import clean_summary, clean_tags

def test_clean_summary_removes_code_fences():
    input_text = "```python\nSummary here\n```"
    expected = "Summary here"
    assert clean_summary(input_text) == expected

def test_clean_tags_removes_stop_words():
    input_text = "#python #the #code #to #testing"
    expected = "#python #code #testing"
    assert clean_tags(input_text) == expected

def test_clean_tags_handles_duplicates():
    input_text = "#python #testing #python #code #testing"
    expected = "#code #python #testing"  # Sorted, unique
    assert clean_tags(input_text) == expected
```

---

## Checklist

- [ ] Move magic numbers to constants
- [ ] Add type hints to key functions
- [ ] Extract nested logic from clean_details
- [ ] Add input validation to generate_obsidian_doc
- [ ] Move file extensions to config
- [ ] Improve exception handling granularity
- [ ] Add docstrings to all functions
- [ ] Consider splitting main.py into modules
- [ ] Add unit tests for cleaners
- [ ] Document all configuration options
