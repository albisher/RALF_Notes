#!/usr/bin/env python3
"""
RALF Note v2.0 - CLI Application

Main command-line interface
"""

import typer
from pathlib import Path
from typing import Optional, List, Tuple
from ollama import Client
from datetime import datetime
import logging
import shutil
import json
import time

from .version import VERSION
from .config_manager import ConfigManager
from .core import (
    StructuredTextGenerator,
    TextParser,
    NoteFormatter,
    DocumentPipeline,
    FileProcessor,
    StructuredTextGeneratorConfig,
    GenerationContext,
)
from rich.table import Table
from rich.text import Text
from rich.panel import Panel as RichPanel
from rich.console import Group
from rich.live import Live
from rich.prompt import Prompt, Confirm
from .tui import Console, ProgressManager
from .tui.ascii_art import Banner, get_dashboard
from .tuning.models import BenchmarkConfig, OptimizedConfig, SystemProfile
from .tuning.orchestrator import BenchmarkOrchestrator
from .tuning.system_profiler import SystemProfiler
from .tuning.model_benchmarker import ModelBenchmarker
from .tuning.latency_benchmarker import LatencyBenchmarker
from .tuning.throughput_benchmarker import ThroughputBenchmarker
from .tuning.sample_generator import SampleCodeGenerator
from .tuning.config_builder import OptimizedConfigBuilder
from .utils.logger import setup_logging
from .tagging.tag_collector import TagCollector
from .tagging.tag_analyzer import TagAnalyzer, TagPattern
from .tagging.tag_refinement_llm import TagRefinementLLM
from .tagging.refinement_guide_builder import RefinementGuideBuilder
from .tagging.tag_replacer import TagReplacer
from .core.watcher import Watcher
from .linking.link_collector import LinkCollector
from .linking.link_resolver import LinkResolver
from .linking.link_refiner import LinkRefiner
from .organization.file_mover import FileMover


def display_config_table(console: Console, config_manager: ConfigManager):
    """Displays the configuration in a formatted table."""
    table = Table(title="[bold]⚙️ Current Configuration[/bold]", style="cyan", show_header=True, header_style="bold magenta")
    table.add_column("Setting", style="dim", width=20)
    table.add_column("Value", style="bold")


    config = config_manager.config
    for key, value in config.items():
        if key == "source_paths":
            if not value:
                table.add_row(key, "[yellow]None configured[/yellow]")
            else:
                path_list = []
                for path in value:
                    exists = "✅" if Path(path).exists() else "❌"
                    path_list.append(f"{exists} {path}")
                table.add_row(key, "\n".join(path_list))
        elif isinstance(value, list):
            table.add_row(key, ", ".join(map(str, value)))
        else:
            table.add_row(key, str(value))
    
    console.print("")
    console.print(table)
    console.print("")
    console.info(f"Config file: {config_manager.config_path}")


def _validate_path_exists(path: Path, param_name: str, console: Console):
    """Validates if a given path exists."""
    if not path.exists():
        console.error(f"Error: Path for '{param_name}' does not exist: {path}")
        raise typer.Exit(1)

def _validate_path_is_dir(path: Path, param_name: str, console: Console):
    """Validates if a given path is a directory."""
    if not path.is_dir():
        console.error(f"Error: Path for '{param_name}' is not a directory: {path}")
        raise typer.Exit(1)

def _validate_path_is_writable(path: Path, param_name: str, console: Console):
    """Validates if a given path is writable."""
    if not path.is_dir(): # Check if it's a directory first
        console.error(f"Error: Path for '{param_name}' is not a directory: {path}")
        raise typer.Exit(1)
    # Test writability by trying to create and delete a temporary file
    try:
        test_file = path / ".ralf_notes_test_write"
        test_file.touch()
        test_file.unlink()
    except OSError as e:
        console.error(f"Error: Path for '{param_name}' is not writable: {path} ({e})")
        raise typer.Exit(1)


app = typer.Typer(
    name="ralf-notes",
    help="🚀 RALF Note v2.0 - AI-Powered Obsidian Documentation Generator",
    add_completion=True
)

def version_callback(value: bool):
    if value:
        console = Console()
        console.banner(Banner.get_renderable(style='simple'))
        console.print("")
        console.info(f"RALF Note v{VERSION} - Structured Text Architecture")
        console.info("Built with: Ollama, Rich, Typer")
        console.print("")
        raise typer.Exit()

@app.callback()
def callback(
    version: Optional[bool] = typer.Option(
        None, "--version", help="Show version information.", callback=version_callback, is_eager=True
    )
):
    """
    RALF Note v2.0 - AI-Powered Obsidian Documentation Generator
    """
    config_manager = ConfigManager() # Initialize config_manager here
    log_level = config_manager.get("log_level", "INFO")
    log_file_path = config_manager.get("log_file", None)
    
    # If log_file is specified in config, convert to Path object
    if log_file_path:
        log_file_path = Path(log_file_path)
    
    setup_logging(log_level, log_file_path) # Initialize logging
    logger = logging.getLogger(__name__)
    logger.debug("Logging initialized via CLI callback.")

def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    """Build the document generation pipeline."""
    ollama_host = config_manager.get("ollama_host")
    model_name = config_manager.get("model_name")
    try:
        client = Client(host=ollama_host)
        # Attempt to list models to verify connection, though a full check is in check_health
        client.list() 
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to connect to Ollama at {ollama_host}: {e}", exc_info=True)
        raise RuntimeError(f"Failed to connect to Ollama at '{ollama_host}'. "
                           f"Please ensure Ollama is running and accessible. "
                           f"Run 'ralf-notes check-health' for diagnostics. Error: {e}") from e
    
    try:
        gen_config = StructuredTextGeneratorConfig(
            model_name=model_name,
            num_ctx=config_manager.get("num_ctx"),
            temperature=config_manager.get("temperature"),
            chunk_size=config_manager.get("chunk_size"),
            max_content_length=config_manager.get("max_content_length"),
            max_chunk_summary_length=config_manager.get("max_chunk_summary_length"),
            ollama_host=ollama_host,
            retry_attempts=config_manager.get("retry_attempts"),
            initial_backoff_seconds=config_manager.get("initial_backoff_seconds"),
            backoff_multiplier=config_manager.get("backoff_multiplier")
        )
        generator = StructuredTextGenerator(client, gen_config)
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to initialize StructuredTextGenerator with model '{model_name}': {e}", exc_info=True)
        raise RuntimeError(f"Failed to initialize generator with model '{model_name}'. "
                           f"Ensure the model is pulled ('ollama pull {model_name}') and configuration is valid. "
                           f"Error: {e}") from e

    parser = TextParser()
    formatter = NoteFormatter()
    return DocumentPipeline(generator, parser, formatter)

def show_summary(results: dict, console: Console, quiet: bool):
    """Display processing summary."""
    if quiet:
        return
    console.rule("Summary")
    summary_text = f"""
Total Files: [bold]{results.get('total', 0)}[/bold]
✅ Success: [success]{results.get('success', 0)}[/success]
❌ Failed: [error]{results.get('failed', 0)}[/error]
⏭️  Skipped: [dim]{results.get('skipped', 0)}[/dim]

Time: {results.get('duration', 0):.1f}s
Speed: {results.get('files_per_second', 0):.1f} files/s"""
    if results.get('dry_run', False):
        title = "📊 Results (Dry Run)"
        summary_text += "\n\n[info]No files were written.[/info]"
    else:
        title = "📊 Results"
    console.panel(summary_text, title=title, style="green")
    if results.get('failed', 0) > 0:
        console.warning(f"Check output for {results.get('failed', 0)} failed files")


@app.callback(invoke_without_command=True)
def _default_welcome(ctx: typer.Context):
    """
    Displays welcome message and basic instructions if no subcommand is given.
    """
    if ctx.invoked_subcommand is None:
        console = Console()
        console.banner(Banner.get_renderable())
        console.print("")
        console.info("Welcome to RALF Note - AI-Powered Obsidian Documentation Generator!")
        console.print("")
        console.print("[bold]To get started:[/bold]")
        console.print("  1. Run [bold green]ralf-notes init[/bold green] to set up your configuration.")
        console.print("     (This will guide you through setting source paths, target directory, and Ollama model.)")
        console.print("  2. Run [bold green]ralf-notes generate[/bold green] to generate documentation.")
        console.print("  3. Run [bold green]ralf-notes tags analyze[/bold green] to refine your documentation tags.")
        console.print("  4. Use [bold green]ralf-notes check-health[/bold green] to verify your Ollama setup.")
        console.print("")
        console.print("For more information, run [bold green]ralf-notes --help[/bold green].")
        raise typer.Exit()


@app.command()
def init(
    show: bool = typer.Option(False, "--show", help="Show current configuration."),
    add_source: Optional[str] = typer.Option(None, "--add-source", help="Add a source path to the configuration."),
    remove_source: Optional[str] = typer.Option(None, "--remove-source", help="Remove a source path."),
    set_target: Optional[str] = typer.Option(None, "--set-target", help="Set the target directory (final output)."),
    set_stage1_raw_output: Optional[str] = typer.Option(None, "--set-stage1-raw-output", help="Set the Stage 1 raw output directory."),
    set_initial_formatted: Optional[str] = typer.Option(None, "--set-initial-formatted", help="Set the Stage 2 initial formatted output directory."),
    set_review_needed: Optional[str] = typer.Option(None, "--set-review-needed", help="Set the directory for files needing review/refinement (Stage 3)."),
    set_model: Optional[str] = typer.Option(None, "--set-model", help="Set the Ollama model name."),
    set_max_files: Optional[int] = typer.Option(None, "--set-max-files", help="Set the max number of files to process (0 for no limit)."),
    reset: bool = typer.Option(False, "--reset", help="Reset configuration to defaults."),
):
    """Initialize or manage RALF Note configuration."""
    console = Console()
    config_manager = ConfigManager()
    action_taken = False
    
    if any([reset, add_source, remove_source, set_target, set_stage1_raw_output, set_initial_formatted, set_review_needed, set_model, set_max_files is not None, show]):
        action_taken = True
        if reset:
            if Confirm.ask("Reset configuration to defaults?"):
                config_manager.reset_to_defaults()
                config_manager.save()
                console.success("Configuration reset to defaults")
            else:
                console.info("Reset cancelled.")
        if add_source:
            source_path_obj = Path(add_source)
            _validate_path_exists(source_path_obj, "add_source", console)
            _validate_path_is_dir(source_path_obj, "add_source", console) # Source path should be a directory
            config_manager.add_source_path(add_source)
            config_manager.save()
            console.success(f"Added source path: {add_source}")
        if remove_source:
            config_manager.remove_source_path(remove_source)
            config_manager.save()
            console.success(f"Removed source path: {remove_source}")
        if set_target:
            target_dir_obj = Path(set_target)
            _validate_path_is_writable(target_dir_obj, "set_target", console)
            config_manager.set_target_dir(set_target)
            config_manager.save()
            console.success(f"Target directory set to: {set_target}")
        
        # ... other settings update logic ... (omitted for brevity in this replace call, but keeping logic consistent)
        if set_stage1_raw_output:
            config_manager.set_stage1_raw_output_dir(set_stage1_raw_output)
            config_manager.save()
            console.success(f"Stage 1 output set to: {set_stage1_raw_output}")
        if set_initial_formatted:
            config_manager.set_initial_formatted_dir(set_initial_formatted)
            config_manager.save()
            console.success(f"Initial formatted output set to: {set_initial_formatted}")
        if set_review_needed:
            config_manager.set_review_needed_dir(set_review_needed)
            config_manager.save()
            console.success(f"Review needed directory set to: {set_review_needed}")
        
        if set_model:
            config_manager.set("model_name", set_model)
            config_manager.save()
            console.success(f"Ollama model name set to: {set_model}")
        if set_max_files is not None:
            config_manager.set("max_files_to_process", set_max_files)
            config_manager.save()
            console.success(f"Max files set to: {set_max_files}")

        if show:
            display_config_table(console, config_manager)
        return

    if config_manager.config_path.exists():
        console.warning(f"Configuration already exists at: {config_manager.config_path}")
        display_config_table(console, config_manager)
        if not Confirm.ask("Do you want to overwrite it?"):
            console.info("Initialization cancelled.")
            raise typer.Exit()
    
    console.banner(Banner.get_renderable(style='simple', subtitle="Configuration Setup Wizard"))
    
    console.step("Source Paths", 1)
    console.print("Enter directories containing your code. Press Enter on an empty line to finish.")
    source_paths = []
    while True:
        path = Prompt.ask("Add source path", default="", show_default=False)
        if not path: break
        source_path_obj = Path(path)
        if not source_path_obj.exists():
            console.error(f"Path does not exist: {path}")
            continue
        source_paths.append(path)
        console.success(f"Added: {path}")
    
    console.step("Target Directory", 2)
    target_dir = Prompt.ask("Where should final Obsidian notes be saved?", default="./to_obsidian")
    
    console.step("Ollama Model", 3)
    model_name = Prompt.ask("Which Ollama model should we use?", default="ministral-3:3b")
    
    config_manager.config["source_paths"] = source_paths
    config_manager.config["target_dir"] = target_dir
    config_manager.set("model_name", model_name)
    config_manager.save()
    
    console.success(f"\n✨ Configuration saved successfully to: [path]{config_manager.config_path}[/path]")
    
    summary = f"""
1. Ensure Ollama is running: [code]ollama serve[/code]
2. Pull the model: [code]ollama pull {model_name}[/code]
3. Test connection: [code]ralf-notes check-health[/code]
4. Generate docs: [code]ralf-notes generate[/code]
"""
    console.panel(summary, title="🚀 Next Steps", style="success")


# --- Single File Processors ---

def _generate_raw_single(
    context: GenerationContext,
    output_path: Path,
    generator: StructuredTextGenerator,
    quiet: bool,
    console: Console
) -> bool:
    try:
        generator.generate_and_save_raw(context, output_path)
        if not quiet:
            console.success(f"Generated Raw: {output_path.name}")
        return True
    except Exception as e:
        console.error(f"Failed to generate raw output for {context.filename}: {e}")
        return False

def _format_initial_single(
    file_path: Path,
    output_dir: Path,
    pipeline: DocumentPipeline,
    dry_run: bool,
    overwrite: bool,
    quiet: bool,
    console: Console
) -> bool:
    filename_stem = file_path.stem
    formatted_output_path = output_dir / f"{filename_stem}.md"
    formatted_output_path.parent.mkdir(parents=True, exist_ok=True)

    if formatted_output_path.exists() and not overwrite:
        if not quiet:
            console.warning(f"Skipping {formatted_output_path.name} (output already exists)")
        return True # Not a failure, just skipped

    if not quiet:
        console.file("Formatting", file_path.name)

    if dry_run:
        return True

    try:
        raw_content = file_path.read_text(encoding='utf-8')
        parsed_data = pipeline.parser.parse_or_fallback(raw_content, filename_stem)
        markdown = pipeline.formatter.format(parsed_data)

        if markdown.strip():
            formatted_output_path.write_text(markdown, encoding='utf-8')
            if not quiet:
                console.success(f"Formatted: {formatted_output_path.name}")
            return True
        else:
            console.error(f"Failed to format {formatted_output_path.name}: Empty markdown.")
            return False
    except Exception as e:
        console.error(f"Failed to format {formatted_output_path.name}: {e}")
        return False

def _finalize_single(
    file_path: Path,
    output_dir: Path,
    review_dir: Path,
    dry_run: bool,
    overwrite: bool,
    delete_source: bool,
    quiet: bool,
    console: Console
) -> bool:
    filename_stem = file_path.stem
    final_output_path = output_dir / f"{filename_stem}.md"
    review_output_path = review_dir / f"{filename_stem}.md"

    if final_output_path.exists() and not overwrite:
        if not quiet:
            console.warning(f"Skipping {final_output_path.name} (output already exists)")
        return True

    if dry_run:
        return True
        
    try:
        # Placeholder for validation
        is_valid = True 
        
        target_path = final_output_path if is_valid else review_output_path
        
        if file_path != target_path:
            shutil.copy2(file_path, target_path)
            if delete_source:
                try:
                    file_path.unlink()
                except Exception as e:
                    console.warning(f"Failed to delete source {file_path}: {e}")
        
        if not quiet:
            if is_valid:
                console.success(f"Finalized: {target_path.name}")
            else:
                console.warning(f"Review Needed: {target_path.name}")
        return True
    except Exception as e:
        console.error(f"Failed to finalize {file_path.name}: {e}")
        return False

# --- Batch Logic Wrappers ---

def _generate_raw_logic(
    source_path: Optional[Path],
    output: Optional[Path],
    quiet: bool,
    model: Optional[str],
    config_manager: ConfigManager,
    console: Console
) -> bool: # Returns True on success, False on failure
    import time
    start_time = time.time()

    source_paths_cfg = [Path(p) for p in config_manager.get("source_paths", [])]
    if source_path:
        _validate_path_exists(source_path, "source_path", console)
        _validate_path_is_dir(source_path, "source_path", console)
        source_paths = [source_path]
    else:
        if not source_paths_cfg:
            console.error("No source paths configured! Cannot generate documentation.")
            return False
        for p in source_paths_cfg:
            _validate_path_exists(p, "configured source path", console)
            _validate_path_is_dir(p, "configured source path", console)
        source_paths = source_paths_cfg

    stage1_raw_output_dir = output if output else Path(config_manager.get("stage1_raw_output_dir"))
    _validate_path_is_writable(stage1_raw_output_dir, "raw_output", console)

    if model: config_manager.set("model_name", model)

    if not quiet:
        console.info(f"Using Model: {config_manager.get('model_name')}")
        console.info(f"Raw Output Folder: {stage1_raw_output_dir}")
        for sp in source_paths: console.info(f"  - {sp}")
        console.print("")

    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        return False

    stage1_raw_output_dir.mkdir(parents=True, exist_ok=True)
    
    files_to_process = FileProcessor.get_files_to_process(
        source_paths,
        config_manager.get('file_extensions', FileProcessor.VALID_EXTENSIONS),
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )

    processed_count = 0
    failed_count = 0

    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Generating Raw Output...", total=len(files_to_process))
        for file_path in files_to_process:
            if not quiet:
                console.file("From Source", file_path.name)

            output_file_path = stage1_raw_output_dir / f"{file_path.stem}.txt"
            content = file_path.read_text(encoding='utf-8')
            context = GenerationContext(
                filename=file_path.stem,
                content=content,
                file_path=str(file_path)
            )

            success = _generate_raw_single(context, output_file_path, pipeline.generator, quiet, console)
            
            if success:
                processed_count += 1
            else:
                failed_count += 1
            progress.update(task, advance=1)
    
    duration = time.time() - start_time
    results = {
        'total': processed_count + failed_count,
        'success': processed_count,
        'failed': failed_count,
        'duration': duration,
        'files_per_second': processed_count / duration if duration > 0 else 0
    }
    show_summary(results, console, quiet)
    return failed_count == 0


def _format_initial_logic(
    path: Optional[Path],
    output: Optional[Path],
    dry_run: bool,
    overwrite: bool,
    quiet: bool,
    model: Optional[str],
    config_manager: ConfigManager,
    console: Console
) -> bool:
    import time
    start_time = time.time()

    stage1_raw_source_paths_cfg = [Path(p) for p in [config_manager.get("stage1_raw_output_dir", "./stage1_raw")]]
    if path:
        _validate_path_exists(path, "path", console)
        _validate_path_is_dir(path, "path", console)
        stage1_raw_source_paths = [path]
    else:
        stage1_raw_source_paths = stage1_raw_source_paths_cfg

    initial_formatted_dir = output if output else Path(config_manager.get("initial_formatted_dir"))
    _validate_path_is_writable(initial_formatted_dir, "formatted_output", console)

    if model: config_manager.set("model_name", model)

    if not quiet:
        console.info(f"Raw Source Folder: {stage1_raw_source_paths[0]}")
        console.info(f"Formatted Output Folder: {initial_formatted_dir}")
        console.print("")

    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        return False

    files_to_format = FileProcessor.get_files_to_process(
        stage1_raw_source_paths,
        ('.txt',),
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )

    processed_count = 0
    failed_count = 0

    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Formatting Raw Output...", total=len(files_to_format))
        for file_path in files_to_format:
            success = _format_initial_single(
                file_path, initial_formatted_dir, pipeline, dry_run, overwrite, quiet, console
            )
            if success:
                processed_count += 1
            else:
                failed_count += 1
            progress.update(task, advance=1)
    
    duration = time.time() - start_time
    results = {
        'total': processed_count + failed_count,
        'success': processed_count,
        'failed': failed_count,
        'dry_run': dry_run,
        'duration': duration,
        'files_per_second': processed_count / duration if duration > 0 else 0
    }
    show_summary(results, console, quiet)
    return failed_count == 0


def _finalize_logic(
    path: Optional[Path],
    output: Optional[Path],
    review_output: Optional[Path],
    dry_run: bool,
    overwrite: bool,
    quiet: bool,
    delete_source: bool,
    config_manager: ConfigManager,
    console: Console
) -> bool:
    import time
    start_time = time.time()

    initial_formatted_source_paths_cfg = [Path(p) for p in [config_manager.get("initial_formatted_dir", "./stage2_formatted")]]
    if path:
        _validate_path_exists(path, "path", console)
        _validate_path_is_dir(path, "path", console)
        initial_formatted_source_paths = [path]
    else:
        initial_formatted_source_paths = initial_formatted_source_paths_cfg

    final_output_dir = output if output else Path(config_manager.get("target_dir"))
    _validate_path_is_writable(final_output_dir, "final_output", console)

    review_needed_dir = review_output if review_output else Path(config_manager.get("review_needed_dir"))
    _validate_path_is_writable(review_needed_dir, "review_output", console)

    if not quiet:
        console.info(f"Source Folder: {initial_formatted_source_paths[0]}")
        console.info(f"Final Output: {final_output_dir}")
        console.info(f"Review Output: {review_needed_dir}")
        console.info(f"Mode: {'Move (Delete Source)' if delete_source else 'Copy (Keep Source)'}")
        console.print("")

    final_output_dir.mkdir(parents=True, exist_ok=True)
    review_needed_dir.mkdir(parents=True, exist_ok=True)

    files_to_finalize = FileProcessor.get_files_to_process(
        initial_formatted_source_paths,
        ('.md',),
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )

    processed_count = 0
    failed_count = 0

    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Finalizing Notes...", total=len(files_to_finalize))
        for file_path in files_to_finalize:
            if not quiet:
                console.file("Finalizing", file_path.name)
            
            success = _finalize_single(
                file_path, final_output_dir, review_needed_dir, dry_run, overwrite, delete_source, quiet, console
            )
            
            if success:
                processed_count += 1
            else:
                failed_count += 1
            progress.update(task, advance=1)
    
    duration = time.time() - start_time
    results = {
        'total': processed_count + failed_count,
        'success': processed_count,
        'failed': failed_count,
        'dry_run': dry_run,
        'duration': duration,
        'files_per_second': processed_count / duration if duration > 0 else 0
    }
    show_summary(results, console, quiet)
    return failed_count == 0

# --- Commands ---

@app.command()
def watch(
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing notes"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    interval: int = typer.Option(1, "--interval", "-i", help="Polling interval in seconds"),
    delete_source: bool = typer.Option(False, "--delete-source", help="Delete source files after finalizing."),
):
    """Watch for new raw files and process them automatically."""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    raw_dir = Path(config_manager.get("stage1_raw_output_dir"))
    formatted_dir = Path(config_manager.get("initial_formatted_dir"))
    final_dir = Path(config_manager.get("target_dir"))
    review_dir = Path(config_manager.get("review_needed_dir"))
    
    # We need a pipeline for formatting
    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline for watch mode: {e}")
        raise typer.Exit(1)

    console.info(f"Watching for new files in: {raw_dir} with interval {interval}s")

    def process_file(file_path: Path):
        console.info(f"New file detected: {file_path.name}")
        
        # Stage 2: Format
        success = _format_initial_single(
            file_path=file_path,
            output_dir=formatted_dir,
            pipeline=pipeline,
            dry_run=False,
            overwrite=overwrite,
            quiet=quiet,
            console=console
        )
        
        if success:
            # Stage 3: Finalize
            formatted_file_path = formatted_dir / f"{file_path.stem}.md"
            if formatted_file_path.exists():
                _finalize_single(
                    file_path=formatted_file_path,
                    output_dir=final_dir,
                    review_dir=review_dir,
                    dry_run=False,
                    overwrite=overwrite,
                    delete_source=delete_source,
                    quiet=quiet,
                    console=console
                )

    watcher = Watcher(raw_dir, process_file, interval=interval)
    watcher.run()


@app.command()
def generate(
    source_path: Optional[Path] = typer.Argument(None, help="Source path to process (overrides config)"),
    final_output: Optional[Path] = typer.Option(None, "--output", "-o", help="Final output directory (overrides config)"),
    raw_output: Optional[Path] = typer.Option(None, "--raw-output", help="Stage 1 raw output directory (overrides config)"),
    formatted_output: Optional[Path] = typer.Option(None, "--formatted-output", help="Stage 2 formatted output directory (overrides config)"),
    review_output: Optional[Path] = typer.Option(None, "--review-output", help="Stage 3 review needed directory (overrides config)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without writing files"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing documents"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override model name"),
    delay: Optional[float] = typer.Option(None, "--delay", help="Delay between file processing in seconds. (Overrides config)"),
    timeout: Optional[int] = typer.Option(None, "--timeout", help="Timeout for each LLM call in seconds. (Overrides config)"),
    retries: Optional[int] = typer.Option(None, "--retries", help="Number of retry attempts for LLM calls. (Overrides config)"),
    delete_source: bool = typer.Option(False, "--delete-source", help="Delete source files after finalizing (move behavior). Default is copy."),
):
    """Generate Obsidian documentation from source files (Process per file through all stages)"""
    import time
    start_time = time.time()
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    if model: config_manager.set("model_name", model)
    if delay is not None: config_manager.set("request_delay_seconds", delay)
    if timeout is not None: config_manager.set("request_timeout_seconds", timeout)
    if retries is not None: config_manager.set("retry_attempts", retries)

    console.banner(Banner.get_renderable())

    # 1. Setup Directories
    console.step("Preparing directories", 1)
    source_paths_cfg = [Path(p) for p in config_manager.get("source_paths", [])]
    if source_path:
        _validate_path_exists(source_path, "source_path", console)
        _validate_path_is_dir(source_path, "source_path", console)
        source_paths = [source_path]
    else:
        if not source_paths_cfg:
            console.error("No source paths configured! Cannot generate documentation.")
            raise typer.Exit(1)
        source_paths = source_paths_cfg

    stage1_raw_output_dir = raw_output if raw_output else Path(config_manager.get("stage1_raw_output_dir"))
    initial_formatted_dir = formatted_output if formatted_output else Path(config_manager.get("initial_formatted_dir"))
    final_output_dir = final_output if final_output else Path(config_manager.get("target_dir"))
    review_needed_dir = review_output if review_output else Path(config_manager.get("review_needed_dir"))

    for d in [stage1_raw_output_dir, initial_formatted_dir, final_output_dir, review_needed_dir]:
        d.mkdir(parents=True, exist_ok=True)
        _validate_path_is_writable(d, f"Output Dir {d}", console)
    
    console.substep(f"Target: [path]{final_output_dir}[/path]")

    # 2. Initialize Pipeline
    console.step("Initializing AI pipeline", 2)
    with console.status("Loading configuration and connecting to Ollama..."):
        try:
            pipeline = build_pipeline(config_manager)
        except Exception as e:
            console.error(f"Failed to initialize pipeline: {e}")
            raise typer.Exit(1)

    # 3. Get Files
    console.step("Scanning source files", 3)
    files_to_process = FileProcessor.get_files_to_process(
        source_paths,
        config_manager.get('file_extensions', FileProcessor.VALID_EXTENSIONS),
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )
    console.substep(f"Found [highlight]{len(files_to_process)}[/highlight] files to process")

    processed_count = 0
    failed_count = 0

    # 4. Process Loop with Live Dashboard
    console.step("Processing files", 4)
    with ProgressManager(console) as progress:
        task = progress.add_task("Generating Docs", total=len(files_to_process))
        
        # Start Live Dashboard
        dashboard_model = config_manager.get('model_name')
        dashboard_target = str(final_output_dir)
        
        with Live(get_dashboard(model=dashboard_model, target=dashboard_target), console=console.console, refresh_per_second=4) as live:
            for i, file_path in enumerate(files_to_process):
                current_file = file_path.name
                pct = (i / len(files_to_process)) * 100
                live.update(get_dashboard(
                    model=dashboard_model, 
                    target=dashboard_target, 
                    status="Processing", 
                    progress=pct,
                    current_file=current_file
                ))
                
                # Stage 1: Generate Raw
                raw_file_path = stage1_raw_output_dir / f"{file_path.stem}.txt"
                
                run_stage_1 = True
                if raw_file_path.exists() and not overwrite:
                    run_stage_1 = False
                
                if run_stage_1:
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        context = GenerationContext(
                            filename=file_path.stem,
                            content=content,
                            file_path=str(file_path)
                        )
                        
                        if not _generate_raw_single(context, raw_file_path, pipeline.generator, True, console):
                            failed_count += 1
                            progress.update(task, advance=1)
                            continue
                    except Exception as e:
                        logger.error(f"Error reading {file_path}: {e}")
                        failed_count += 1
                        progress.update(task, advance=1)
                        continue

                # Stage 2: Format
                if not _format_initial_single(raw_file_path, initial_formatted_dir, pipeline, dry_run, overwrite, True, console):
                    failed_count += 1
                    progress.update(task, advance=1)
                    continue
                
                # Extract tags for the unique list
                try:
                    raw_content = raw_file_path.read_text(encoding='utf-8')
                    parsed_tags = pipeline.parser._parse_tags(pipeline.parser._split_into_sections(raw_content).get("TAGS", ""))
                    for tag in parsed_tags:
                        pipeline.unique_tags.add(tag)
                except:
                    pass

                # Stage 3: Finalize
                formatted_file_path = initial_formatted_dir / f"{file_path.stem}.md"
                if not _finalize_single(formatted_file_path, final_output_dir, review_needed_dir, dry_run, overwrite, delete_source, True, console):
                    failed_count += 1
                    progress.update(task, advance=1)
                    continue
                
                processed_count += 1
                progress.update(task, advance=1)
            
            # Final Dashboard update
            live.update(get_dashboard(
                model=dashboard_model, 
                target=dashboard_target, 
                status="Finished", 
                progress=100.0,
                current_file="All files processed"
            ))

    duration = time.time() - start_time
    results = {
        'total': len(files_to_process),
        'success': processed_count,
        'failed': failed_count,
        'dry_run': dry_run,
        'duration': duration,
        'files_per_second': processed_count / duration if duration > 0 else 0
    }
    
    # Save unique tags list
    if pipeline.unique_tags:
        tags_file = final_output_dir / "unique_tags.txt"
        tags_file.write_text("\n".join(sorted(list(pipeline.unique_tags))), encoding='utf-8')
        if not quiet:
            console.print(f"\n✨ [bold]Unique tags saved to:[/bold] [path]{tags_file}[/path]")

    show_summary(results, console, quiet)


@app.command(name="generate-raw")
def generate_raw(
    path: Optional[Path] = typer.Argument(None, help="Source path to process (overrides config)"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output directory for raw LLM responses (overrides config)"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override model name"),
):
    """Generate raw LLM responses from source files (Stage 1)"""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()
    
    if not _generate_raw_logic(
        source_path=path,
        output=output,
        quiet=quiet,
        model=model,
        config_manager=config_manager,
        console=console
    ):
        raise typer.Exit(1)


@app.command(name="format-initial")
def format_initial(
    path: Optional[Path] = typer.Argument(None, help="Raw output path to process (overrides config)"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output directory for formatted notes (overrides config)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without writing files"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing notes"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override model name"), # Model needed for pipeline initialization
):
    """Format raw LLM responses into Obsidian notes (Stage 2)"""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    if not _format_initial_logic(
        path=path,
        output=output,
        dry_run=dry_run,
        overwrite=overwrite,
        quiet=quiet,
        model=model,
        config_manager=config_manager,
        console=console
    ):
        raise typer.Exit(1)


@app.command(name="finalize")
def finalize(
    path: Optional[Path] = typer.Argument(None, help="Initial formatted notes path to finalize (overrides config)"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Final output directory (overrides config)"),
    review_output: Optional[Path] = typer.Option(None, "--review-output", help="Directory for files needing review (overrides config)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without writing files or moving files"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing files in final output"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    delete_source: bool = typer.Option(False, "--delete-source", help="Delete source files after finalizing (move behavior). Default is copy."),
):
    """Finalize formatted notes by validating and moving to final destinations (Stage 3)"""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    if not _finalize_logic(
        path=path,
        output=output,
        review_output=review_output,
        dry_run=dry_run,
        overwrite=overwrite,
        quiet=quiet,
        delete_source=delete_source,
        config_manager=config_manager,
        console=console
    ):
        raise typer.Exit(1)


@app.command()
def check_health():
    """
    Checks the health of the RALF Note system, including Ollama connection and model availability.
    """
    console = Console()
    config_manager = ConfigManager()

    console.banner(Banner.get_renderable(style='simple', subtitle="System Health Check"))

    ollama_host = config_manager.get("ollama_host")
    model_name = config_manager.get("model_name")

    console.step(f"Connecting to Ollama at [path]{ollama_host}[/path]", 1)
    try:
        with console.status("Pinging Ollama..."):
            client = Client(host=ollama_host)
            client.list() # Attempt to list models to verify connection
        console.success(f"Successfully connected to Ollama at {ollama_host}")
    except Exception as e:
        console.error(f"Failed to connect to Ollama at {ollama_host}.")
        console.info(f"Please ensure Ollama is running and accessible at this address.")
        console.info(f"Error details: {e}")
        raise typer.Exit(1)

    console.step(f"Checking model availability: [highlight]{model_name}[/highlight]", 2)
    try:
        with console.status(f"Looking for {model_name}..."):
            client.show(model_name)
        console.success(f"Model '{model_name}' is available and ready for use.")
    except Exception as e:
        console.error(f"Model '{model_name}' is not available on your Ollama instance.")
        console.info(f"Please pull the model using: [code]ollama pull {model_name}[/code]")
        console.info(f"Error details: {e}")
        raise typer.Exit(1)

    console.rule("Result", style="green")
    console.success("RALF Note health check passed! Your system is ready. 🚀")


# --- Tuning System Helpers ---

def estimate_throughput(config: OptimizedConfig) -> float:
    """Estimate throughput in files/minute based on optimized settings."""
    # Base throughput from delay
    if config.request_delay_seconds > 0:
        base_fps = 1.0 / config.request_delay_seconds
    else:
        # If no delay, limited by timeout or processing time (assume 5s per file avg optimized)
        base_fps = 1.0 / 5.0
        
    # Scale by parallelism
    fps = base_fps * config.max_concurrent_requests
    
    return fps * 60 # per minute

def save_optimized_config(config_manager: ConfigManager, config: OptimizedConfig):
    """Save the optimized configuration to the config file."""
    # Model Settings
    config_manager.set("model_name", config.model_name)
    config_manager.set("num_ctx", config.num_ctx)
    config_manager.set("temperature", config.temperature)
    config_manager.set("chunk_size", config.chunk_size)
    config_manager.set("max_content_length", config.max_content_length)
    config_manager.set("max_chunk_summary_length", config.max_chunk_summary_length)

    # Performance Settings
    config_manager.set("request_delay_seconds", config.request_delay_seconds)
    config_manager.set("max_concurrent_requests", config.max_concurrent_requests)
    config_manager.set("retry_attempts", config.retry_attempts)
    config_manager.set("initial_backoff_seconds", config.initial_backoff_seconds)
    config_manager.set("backoff_multiplier", config.backoff_multiplier)
    config_manager.set("request_timeout_seconds", config.request_timeout_seconds)

    # Batch Settings
    config_manager.set("batch_size", config.batch_size)
    config_manager.set("batch_delay_seconds", config.batch_delay_seconds)
    
    config_manager.save()

def display_tuning_report(console: Console, config: OptimizedConfig):
    """Display comprehensive tuning report."""

    # System Profile
    console.panel(
        f"""CPU: {config.system_profile.cpu_cores} cores / {config.system_profile.cpu_threads} threads\nRAM: {config.system_profile.available_ram_gb:.1f} GB available / {config.system_profile.total_ram_gb:.1f} GB total\nGPU: {"Yes" if config.system_profile.has_gpu else "No"}\nOllama: {config.system_profile.ollama_version} @ {config.system_profile.ollama_host}""",
        title="💻 System Profile",
        style="cyan"
    )

    console.print("")

    # Optimized Settings
    console.panel(
        f"""Model: {config.model_name}\nContext Size: {config.num_ctx}\nChunk Size: {config.chunk_size}\nTemperature: {config.temperature}\nMax Content Length: {config.max_content_length}""",
        title="🤖 Model Settings",
        style="green"
    )

    console.print("")

    console.panel(
        f"""Parallel Requests: {config.max_concurrent_requests}\nRequest Delay: {config.request_delay_seconds}s\nTimeout: {config.request_timeout_seconds}s\nRetry Attempts: {config.retry_attempts}\nBackoff: {config.initial_backoff_seconds}s × {config.backoff_multiplier}""",
        title="⚡ Performance Settings",
        style="magenta"
    )

    console.print("")

    console.panel(
        f"""Batch Size: {config.batch_size} files\nBatch Delay: {config.batch_delay_seconds}s\nEstimated Throughput: {estimate_throughput(config):.2f} files/min""",
        title="📦 Batch Settings",
        style="yellow"
    )

    console.print("")
    console.info(f"Confidence Score: [bold green]{config.confidence_score:.1f}%[/bold green]")
    console.info(f"Benchmarked: {config.benchmark_date}")

@app.command(name="fine-tune")
def fine_tune(
    quick: bool = typer.Option(
        False,
        "--quick",
        help="Quick tune (fewer tests, faster)"
    ),
    full: bool = typer.Option(
        False,
        "--full",
        help="Full comprehensive tuning (more tests, slower)"
    ),
    save: bool = typer.Option(
        True,
        "--save/--no-save",
        help="Save results to config file"
    ),
    report: bool = typer.Option(
        True,
        "--report/--no-report",
        help="Show detailed report"
    )
):
    """
    Automatically tune RALF Note for optimal performance on this system.
    """
    console = Console()
    config_manager = ConfigManager()

    console.banner(Banner.get_renderable(style='full', subtitle="Auto-Tuning System"))

    # Initialize components
    system_profiler = SystemProfiler()
    sample_generator = SampleCodeGenerator()

    client = Client(host=config_manager.get("ollama_host"))

    model_benchmarker = ModelBenchmarker(client, sample_generator)
    latency_benchmarker = LatencyBenchmarker(client, sample_generator)
    throughput_benchmarker = ThroughputBenchmarker(client, sample_generator)
    config_builder = OptimizedConfigBuilder()

    orchestrator = BenchmarkOrchestrator(
        config_manager=config_manager,
        system_profiler=system_profiler,
        model_benchmarker=model_benchmarker,
        latency_benchmarker=latency_benchmarker,
        throughput_benchmarker=throughput_benchmarker,
        optimized_config_builder=config_builder,
        console=console
    )

    # Set benchmark intensity
    if quick:
        benchmark_config = BenchmarkConfig(intensity="quick")
    elif full:
        benchmark_config = BenchmarkConfig(intensity="full")
    else:
        benchmark_config = BenchmarkConfig(intensity="normal")

    # Run benchmarks
    try:
        console.step(f"Starting benchmarks (Intensity: [highlight]{benchmark_config.intensity}[/highlight])", 1)
        optimized = orchestrator.run_full_benchmark(benchmark_config)

        console.rule("Tuning Complete", style="green")

        # Show report
        if report:
            display_tuning_report(console, optimized)

        # Save to config
        if save:
            console.print("")
            if Confirm.ask("Save optimized settings to configuration?"):
                save_optimized_config(config_manager, optimized)
                console.success("Configuration updated successfully!")
            else:
                console.info("Optimization results discarded.")

    except Exception as e:
        console.error(f"Tuning failed: {e}")
        raise typer.Exit(1)


tags_app = typer.Typer(
    name="tags",
    help="🏷️ Commands for managing and refining document tags."
)
app.add_typer(tags_app, name="tags")

@tags_app.callback(invoke_without_command=True)
def _tags_default_welcome(ctx: typer.Context):
    """
    Displays welcome message and basic instructions for tags commands if no subcommand is given.
    """
    if ctx.invoked_subcommand is None:
        console = Console()
        console.info("Welcome to RALF Note Tag Management!")
        console.print("")
        console.print("[bold]To manage tags:[/bold]")
        console.print("  1. Run [bold green]ralf-notes tags analyze[/bold green] to generate a refinement guide.")
        console.print("  2. Review the generated guide (e.g., [green]tag_refinement_guide.json[/green]).")
        console.print("  3. Run [bold green]ralf-notes tags apply[/bold green] to apply the refinements.")
        console.print("  4. Use [bold green]ralf-notes tags stats[/bold green] to view current tag statistics.")
        console.print("")
        console.print("For more information, run [bold green]ralf-notes tags --help[/bold green].")
        raise typer.Exit()


@tags_app.command("analyze")
def tags_analyze(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory containing markdown files (overrides config)."),
    output: Path = typer.Option("tag_refinement_guide.json", "--output", "-o", help="Output JSON file for the refinement guide."),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override LLM model name for tag refinement."),
    max_tags: int = typer.Option(100, "--max-tags", help="Maximum number of tags to send to LLM for refinement."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Analyzes existing tags and generates a refinement guide using an LLM.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()
    
    console.banner(Banner.get_renderable(style='simple', subtitle="Tag Analysis System"))

    if target_dir:
        _validate_path_exists(target_dir, "target_dir", console)
        _validate_path_is_dir(target_dir, "target_dir", console)
    else:
        target_dir = Path(config_manager.get("target_dir"))
        _validate_path_exists(target_dir, "configured target_dir", console)
        _validate_path_is_dir(target_dir, "configured target_dir", console)
    
    _validate_path_is_writable(output.parent, "output directory", console)

    if model:
        try:
            config_manager.set("model_name", model)
        except ValueError as e:
            console.error(f"Invalid model name '{model}': {e}. Please ensure it's a valid Ollama model.")
            raise typer.Exit(1)

    console.step(f"Scanning markdown files in [path]{target_dir}[/path]", 1)
    
    collector = TagCollector()
    with console.status("Collecting tags..."):
        tag_data = collector.collect_tags(target_dir)

    console.success(f"Collected {tag_data['total_unique_tags']} unique tags from {tag_data['total_files']} files.")
    
    console.step("Analyzing tag patterns", 2)
    analyzer = TagAnalyzer()
    analysis_report = analyzer.analyze(tag_data)
    
    console.info(f"Identified {analysis_report['total_patterns']} potential tag patterns.")

    console.step("Generating refinement suggestions", 3)
    llm_client = Client(host=config_manager.get("ollama_host"))
    llm_refiner = TagRefinementLLM(llm_client, model=config_manager.get("model_name"))

    with console.status("Requesting LLM analysis (this may take a moment)..."):
        llm_suggestions = llm_refiner.generate_refinements(analysis_report)
    
    guide_builder = RefinementGuideBuilder()
    final_guide = guide_builder.build_guide(llm_suggestions, analysis_report, output)

    if final_guide.get('llm_error'):
        console.error(f"LLM encountered an error during refinement suggestion: {final_guide['llm_error']}")
        console.info("The guide was still generated but may be incomplete or contain errors.")
    
    console.success(f"Tag refinement guide generated successfully: [path]{output}[/path]")
    console.panel("Please review the guide JSON file before applying changes.", title="Next Step", style="warning")

@tags_app.command("apply")
def tags_apply(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory containing markdown files (overrides config)."),
    guide: Path = typer.Option(Path("tag_refinement_guide.json"), "--guide", "-g", help="Path to the tag refinement guide JSON file."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without writing to files."),
    no_backup: bool = typer.Option(False, "--no-backup", help="Do NOT create a backup before applying changes."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Applies tag refinements to markdown files based on a generated guide.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    console.banner(Banner.get_renderable(style='simple', subtitle="Tag Refinement Applicator"))

    if target_dir:
        _validate_path_exists(target_dir, "target_dir", console)
        _validate_path_is_dir(target_dir, "target_dir", console)
    else:
        target_dir = Path(config_manager.get("target_dir"))
        _validate_path_exists(target_dir, "configured target_dir", console)
        _validate_path_is_dir(target_dir, "configured target_dir", console)

    if not guide.exists():
        console.error(f"Guide file not found: {guide}")
        console.info("Please run 'ralf-notes tags analyze' first to generate a guide, or specify one with --guide.")
        raise typer.Exit(1)

    try:
        guide_content = guide.read_text(encoding='utf-8')
        refinement_guide = json.loads(guide_content)
    except Exception as e:
        console.error(f"Failed to load or parse refinement guide from '{guide}': {e}")
        raise typer.Exit(1)

    console.step(f"Applying refinements to [path]{target_dir}[/path]", 1)

    replacer = TagReplacer(refinement_guide)
    with console.status("Processing files..."):
        results = replacer.apply_refinements(target_dir, dry_run=dry_run, backup=not no_backup)

    if results.get('backup_path'):
        console.info(f"Backup created at: [path]{results['backup_path']}[/path]")

    summary = f"""
Files Processed: {results['files_processed']}
Files Modified: {results['files_modified']}
Tags Replaced/Deleted: {results['tags_replaced']}
"""
    console.panel(summary, title="📊 Result Summary", style="success")
    
    if dry_run:
        console.warning("This was a DRY RUN. No files were actually modified.")

    if results['errors']:
        console.error(f"Errors encountered during application for {len(results['errors'])} files.")
        for error_info in results['errors']:
            console.error(f"  File: {error_info['file']}, Error: {error_info['error']}")
        raise typer.Exit(1)
    
    console.success("Tag refinement application complete.")


@tags_app.command("stats")
def tags_stats(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory containing markdown files (overrides config)."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Displays statistics about tags found in markdown files.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    if target_dir:
        _validate_path_exists(target_dir, "target_dir", console)
        _validate_path_is_dir(target_dir, "target_dir", console)
    else:
        target_dir = Path(config_manager.get("target_dir"))
        _validate_path_exists(target_dir, "configured target_dir", console)
        _validate_path_is_dir(target_dir, "configured target_dir", console)

    console.info(f"Collecting tag statistics from '{target_dir}'...")
    
    collector = TagCollector()
    with console.status("Analyzing tags..."):
        tag_data = collector.collect_tags(target_dir)

    tag_frequency = tag_data['tag_frequency']
    total_files = tag_data['total_files']
    total_unique_tags = tag_data['total_unique_tags']

    console.print(f"\n📊 [bold]Tag Statistics for[/bold] [path]{target_dir}[/path]")
    stats = {
        "Total files analyzed": total_files,
        "Total unique tags found": total_unique_tags
    }
    console.table_from_dict(stats, title="General Stats")

    if tag_frequency:
        sorted_tags = sorted(tag_frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Frequency table
        freq_table = Table(title="Top 10 Most Frequent Tags")
        freq_table.add_column("Tag", style="cyan")
        freq_table.add_column("Uses", justify="right", style="green")
        
        for tag, count in sorted_tags[:10]:
            freq_table.add_row(tag, str(count))
        
        console.print(freq_table)
    else:
        console.info("No tags found in the specified directory.")


# --- Links Management ---

links_app = typer.Typer(
    name="links",
    help="🔗 Commands for managing and fixing document wikilinks."
)
app.add_typer(links_app, name="links")

@links_app.command("analyze")
def links_analyze(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory containing markdown files (overrides config)."),
    output: Path = typer.Option("link_refinement_guide.json", "--output", "-o", help="Output JSON file for the refinement guide."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Analyzes wikilinks and generates a refinement guide.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()
    
    console.banner(Banner.get_renderable(style='simple', subtitle="Link Analysis System"))

    if not target_dir:
        target_dir = Path(config_manager.get("target_dir"))
    
    _validate_path_exists(target_dir, "target_dir", console)
    _validate_path_is_dir(target_dir, "target_dir", console)

    console.step(f"Analyzing links in [path]{target_dir}[/path]", 1)
    
    collector = LinkCollector()
    with console.status("Collecting links..."):
        link_data = collector.collect_links(target_dir)
    
    resolver = LinkResolver()
    with console.status("Resolving references..."):
        analysis_report = resolver.resolve_links(link_data)
    
    console.success(f"Found {link_data['total_links']} links across {link_data['total_files']} files.")
    console.info(f"Identified {analysis_report['broken_count']} broken links and {analysis_report['none_count']} 'none' links.")
    console.info(f"Identified {len(analysis_report['orphans'])} orphan files.")

    # Save guide
    try:
        output.write_text(json.dumps(analysis_report, indent=2), encoding='utf-8')
        console.success(f"Link refinement guide generated: [path]{output}[/path]")
    except Exception as e:
        console.error(f"Failed to save guide: {e}")

@links_app.command("apply")
def links_apply(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory containing markdown files (overrides config)."),
    guide: Path = typer.Option(Path("link_refinement_guide.json"), "--guide", "-g", help="Path to the link refinement guide JSON file."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without writing to files."),
    no_backup: bool = typer.Option(False, "--no-backup", help="Do NOT create a backup before applying changes."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Applies link refinements to markdown files.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    console.banner(Banner.get_renderable(style='simple', subtitle="Link Refinement Applicator"))

    if not target_dir:
        target_dir = Path(config_manager.get("target_dir"))
    
    _validate_path_exists(target_dir, "target_dir", console)
    
    if not guide.exists():
        console.error(f"Guide file not found: {guide}")
        raise typer.Exit(1)

    try:
        refinement_guide = json.loads(guide.read_text(encoding='utf-8'))
    except Exception as e:
        console.error(f"Failed to parse guide: {e}")
        raise typer.Exit(1)

    console.step(f"Applying refinements to [path]{target_dir}[/path]", 1)

    refiner = LinkRefiner(refinement_guide)
    with console.status("Updating wikilinks..."):
        results = refiner.apply_fixes(target_dir, dry_run=dry_run, backup=not no_backup)

    console.success("Link refinement summary:")
    console.print(f"  Files processed: {results['files_processed']}")
    console.print(f"  Files modified: {results['files_modified']}")
    console.print(f"  Links fixed/removed: {results['links_fixed']}")
    
    if not dry_run:
        console.success(f"Applied Link Schema saved to: [path]{target_dir}/applied_links.md[/path]")

# --- Organization ---

@app.command()
def organize(
    target_dir: Optional[Path] = typer.Argument(None, help="Directory to organize (overrides config)."),
    strategy: str = typer.Option("flat", help="Organization strategy: flat, type, or tag."),
    clean_names: bool = typer.Option(True, "--clean-names/--no-clean-names", help="Remove numeric prefixes from filenames."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without moving files."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output."),
):
    """
    Organize markdown files into folders and clean up filenames.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    console.banner(Banner.get_renderable(style='simple', subtitle="File Organization System"))

    if not target_dir:
        target_dir = Path(config_manager.get("target_dir"))
    
    _validate_path_exists(target_dir, "target_dir", console)
    _validate_path_is_dir(target_dir, "target_dir", console)

    console.step(f"Organizing files in [path]{target_dir}[/path]", 1)
    console.substep(f"Strategy: [highlight]{strategy}[/highlight]")
    console.substep(f"Clean Names: [highlight]{'Yes' if clean_names else 'No'}[/highlight]")

    mover = FileMover()
    with console.status("Reorganizing files..."):
        results = mover.organize_directory(
            directory=target_dir,
            strategy=strategy,
            clean_names=clean_names,
            dry_run=dry_run
        )

    console.success("Organization summary:")
    console.print(f"  Files processed: {results['processed']}")
    console.print(f"  Files moved/renamed: {results['moved']}")
    
    if results['errors']:
        console.warning(f"Encountered {len(results['errors'])} errors during organization.")

if __name__ == "__main__":
    app()