"""
Box: File Processor

Input: Source paths, processing options
Output: Processing results and statistics
Responsibility: Batch file processing with progress tracking
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
from .document_pipeline import DocumentPipeline
from ..config_manager import ConfigManager # Import ConfigManager


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
        self.config_manager = config_manager # Store config_manager

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
            self.config_manager.get('file_extensions', self.VALID_EXTENSIONS), # Use config, fallback to default
            self.config_manager.get('skip_dirs', self.SKIP_DIRS), # Use config, fallback to default
            self.config_manager.get('skip_files', self.SKIP_FILES) # Use config, fallback to default
        )
        
        # Limit files if configured
        max_files = self.config_manager.get('max_files_to_process', 0)
        if max_files > 0:
            files = all_files[:max_files]
        else:
            files = all_files

        if console:
            console.info(f"Found {len(all_files)} files, processing {len(files)}.")

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

        for i, file_path in enumerate(files, 1):
            src_root = next((p for p in source_paths if str(file_path).startswith(str(p))), None)

            if src_root and src_root.is_file():
                calc_root = src_root.parent
            else:
                calc_root = src_root

            if not calc_root:
                if console:
                    console.warning(f"Skipping {file_path.name} (no source root)")
                results['skipped'] += 1
                continue
            
            relative_path = file_path.relative_to(calc_root)
            target_path = target_dir / relative_path.with_suffix('.md')
            target_path.parent.mkdir(parents=True, exist_ok=True)

            if target_path.exists() and not overwrite:
                if console:
                    console.warning(f"Skipping {file_path.name} (output already exists. Use --overwrite to replace.)")
                results['skipped'] += 1
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
                continue

            if console:
                console.file("Analyzing", file_path.name)

            if not dry_run:
                try:
                    markdown, metadata = self.pipeline.generate_document(file_path)
                    if markdown.strip():
                        target_path.write_text(markdown, encoding='utf-8')
                        results['success'] += 1
                        if console:
                            if metadata.get('valid'):
                                console.success(f"Generated: {target_path.name}")
                            else:
                                console.warning(f"Generated with warnings: {target_path.name}")
                    else:
                        results['failed'] += 1
                except Exception as e:
                    results['failed'] += 1
                    results['errors'].append({'file': str(file_path), 'error': str(e)})
            else:
                results['success'] += 1

            if progress and task_id is not None:
                progress.update(task_id, advance=1)

        duration = time.time() - start_time
        results['duration'] = duration
        results['files_per_second'] = results['total'] / duration if duration > 0 else 0

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
                continue
            if path.is_file():
                if path.suffix in valid_extensions and path.name not in skip_files:
                    files.append(path)
            else:
                for item in path.rglob('*'):
                    if item.is_file():
                        if any(skip_dir in item.parts for skip_dir in skip_dirs):
                            continue
                        if item.suffix in valid_extensions and item.name not in skip_files:
                            files.append(item)
        return sorted(files)