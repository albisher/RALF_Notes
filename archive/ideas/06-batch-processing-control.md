# Enhancement 6: Batch Processing Control

## Priority: ⭐⭐⭐ MEDIUM VALUE

## Problem
Current implementation processes all files sequentially without:
- Resource monitoring (RAM, CPU)
- Throttling when system is overloaded
- Progress reporting
- Ability to pause/resume
- Handling of large batches (100+ files)

## Current Code Location
`main.py:603-677` - `main()` function processes all files in single loop

## Solution
Add intelligent batch processing with resource monitoring and throttling.

## Implementation

### Step 1: Add resource monitoring

```python
import psutil  # Add to imports, install: pip install psutil

def get_system_resources():
    """Check available system resources"""
    mem = psutil.virtual_memory()
    return {
        'ram_available_gb': mem.available / (1024**3),
        'ram_percent': mem.percent,
        'ram_total_gb': mem.total / (1024**3),
        'cpu_percent': psutil.cpu_percent(interval=1),
        'cpu_count': psutil.cpu_count()
    }

def should_throttle():
    """Determine if we need to slow down processing"""
    resources = get_system_resources()

    # Throttle if RAM > 85% or CPU > 90%
    if resources['ram_percent'] > 85:
        logger.warning(f"High RAM usage: {resources['ram_percent']:.1f}%")
        return True

    if resources['cpu_percent'] > 90:
        logger.warning(f"High CPU usage: {resources['cpu_percent']:.1f}%")
        return True

    return False

def log_resource_stats():
    """Log current resource usage"""
    resources = get_system_resources()
    logger.info(f"Resources: RAM {resources['ram_percent']:.1f}% ({resources['ram_available_gb']:.1f}GB free), CPU {resources['cpu_percent']:.1f}%")
```

### Step 2: Add progress tracking

```python
from tqdm import tqdm  # Install: pip install tqdm

def process_files_with_progress(files_to_process, batch_size=5):
    """
    Process files in batches with progress tracking and resource monitoring.

    Args:
        files_to_process: List of file paths
        batch_size: Number of files to process before checking resources

    Returns:
        Dictionary with processing statistics
    """
    stats = {
        'total_files': len(files_to_process),
        'processed': 0,
        'failed': 0,
        'skipped': 0,
        'throttle_pauses': 0,
        'start_time': time.time()
    }

    with tqdm(total=len(files_to_process), desc="Processing files", unit="file") as pbar:
        for i in range(0, len(files_to_process), batch_size):
            batch = files_to_process[i:i+batch_size]

            # Check resources before batch
            if should_throttle():
                stats['throttle_pauses'] += 1
                logger.warning("System resources constrained, pausing for 30s...")
                log_resource_stats()
                time.sleep(30)

            # Process batch
            for file_path in batch:
                try:
                    src_root = next((root for root in SOURCE_PATHS if file_path.startswith(root)), None)
                    if not src_root:
                        logger.warning(f"No root for {file_path}")
                        stats['skipped'] += 1
                        continue

                    relative_path = os.path.relpath(file_path, src_root)
                    target_path = os.path.join(TARGET_DIR, relative_path)
                    target_sub_dir = os.path.dirname(target_path)
                    ensure_dir(target_sub_dir)

                    base_name_without_ext = os.path.splitext(os.path.basename(file_path))[0]
                    target_path = os.path.join(target_sub_dir, f"{base_name_without_ext}.md")

                    # Update progress bar with current file
                    pbar.set_postfix_str(os.path.basename(file_path)[:30])

                    if os.path.exists(target_path) and not OVERWRITE_EXISTING:
                        stats['skipped'] += 1
                        pbar.update(1)
                        continue

                    doc_md = generate_obsidian_doc(file_path)
                    if doc_md:
                        with open(target_path, 'w', encoding='utf-8') as f:
                            f.write(doc_md)
                        stats['processed'] += 1
                    else:
                        stats['failed'] += 1

                except Exception as e:
                    logger.error(f"Failed to process {file_path}: {e}")
                    stats['failed'] += 1

                pbar.update(1)

            # Brief pause between batches
            time.sleep(2)

    # Calculate summary
    elapsed = time.time() - stats['start_time']
    stats['elapsed_seconds'] = elapsed
    stats['files_per_minute'] = (stats['processed'] / elapsed) * 60 if elapsed > 0 else 0

    return stats
```

### Step 3: Update main() to use batch processing

```python
def main():
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Validate and warm up
    if not validate_model_availability():
        logger.error("Aborting: Model not available")
        return

    warmup_model()

    # Check target directory
    try:
        ensure_dir(TARGET_DIR)
        if not os.access(TARGET_DIR, os.W_OK):
            logger.error(f"Error: The target directory '{TARGET_DIR}' is not writable.")
            return
    except Exception as e:
        logger.error(f"Error: Could not create or access the target directory '{TARGET_DIR}'.")
        logger.error(f"Details: {e}")
        return

    # Get all files
    all_files = get_all_files(SOURCE_PATHS)
    logger.info(f"Found {len(all_files)} files to process.")

    if not all_files:
        logger.warning("No files found to process.")
        return

    # Log initial resources
    log_resource_stats()

    # Process with batching and progress
    stats = process_files_with_progress(all_files, batch_size=BATCH_SIZE)

    # Log summary
    logger.info("="*60)
    logger.info("Processing Complete")
    logger.info("="*60)
    logger.info(f"Total files: {stats['total_files']}")
    logger.info(f"Processed: {stats['processed']}")
    logger.info(f"Failed: {stats['failed']}")
    logger.info(f"Skipped: {stats['skipped']}")
    logger.info(f"Time: {stats['elapsed_seconds']:.1f}s ({stats['elapsed_seconds']/60:.1f}m)")
    logger.info(f"Speed: {stats['files_per_minute']:.1f} files/minute")
    logger.info(f"Throttle pauses: {stats['throttle_pauses']}")
    logger.info("="*60)
```

### Step 4: Add configuration to config.py

```python
# Batch processing configuration
BATCH_SIZE = 5                    # Files per batch
THROTTLE_RAM_PERCENT = 85         # Pause if RAM exceeds this
THROTTLE_CPU_PERCENT = 90         # Pause if CPU exceeds this
THROTTLE_PAUSE_SECONDS = 30       # How long to pause when throttling
BATCH_PAUSE_SECONDS = 2           # Pause between batches
```

## Advanced: Checkpoint/Resume Support

```python
import json

CHECKPOINT_FILE = './progress_checkpoint.json'

def save_checkpoint(processed_files, total_files):
    """Save processing progress"""
    checkpoint = {
        'processed_files': processed_files,
        'total_files': total_files,
        'timestamp': datetime.now().isoformat()
    }
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f)

def load_checkpoint():
    """Load previous progress"""
    if not os.path.exists(CHECKPOINT_FILE):
        return None
    try:
        with open(CHECKPOINT_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

def resume_processing(all_files):
    """Resume from checkpoint if exists"""
    checkpoint = load_checkpoint()
    if checkpoint:
        processed_count = checkpoint['processed_files']
        logger.info(f"Found checkpoint: {processed_count}/{checkpoint['total_files']} files processed")
        response = input("Resume from checkpoint? (y/n): ")
        if response.lower() == 'y':
            return all_files[processed_count:]
    return all_files
```

## Expected Impact
- Better system stability on long runs
- Clear progress feedback
- Ability to pause/resume processing
- Avoid system overload
- Better logging and statistics

## Testing
- [ ] Process 10 files and verify progress bar
- [ ] Simulate high memory usage, verify throttling
- [ ] Test checkpoint save/resume
- [ ] Verify resource stats logging
- [ ] Test with different batch sizes

## Notes
- Requires `psutil` and `tqdm`: `pip install psutil tqdm`
- Adjust throttle thresholds based on your system
- Checkpoint file allows safe Ctrl+C interruption
