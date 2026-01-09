import os
import logging
from typing import List

class FileProcessor:
    """
    Box: File Processor
    
    Input: paths
    Output: file paths, file content
    Responsibility: Handle file system operations like finding files and reading them.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_all_files(self, paths: List[str]) -> List[str]:
        valid_extensions = ('.py', '.txt', '.md', '.sh')
        skip_dirs = {'__pycache__', '.git', 'venv', '.obsidian', '.venv', 'To_Obsidian'}
        files_to_process = []

        for base_path in paths:
            if not os.path.exists(base_path):
                self.logger.warning(f"Path not found: {base_path}")
                continue
            for root, dirs, files in os.walk(base_path):
                dirs[:] = [d for d in dirs if d not in skip_dirs]
                for file in files:
                    if file.endswith(valid_extensions) and file not in {'recursive_obsidian_checks.py', 'obsidian_generator.py', 'debug_output.txt', 'prompt1.txt', 'document2obsidian.py'}:
                        files_to_process.append(os.path.join(root, file))
        return files_to_process

    def read_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            self.logger.error(f"Error reading {file_path}: {e}")
            return ""
