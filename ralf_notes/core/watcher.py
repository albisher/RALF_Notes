"""
Box: Filesystem Watcher

Input: Paths to watch
Output: Triggers processing for new files
Responsibility: Monitor a directory for new files and trigger a processing pipeline.
"""
import time
from pathlib import Path

from typing import Callable, Dict

class Watcher:
    def __init__(self, watch_dir: Path, handler: Callable[[Path], None], interval: int = 1):
        self.watch_dir = watch_dir
        self.handler = handler
        self.interval = interval  # Polling interval in seconds
        self.last_known_files = self._scan_files()

    def _scan_files(self) -> Dict[Path, float]:
        """Scans the watch directory and returns a dict of {filepath: mtime}."""
        files = {}
        if not self.watch_dir.exists():
            return files
        for path in self.watch_dir.iterdir():
            if path.is_file() and path.name.endswith('.txt'):
                try:
                    files[path] = path.stat().st_mtime
                except OSError:
                    # File might have been deleted between iterdir and stat
                    continue
        return files

    def _check_for_changes(self):
        current_files = self._scan_files()
        
        # Detect new or modified files
        for path, mtime in current_files.items():
            if path not in self.last_known_files or self.last_known_files[path] < mtime:
                # New file or modified file
                # Wait a moment to ensure the file is fully written before processing
                time.sleep(0.5)
                self.handler(path)
        
        # Update last known files
        self.last_known_files = current_files

    def run(self):
        try:
            while True:
                self._check_for_changes()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print(f"Stopping watcher for {self.watch_dir}")



def _format_initial_single(
    file_path: Path,
    output_dir: Path,
    dry_run: bool,
    overwrite: bool,
    config_manager,
    console
):
    # This logic is extracted and simplified from _format_initial_logic
    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        return

    filename_stem = file_path.stem
    formatted_output_path = output_dir / f"{filename_stem}.md"
    formatted_output_path.parent.mkdir(parents=True, exist_ok=True)

    if formatted_output_path.exists() and not overwrite:
        console.warning(f"Skipping {formatted_output_path.name} (output already exists. Use --overwrite to replace.)")
        return

    console.file("Formatting", file_path.name)

    if not dry_run:
        try:
            raw_content = file_path.read_text(encoding='utf-8')
            parsed_data = pipeline.parser.parse_or_fallback(raw_content, filename_stem)
            markdown = pipeline.formatter.format(parsed_data)

            if markdown.strip():
                formatted_output_path.write_text(markdown, encoding='utf-8')
                console.success(f"Formatted: {formatted_output_path.name}")
            else:
                console.error(f"Failed to format {formatted_output_path.name}: Empty markdown generated.")
        except Exception as e:
            console.error(f"Failed to format {formatted_output_path.name}: {e}")

def _finalize_single(
    file_path: Path,
    output_dir: Path,
    review_dir: Path,
    dry_run: bool,
    overwrite: bool,
    console
):
    # This logic is extracted and simplified from _finalize_logic
    filename_stem = file_path.stem
    final_output_path = output_dir / f"{filename_stem}.md"
    review_output_path = review_dir / f"{filename_stem}.md"

    if final_output_path.exists() and not overwrite:
        console.warning(f"Skipping {final_output_path.name} (output already exists. Use --overwrite to replace.)")
        return
    
    if not dry_run:
        try:
            is_valid = True  # Placeholder
            if is_valid:
                if file_path != final_output_path:
                    file_path.rename(final_output_path)
                console.success(f"Finalized: {final_output_path.name}")
            else:
                file_path.rename(review_output_path)
                console.warning(f"Validation failed for {file_path.name}. Moved to review needed.")
        except Exception as e:
            console.error(f"Failed to finalize {file_path.name}: {e}")