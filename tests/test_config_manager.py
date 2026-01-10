from pathlib import Path
import json
import os
import pytest
from ralf_notes.config_manager import ConfigManager

@pytest.fixture
def temp_config_file(tmp_path):
    """Fixture to create a temporary config file for testing."""
    config_dir = tmp_path / ".ralf-notes"
    config_dir.mkdir()
    return config_dir / "config.json"

def test_default_config_loading(temp_config_file):
    """Test that default configuration is loaded correctly when no file exists."""
    # Ensure no config file exists initially
    assert not temp_config_file.exists()

    config_manager = ConfigManager(config_path=temp_config_file)
    
    assert config_manager.config == config_manager.DEFAULT_CONFIG
    assert config_manager.get("model_name") == "ministral-3:3b"
    assert config_manager.get("ollama_host") == "http://127.0.0.1:11434"
    assert config_manager.get("temperature") == 0.1

def test_existing_config_loading(temp_config_file):
    """Test that existing configuration is loaded and merged correctly."""
    initial_config = {
        "model_name": "test-model:latest",
        "temperature": 0.5,
        "new_setting": "some_value"
    }
    with open(temp_config_file, 'w') as f:
        json.dump(initial_config, f)

    config_manager = ConfigManager(config_path=temp_config_file)
    
    expected_config = ConfigManager.DEFAULT_CONFIG.copy()
    expected_config.update(initial_config)

    assert config_manager.config == expected_config
    assert config_manager.get("model_name") == "test-model:latest"
    assert config_manager.get("ollama_host") == "http://127.0.0.1:11434" # From default
    assert config_manager.get("temperature") == 0.5
    assert config_manager.get("new_setting") == "some_value"

def test_save_config(temp_config_file):
    """Test that configuration can be saved to a file."""
    config_manager = ConfigManager(config_path=temp_config_file)
    config_manager.set("model_name", "saved-model")
    config_manager.save()

    assert temp_config_file.exists()
    with open(temp_config_file, 'r') as f:
        saved_config = json.load(f)
    
    # Only changed values are in the saved file if they differ from default
    assert saved_config["model_name"] == "saved-model"
    assert "ollama_host" not in saved_config or saved_config["ollama_host"] == ConfigManager.DEFAULT_CONFIG["ollama_host"]

def test_add_remove_source_path(temp_config_file):
    """Test adding and removing source paths."""
    config_manager = ConfigManager(config_path=temp_config_file)
    
    # Add path
    config_manager.add_source_path("/path/to/source1")
    config_manager.add_source_path("/path/to/source2")
    assert config_manager.get("source_paths") == ["/path/to/source1", "/path/to/source2"]
    
    # Add existing path (should not duplicate)
    config_manager.add_source_path("/path/to/source1")
    assert config_manager.get("source_paths") == ["/path/to/source1", "/path/to/source2"]

    # Remove path
    config_manager.remove_source_path("/path/to/source1")
    assert config_manager.get("source_paths") == ["/path/to/source2"]

    # Remove non-existent path
    config_manager.remove_source_path("/path/to/nonexistent")
    assert config_manager.get("source_paths") == ["/path/to/source2"]

def test_set_target_dir(temp_config_file):
    """Test setting target directory."""
    config_manager = ConfigManager(config_path=temp_config_file)
    config_manager.set_target_dir("/new/target")
    assert config_manager.get("target_dir") == "/new/target"

def test_set_model(temp_config_file):
    """Test setting model name."""
    config_manager = ConfigManager(config_path=temp_config_file)
    config_manager.set_model("new-model:13b")
    assert config_manager.get("model_name") == "new-model:13b"

def test_reset_to_defaults(temp_config_file):
    """Test resetting configuration to defaults."""
    initial_config = {
        "model_name": "test-model:latest",
        "temperature": 0.5,
        "new_setting": "some_value"
    }
    with open(temp_config_file, 'w') as f:
        json.dump(initial_config, f)
    
    config_manager = ConfigManager(config_path=temp_config_file)
    config_manager.reset_to_defaults()
    assert config_manager.config == config_manager.DEFAULT_CONFIG
