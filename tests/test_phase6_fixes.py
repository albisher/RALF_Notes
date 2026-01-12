import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
import time
import os

from ralf_notes.config_manager import ConfigManager
from ralf_notes.core.document_pipeline import DocumentPipeline, ResponseError, TimeoutException, timeout_context
from ralf_notes.core.file_processor import FileProcessor
from ralf_notes.core.structured_text_generator import StructuredTextGenerator
from ralf_notes.core.text_parser import TextParser
from ralf_notes.core.note_formatter import NoteFormatter
from ralf_notes.core.models import GenerationContext, StructuredTextGeneratorConfig

from typer.testing import CliRunner
from ralf_notes.cli import app, _generate_raw_logic, _format_initial_logic, _finalize_logic # Import logic functions for direct testing

# --- Fixtures ---

@pytest.fixture
def mock_config_manager():
    """Mocks ConfigManager to return predefined values."""
    config_manager = MagicMock(spec=ConfigManager)
    config_manager.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "test-model",
        "num_ctx": 4096,
        "temperature": 0.1,
        "chunk_size": 10000,
        "max_content_length": 8000,
        "max_chunk_summary_length": 4000,
        "request_delay_seconds": 0,
        "request_timeout_seconds": 5, # Shorter timeout for tests
        "retry_attempts": 3,
        "initial_backoff_seconds": 0.1,
        "backoff_multiplier": 2,
        "source_paths": [],
        "stage1_raw_output_dir": "stage1_raw",
        "initial_formatted_dir": "stage2_formatted",
        "target_dir": "to_obsidian",
        "review_needed_dir": "review_needed",
        "log_level": "DEBUG",
        "log_file": None,
    }.get(key, default)
    config_manager.set.return_value = None # Allow setting values without error
    return config_manager

@pytest.fixture
def mock_ollama_client():
    """Mocks the Ollama Client."""
    client = MagicMock()
    client.generate.return_value = {"response": "### SUMMARY\nTest summary\n### TAGS\n#test\n### TYPE\ncode-notes"}
    return client

@pytest.fixture
def mock_console():
    """Mocks the Console for Rich output suppression."""
    console = MagicMock()
    console.info.return_value = None
    console.warning.return_value = None
    console.error.return_value = None
    console.success.return_value = None
    console.print.return_value = None
    console.rule.return_value = None
    console.panel.return_value = None
    console.file.return_value = None
    return console

@pytest.fixture
def mock_progress_manager():
    """Mocks the ProgressManager for Rich output suppression."""
    progress = MagicMock()
    progress.add_task.return_value = "task_id"
    progress.update.return_value = None
    return progress

@pytest.fixture
def cli_runner():
    return CliRunner()

# --- Tests for Phase 6 Fixes ---

# Task 6.1.1: Fix Schema-Parser Mismatch (DEPENDENCIES)
def test_text_parser_dependencies_parsing():
    raw_text = "### SUMMARY\nSummary text\n### TAGS\n#tag1\n### TYPE\ncode-notes\n### DEPENDENCIES\ndep1, dep2, dep3"
    parser = TextParser()
    parsed_data = parser.parse(raw_text, "test_file")
    assert "dependencies" in parsed_data
    assert parsed_data["dependencies"] == ["dep1", "dep2", "dep3"]

    raw_text_none = "### SUMMARY\nSummary text\n### TAGS\n#tag1\n### TYPE\ncode-notes\n### DEPENDENCIES\nnone"
    parsed_data_none = parser.parse(raw_text_none, "test_file_none")
    assert parsed_data_none["dependencies"] == []

    raw_text_empty = "### SUMMARY\nSummary text\n### TAGS\n#tag1\n### TYPE\ncode-notes\n### DEPENDENCIES\n"
    parsed_data_empty = parser.parse(raw_text_empty, "test_file_empty")
    assert parsed_data_empty["dependencies"] == []

# Task 6.1.2: Fix Config Propagation
def test_config_propagation_to_generator(mock_config_manager):
    config_manager = mock_config_manager
    config_manager.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "test-model",
        "num_ctx": 4000,
        "temperature": 0.5,
        "chunk_size": 1000,
        "max_content_length": 5000,
        "max_chunk_summary_length": 2000,
        "retry_attempts": 2,
        "initial_backoff_seconds": 0.5,
        "backoff_multiplier": 3,
    }.get(key, default)

    pipeline = app.command()(lambda: None) # Dummy command for testing build_pipeline
    with patch('ralf_notes.cli.Client') as MockClient:
        pipeline_instance = app.command()(lambda: None)
        pipeline_instance = app.command()(lambda: None)

@patch('ralf_notes.cli.build_pipeline')
@patch('ralf_notes.cli.FileProcessor')
def test_cli_generate_raw_logic_path_validation(
    MockFileProcessor,
    MockBuildPipeline,
    mock_config_manager,
    mock_console,
    tmp_path
):
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "file1.py").write_text("content")

    output_dir = tmp_path / "output"
    # output_dir.mkdir() # Should be created by the logic

    # Test with valid paths
    result = _generate_raw_logic(
        source_path=source_dir,
        output=output_dir,
        quiet=True,
        model=None,
        config_manager=mock_config_manager,
        console=mock_console
    )
    assert result is True
    assert MockFileProcessor.get_files_to_process.called

    # Test with non-existent source path
    non_existent_path = tmp_path / "non_existent"
    with pytest.raises(typer.Exit) as exc_info:
        _generate_raw_logic(
            source_path=non_existent_path,
            output=output_dir,
            quiet=True,
            model=None,
            config_manager=mock_config_manager,
            console=mock_console
        )
    assert exc_info.value.exit_code == 1
    mock_console.error.assert_any_call(f"Error: Path for 'source_path' does not exist: {non_existent_path}")

    # Test with non-writable output path (mock os.access)
    unwritable_dir = tmp_path / "unwritable"
    unwritable_dir.mkdir()
    with patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=False): # Mock os.access for writability
        with pytest.raises(typer.Exit) as exc_info:
            _generate_raw_logic(
                source_path=source_dir,
                output=unwritable_dir,
                quiet=True,
                model=None,
                config_manager=mock_config_manager,
                console=mock_console
            )
        assert exc_info.value.exit_code == 1
        mock_console.error.assert_any_call(f"Error: Path for 'raw_output' is not writable: {unwritable_dir} (None)") # Error message from mock

@patch('ralf_notes.cli.build_pipeline')
@patch('ralf_notes.cli.FileProcessor')
def test_cli_format_initial_logic_path_validation(
    MockFileProcessor,
    MockBuildPipeline,
    mock_config_manager,
    mock_console,
    tmp_path
):
    source_dir = tmp_path / "raw_output"
    source_dir.mkdir()
    (source_dir / "file1.txt").write_text("content")

    output_dir = tmp_path / "formatted_output"

    # Test with valid paths
    result = _format_initial_logic(
        path=source_dir,
        output=output_dir,
        dry_run=True,
        overwrite=False,
        quiet=True,
        model=None,
        config_manager=mock_config_manager,
        console=mock_console
    )
    assert result is True
    assert MockFileProcessor.get_files_to_process.called

    # Test with non-existent source path
    non_existent_path = tmp_path / "non_existent_raw"
    with pytest.raises(typer.Exit) as exc_info:
        _format_initial_logic(
            path=non_existent_path,
            output=output_dir,
            dry_run=True,
            overwrite=False,
            quiet=True,
            model=None,
            config_manager=mock_config_manager,
            console=mock_console
        )
    assert exc_info.value.exit_code == 1
    mock_console.error.assert_any_call(f"Error: Path for 'path' does not exist: {non_existent_path}")

    # Test with non-writable output path
    unwritable_dir = tmp_path / "unwritable_formatted"
    unwritable_dir.mkdir()
    with patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=False):
        with pytest.raises(typer.Exit) as exc_info:
            _format_initial_logic(
                path=source_dir,
                output=unwritable_dir,
                dry_run=True,
                overwrite=False,
                quiet=True,
                model=None,
                config_manager=mock_config_manager,
                console=mock_console
            )
        assert exc_info.value.exit_code == 1
        mock_console.error.assert_any_call(f"Error: Path for 'formatted_output' is not writable: {unwritable_dir} (None)")


@patch('ralf_notes.cli.FileProcessor')
def test_cli_finalize_logic_path_validation(
    MockFileProcessor,
    mock_config_manager,
    mock_console,
    tmp_path
):
    source_dir = tmp_path / "formatted_input"
    source_dir.mkdir()
    (source_dir / "file1.md").write_text("content")

    final_output_dir = tmp_path / "final_output"
    review_output_dir = tmp_path / "review_output"

    # Test with valid paths
    result = _finalize_logic(
        path=source_dir,
        output=final_output_dir,
        review_output=review_output_dir,
        dry_run=True,
        overwrite=False,
        quiet=True,
        config_manager=mock_config_manager,
        console=mock_console
    )
    assert result is True
    assert MockFileProcessor.get_files_to_process.called

    # Test with non-existent source path
    non_existent_path = tmp_path / "non_existent_formatted"
    with pytest.raises(typer.Exit) as exc_info:
        _finalize_logic(
            path=non_existent_path,
            output=final_output_dir,
            review_output=review_output_dir,
            dry_run=True,
            overwrite=False,
            quiet=True,
            config_manager=mock_config_manager,
            console=mock_console
        )
    assert exc_info.value.exit_code == 1
    mock_console.error.assert_any_call(f"Error: Path for 'path' does not exist: {non_existent_path}")

    # Test with non-writable final output path
    unwritable_final_dir = tmp_path / "unwritable_final"
    unwritable_final_dir.mkdir()
    with patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=False):
        with pytest.raises(typer.Exit) as exc_info:
            _finalize_logic(
                path=source_dir,
                output=unwritable_final_dir,
                review_output=review_output_dir,
                dry_run=True,
                overwrite=False,
                quiet=True,
                config_manager=mock_config_manager,
                console=mock_console
            )
        assert exc_info.value.exit_code == 1
        mock_console.error.assert_any_call(f"Error: Path for 'final_output' is not writable: {unwritable_final_dir} (None)")

    # Test with non-writable review output path
    unwritable_review_dir = tmp_path / "unwritable_review"
    unwritable_review_dir.mkdir()
    with patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=False):
        with pytest.raises(typer.Exit) as exc_info:
            _finalize_logic(
                path=source_dir,
                output=final_output_dir,
                review_output=unwritable_review_dir,
                dry_run=True,
                overwrite=False,
                quiet=True,
                config_manager=mock_config_manager,
                console=mock_console
            )
        assert exc_info.value.exit_code == 1
        mock_console.error.assert_any_call(f"Error: Path for 'review_output' is not writable: {unwritable_review_dir} (None)")

# Task 6.1.3: Fix Metadata Inconsistency
def test_document_pipeline_metadata_consistency_success(mock_ollama_client, mock_config_manager, tmp_path):
    temp_file = tmp_path / "test_file.py"
    temp_file.write_text("print('hello')")

    generator_config = StructuredTextGeneratorConfig(
        model_name="test-model", num_ctx=4096, temperature=0.1, chunk_size=10000,
        max_content_length=8000, max_chunk_summary_length=4000, ollama_host="http://localhost",
        retry_attempts=1, initial_backoff_seconds=0, backoff_multiplier=1
    )
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    parser = TextParser()
    formatter = NoteFormatter()
    pipeline = DocumentPipeline(generator, parser, formatter)

    _, metadata = pipeline.generate_document(temp_file)
    assert 'data' in metadata
    assert metadata['data']['filename'] == "test_file"
    assert metadata['valid'] is True
    assert metadata['errors'] == []

def test_document_pipeline_metadata_consistency_ollama_error(mock_ollama_client, mock_config_manager, tmp_path):
    mock_ollama_client.generate.side_effect = ResponseError("Ollama broke!")
    
    temp_file = tmp_path / "test_file.py"
    temp_file.write_text("print('hello')")

    generator_config = StructuredTextGeneratorConfig(
        model_name="test-model", num_ctx=4096, temperature=0.1, chunk_size=10000,
        max_content_length=8000, max_chunk_summary_length=4000, ollama_host="http://localhost",
        retry_attempts=1, initial_backoff_seconds=0, backoff_multiplier=1
    )
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    parser = TextParser()
    formatter = NoteFormatter()
    pipeline = DocumentPipeline(generator, parser, formatter)

    _, metadata = pipeline.generate_document(temp_file)
    assert 'data' in metadata
    assert metadata['data'] == {} # Should be empty for error
    assert metadata['valid'] is False
    assert "Ollama API Error" in metadata['errors'][0]

def test_document_pipeline_metadata_consistency_unexpected_error(mock_ollama_client, mock_config_manager, tmp_path):
    mock_ollama_client.generate.side_effect = Exception("Something unexpected happened!")
    
    temp_file = tmp_path / "test_file.py"
    temp_file.write_text("print('hello')")

    generator_config = StructuredTextGeneratorConfig(
        model_name="test-model", num_ctx=4096, temperature=0.1, chunk_size=10000,
        max_content_length=8000, max_chunk_summary_length=4000, ollama_host="http://localhost",
        retry_attempts=1, initial_backoff_seconds=0, backoff_multiplier=1
    )
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    parser = TextParser()
    formatter = NoteFormatter()
    pipeline = DocumentPipeline(generator, parser, formatter)

    _, metadata = pipeline.generate_document(temp_file)
    assert 'data' in metadata
    assert metadata['data'] == {} # Should be empty for error
    assert metadata['valid'] is False
    assert "Unexpected Error" in metadata['errors'][0]


# Task 6.2.3: Implement Basic Rate Limiting
@patch('ralf_notes.core.file_processor.time.sleep', MagicMock())
def test_file_processor_delay(mock_config_manager, mock_ollama_client, tmp_path):
    mock_config_manager.get.side_effect = lambda key, default=None: {
        "request_delay_seconds": 0.01,
        "max_files_to_process": 2
    }.get(key, default)

    # Create dummy files
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "file1.py").write_text("content")
    (source_dir / "file2.py").write_text("content")

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Create generator and parser mocks
    generator_config = MagicMock(spec=StructuredTextGeneratorConfig)
    generator_config.model_name = "test-model"
    generator_config.num_ctx = 4096
    generator_config.temperature = 0.1
    generator_config.chunk_size = 10000
    generator_config.max_content_length = 8000
    generator_config.max_chunk_summary_length = 4000
    generator_config.ollama_host = "http://localhost"
    generator_config.retry_attempts = 1
    generator_config.initial_backoff_seconds = 0
    generator_config.backoff_multiplier = 1
    
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    parser = TextParser()
    formatter = NoteFormatter()
    pipeline = DocumentPipeline(generator, parser, formatter)

    processor = FileProcessor(pipeline, mock_config_manager)

    processor.process_paths([source_dir], output_dir, console=MagicMock(), progress=MagicMock())
    
    # sleep should be called once between 2 files
    assert ralf_notes.core.file_processor.time.sleep.call_count == 1

@patch('ralf_notes.core.file_processor.signal.signal')
@patch('ralf_notes.core.file_processor.signal.alarm')
def test_file_processor_timeout(mock_alarm, mock_signal, mock_config_manager, mock_ollama_client, tmp_path):
    mock_config_manager.get.side_effect = lambda key, default=None: {
        "request_timeout_seconds": 1, # 1 second timeout
        "max_files_to_process": 1
    }.get(key, default)

    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "file1.py").write_text("content")

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Simulate timeout by raising TimeoutException on pipeline call
    pipeline_mock = MagicMock(spec=DocumentPipeline)
    pipeline_mock.generate_document.side_effect = TimeoutException("Simulated timeout")

    processor = FileProcessor(pipeline_mock, mock_config_manager)
    results = processor.process_paths([source_dir], output_dir, console=MagicMock(), progress=MagicMock())

    assert results['failed'] == 1
    assert "Operation timed out." in results['errors'][0]['error']
    mock_alarm.assert_any_call(1) # Verify alarm was set
    mock_alarm.assert_any_call(0) # Verify alarm was cleared

@patch('ralf_notes.core.structured_text_generator.time.sleep', MagicMock())
def test_structured_text_generator_retries(mock_config_manager, mock_ollama_client, tmp_path):
    mock_ollama_client.generate.side_effect = [Exception("API Error"), Exception("API Error"), {"response": "Success"}]
    mock_config_manager.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "test-model",
        "num_ctx": 4096,
        "temperature": 0.1,
        "chunk_size": 10000,
        "max_content_length": 8000,
        "max_chunk_summary_length": 4000,
        "retry_attempts": 3,
        "initial_backoff_seconds": 0.01, # Small backoff for fast test
        "backoff_multiplier": 2,
    }.get(key, default)

    generator_config = StructuredTextGeneratorConfig(
        model_name="test-model", num_ctx=4096, temperature=0.1, chunk_size=10000,
        max_content_length=8000, max_chunk_summary_length=4000, ollama_host="http://localhost",
        retry_attempts=3, initial_backoff_seconds=0.01, backoff_multiplier=2
    )
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    context = GenerationContext(filename="test", content="some content", file_path="test.py")

    response = generator.generate(context)
    assert response == "Success"
    assert mock_ollama_client.generate.call_count == 3 # Initial call + 2 retries
    assert ralf_notes.core.structured_text_generator.time.sleep.call_count == 2 # 2 sleeps for 2 retries

@patch('ralf_notes.core.structured_text_generator.time.sleep', MagicMock())
def test_structured_text_generator_max_retries_fail(mock_config_manager, mock_ollama_client, tmp_path):
    mock_ollama_client.generate.side_effect = [Exception("API Error")] * 3 # Fail all 3 attempts
    mock_config_manager.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "test-model",
        "num_ctx": 4096,
        "temperature": 0.1,
        "chunk_size": 10000,
        "max_content_length": 8000,
        "max_chunk_summary_length": 4000,
        "retry_attempts": 3,
        "initial_backoff_seconds": 0.01,
        "backoff_multiplier": 2,
    }.get(key, default)

    generator_config = StructuredTextGeneratorConfig(
        model_name="test-model", num_ctx=4096, temperature=0.1, chunk_size=10000,
        max_content_length=8000, max_chunk_summary_length=4000, ollama_host="http://localhost",
        retry_attempts=3, initial_backoff_seconds=0.01, backoff_multiplier=2
    )
    generator = StructuredTextGenerator(mock_ollama_client, generator_config)
    context = GenerationContext(filename="test", content="some content", file_path="test.py")

    with pytest.raises(Exception, match="API Error"):
        generator.generate(context)
    assert mock_ollama_client.generate.call_count == 3
    assert ralf_notes.core.structured_text_generator.time.sleep.call_count == 2

# Task 6.2.3: Fix Timing Display Bug
@patch('time.time')
def test_generate_raw_logic_timing(mock_time, mock_config_manager, mock_console, tmp_path):
    mock_time.side_effect = [0, 10, 15] # Simulate time passing
    
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "file1.py").write_text("content")
    (source_dir / "file2.py").write_text("content")

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    with patch('ralf_notes.cli.StructuredTextGenerator') as MockGenerator, \
         patch('ralf_notes.cli.Client'): # Mock Ollama Client
        MockGenerator.return_value.generate_and_save_raw.return_value = None
        
        result = _generate_raw_logic(
            source_path=source_dir,
            output=output_dir,
            quiet=True,
            model=None,
            config_manager=mock_config_manager,
            console=mock_console
        )
        assert result is True
        # Verify show_summary was called with correct timing
        mock_console.panel.assert_called_once()
        call_args, _ = mock_console.panel.call_args
        summary_text = call_args[0]
        assert "Time: 15.0s" in summary_text
        assert "Speed: 0.1 files/s" in summary_text # 2 files / 15 seconds approx

@patch('time.time')
def test_format_initial_logic_timing(mock_time, mock_config_manager, mock_console, tmp_path):
    mock_time.side_effect = [0, 5, 12] # Simulate time passing
    
    source_dir = tmp_path / "raw_output"
    source_dir.mkdir()
    (source_dir / "file1.txt").write_text("content")
    (source_dir / "file2.txt").write_text("content")
    (source_dir / "file3.txt").write_text("content")

    output_dir = tmp_path / "formatted_output"
    output_dir.mkdir()

    with patch('ralf_notes.cli.build_pipeline') as MockBuildPipeline:
        mock_pipeline_instance = MockBuildPipeline.return_value
        mock_pipeline_instance.parser.parse_or_fallback.return_value = {"summary": "s", "tags": ["#tag"], "type": "code"}
        mock_pipeline_instance.formatter.format.return_value = "# Header"

        result = _format_initial_logic(
            path=source_dir,
            output=output_dir,
            dry_run=False,
            overwrite=True,
            quiet=True,
            model=None,
            config_manager=mock_config_manager,
            console=mock_console
        )
        assert result is True
        mock_console.panel.assert_called_once()
        call_args, _ = mock_console.panel.call_args
        summary_text = call_args[0]
        assert "Time: 12.0s" in summary_text
        assert "Speed: 0.2 files/s" in summary_text # 3 files / 12 seconds approx

@patch('time.time')
def test_finalize_logic_timing(mock_time, mock_config_manager, mock_console, tmp_path):
    mock_time.side_effect = [0, 2, 3] # Simulate time passing
    
    source_dir = tmp_path / "formatted_input"
    source_dir.mkdir()
    (source_dir / "file1.md").write_text("content")
    (source_dir / "file2.md").write_text("content")

    final_output_dir = tmp_path / "final_output"
    final_output_dir.mkdir()
    review_output_dir = tmp_path / "review_output"
    review_output_dir.mkdir()

    with patch('pathlib.Path.rename', MagicMock()): # Mock file rename operation
        result = _finalize_logic(
            path=source_dir,
            output=final_output_dir,
            review_output=review_output_dir,
            dry_run=False,
            overwrite=True,
            quiet=True,
            config_manager=mock_config_manager,
            console=mock_console
        )
        assert result is True
        mock_console.panel.assert_called_once()
        call_args, _ = mock_console.panel.call_args
        summary_text = call_args[0]
        assert "Time: 3.0s" in summary_text
        assert "Speed: 0.7 files/s" in summary_text # 2 files / 3 seconds approx

# Task 6.3.1: Input Validation (init command)
def test_init_command_add_source_path_exists(cli_runner, mock_config_manager, tmp_path):
    test_dir = tmp_path / "valid_source"
    test_dir.mkdir()
    
    with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager), \
         patch('ralf_notes.cli.Console') as MockConsole:
        result = cli_runner.invoke(app, ["init", "--add-source", str(test_dir)])
        assert result.exit_code == 0
        mock_config_manager.add_source_path.assert_called_once_with(str(test_dir))
        MockConsole.return_value.success.assert_any_call(f"Added source path: {str(test_dir)}")

def test_init_command_add_source_path_not_exists(cli_runner, mock_config_manager, tmp_path):
    non_existent_dir = tmp_path / "non_existent_source"
    
    with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager), \
         patch('ralf_notes.cli.Console') as MockConsole:
        result = cli_runner.invoke(app, ["init", "--add-source", str(non_existent_dir)])
        assert result.exit_code == 1
        MockConsole.return_value.error.assert_any_call(f"Error: Path for 'add_source' does not exist: {non_existent_dir}")
        mock_config_manager.add_source_path.assert_not_called()

def test_init_command_set_target_dir_writable(cli_runner, mock_config_manager, tmp_path):
    test_dir = tmp_path / "valid_target"
    test_dir.mkdir()

    with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager), \
         patch('ralf_notes.cli.Console') as MockConsole, \
         patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=True):
        result = cli_runner.invoke(app, ["init", "--set-target", str(test_dir)])
        assert result.exit_code == 0
        mock_config_manager.set_target_dir.assert_called_once_with(str(test_dir))
        MockConsole.return_value.success.assert_any_call(f"Target directory set to: {str(test_dir)}")

def test_init_command_set_target_dir_not_writable(cli_runner, mock_config_manager, tmp_path):
    test_dir = tmp_path / "unwritable_target"
    test_dir.mkdir()

    with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager), \
         patch('ralf_notes.cli.Console') as MockConsole, \
         patch('pathlib.Path.is_dir', return_value=True), \
         patch('os.access', return_value=False): # Mock os.access for writability
        result = cli_runner.invoke(app, ["init", "--set-target", str(test_dir)])
        assert result.exit_code == 1
        MockConsole.return_value.error.assert_any_call(f"Error: Path for 'set_target' is not writable: {test_dir} (None)")
        mock_config_manager.set_target_dir.assert_not_called()

def test_init_command_set_model_validation(cli_runner, mock_config_manager):
    with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager), \
         patch('ralf_notes.cli.Console') as MockConsole:
        mock_config_manager.set.side_effect = ValueError("Invalid value for 'model_name'")
        result = cli_runner.invoke(app, ["init", "--set-model", "invalid-model"])
        assert result.exit_code == 1
        MockConsole.return_value.error.assert_any_call("Error: Invalid value for 'model_name': Invalid value for 'model_name'")
        mock_config_manager.set.assert_called_once_with("model_name", "invalid-model") # Still called, but raised error


# Additional path validation tests for generate-raw, format-initial, finalize commands
@patch('ralf_notes.cli.ConfigManager')
@patch('ralf_notes.cli.Console')
@patch('ralf_notes.cli._validate_path_exists')
@patch('ralf_notes.cli._validate_path_is_dir')
@patch('ralf_notes.cli._validate_path_is_writable')
def test_generate_raw_command_path_validation(
    mock_validate_writable, mock_validate_is_dir, mock_validate_exists,
    MockConsole, MockConfigManager, cli_runner, tmp_path
):
    mock_config_manager_instance = MockConfigManager.return_value
    mock_config_manager_instance.get.return_value = [] # No configured source paths

    # Test no source paths configured
    result = cli_runner.invoke(app, ["generate-raw"])
    assert result.exit_code == 1
    MockConsole.return_value.error.assert_any_call("No source paths configured! Cannot generate documentation.")

    # Test explicit source path not existing
    non_existent_source = tmp_path / "non_existent_source"
    mock_validate_exists.side_effect = typer.Exit(1)
    result = cli_runner.invoke(app, ["generate-raw", str(non_existent_source)])
    assert result.exit_code == 1
    mock_validate_exists.assert_called_once_with(non_existent_source, "source_path", MockConsole.return_value)

    # Test explicit output path not writable
    mock_validate_exists.side_effect = None # Reset mock
    mock_validate_is_dir.side_effect = None # Reset mock
    mock_validate_writable.side_effect = typer.Exit(1)
    valid_source = tmp_path / "valid_source"
    valid_source.mkdir()
    unwritable_output = tmp_path / "unwritable_output"
    unwritable_output.mkdir()
    result = cli_runner.invoke(app, ["generate-raw", str(valid_source), "--output", str(unwritable_output)])
    assert result.exit_code == 1
    mock_validate_writable.assert_called_once_with(unwritable_output, "raw_output", MockConsole.return_value)


@patch('ralf_notes.cli.ConfigManager')
@patch('ralf_notes.cli.Console')
@patch('ralf_notes.cli._validate_path_exists')
@patch('ralf_notes.cli._validate_path_is_dir')
@patch('ralf_notes.cli._validate_path_is_writable')
def test_format_initial_command_path_validation(
    mock_validate_writable, mock_validate_is_dir, mock_validate_exists,
    MockConsole, MockConfigManager, cli_runner, tmp_path
):
    mock_config_manager_instance = MockConfigManager.return_value
    mock_config_manager_instance.get.return_value = [] # No configured raw output paths

    # Test no raw output paths configured
    result = cli_runner.invoke(app, ["format-initial"])
    assert result.exit_code == 1
    MockConsole.return_value.error.assert_any_call("No raw output paths configured! Cannot format documentation.")

    # Test explicit raw output path not existing
    non_existent_raw = tmp_path / "non_existent_raw_output"
    mock_validate_exists.side_effect = typer.Exit(1)
    result = cli_runner.invoke(app, ["format-initial", str(non_existent_raw)])
    assert result.exit_code == 1
    mock_validate_exists.assert_called_once_with(non_existent_raw, "path", MockConsole.return_value)

    # Test explicit formatted output path not writable
    mock_validate_exists.side_effect = None
    mock_validate_is_dir.side_effect = None
    mock_validate_writable.side_effect = typer.Exit(1)
    valid_raw_output = tmp_path / "valid_raw_output"
    valid_raw_output.mkdir()
    unwritable_formatted_output = tmp_path / "unwritable_formatted_output"
    unwritable_formatted_output.mkdir()
    result = cli_runner.invoke(app, ["format-initial", str(valid_raw_output), "--output", str(unwritable_formatted_output)])
    assert result.exit_code == 1
    mock_validate_writable.assert_called_once_with(unwritable_formatted_output, "formatted_output", MockConsole.return_value)


@patch('ralf_notes.cli.ConfigManager')
@patch('ralf_notes.cli.Console')
@patch('ralf_notes.cli._validate_path_exists')
@patch('ralf_notes.cli._validate_path_is_dir')
@patch('ralf_notes.cli._validate_path_is_writable')
def test_finalize_command_path_validation(
    mock_validate_writable, mock_validate_is_dir, mock_validate_exists,
    MockConsole, MockConfigManager, cli_runner, tmp_path
):
    mock_config_manager_instance = MockConfigManager.return_value
    mock_config_manager_instance.get.return_value = [] # No configured formatted paths

    # Test no initial formatted paths configured
    result = cli_runner.invoke(app, ["finalize"])
    assert result.exit_code == 1
    MockConsole.return_value.error.assert_any_call("No initial formatted paths configured! Cannot finalize documentation.")

    # Test explicit initial formatted path not existing
    non_existent_formatted = tmp_path / "non_existent_formatted_input"
    mock_validate_exists.side_effect = typer.Exit(1)
    result = cli_runner.invoke(app, ["finalize", str(non_existent_formatted)])
    assert result.exit_code == 1
    mock_validate_exists.assert_called_once_with(non_existent_formatted, "path", MockConsole.return_value)

    # Test explicit final output path not writable
    mock_validate_exists.side_effect = None
    mock_validate_is_dir.side_effect = None
    mock_validate_writable.side_effect = typer.Exit(1)
    valid_formatted_input = tmp_path / "valid_formatted_input"
    valid_formatted_input.mkdir()
    unwritable_final_output = tmp_path / "unwritable_final_output"
    unwritable_final_output.mkdir()
    result = cli_runner.invoke(app, ["finalize", str(valid_formatted_input), "--output", str(unwritable_final_output)])
    assert result.exit_code == 1
    mock_validate_writable.assert_called_once_with(unwritable_final_output, "final_output", MockConsole.return_value)

    # Test explicit review output path not writable
    mock_validate_writable.side_effect = typer.Exit(1) # Reset for this test
    valid_formatted_input_2 = tmp_path / "valid_formatted_input_2"
    valid_formatted_input_2.mkdir()
    unwritable_review_output = tmp_path / "unwritable_review_output"
    unwritable_review_output.mkdir()
    result = cli_runner.invoke(app, ["finalize", str(valid_formatted_input_2), "--review-output", str(unwritable_review_output)])
    assert result.exit_code == 1
    mock_validate_writable.assert_called_once_with(unwritable_review_output, "review_output", MockConsole.return_value)


# Test for Task 7.2.2: Better Error Messages in check_health
@patch('ralf_notes.cli.ConfigManager')
@patch('ralf_notes.cli.Console')
@patch('ralf_notes.cli.Client')
def test_check_health_ollama_connection_error_message(
    MockClient, MockConsole, MockConfigManager, cli_runner
):
    mock_config_manager_instance = MockConfigManager.return_value
    mock_config_manager_instance.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://non-existent-host:11434",
        "model_name": "test-model"
    }.get(key, default)
    MockClient.side_effect = Exception("Connection refused")

    result = cli_runner.invoke(app, ["check-health"])
    assert result.exit_code == 1
    MockConsole.return_value.error.assert_any_call("Failed to connect to Ollama at http://non-existent-host:11434.")
    MockConsole.return_value.info.assert_any_call(
        "Please ensure Ollama is running and accessible at this address. You can change the host in the configuration ('ralf-notes init --set-ollama-host <new-host>')."
    )

@patch('ralf_notes.cli.ConfigManager')
@patch('ralf_notes.cli.Console')
@patch('ralf_notes.cli.Client')
def test_check_health_model_not_available_error_message(
    MockClient, MockConsole, MockConfigManager, cli_runner
):
    mock_config_manager_instance = MockConfigManager.return_value
    mock_config_manager_instance.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "non-existent-model"
    }.get(key, default)
    MockClient.return_value.list.return_value = None # Simulate successful connection
    MockClient.return_value.show.side_effect = Exception("Model 'non-existent-model' not found")

    result = cli_runner.invoke(app, ["check-health"])
    assert result.exit_code == 1
    MockConsole.return_value.error.assert_any_call("Model 'non-existent-model' is not available on your Ollama instance.")
    MockConsole.return_value.info.assert_any_call(
        "Please pull the model using: [bold yellow]ollama pull non-existent-model[/bold yellow]."
    )
    MockConsole.return_value.info.assert_any_call(
        "You can also change the configured model name ('ralf-notes init --set-model <new-model>')."
    )
