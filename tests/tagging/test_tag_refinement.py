import pytest
from unittest.mock import MagicMock, patch, mock_open
from pathlib import Path
import json
import os
import shutil

from typer.testing import CliRunner

from ralf_notes.config_manager import ConfigManager
from ralf_notes.cli import app
from ralf_notes.tagging.tag_collector import TagCollector
from ralf_notes.tagging.tag_analyzer import TagAnalyzer, TagPattern
from ralf_notes.tagging.tag_refinement_llm import TagRefinementLLM
from ralf_notes.tagging.refinement_guide_builder import RefinementGuideBuilder
from ralf_notes.tagging.tag_replacer import TagReplacer


# --- Fixtures ---

@pytest.fixture
def cli_runner():
    return CliRunner()

@pytest.fixture
def mock_config_manager_tags():
    """Mocks ConfigManager for tagging tests."""
    config_manager = MagicMock(spec=ConfigManager)
    config_manager.get.side_effect = lambda key, default=None: {
        "ollama_host": "http://localhost:11434",
        "model_name": "test-model",
        "target_dir": "/tmp/to_obsidian", # Default target for CLI tests
    }.get(key, default)
    config_manager.set.return_value = None
    return config_manager

@pytest.fixture
def mock_ollama_client_tags():
    """Mocks Ollama Client for tagging LLM tests."""
    client = MagicMock()
    client.chat.return_value = {
        'message': {'content': json.dumps({
            "refinements": [
                {"old_tags": ["#data-processing", "#dataprocessing"], "new_tag": "#dataproc", "reason": "Standardize and simplify"}
            ],
            "new_tags": [],
            "keep_as_is": ["#python", "#feature"],
            "delete": ["#none-tag"]
        })}
    }
    return client

@pytest.fixture
def temp_markdown_dir(tmp_path):
    """Creates a temporary directory with some markdown files."""
    test_dir = tmp_path / "test_docs"
    test_dir.mkdir()
    (test_dir / "file1.md").write_text("---\ntags: #python, #feature, #data-processing, #none\n---\n# File 1")
    (test_dir / "file2.md").write_text("---\ntags: #python, #bug-fix, #dataprocessing\n---\n# File 2")
    (test_dir / "file3.md").write_text("---\ntags: #feature, #test_suite\n---\n# File 3")
    (test_dir / "file4.md").write_text("No frontmatter here.")
    (test_dir / "file5.md").write_text("---\ntags: #long-named-tag, #another-long-tag, none\n---\n# File 5")
    return test_dir

@pytest.fixture
def mock_tag_data():
    return {
        'tag_frequency': {'#python': 2, '#feature': 2, '#dataprocessing': 1, '#bugfix': 1, '#testsuite': 1},
        'tag_to_files': {
            '#python': ['file1.md', 'file2.md'],
            '#feature': ['file1.md', 'file3.md'],
            '#dataprocessing': ['file2.md'],
            '#bugfix': ['file2.md'],
            '#testsuite': ['file3.md']
        },
        'total_files': 3,
        'total_unique_tags': 5
    }

@pytest.fixture
def mock_analysis_report():
    return {
        'patterns': [
            TagPattern(pattern_type='compound', tags=['#data-processing', '#dataprocessing'], suggestion='Group under #dataproc', confidence=0.8),
            TagPattern(pattern_type='similar', tags=['#bugfix', '#bug_fix'], suggestion='Standardize to #bugfix', confidence=0.7)
        ],
        'statistics': {
            'mean_usage': 1.4,
            'max_usage': 2,
            'min_usage': 1,
            'rare_tags': ['#bugfix', '#testsuite'],
            'common_tags': ['#python']
        },
        'total_patterns': 2
    }

@pytest.fixture
def mock_llm_suggestions():
    return {
        "refinements": [
            {"old_tags": ["#data-processing", "#dataprocessing"], "new_tag": "#dataproc", "reason": "Standardize and simplify"},
            {"old_tags": ["#bug-fix"], "new_tag": "#bugfix", "reason": "Enforce single word rule"}
        ],
        "new_tags": [
            {"tag": "#coredev", "reason": "New tag for core development", "merge_from": ["#core", "#development"]}
        ],
        "keep_as_is": ["#python", "#feature", "#testsuite"],
        "delete": ["#oldtag", "#legacy"]
    }

@pytest.fixture
def mock_refinement_guide():
    return {
        "version": "1.0",
        "generated_at": "2026-01-12",
        "total_tags_analyzed": 5,
        "refinements": [
            {"old_tags": ["#data-processing", "#dataprocessing"], "new_tag": "#dataproc", "reason": "Standardize and simplify"},
            {"old_tags": ["#bug-fix"], "new_tag": "#bugfix", "reason": "Enforce single word rule"}
        ],
        "new_tags": [
            {"tag": "#coredev", "reason": "New tag for core development", "merge_from": ["#core", "#development"]}
        ],
        "keep_as_is": ["#python", "#feature", "#testsuite"],
        "delete": ["#oldtag", "#legacy"],
        "statistics": {},
        "patterns_found": 2,
        "llm_error": None
    }


# --- TagCollector Tests ---

class TestTagCollector:
    def test_extract_tags_from_frontmatter_valid(self):
        content = "---\ntags: #python, #feature\n---\nBody"
        collector = TagCollector()
        tags = collector._extract_tags_from_frontmatter(content)
        assert sorted(tags) == sorted(["#python", "#feature"])

    def test_extract_tags_from_frontmatter_invalid_format(self):
        content = "---\ntags: ['#python', '#feature']\n---\nBody" # List format
        collector = TagCollector()
        tags = collector._extract_tags_from_frontmatter(content)
        assert sorted(tags) == sorted(["#python", "#feature"])
        
    def test_extract_tags_from_frontmatter_none_tag_filtered(self):
        content = "---\ntags: #python, #none, #none-value\n---\nBody"
        collector = TagCollector()
        tags = collector._extract_tags_from_frontmatter(content)
        assert tags == ["#python"]

    def test_extract_tags_from_frontmatter_multi_word_filtered(self):
        content = "---\ntags: #singleword, #multi word, #with-hyphen, #with_underscore\n---\nBody"
        collector = TagCollector()
        tags = collector._extract_tags_from_frontmatter(content)
        assert tags == ["#singleword"] # Only single word tags without separators should pass

    def test_extract_tags_from_frontmatter_no_frontmatter(self):
        content = "No frontmatter here."
        collector = TagCollector()
        tags = collector._extract_tags_from_frontmatter(content)
        assert tags == []

    def test_collect_tags(self, temp_markdown_dir):
        collector = TagCollector()
        tag_data = collector.collect_tags(temp_markdown_dir)
        
        expected_frequency = {
            '#python': 2, 
            '#feature': 2, 
            '#test_suite': 1 # Only valid single-word tags are collected
        }
        assert tag_data['tag_frequency'] == expected_frequency
        assert tag_data['total_files'] == 3 # file1, file2, file3 have frontmatter
        assert tag_data['total_unique_tags'] == len(expected_frequency)
        assert '#data-processing' not in tag_data['tag_frequency'] # Filtered
        assert '#long-named-tag' not in tag_data['tag_frequency'] # Filtered
        assert '#none' not in tag_data['tag_frequency'] # Filtered


# --- TagAnalyzer Tests ---

class TestTagAnalyzer:
    def test_find_compound_patterns(self, mock_tag_data):
        analyzer = TagAnalyzer()
        patterns = analyzer._find_compound_patterns(mock_tag_data['tag_frequency'])
        assert any(p.pattern_type == 'compound' and p.suggestion == 'Group under #dataproc' for p in patterns)

    def test_find_similar_tags(self, mock_tag_data):
        analyzer = TagAnalyzer()
        patterns = analyzer._find_similar_tags(mock_tag_data['tag_frequency'])
        assert any(p.pattern_type == 'similar' for p in patterns)

    def test_analyze(self, mock_tag_data):
        analyzer = TagAnalyzer()
        analysis_report = analyzer.analyze(mock_tag_data)
        assert 'patterns' in analysis_report
        assert 'statistics' in analysis_report
        assert analysis_report['total_patterns'] >= 1 # At least one pattern should be found

# --- TagRefinementLLM Tests ---

class TestTagRefinementLLM:
    def test_generate_refinements_success(self, mock_ollama_client_tags, mock_analysis_report):
        refiner = TagRefinementLLM(mock_ollama_client_tags)
        suggestions = refiner.generate_refinements(mock_analysis_report)
        assert "refinements" in suggestions
        mock_ollama_client_tags.chat.assert_called_once()
        # Verify that the prompt contains the new rules
        call_args, _ = mock_ollama_client_tags.chat.call_args
        prompt = call_args[1][0]['content'] # system message
        assert "No \"none\" tags" in prompt
        assert "Single-worded tags" in prompt
        assert "No separators in tags" in prompt
        assert "NOT #data-processing, NOT #data_processing" in prompt

    def test_generate_refinements_llm_json_error(self, mock_ollama_client_tags, mock_analysis_report):
        mock_ollama_client_tags.chat.return_value = {'message': {'content': 'invalid json'}}
        refiner = TagRefinementLLM(mock_ollama_client_tags)
        suggestions = refiner.generate_refinements(mock_analysis_report)
        assert "error" in suggestions
        assert "LLM response not valid JSON" in suggestions['error']
        assert not suggestions['refinements']

# --- RefinementGuideBuilder Tests ---

class TestRefinementGuideBuilder:
    def test_build_guide_and_save(self, tmp_path, mock_llm_suggestions, mock_analysis_report):
        output_file = tmp_path / "guide.json"
        builder = RefinementGuideBuilder()
        guide = builder.build_guide(mock_llm_suggestions, mock_analysis_report, output_file)

        assert output_file.exists()
        with open(output_file, 'r') as f:
            saved_guide = json.load(f)
        
        assert saved_guide['refinements'] == mock_llm_suggestions['refinements']
        assert saved_guide['new_tags'] == mock_llm_suggestions['new_tags']
        assert saved_guide['total_tags_analyzed'] == mock_analysis_report['total_unique_tags']

# --- TagReplacer Tests ---

class TestTagReplacer:
    def test_build_replacement_map(self, mock_refinement_guide):
        replacer = TagReplacer(mock_refinement_guide)
        replacement_map = replacer.replacement_map
        assert replacement_map['#data-processing'] == '#dataproc'
        assert replacement_map['#dataprocessing'] == '#dataproc'
        assert replacement_map['#bug-fix'] == '#bugfix'
        assert replacement_map['#core'] == '#coredev'
        assert replacement_map['#development'] == '#coredev'
        assert replacement_map['#oldtag'] is None

    def test_replace_tags_in_file(self, mock_refinement_guide):
        replacer = TagReplacer(mock_refinement_guide)
        original_content = "---\ntags: #python, #data-processing, #bug-fix, #oldtag, #feature\n---\nBody"
        new_content, modified, replaced_count = replacer._replace_tags_in_file(original_content)
        
        assert modified is True
        assert replaced_count == 4 # data-processing, bug-fix, oldtag, feature (as it's in keep_as_is and not mapped)
        
        # Parse new content's frontmatter to verify
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_content, re.DOTALL)
        frontmatter_str = frontmatter_match.group(1)
        data = yaml.safe_load(frontmatter_str)
        
        expected_tags = sorted(['#python', '#dataproc', '#bugfix', '#feature']) # Note: #feature is not changed by the guide, should remain.
        assert sorted(data['tags']) == expected_tags

    @patch('shutil.copytree')
    def test_apply_refinements_with_backup(self, mock_copytree, tmp_path, mock_refinement_guide):
        test_dir = tmp_path / "test_docs_apply"
        test_dir.mkdir()
        (test_dir / "file1.md").write_text("---\ntags: #data-processing\n---\nBody")
        (test_dir / "file2.md").write_text("---\ntags: #python\n---\nBody")

        replacer = TagReplacer(mock_refinement_guide)
        results = replacer.apply_refinements(test_dir, dry_run=False, backup=True)

        assert results['files_processed'] == 2
        assert results['files_modified'] == 1 # file1 should be modified
        assert results['backup_path'] is not None
        mock_copytree.assert_called_once()
        
        # Verify file1 content
        file1_content = (test_dir / "file1.md").read_text()
        assert '#dataproc' in file1_content
        assert '#data-processing' not in file1_content
        
        # Verify file2 content (should not change)
        file2_content = (test_dir / "file2.md").read_text()
        assert '#python' in file2_content

    def test_apply_refinements_dry_run(self, tmp_path, mock_refinement_guide):
        test_dir = tmp_path / "test_docs_dry_run"
        test_dir.mkdir()
        file1_path = test_dir / "file1.md"
        file1_path.write_text("---\ntags: #data-processing\n---\nBody")

        replacer = TagReplacer(mock_refinement_guide)
        results = replacer.apply_refinements(test_dir, dry_run=True, backup=False)

        assert results['files_processed'] == 1
        assert results['files_modified'] == 1
        assert results['backup_path'] is None # No backup in dry run
        
        # Verify file content is unchanged
        assert '#data-processing' in file1_path.read_text()
        assert '#dataproc' not in file1_path.read_text()

# --- CLI Integration Tests for 'ralf-notes tags' commands ---

@patch('ralf_notes.cli.TagCollector')
@patch('ralf_notes.cli.TagAnalyzer')
@patch('ralf_notes.cli.TagRefinementLLM')
@patch('ralf_notes.cli.RefinementGuideBuilder')
@patch('ralf_notes.cli.ConfigManager', new=MagicMock) # Mock ConfigManager explicitly here
@patch('ralf_notes.cli.Client', new=MagicMock) # Mock Ollama Client here
def test_cli_tags_analyze_command(
    MockRefinementGuideBuilder, MockTagRefinementLLM, MockTagAnalyzer, MockTagCollector,
    cli_runner, tmp_path, mock_config_manager_tags
):
    # Mock return values for the components
    MockTagCollector.return_value.collect_tags.return_value = {
        'tag_frequency': {'#python': 5, '#feature': 3}, 'total_unique_tags': 2, 'total_files': 2
    }
    MockTagAnalyzer.return_value.analyze.return_value = {
        'patterns': [TagPattern('compound', ['#data-analysis', '#dataanalysis'], '#data', 0.8)], 'total_patterns': 1
    }
    MockTagRefinementLLM.return_value.generate_refinements.return_value = {
        'refinements': [], 'new_tags': [], 'keep_as_is': ['#python'], 'delete': []
    }
    MockRefinementGuideBuilder.return_value.build_guide.return_value = {
        'refinements': [], 'new_tags': [], 'keep_as_is': ['#python'], 'delete': [], 'llm_error': None
    }
    
    # Mock console for output checks
    with patch('ralf_notes.cli.Console') as MockConsole:
        # Use a mock config manager for the cli app as well
        with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager_tags):
            output_file = tmp_path / "guide.json"
            result = cli_runner.invoke(app, ["tags", "analyze", str(tmp_path), "--output", str(output_file)])

            assert result.exit_code == 0
            MockTagCollector.return_value.collect_tags.assert_called_once_with(Path(str(tmp_path)))
            MockTagAnalyzer.return_value.analyze.assert_called_once()
            MockTagRefinementLLM.return_value.generate_refinements.assert_called_once()
            MockRefinementGuideBuilder.return_value.build_guide.assert_called_once()
            MockConsole.return_value.success.assert_any_call(f"Tag refinement guide generated successfully: {output_file}")


@patch('ralf_notes.cli.TagReplacer')
@patch('ralf_notes.cli.ConfigManager', new=MagicMock)
def test_cli_tags_apply_command(MockTagReplacer, cli_runner, tmp_path, mock_config_manager_tags):
    guide_file = tmp_path / "guide.json"
    guide_file.write_text(json.dumps({"refinements": []})) # Dummy guide content

    target_dir = tmp_path / "target_docs"
    target_dir.mkdir()

    MockTagReplacer.return_value.apply_refinements.return_value = {
        'files_processed': 5, 'files_modified': 2, 'tags_replaced': 3, 'errors': [], 'backup_path': '/tmp/backup'
    }

    with patch('ralf_notes.cli.Console') as MockConsole:
        with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager_tags):
            result = cli_runner.invoke(app, ["tags", "apply", str(target_dir), "--guide", str(guide_file)])
            
            assert result.exit_code == 0
            MockTagReplacer.assert_called_once()
            MockTagReplacer.return_value.apply_refinements.assert_called_once_with(
                Path(str(target_dir)), dry_run=False, backup=True
            )
            MockConsole.return_value.success.assert_any_call("Tag refinement application complete.")
            MockConsole.return_value.info.assert_any_call("Backup created at: /tmp/backup")

@patch('ralf_notes.cli.TagCollector')
@patch('ralf_notes.cli.ConfigManager', new=MagicMock)
def test_cli_tags_stats_command(MockTagCollector, cli_runner, tmp_path, mock_config_manager_tags):
    target_dir = tmp_path / "target_docs"
    target_dir.mkdir()

    MockTagCollector.return_value.collect_tags.return_value = {
        'tag_frequency': {'#python': 5, '#feature': 3, '#test': 1},
        'tag_to_files': {
            '#python': ['file1.md', 'file2.md'],
            '#feature': ['file1.md'],
            '#test': ['file3.md']
        },
        'total_files': 3,
        'total_unique_tags': 3
    }

    with patch('ralf_notes.cli.Console') as MockConsole:
        with patch('ralf_notes.cli.ConfigManager', return_value=mock_config_manager_tags):
            result = cli_runner.invoke(app, ["tags", "stats", str(target_dir)])

            assert result.exit_code == 0
            MockTagCollector.return_value.collect_tags.assert_called_once_with(Path(str(target_dir)))
            MockConsole.return_value.print.assert_any_call("\n📊 Tag Statistics:")
            MockConsole.return_value.print.assert_any_call("  Total unique tags found: 3")
