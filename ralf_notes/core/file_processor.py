import signal
from contextlib import contextmanager
from pathlib import Path
from typing import List, Dict, Any, Optional
from .document_pipeline import DocumentPipeline
from ..config_manager import ConfigManager # Import ConfigManager
import logging

logger = logging.getLogger(__name__)


class TimeoutException(Exception):
    pass

@contextmanager
def timeout_context(seconds: int):
    def signal_handler(signum, frame):
        raise TimeoutException("Operation timed out.")
    
    original_handler = signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0) # Disable the alarm
        signal.signal(signal.SIGALRM, original_handler) # Restore original handler


class FileProcessor:
    """
    Box: File Processor

    Input: Paths, target directory, options
    Output: Processing results
    Responsibility: Batch process files with statistics
    """

    # Valid file extensions to process
    VALID_EXTENSIONS = ('.py', '.txt', '.md', '.sh', '.js', '.ts', '.go', '.rs', '.java')

    # Directories to skip
    SKIP_DIRS = {'__pycache__', '.git', 'venv', '.venv', '.obsidian', 'node_modules', 'archive'}

    # Files to skip
    SKIP_FILES = {'recursive_obsidian_checks.py', 'obsidian_generator.py'}

    def __init__(self, pipeline: DocumentPipeline, config_manager: ConfigManager):
        """
        Initialize file processor.

        Args:
            pipeline: Document generation pipeline
            config_manager: Configuration Manager instance
        """
        self.pipeline = pipeline
        self.config_manager = config_manager

    def process_paths(self,
                      source_paths: List[Path],
                      target_dir: Path,
                      dry_run: bool = False,
                      overwrite: bool = False,
                      console: Optional[Any] = None,
                      progress: Optional[Any] = None) -> Dict[str, Any]:
        """
        Process multiple source paths.
        """
        import time
        start_time = time.time()

        # Get all files to process using the static method
        all_files = FileProcessor.get_files_to_process(
            source_paths,
            self.config_manager.get('file_extensions', self.VALID_EXTENSIONS),
            self.config_manager.get('skip_dirs', self.SKIP_DIRS),
            self.config_manager.get('skip_files', self.SKIP_FILES)
        )
        
        # Limit files if configured
        max_files = self.config_manager.get('max_files_to_process', 0)
        if max_files > 0:
            files = all_files[:max_files]
        else:
            files = all_files

        logger.info("Found %d files, processing %d.", len(all_files), len(files))

        # Setup progress tracking
        task_id = None
        if progress:
            task_id = progress.add_task("Processing files", total=len(files))

        # Process each file
        results = {
            'total': len(files),
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'errors': [],
            'dry_run': dry_run
        }

        # Get timeout setting
        request_timeout = self.config_manager.get('request_timeout_seconds', 300)


        for i, file_path in enumerate(files, 1):
            src_root = next((p for p in source_paths if str(file_path).startswith(str(p))), None)

            if src_root and src_root.is_file():
                calc_root = src_root.parent
            else:
                calc_root = src_root

            if not calc_root:
                logger.warning("Skipping %s (no source root)", file_path.name)
                results['skipped'] += 1
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
                continue
            
            relative_path = file_path.relative_to(calc_root)
            target_path = target_dir / relative_path.with_suffix('.md')
            target_path.parent.mkdir(parents=True, exist_ok=True)

            if target_path.exists() and not overwrite:
                logger.warning("Skipping %s (output already exists. Use --overwrite to replace.)", file_path.name)
                results['skipped'] += 1
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
                continue

            logger.info("Analyzing file: %s", file_path.name)

            if not dry_run:
                try:
                    with timeout_context(request_timeout):
                        markdown, metadata = self.pipeline.generate_document(file_path)
                    if markdown.strip():
                        target_path.write_text(markdown, encoding='utf-8')
                        results['success'] += 1
                        logger.info("Generated: %s", target_path.name)
                        if not metadata.get('valid'):
                            logger.warning("Generated with warnings: %s", target_path.name)
                    else:
                        results['failed'] += 1
                        logger.error("Failed to generate markdown for %s: Empty markdown.", file_path.name)
                except TimeoutException:
                    results['failed'] += 1
                    results['errors'].append({'file': str(file_path), 'error': "Operation timed out."})
                    logger.error("Generation timed out for %s", file_path.name)
                except Exception as e:
                    results['failed'] += 1
                    results['errors'].append({'file': str(file_path), 'error': str(e)})
                    logger.error("Failed to process %s: %s", file_path.name, e, exc_info=True)
            else:
                results['success'] += 1
                logger.info("Dry run: Would have processed %s", file_path.name)

            if progress and task_id is not None:
                progress.update(task_id, advance=1)
            
            # Apply delay between requests if configured
            request_delay = self.config_manager.get('request_delay_seconds', 0)
            if request_delay > 0 and i < len(files):
                logger.debug("Applying request delay of %s seconds.", request_delay)
                time.sleep(request_delay)

        duration = time.time() - start_time
        results['duration'] = duration
        results['files_per_second'] = results['total'] / duration if duration > 0 else 0
        logger.info("File processing completed in %.2f seconds.", duration)

        return results

    @staticmethod
    def get_files_to_process(source_paths: List[Path],
                             valid_extensions: tuple,
                             skip_dirs: set,
                             skip_files: set) -> List[Path]:
        """
        Static method to recursively find all valid files in paths, respecting skip patterns.
        """
        files = []
        for path in source_paths:
            if not path.exists():
                logger.warning("Source path does not exist: %s", path)
                continue
            if path.is_file():
                if path.suffix in valid_extensions and path.name not in skip_files:
                    files.append(path)
                    logger.debug("Adding file: %s", path)
                else:
                    logger.debug("Skipping file (extension/name): %s", path)
            else:
                for item in path.rglob('*'):
                    if any(skip_dir in item.parts for skip_dir in skip_dirs):
                        logger.debug("Skipping directory: %s", item)
                        continue
                    if item.is_file():
                        if item.suffix in valid_extensions and item.name not in skip_files:
                            files.append(item)
                            logger.debug("Adding file: %s", item)
                        else:
                            logger.debug("Skipping file (extension/name): %s", item)
        return sorted(files)