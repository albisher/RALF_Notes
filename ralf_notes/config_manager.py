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
        "target_dir": "./to_obsidian",
        "model_name": "ministral-3:3b",
        "ollama_host": "http://127.0.0.1:11434",
        "temperature": 0.1,
        "num_ctx": 10000,
        "chunk_size": 100000,
        "max_content_length": 8000,
        "max_chunk_summary_length": 4000
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
                    return json.load(f)
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
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """Set configuration value."""
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

    def set_model(self, model_name: str):
        """Set Ollama model name."""
        self.config["model_name"] = model_name

    def reset_to_defaults(self):
        """Reset configuration to defaults."""
        self.config = self.DEFAULT_CONFIG.copy()
