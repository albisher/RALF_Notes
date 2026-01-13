# Rate Limiting Options for RALF Notes

## Current State
RALF Notes currently has **no rate limiting** implemented. Files are processed as fast as Ollama can respond.

---

## Available Configuration Options

### 1. **Request Delay Between Files**
Add a delay between processing each file to avoid overwhelming Ollama.

**Config Parameter:**
```json
{
  "request_delay_seconds": 0.5
}
```

**Implementation:**
```python
# In file_processor.py after each file
import time
time.sleep(config.get("request_delay_seconds", 0))
```

**Use Cases:**
- Prevent Ollama server overload
- Give system time to cool down
- Better for shared Ollama instances

---

### 2. **Max Concurrent Requests**
Limit how many files can be processed in parallel.

**Config Parameter:**
```json
{
  "max_concurrent_requests": 1
}
```

**Implementation:**
```python
# Use ThreadPoolExecutor with max_workers
from concurrent.futures import ThreadPoolExecutor

max_workers = config.get("max_concurrent_requests", 1)
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Process files in parallel
```

**Use Cases:**
- Single file at a time (current behavior): `1`
- Light parallelization: `2-4`
- Aggressive parallelization: `8+`

---

### 3. **Requests Per Minute Limit**
Cap the maximum number of LLM calls per minute.

**Config Parameter:**
```json
{
  "max_requests_per_minute": 30
}
```

**Implementation:**
```python
# Track request timestamps and throttle if needed
from collections import deque
from time import time, sleep

class RateLimiter:
    def __init__(self, max_per_minute):
        self.max_per_minute = max_per_minute
        self.requests = deque()

    def wait_if_needed(self):
        now = time()
        # Remove requests older than 1 minute
        while self.requests and self.requests[0] < now - 60:
            self.requests.popleft()

        # If at limit, wait
        if len(self.requests) >= self.max_per_minute:
            sleep(60 - (now - self.requests[0]))

        self.requests.append(time())
```

**Use Cases:**
- Respect API quotas
- Prevent server bans
- Share Ollama with other apps

---

### 4. **Backoff Strategy for Errors**
Implement exponential backoff when Ollama returns errors.

**Config Parameters:**
```json
{
  "retry_attempts": 3,
  "initial_backoff_seconds": 1,
  "backoff_multiplier": 2
}
```

**Implementation:**
```python
def generate_with_retry(self, context, max_retries=3):
    backoff = 1
    for attempt in range(max_retries):
        try:
            return self.generator.generate(context)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            sleep(backoff)
            backoff *= 2  # Exponential backoff
```

**Use Cases:**
- Handle temporary Ollama unavailability
- Recover from network issues
- More robust processing

---

### 5. **Batch Size Limit**
Process files in smaller batches with breaks between batches.

**Config Parameters:**
```json
{
  "batch_size": 10,
  "batch_delay_seconds": 5
}
```

**Implementation:**
```python
# In file_processor.py
for i in range(0, len(files), batch_size):
    batch = files[i:i + batch_size]
    process_batch(batch)
    if i + batch_size < len(files):
        time.sleep(batch_delay_seconds)
```

**Use Cases:**
- Give Ollama breaks to recover
- Better memory management
- Easier to pause/resume

---

### 6. **Timeout Limits**
Set maximum time allowed for each request.

**Config Parameter:**
```json
{
  "request_timeout_seconds": 120
}
```

**Implementation:**
```python
# Use threading.Timer or asyncio.timeout
import signal
from contextlib import contextmanager

@contextmanager
def timeout(seconds):
    def timeout_handler(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

# Usage
with timeout(config.get("request_timeout_seconds", 120)):
    result = generator.generate(context)
```

**Use Cases:**
- Prevent hanging on stuck requests
- Fail fast on problematic files
- Better user experience

---

### 7. **Token Budget Limits**
Track and limit total tokens processed per session.

**Config Parameters:**
```json
{
  "max_tokens_per_session": 1000000,
  "warn_at_token_percentage": 80
}
```

**Implementation:**
```python
class TokenTracker:
    def __init__(self, max_tokens):
        self.max_tokens = max_tokens
        self.used_tokens = 0

    def can_process(self, estimated_tokens):
        return self.used_tokens + estimated_tokens <= self.max_tokens

    def add_usage(self, tokens):
        self.used_tokens += tokens
        if self.used_tokens > self.max_tokens * 0.8:
            console.warning(f"80% of token budget used")
```

**Use Cases:**
- Control costs (if using paid API)
- Prevent excessive usage
- Budget awareness

---

## Recommended Default Configuration

```json
{
  "request_delay_seconds": 0,
  "max_concurrent_requests": 1,
  "max_requests_per_minute": 0,
  "retry_attempts": 3,
  "initial_backoff_seconds": 1,
  "backoff_multiplier": 2,
  "batch_size": 0,
  "batch_delay_seconds": 0,
  "request_timeout_seconds": 300,
  "max_tokens_per_session": 0
}
```

**Note:** `0` means "no limit" for most settings.

---

## CLI Options to Add

```bash
# Delay between files
ralf-notes generate --delay 0.5

# Parallel processing
ralf-notes generate --parallel 4

# Rate limit
ralf-notes generate --rate-limit 30

# Batch processing
ralf-notes generate --batch-size 10 --batch-delay 5

# Timeout
ralf-notes generate --timeout 120
```

---

## Priority Implementation Order

### High Priority (Implement First)
1. ✅ **Request Delay** - Simple, effective, prevents overload
2. ✅ **Retry with Backoff** - Improves reliability
3. ✅ **Timeout Limits** - Prevents hanging

### Medium Priority
4. **Batch Processing** - Better control for large codebases
5. **Max Concurrent Requests** - Enable parallelization when safe

### Low Priority (Nice to Have)
6. **Requests Per Minute** - Only if using shared/remote Ollama
7. **Token Budget** - Only relevant for paid APIs

---

## Implementation Example

Here's how to add request delay (simplest option):

### 1. Update Config
```python
# config_manager.py
DEFAULT_CONFIG = {
    ...
    "request_delay_seconds": 0.0,
}
```

### 2. Update File Processor
```python
# file_processor.py
import time

def process_paths(self, ...):
    delay = config_manager.get("request_delay_seconds", 0.0)

    for i, file_path in enumerate(files, 1):
        # ... process file ...

        # Add delay after processing (except last file)
        if delay > 0 and i < len(files):
            time.sleep(delay)
```

### 3. Add CLI Option
```python
# cli.py
@app.command()
def generate(
    ...
    delay: float = typer.Option(
        None,
        "--delay",
        help="Delay in seconds between files"
    ),
):
    if delay is not None:
        config_manager.set("request_delay_seconds", delay)
```

### 4. Test
```bash
# No delay (default)
ralf-notes generate

# 0.5 second delay between files
ralf-notes generate --delay 0.5

# 2 second delay
ralf-notes generate --delay 2
```

---

## Current Performance Metrics

Based on testing:
- **Average processing time:** ~14 seconds per file
- **LLM calls per file:** 1 (unified JSON approach)
- **Batch of 100 files:** ~23 minutes
- **Bottleneck:** LLM inference time (not rate limiting)

**Conclusion:** For local Ollama, rate limiting is **optional**. The LLM inference is naturally slow enough that there's no risk of overwhelming the system.

---

## When You Actually Need Rate Limiting

### ✅ **Yes, implement rate limiting if:**
- Using shared Ollama instance with multiple users
- Using remote Ollama API with quotas
- Using paid LLM API (OpenAI, Anthropic, etc.)
- Processing thousands of files regularly
- Running on resource-constrained system

### ❌ **No, skip rate limiting if:**
- Using local Ollama instance
- Processing < 1000 files at a time
- Have dedicated hardware for Ollama
- No quota/cost concerns

---

## Future Enhancements

### Smart Rate Limiting
- Auto-detect Ollama capacity
- Adjust rate based on response times
- Pause if Ollama becomes unresponsive

### Adaptive Batching
- Smaller batches for large files
- Larger batches for small files
- Dynamic batch sizing

### Cost Tracking
- Log tokens used per file
- Show cost estimates
- Budget warnings

---

## Summary

**Current State:** No rate limiting (works fine for local Ollama)

**Recommended First Step:** Add `--delay` option for simple throttling

**Full Implementation:** 2-3 hours of development work

**Value:** Medium (nice to have, not critical for most users)
