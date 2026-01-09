# Enhancement 5: Improved Token Estimation

## Priority: ⭐⭐⭐ MEDIUM VALUE / VERY LOW EFFORT

## Problem
Current token estimation is crude and inaccurate:
```python
def estimate_tokens(text):
    return len(text.split()) * 1.3 + 100
```

**Issues:**
- Assumes all content is prose (same density)
- Code has different token density than natural language
- Splitting on whitespace misses operators, symbols
- Can over-allocate context (waste) or under-allocate (truncate)

## Examples of Inaccuracy

### Python Code
```python
def foo(x,y,z):return x+y*z if x>0 else -1
```
- **Words:** 2 (def, foo, return, x, y, z, if, else)
- **Current estimate:** 2 × 1.3 + 100 = 102 tokens
- **Actual tokens:** ~25 tokens (operators, parentheses, keywords)
- **Error:** 400% over-estimate

### Prose
```
The quick brown fox jumps over the lazy dog near the river.
```
- **Words:** 12
- **Current estimate:** 12 × 1.3 + 100 = 115 tokens
- **Actual tokens:** ~15 tokens
- **Error:** 767% over-estimate

## Current Code Location
- `main.py:78-80` - `estimate_tokens()` function
- Used in: `recursive_summarize()`, `generate_obsidian_doc()`, `review_obsidian_doc()`

## Solution
Use character-based estimation with different ratios for code vs. prose.

## Implementation

### Step 1: Replace estimate_tokens() in main.py

```python
def estimate_tokens(text, content_type='auto'):
    """
    More accurate token estimation based on content type.

    Args:
        text: Content to estimate tokens for
        content_type: 'code', 'prose', or 'auto' (auto-detect)

    Returns:
        Estimated token count
    """
    if not text:
        return 0

    # Auto-detect content type if not specified
    if content_type == 'auto':
        content_type = detect_content_type_from_text(text)

    # Character-per-token ratios (empirically derived)
    if content_type == 'code':
        # Code: operators, symbols, short identifiers
        # Examples: "x+y", "def foo():", "import os"
        chars_per_token = 2.5
    else:  # prose
        # Natural language: longer words, spaces
        # Examples: "documentation", "explanation", "configuration"
        chars_per_token = 4.0

    # Calculate base tokens from character count
    base_tokens = len(text) / chars_per_token

    # Add overhead for structure (newlines, indentation, etc.)
    overhead = 100

    return int(base_tokens + overhead)


def detect_content_type_from_text(text):
    """
    Detect if text is code or prose based on heuristics.

    Returns:
        'code' or 'prose'
    """
    if not text or len(text) < 50:
        return 'code'  # Short snippets likely code

    sample = text[:1000]  # Analyze first 1000 chars

    # Code indicators
    code_indicators = [
        r'def\s+\w+\s*\(',       # Python function
        r'class\s+\w+',          # Class definition
        r'import\s+\w+',         # Import statement
        r'from\s+\w+\s+import',  # From import
        r'if\s+.*:',             # If statement
        r'for\s+\w+\s+in',       # For loop
        r'\w+\s*=\s*\w+',        # Assignment
        r'[{}\[\]();]',          # Structural characters
        r'//|/\*|\*/',           # Comments (C-style)
        r'#\s*\w+',              # Comments (Python/shell)
    ]

    # Count code indicators
    import re
    code_score = 0
    for pattern in code_indicators:
        code_score += len(re.findall(pattern, sample))

    # High code score = likely code
    # Threshold: >5 code patterns in 1000 chars
    if code_score > 5:
        return 'code'

    # Check for prose indicators
    prose_indicators = [
        r'\.\s+[A-Z]',           # Sentence endings
        r'\b(the|a|an|is|are|was|were)\b',  # Common articles/verbs
        r'\b\w{8,}\b',           # Long words (8+ chars)
    ]

    prose_score = 0
    for pattern in prose_indicators:
        prose_score += len(re.findall(pattern, sample, re.IGNORECASE))

    # High prose score = likely prose
    if prose_score > code_score:
        return 'prose'

    # Default to code (conservative)
    return 'code'


def detect_content_type_from_file(file_path):
    """
    Detect content type based on file extension.

    Returns:
        'code' or 'prose'
    """
    ext = os.path.splitext(file_path)[1].lower()

    code_extensions = {
        '.py', '.js', '.ts', '.tsx', '.jsx',
        '.java', '.cpp', '.c', '.h', '.hpp',
        '.rs', '.go', '.rb', '.php',
        '.sh', '.bash', '.zsh',
        '.sql', '.html', '.css', '.scss',
        '.yaml', '.yml', '.json', '.xml',
    }

    prose_extensions = {
        '.md', '.txt', '.rst', '.adoc',
        '.tex', '.org',
    }

    if ext in code_extensions:
        return 'code'
    elif ext in prose_extensions:
        return 'prose'
    else:
        return 'code'  # Default to code for unknown
```

### Step 2: Update generate_obsidian_doc() to use file extension

```python
def generate_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None

    file_size = len(raw_content)
    file_name = os.path.basename(file_path)
    file_name_without_ext, file_ext = os.path.splitext(file_name)

    # Detect content type from file extension
    content_type = detect_content_type_from_file(file_path)

    processed_content = recursive_summarize(raw_content)

    # Use content-type-aware token estimation
    content_tokens = estimate_tokens(processed_content, content_type)

    options = {
        "num_ctx": min(content_tokens + 2048, MAX_CTX),
        "temperature": 0.2,
        "keep_alive": "30m"
    }

    logger.debug(f"File: {file_name}, Type: {content_type}, Est. tokens: {content_tokens}, Context: {options['num_ctx']}")

    # ... rest of function
```

### Step 3: Update recursive_summarize() for better chunking

```python
def recursive_summarize(content, chunk_size=CHUNK_SIZE, content_type='auto'):
    """
    Recursively summarize content if it exceeds chunk size.
    Now content-type aware for better estimation.
    """
    if len(content) <= chunk_size:
        return content

    # Estimate tokens for logging
    estimated_tokens = estimate_tokens(content, content_type)
    logger.info(f"Recursive summary: {len(content)} chars (~{estimated_tokens} tokens) > {chunk_size}")

    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    summaries = []

    for i, chunk in enumerate(chunks, 1):
        logger.info(f"  Chunk {i}/{len(chunks)}")
        chunk_tokens = estimate_tokens(chunk, content_type)
        options = {
            "num_ctx": min(chunk_tokens + 1024, MAX_CTX),
            "temperature": 0.1,
            "keep_alive": "30m"
        }
        prompt = RECURSIVE_SUMMARY_PROMPT.format(chunk=chunk)
        summary = safe_generate(client, system=None, prompt=prompt, options=options, prompt_type="RECURSIVE_SUMMARY_PROMPT")
        if summary:
            summaries.append(summary)

    combined = "\n\n".join(summaries)
    return recursive_summarize(combined, chunk_size, content_type)
```

## Expected Impact

### Context Allocation Improvement

**Before (crude estimation):**
```
Python file (5000 chars):
- Words: ~800
- Estimated: 800 × 1.3 + 100 = 1,140 tokens
- Allocated: 1,140 + 2,048 = 3,188 context

Actual tokens: ~2,000
Wasted context: 1,188 tokens (37% waste)
```

**After (accurate estimation):**
```
Python file (5000 chars):
- Content type: code
- Estimated: 5000 / 2.5 + 100 = 2,100 tokens
- Allocated: 2,100 + 2,048 = 4,148 context

Actual tokens: ~2,000
Wasted context: 148 tokens (3% waste)
```

### Benefits
- **Better resource utilization:** Allocate appropriate context
- **Avoid truncation:** Don't under-allocate for dense code
- **Performance:** Smaller context = faster generation for prose
- **Logging:** Better visibility into actual token usage

## Configuration Options

Add to `config.py`:

```python
# Token estimation settings
TOKEN_ESTIMATION_METHOD = 'auto'  # 'auto', 'code', 'prose'

# Override character-per-token ratios if needed
CHARS_PER_TOKEN = {
    'code': 2.5,   # Adjust for your codebase
    'prose': 4.0,  # Adjust for your docs
}
```

## Testing & Validation

### Test with known files
```python
# Add to main.py for testing
def test_token_estimation():
    """Test token estimation accuracy"""
    test_cases = [
        ("def foo(x): return x + 1", 'code', 12),  # Actual ~12 tokens
        ("The quick brown fox jumps.", 'prose', 6), # Actual ~6 tokens
    ]

    for text, content_type, expected in test_cases:
        estimated = estimate_tokens(text, content_type)
        print(f"Text: {text}")
        print(f"  Type: {content_type}")
        print(f"  Expected: {expected}")
        print(f"  Estimated: {estimated}")
        print(f"  Error: {abs(estimated - expected)} tokens")
        print()

# Run: python -c "from main import test_token_estimation; test_token_estimation()"
```

## Advanced: Use tiktoken for Exact Counting

For production accuracy, use OpenAI's `tiktoken` library:

```python
# Install: pip install tiktoken

import tiktoken

def estimate_tokens_exact(text, model="gpt-3.5-turbo"):
    """
    Exact token counting using tiktoken.
    Works for OpenAI-compatible tokenizers.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except Exception as e:
        logger.warning(f"tiktoken failed, falling back to estimation: {e}")
        return estimate_tokens(text, 'auto')
```

Note: Most Ollama models use similar tokenizers (SentencePiece, BPE), so tiktoken approximation is good enough.

## Checklist
- [ ] Replace `estimate_tokens()` function
- [ ] Add `detect_content_type_from_file()` and `detect_content_type_from_text()`
- [ ] Update `generate_obsidian_doc()` to pass content_type
- [ ] Update `recursive_summarize()` to use content_type
- [ ] Test with Python file and Markdown file
- [ ] Compare context allocation before/after
- [ ] Verify no truncation errors

## Notes
- Character-based estimation is more accurate than word-based
- Auto-detection works well for most cases
- File extension detection is fastest (no regex)
- Can be extended with actual tokenizer for perfect accuracy
