# Enhancement 7: Response Caching

## Priority: ⭐⭐⭐⭐ HIGH VALUE

## Problem
Every run regenerates documentation for all files, even if:
- File content hasn't changed
- Previous generation was successful
- Cache is fresh (< 7 days old)

This wastes time and Ollama resources.

## Current Code Location
`main.py:459-601` - `generate_obsidian_doc()` regenerates everything

## Solution
Implement file-hash based caching to skip unchanged files.

## Implementation

### Step 1: Create cache management module

Create new file: `cache_manager.py`

```python
import os
import json
import hashlib
import time
from datetime import datetime

CACHE_DIR = './cache'
CACHE_VERSION = '1.0'  # Increment when prompt changes
CACHE_TTL_DAYS = 7     # Cache validity period

def ensure_cache_dir():
    """Create cache directory if doesn't exist"""
    os.makedirs(CACHE_DIR, exist_ok=True)

def get_file_hash(file_path):
    """Calculate MD5 hash of file content"""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        return None

def get_cache_key(file_path, section_type, model_name):
    """Generate cache key including file hash, section, and model"""
    file_hash = get_file_hash(file_path)
    if not file_hash:
        return None

    # Include model name and cache version in key
    key_parts = [file_hash, section_type, model_name, CACHE_VERSION]
    key_string = '_'.join(key_parts)
    return hashlib.md5(key_string.encode()).hexdigest()

def get_cache_path(cache_key):
    """Get filesystem path for cache entry"""
    return os.path.join(CACHE_DIR, f"{cache_key}.json")

def get_cached_response(file_path, section_type, model_name):
    """
    Retrieve cached response if valid.

    Returns:
        Cached response text or None
    """
    ensure_cache_dir()
    cache_key = get_cache_key(file_path, section_type, model_name)
    if not cache_key:
        return None

    cache_path = get_cache_path(cache_key)
    if not os.path.exists(cache_path):
        return None

    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            cached = json.load(f)

        # Check cache age
        cache_age_days = (time.time() - cached['timestamp']) / (24 * 3600)
        if cache_age_days > CACHE_TTL_DAYS:
            return None

        # Verify cache version
        if cached.get('cache_version') != CACHE_VERSION:
            return None

        return cached['response']

    except Exception:
        return None

def cache_response(file_path, section_type, model_name, response):
    """Save response to cache"""
    ensure_cache_dir()
    cache_key = get_cache_key(file_path, section_type, model_name)
    if not cache_key:
        return

    cache_path = get_cache_path(cache_key)

    cache_entry = {
        'timestamp': time.time(),
        'cache_version': CACHE_VERSION,
        'file_path': file_path,
        'section_type': section_type,
        'model_name': model_name,
        'response': response,
        'created': datetime.now().isoformat()
    }

    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache_entry, f, indent=2)
    except Exception as e:
        # Caching is optional, don't fail if it errors
        pass

def clear_cache(older_than_days=None):
    """Clear cache entries"""
    ensure_cache_dir()

    if older_than_days is None:
        # Clear all
        for filename in os.listdir(CACHE_DIR):
            if filename.endswith('.json'):
                os.remove(os.path.join(CACHE_DIR, filename))
        return

    # Clear old entries
    cutoff_time = time.time() - (older_than_days * 24 * 3600)
    for filename in os.listdir(CACHE_DIR):
        if not filename.endswith('.json'):
            continue

        cache_path = os.path.join(CACHE_DIR, filename)
        try:
            with open(cache_path, 'r') as f:
                cached = json.load(f)
            if cached.get('timestamp', 0) < cutoff_time:
                os.remove(cache_path)
        except:
            # Remove corrupted cache files
            os.remove(cache_path)

def get_cache_stats():
    """Get cache statistics"""
    ensure_cache_dir()

    total_size = 0
    entry_count = 0
    oldest_entry = time.time()

    for filename in os.listdir(CACHE_DIR):
        if not filename.endswith('.json'):
            continue

        cache_path = os.path.join(CACHE_DIR, filename)
        total_size += os.path.getsize(cache_path)
        entry_count += 1

        try:
            with open(cache_path, 'r') as f:
                cached = json.load(f)
                oldest_entry = min(oldest_entry, cached.get('timestamp', time.time()))
        except:
            pass

    return {
        'entry_count': entry_count,
        'total_size_mb': total_size / (1024 * 1024),
        'oldest_age_days': (time.time() - oldest_entry) / (24 * 3600) if entry_count > 0 else 0
    }
```

### Step 2: Update main.py to use caching

```python
from cache_manager import (
    get_cached_response,
    cache_response,
    get_cache_stats,
    clear_cache
)

def generate_obsidian_doc(file_path):
    """Generate documentation with caching support"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None

    file_size = len(raw_content)
    file_name = os.path.basename(file_path)
    file_name_without_ext, file_ext = os.path.splitext(file_name)

    processed_content = recursive_summarize(raw_content)

    options = {
        "num_ctx": min(estimate_tokens(processed_content) + 2048, MAX_CTX),
        "temperature": 0.2,
        "keep_alive": "30m"
    }

    system_prompt = f"{RALF_ANALYST_PERSONA}\n\n{TASK_ANALYZE_AND_GENERATE}\n\n**Output Requirements:**\n{OUTPUT_FRONTMATTER}\n{OUTPUT_DOCUMENT_STRUCTURE}\n{CONTENT_INSTRUCTIONS}\n{CRUCIAL_RULES}\n\nBegin."

    summary_length = get_summary_length(file_size)
    num_tags = get_dynamic_count(file_size, 5, 20, 10000)
    num_links = get_dynamic_count(file_size, 2, 30, 10000)

    # Try cache first for each section
    cache_hits = 0
    cache_misses = 0

    # Summary
    summary = get_cached_response(file_path, 'SUMMARY', MODEL_NAME)
    if summary:
        cache_hits += 1
        logger.debug(f"Cache hit: SUMMARY")
    else:
        cache_misses += 1
        summary_prompt = SUMMARY_PROMPT.format(processed_content=processed_content, summary_length=summary_length)
        summary = safe_generate(client, system=system_prompt, prompt=summary_prompt, options=options, prompt_type="SUMMARY_PROMPT")
        summary = validate_and_regenerate(summary, is_summary_valid, SUMMARY_PROMPT, system_prompt, options, "SUMMARY_PROMPT", processed_content, {'summary_length': summary_length})
        cache_response(file_path, 'SUMMARY', MODEL_NAME, summary)

    summary = clean_summary(summary)

    # Details
    details = get_cached_response(file_path, 'DETAILS', MODEL_NAME)
    if details:
        cache_hits += 1
    else:
        cache_misses += 1
        details_prompt = DETAILS_PROMPT.format(processed_content=processed_content)
        details = safe_generate(client, system=system_prompt, prompt=details_prompt, options=options, prompt_type="DETAILS_PROMPT")
        details = validate_and_regenerate(details, has_no_questions, DETAILS_PROMPT, system_prompt, options, "DETAILS_PROMPT", processed_content)
        cache_response(file_path, 'DETAILS', MODEL_NAME, details)

    details = clean_details(details)

    # ... repeat for all sections ...

    if cache_hits > 0:
        logger.info(f"Cache: {cache_hits} hits, {cache_misses} misses")

    # ... rest of document assembly ...
```

### Step 3: Add cache management to config.py

```python
# Cache configuration
ENABLE_CACHING = True              # Enable response caching
CACHE_TTL_DAYS = 7                 # Cache validity (days)
CLEAR_CACHE_ON_START = False       # Clear cache before processing
```

### Step 4: Add cache management to main()

```python
def main():
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Cache management
    if CLEAR_CACHE_ON_START:
        logger.info("Clearing cache...")
        clear_cache()

    if ENABLE_CACHING:
        cache_stats = get_cache_stats()
        logger.info(f"Cache: {cache_stats['entry_count']} entries, {cache_stats['total_size_mb']:.2f} MB")

    # ... rest of main ...
```

## Configuration Options

### config.py additions:
```python
# Caching settings
ENABLE_CACHING = True
CACHE_TTL_DAYS = 7
CACHE_DIR = './cache'
CLEAR_CACHE_ON_START = False
```

## Expected Impact

### Time Savings
**First run (100 files):**
- 100 files × 8 sections × 10s = 800s (13 minutes)
- Cache misses: 800

**Second run (10 files changed):**
- 10 changed files: 80 sections × 10s = 800s
- 90 unchanged files: 0s (all cached)
- **Total: 800s vs. 8000s (10x faster)**

### Resource Savings
- Reduced Ollama load (fewer requests)
- Lower CPU usage
- Less context switching

## Cache Invalidation

Cache is invalidated when:
1. File content changes (different hash)
2. Cache is older than TTL (7 days)
3. Cache version changes (prompts updated)
4. Model changes (different model name)

## CLI Commands

Add command-line cache management:

```python
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == '--clear-cache':
            print("Clearing cache...")
            clear_cache()
            print("Cache cleared.")
            sys.exit(0)
        elif sys.argv[1] == '--cache-stats':
            stats = get_cache_stats()
            print(f"Cache Statistics:")
            print(f"  Entries: {stats['entry_count']}")
            print(f"  Size: {stats['total_size_mb']:.2f} MB")
            print(f"  Oldest: {stats['oldest_age_days']:.1f} days")
            sys.exit(0)

    main()
```

Usage:
```bash
python main.py --clear-cache     # Clear all cache
python main.py --cache-stats     # Show cache statistics
python main.py                   # Normal run with caching
```

## Testing
- [ ] Process files, verify cache created
- [ ] Re-run without changes, verify cache hits
- [ ] Modify file, verify cache miss
- [ ] Change model, verify cache miss
- [ ] Wait 8 days, verify TTL expiration
- [ ] Check cache directory size

## Notes
- Cache directory can grow large (1-2 MB per file)
- Run `--clear-cache` periodically
- Increment `CACHE_VERSION` when prompts change
- Cache is local only (not shared across machines)
