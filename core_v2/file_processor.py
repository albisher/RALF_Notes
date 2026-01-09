"""
Box: File Processor

Input: Source paths, processing options
Output: Processing results and statistics
Responsibility: Batch file processing with progress tracking
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
from .document_pipeline import DocumentPipeline


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

    def __init__(self, pipeline: DocumentPipeline):
        """
        Initialize file processor.

        Args:
            pipeline: Document generation pipeline
        """
        self.pipeline = pipeline

    def process_paths(self,
                      source_paths: List[Path],
                      target_dir: Path,
                      dry_run: bool = False,
                      overwrite: bool = False,
                      console: Optional[Any] = None,
                      progress: Optional[Any] = None) -> Dict[str, Any]:
        """
        Process multiple source paths.

        Args:
            source_paths: List of source directories/files
            target_dir: Target output directory
            dry_run: If True, preview without writing
            overwrite: If True, regenerate existing docs
            console: Optional console for output
            progress: Optional progress tracker

        Returns:
            Dictionary with processing results
        """
        import time
        start_time = time.time()

        # Get all files to process
        files = self._get_all_files(source_paths)

        if console:
            console.info(f"Found {len(files)} files to process")

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
            'errors': []
        }

        for i, file_path in enumerate(files, 1):
            # Find source root
            src_root = next((p for p in source_paths if str(file_path).startswith(str(p))), None)
            if not src_root:
                if console:
                    console.warning(f"Skipping {file_path.name} (no source root)")
                results['skipped'] += 1
                continue

            # Calculate target path
            relative_path = file_path.relative_to(src_root)
            target_path = target_dir / relative_path.with_suffix('.md')

            # Ensure target directory exists
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Check if should skip
            if target_path.exists() and not overwrite:
                if console:
                    console.processing(f"[{i}/{len(files)}] Skip existing: {target_path.name}")
                results['skipped'] += 1
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
                continue

            # Process file
            if console:
                console.file("Analyzing", file_path.name)

            if not dry_run:
                try:
                    # Generate documentation
                    markdown, metadata = self.pipeline.generate_document(file_path)

                    # Write output
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
                        if console:
                            console.error(f"Empty content: {file_path.name}")

                except Exception as e:
                    results['failed'] += 1
                    results['errors'].append({'file': str(file_path), 'error': str(e)})
                    if console:
                        console.error(f"Failed: {file_path.name} - {str(e)}")
            else:
                # Dry run - just preview
                if console:
                    console.processing(f"[DRY RUN] Would generate: {target_path}")
                results['success'] += 1

            # Update progress
            if progress and task_id is not None:
                progress.update(task_id, advance=1)

        # Calculate final stats
        duration = time.time() - start_time
        results['duration'] = duration
        results['files_per_second'] = results['total'] / duration if duration > 0 else 0

        return results

    def _get_all_files(self, paths: List[Path]) -> List[Path]:
        """
        Recursively find all valid files in paths.

        Args:
            paths: List of source paths

        Returns:
            List of file paths to process
        """
        files = []

        for path in paths:
            if not path.exists():
                continue

            if path.is_file():
                # Single file
                if path.suffix in self.VALID_EXTENSIONS and path.name not in self.SKIP_FILES:
                    files.append(path)
            else:
                # Directory - walk recursively
                for item in path.rglob('*'):
                    if item.is_file():
                        # Check if in skip directory
                        if any(skip_dir in item.parts for skip_dir in self.SKIP_DIRS):
                            continue

                        # Check if valid file
                        if item.suffix in self.VALID_EXTENSIONS and item.name not in self.SKIP_FILES:
                            files.append(item)

        # Sort by path for consistent ordering
        return sorted(files)
