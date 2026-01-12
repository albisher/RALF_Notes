"""
Box: Configuration Manager

Responsibility: Handle configuration setup and management
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigManager:
    """
    Box: Configuration Manager

    Input: Config file path
    Output: Configuration dictionary
    Responsibility: Load, save, and manage configuration
    """

    DEFAULT_CONFIG = {
        "source_paths": [],
        "target_dir": "./to_obsidian", # Final output
        "stage1_raw_output_dir": "./stage1_raw", # Raw LLM output
        "initial_formatted_dir": "./stage2_formatted", # Formatted but not validated
        "review_needed_dir": "./review_needed", # Files failing validation
        "model_name": "ministral-3:3b",
        "ollama_host": "http://127.0.0.1:11434",
        "temperature": 0.1,
        "num_ctx": 10000,
        "chunk_size": 100000,
        "max_content_length": 8000,
        "max_chunk_summary_length": 4000,
        "max_files_to_process": 0  # 0 for no limit
    }

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize config manager.

        Args:
            config_path: Path to config file (defaults to ~/.ralf-notes/config.json)
        """
        if config_path is None:
            config_dir = Path.home() / ".ralf-notes"
            config_dir.mkdir(exist_ok=True)
            config_path = config_dir / "config.json"

        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    # Start with defaults and override with user's config
                    config = self.DEFAULT_CONFIG.copy()
                    config.update(json.load(f))
                    return config
            except Exception:
                return self.DEFAULT_CONFIG.copy()
        return self.DEFAULT_CONFIG.copy()

    def save(self):
        """Save current configuration to file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        value = self.config.get(key, default)
        if isinstance(value, str):
            return value.strip().strip("'\"")
        return value

    _VALIDATORS = {
        "temperature": lambda x: isinstance(x, (int, float)) and 0.0 <= x <= 2.0,
        "num_ctx": lambda x: isinstance(x, int) and x > 0,
        "chunk_size": lambda x: isinstance(x, int) and x > 0,
        "max_content_length": lambda x: isinstance(x, int) and x > 0,
        "max_chunk_summary_length": lambda x: isinstance(x, int) and x > 0,
        "max_files_to_process": lambda x: isinstance(x, int) and x >= 0,
        "stage1_raw_output_dir": lambda x: isinstance(x, str),
        "initial_formatted_dir": lambda x: isinstance(x, str),
        "review_needed_dir": lambda x: isinstance(x, str),
        "ollama_host": lambda x: isinstance(x, str) and (x.startswith("http://") or x.startswith("https://"))
    }

    def set(self, key: str, value: Any):
        """Set configuration value with validation."""
        if key in self._VALIDATORS:
            if not self._VALIDATORS[key](value):
                raise ValueError(f"Invalid value for '{key}': {value}. Does not meet validation criteria.")
        self.config[key] = value

    def add_source_path(self, path: str):
        """Add a source path to configuration."""
        paths = self.config.get("source_paths", [])
        if path not in paths:
            paths.append(path)
            self.config["source_paths"] = paths

    def remove_source_path(self, path: str):
        """Remove a source path from configuration."""
        paths = self.config.get("source_paths", [])
        if path in paths:
            paths.remove(path)
            self.config["source_paths"] = paths

    def set_target_dir(self, path: str):
        """Set target directory."""
        self.config["target_dir"] = path

    def set_stage1_raw_output_dir(self, path: str):
        """Set Stage 1 raw output directory."""
        self.config["stage1_raw_output_dir"] = path

    def set_initial_formatted_dir(self, path: str):
        """Set initial formatted output directory (Stage 2)."""
        self.config["initial_formatted_dir"] = path

    def set_review_needed_dir(self, path: str):
        """Set review needed directory (for failed Stage 3 files)."""
        self.config["review_needed_dir"] = path

    def set_model(self, model_name: str):
        """Set Ollama model name."""
        self.config["model_name"] = model_name

    def reset_to_defaults(self):
        """Reset configuration to defaults."""
        self.config = self.DEFAULT_CONFIG.copy()