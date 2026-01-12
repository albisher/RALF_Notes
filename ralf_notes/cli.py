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
from .tui import Console, ProgressManager, get_banner, get_banner_with_status
from .tuning.models import BenchmarkConfig, OptimizedConfig, SystemProfile
from .tuning.orchestrator import BenchmarkOrchestrator
from .tuning.system_profiler import SystemProfiler
from .tuning.model_benchmarker import ModelBenchmarker
from .tuning.latency_benchmarker import LatencyBenchmarker
from .tuning.throughput_benchmarker import ThroughputBenchmarker
from .tuning.sample_generator import SampleCodeGenerator
from .tuning.config_builder import OptimizedConfigBuilder


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


app = typer.Typer(
    name="ralf-notes",
    help="🚀 RALF Note v2.0 - AI-Powered Obsidian Documentation Generator",
    add_completion=True
)

def version_callback(value: bool):
    if value:
        console = Console()
        console.banner(get_banner('simple'))
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
    pass

def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    """Build the document generation pipeline."""
    client = Client(host=config_manager.get("ollama_host"))
    gen_config = StructuredTextGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature"),
        chunk_size=config_manager.get("chunk_size"),
        max_content_length=config_manager.get("max_content_length"),  # ADD
        max_chunk_summary_length=config_manager.get("max_chunk_summary_length"),  # ADD
        ollama_host=config_manager.get("ollama_host")
    )
    generator = StructuredTextGenerator(client, gen_config)
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
        console.banner(get_banner('full'))
        console.print("")
        console.info("Welcome to RALF Note - AI-Powered Obsidian Documentation Generator!")
        console.print("")
        console.print("[bold]To get started:[/bold]")
        console.print("  1. Run [bold green]ralf-notes init[/bold green] to set up your configuration.")
        console.print("     (This will guide you through setting source paths, target directory, and Ollama model.)")
        console.print("  2. Run [bold green]ralf-notes generate-raw[/bold green] to generate raw documentation (Stage 1).")
        console.print("  3. Run [bold green]ralf-notes format-initial[/bold green] to format raw documentation (Stage 2).")
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
            if typer.confirm("Reset configuration to defaults?"):
                config_manager.reset_to_defaults()
                config_manager.save()
                console.success("Configuration reset to defaults")
            else:
                console.info("Reset cancelled.")
        if add_source:
            if not Path(add_source).exists():
                console.error(f"Path does not exist: {add_source}")
                raise typer.Exit(1)
            config_manager.add_source_path(add_source)
            config_manager.save()
            console.success(f"Added source path: {add_source}")
        if remove_source:
            config_manager.remove_source_path(remove_source)
            config_manager.save()
            console.success(f"Removed source path: {remove_source}")
        if set_target:
            config_manager.set_target_dir(set_target)
            config_manager.save()
            console.success(f"Target directory set to: {set_target}")
        if set_stage1_raw_output:
            config_manager.set_stage1_raw_output_dir(set_stage1_raw_output)
            config_manager.save()
            console.success(f"Stage 1 raw output directory set to: {set_stage1_raw_output}")
        if set_initial_formatted:
            config_manager.set_initial_formatted_dir(set_initial_formatted)
            config_manager.save()
            console.success(f"Initial formatted output directory set to: {set_initial_formatted}")
        if set_review_needed:
            config_manager.set_review_needed_dir(set_review_needed)
            config_manager.save()
            console.success(f"Review needed directory set to: {set_review_needed}")
        
        if show:
            display_config_table(console, config_manager)
        return

    if config_manager.config_path.exists():
        console.warning(f"Configuration already exists at: {config_manager.config_path}")
        display_config_table(console, config_manager)
        if not typer.confirm("Do you want to overwrite it?"):
            console.info("Initialization cancelled.")
            raise typer.Exit()
    
    console.banner(get_banner('simple'))
    console.print("\nSetting up RALF Note configuration...")
    source_paths = []
    while True:
        path = typer.prompt("Source path (leave empty to finish)", default="", show_default=False)
        if not path: break
        if Path(path).exists():
            source_paths.append(path)
            console.success(f"Added: {path}")
        else:
            console.warning(f"Path does not exist: {path}")
    
    target_dir = typer.prompt("Target directory for final Obsidian notes", default="./to_obsidian")
    stage1_raw_output_dir = typer.prompt("Stage 1 raw output directory", default="./stage1_raw")
    initial_formatted_dir = typer.prompt("Stage 2 initial formatted directory", default="./stage2_formatted")
    review_needed_dir = typer.prompt("Stage 3 review needed directory", default="./review_needed")
    model_name = typer.prompt("Ollama model name", default="ministral-3:3b")
    
    config_manager.config["source_paths"] = source_paths
    config_manager.config["target_dir"] = target_dir
    config_manager.config["stage1_raw_output_dir"] = stage1_raw_output_dir
    config_manager.config["initial_formatted_dir"] = initial_formatted_dir
    config_manager.config["review_needed_dir"] = review_needed_dir
    config_manager.config["model_name"] = model_name
    config_manager.save()
    
    console.success(f"\nConfiguration saved to: {config_manager.config_path}")
    console.info("\nNext steps:\n  1. Ensure Ollama is running: ollama serve\n  2. Pull the model: ollama pull {model_name}\n  3. Test connection: ralf-notes check-health\n  4. Generate docs: ralf-notes generate\n")

def _generate_raw_logic(
    source_path: Optional[Path],
    output: Optional[Path],
    quiet: bool,
    model: Optional[str],
    config_manager: ConfigManager,
    console: Console
) -> bool: # Returns True on success, False on failure
    source_paths = [source_path] if source_path else [Path(p) for p in config_manager.get("source_paths", [])]
    if not source_paths:
        console.error("No source paths configured!")
        console.info("Run 'ralf-notes init' to set up configuration")
        return False

    stage1_raw_output_dir = output if output else Path(config_manager.get("stage1_raw_output_dir"))
    if model: config_manager.set_model(model)

    if not quiet:
        console.info(f"Model: {config_manager.get('model_name')}")
        console.info(f"Raw output folder: {stage1_raw_output_dir}")
        console.info("Source folders:")
        for sp in source_paths: console.info(f"  - {sp}")
        console.print("")

    try:
        client = Client(host=config_manager.get("ollama_host"))
        gen_config = StructuredTextGeneratorConfig(
            model_name=config_manager.get("model_name"),
            num_ctx=config_manager.get("num_ctx"),
            temperature=config_manager.get("temperature"),
            chunk_size=config_manager.get("chunk_size"),
            max_content_length=config_manager.get("max_content_length"),
            max_chunk_summary_length=config_manager.get("max_chunk_summary_length"),
            ollama_host=config_manager.get("ollama_host")
        )
        generator = StructuredTextGenerator(client, gen_config)
    except Exception as e:
        console.error(f"Failed to initialize generator: {e}")
        return False

    stage1_raw_output_dir.mkdir(parents=True, exist_ok=True)
    processed_count = 0
    failed_count = 0
    
    valid_extensions_for_stage1 = config_manager.get('file_extensions', FileProcessor.VALID_EXTENSIONS)
    skip_dirs_for_stage1 = config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS)
    skip_files_for_stage1 = config_manager.get('skip_files', FileProcessor.SKIP_FILES)

    files_to_process = FileProcessor.get_files_to_process(
        source_paths,
        valid_extensions_for_stage1,
        skip_dirs_for_stage1,
        skip_files_for_stage1
    )


    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Generating Raw Output...", total=len(files_to_process))
        for file_path in files_to_process:
            filename_stem = file_path.stem
            output_file_path = stage1_raw_output_dir / f"{filename_stem}.txt"

            if not quiet:
                console.file("From Source", file_path.name)

            try:
                content = file_path.read_text(encoding='utf-8')
                context = GenerationContext(
                    filename=filename_stem,
                    content=content,
                    file_path=str(file_path)
                )
                generator.generate_and_save_raw(context, output_file_path)
                processed_count += 1
                if not quiet:
                    console.success(f"Generated Raw: {output_file_path.name}")
            except Exception as e:
                console.error(f"Failed to generate raw output for {file_path.name}: {e}")
                failed_count += 1
            progress.update(task, advance=1)
    
    results = {
        'total': processed_count + failed_count,
        'success': processed_count,
        'failed': failed_count,
        'dry_run': False,
        'duration': 0,
        'files_per_second': 0
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
) -> bool: # Returns True on success, False on failure
    stage1_raw_source_paths = [path] if path else [Path(p) for p in [config_manager.get("stage1_raw_output_dir", "./stage1_raw")]]
    if not stage1_raw_source_paths:
        console.error("No raw output paths configured!")
        console.info("Run 'ralf-notes init' to set up configuration or specify --path")
        return False

    initial_formatted_dir = output if output else Path(config_manager.get("initial_formatted_dir"))
    if model: config_manager.set_model(model)

    if not quiet:
        console.info(f"Model: {config_manager.get('model_name')} (for pipeline setup)")
        console.info(f"Raw source folder: {stage1_raw_source_paths[0]}")
        console.info(f"Formatted output folder: {initial_formatted_dir}")
        console.print("")

    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        return False

    processor = FileProcessor(pipeline, config_manager)
    initial_formatted_dir.mkdir(parents=True, exist_ok=True)

    files_to_format = FileProcessor.get_files_to_process(
        stage1_raw_source_paths,
        ('.txt',),
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )

    processed_count = 0
    failed_count = 0
    skipped_count = 0

    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Formatting Raw Output...", total=len(files_to_format))
        for file_path in files_to_format:
            filename_stem = file_path.stem
            formatted_output_path = initial_formatted_dir / f"{filename_stem}.md"
            formatted_output_path.parent.mkdir(parents=True, exist_ok=True)

            if formatted_output_path.exists() and not overwrite:
                if not quiet:
                    console.warning(f"Skipping {formatted_output_path.name} (output already exists. Use --overwrite to replace.)")
                skipped_count += 1
                progress.update(task, advance=1)
                continue
            
            if not quiet:
                console.file("Formatting", file_path.name)

            if not dry_run:
                try:
                    raw_content = file_path.read_text(encoding='utf-8')
                    parsed_data = pipeline.parser.parse_or_fallback(raw_content, filename_stem)
                    markdown = pipeline.formatter.format(parsed_data)

                    if markdown.strip():
                        formatted_output_path.write_text(markdown, encoding='utf-8')
                        processed_count += 1
                        if not quiet:
                            console.success(f"Formatted: {formatted_output_path.name}")
                    else:
                        failed_count += 1
                        console.error(f"Failed to format {formatted_output_path.name}: Empty markdown generated.")
                except Exception as e:
                    failed_count += 1
                    console.error(f"Failed to format {formatted_output_path.name}: {e}")
            else:
                processed_count += 1

            progress.update(task, advance=1)
    
    results = {
        'total': processed_count + failed_count + skipped_count,
        'success': processed_count,
        'failed': failed_count,
        'skipped': skipped_count,
        'dry_run': dry_run
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
    config_manager: ConfigManager,
    console: Console
) -> bool:
    initial_formatted_source_paths = [path] if path else [Path(p) for p in [config_manager.get("initial_formatted_dir", "./stage2_formatted")]]
    if not initial_formatted_source_paths:
        console.error("No initial formatted paths configured!")
        console.info("Run 'ralf-notes init' to set up configuration or specify --path")
        return False

    final_output_dir = output if output else Path(config_manager.get("target_dir"))
    review_needed_dir = review_output if review_output else Path(config_manager.get("review_needed_dir"))

    if not quiet:
        console.info(f"Initial formatted source folder: {initial_formatted_source_paths[0]}")
        console.info(f"Final output folder: {final_output_dir}")
        console.info(f"Review needed folder: {review_needed_dir}")
        console.print("")

    final_output_dir.mkdir(parents=True, exist_ok=True)
    review_needed_dir.mkdir(parents=True, exist_ok=True)

    files_to_finalize = FileProcessor.get_files_to_process(
        initial_formatted_source_paths,
        ('.md',), # Finalize operates on .md files
        config_manager.get('skip_dirs', FileProcessor.SKIP_DIRS),
        config_manager.get('skip_files', FileProcessor.SKIP_FILES)
    )

    processed_count = 0
    failed_count = 0
    skipped_count = 0

    with ProgressManager(console) as progress:
        task = progress.add_task("[cyan]Finalizing Notes...", total=len(files_to_finalize))
        for file_path in files_to_finalize:
            if not quiet:
                console.file("Finalizing", file_path.name)

            try:
                filename_stem = file_path.stem
                final_output_path = final_output_dir / f"{filename_stem}.md"
                review_output_path = review_needed_dir / f"{filename_stem}.md"

                if final_output_path.exists() and not overwrite:
                    if not quiet:
                        console.warning(f"Skipping {final_output_path.name} (output already exists. Use --overwrite to replace.)")
                    skipped_count += 1
                    progress.update(task, advance=1)
                    continue
                
                if not dry_run:
                    # Placeholder for actual validation logic, if any, before moving
                    is_valid = True # For now, assume valid. Actual validation can be added here.
                    if is_valid:
                        if file_path != final_output_path:
                            file_path.rename(final_output_path)
                        processed_count += 1
                        if not quiet:
                            console.success(f"Finalized: {final_output_path.name}")
                    else:
                        file_path.rename(review_output_path)
                        failed_count += 1
                        if not quiet:
                            console.warning(f"Validation failed for {file_path.name}. Moved to review needed.")
                else:
                    processed_count += 1 # In dry run, we still count as processed if it would have been.

            except Exception as e:
                failed_count += 1
                console.error(f"Failed to finalize {file_path.name}: {e}")
            progress.update(task, advance=1)
    
    results = {
        'total': processed_count + failed_count + skipped_count,
        'success': processed_count,
        'failed': failed_count,
        'skipped': skipped_count,
        'dry_run': dry_run
    }
    show_summary(results, console, quiet)
    return failed_count == 0


def _format_initial_single(
    file_path: Path,
    output_dir: Path,
    dry_run: bool,
    overwrite: bool,
    config_manager,
    console
):
    # This logic is extracted and simplified from _format_initial_logic
    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        return

    filename_stem = file_path.stem
    formatted_output_path = output_dir / f"{filename_stem}.md"
    formatted_output_path.parent.mkdir(parents=True, exist_ok=True)

    if formatted_output_path.exists() and not overwrite:
        console.warning(f"Skipping {formatted_output_path.name} (output already exists. Use --overwrite to replace.)")
        return

    console.file("Formatting", file_path.name)

    if not dry_run:
        try:
            raw_content = file_path.read_text(encoding='utf-8')
            parsed_data = pipeline.parser.parse_or_fallback(raw_content, filename_stem)
            markdown = pipeline.formatter.format(parsed_data)

            if markdown.strip():
                formatted_output_path.write_text(markdown, encoding='utf-8')
                console.success(f"Formatted: {formatted_output_path.name}")
            else:
                console.error(f"Failed to format {formatted_output_path.name}: Empty markdown generated.")
        except Exception as e:
            console.error(f"Failed to format {formatted_output_path.name}: {e}")

def _finalize_single(
    file_path: Path,
    output_dir: Path,
    review_dir: Path,
    dry_run: bool,
    overwrite: bool,
    console
):
    # This logic is extracted and simplified from _finalize_logic
    filename_stem = file_path.stem
    final_output_path = output_dir / f"{filename_stem}.md"
    review_output_path = review_dir / f"{filename_stem}.md"

    if final_output_path.exists() and not overwrite:
        console.warning(f"Skipping {final_output_path.name} (output already exists. Use --overwrite to replace.)")
        return
    
    if not dry_run:
        try:
            is_valid = True  # Placeholder
            if is_valid:
                if file_path != final_output_path:
                    file_path.rename(final_output_path)
                console.success(f"Finalized: {final_output_path.name}")
            else:
                file_path.rename(review_output_path)
                console.warning(f"Validation failed for {file_path.name}. Moved to review needed.")
        except Exception as e:
            console.error(f"Failed to finalize {file_path.name}: {e}")

from .core.watcher import Watcher

@app.command()
def watch(
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing notes"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    interval: int = typer.Option(1, "--interval", "-i", help="Polling interval in seconds"),
):
    """Watch for new raw files and process them automatically."""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    raw_dir = Path(config_manager.get("stage1_raw_output_dir"))
    formatted_dir = Path(config_manager.get("initial_formatted_dir"))
    final_dir = Path(config_manager.get("target_dir"))
    review_dir = Path(config_manager.get("review_needed_dir"))

    console.info(f"Watching for new files in: {raw_dir} with interval {interval}s")

    def process_file(file_path: Path):
        console.info(f"New file detected: {file_path.name}")
        
        # Stage 2: Format
        _format_initial_single(
            file_path=file_path,
            output_dir=formatted_dir,
            dry_run=False, # Watch mode should not be dry run
            overwrite=overwrite,
            config_manager=config_manager,
            console=console
        )
        
        # Stage 3: Finalize
        formatted_file_path = formatted_dir / f"{file_path.stem}.md"
        if formatted_file_path.exists():
            _finalize_single(
                file_path=formatted_file_path,
                output_dir=final_dir,
                review_dir=review_dir,
                dry_run=False, # Watch mode should not be dry run
                overwrite=overwrite,
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
):
    """Generate Obsidian documentation from source files (Stage 1 + 2 + 3)"""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    if model: config_manager.set_model(model)

    console.info("[bold green]--- Stage 1: Raw Content Generation ---[/bold green]")
    if not _generate_raw_logic(
        source_path=source_path,
        output=raw_output,
        quiet=quiet,
        model=model,
        config_manager=config_manager,
        console=console
    ):
        console.error("Stage 1 failed. Aborting full generation.")
        raise typer.Exit(1)

    console.info("[bold green]--- Stage 2: Initial Formatting ---[/bold green]")
    if not _format_initial_logic(
        path=raw_output,
        output=formatted_output,
        dry_run=dry_run,
        overwrite=overwrite,
        quiet=quiet,
        model=model,
        config_manager=config_manager,
        console=console
    ):
        console.error("Stage 2 failed. Aborting full generation.")
        raise typer.Exit(1)

    console.info("[bold green]--- Stage 3: Validation, Filtering & Finalization ---[/bold green]")
    if not _finalize_logic(
        path=formatted_output,
        output=final_output,
        review_output=review_output,
        dry_run=dry_run,
        overwrite=overwrite,
        quiet=quiet,
        config_manager=config_manager,
        console=console
    ):
        console.error("Stage 3 failed. Aborting full generation.")
        raise typer.Exit(1)

    console.success("\nFull generation pipeline completed successfully!")


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
        config_manager=config_manager,
        console=console
    ):
        raise typer.Exit(1)


@app.command()
def check_health():
    """
    Checks the health of the RALF Note system, including Ollama connection.
    """
    console = Console()
    config_manager = ConfigManager()

    ollama_host = config_manager.get("ollama_host")
    model_name = config_manager.get("model_name")

    console.info(f"Checking Ollama connection to {ollama_host}...")
    try:
        client = Client(host=ollama_host)
        # Attempt to list models to verify connection
        client.list()
        console.success(f"Successfully connected to Ollama at {ollama_host}")
    except Exception as e:
        console.error(f"Failed to connect to Ollama at {ollama_host}: {e}")
        raise typer.Exit(1)

    console.info(f"Checking if model '{model_name}' is available...")
    try:
        client.show(model_name)
        console.success(f"Model '{model_name}' is available.")
    except Exception as e:
        console.error(f"Model '{model_name}' is not available: {e}")
        console.info(f"Please pull the model using: ollama pull {model_name}")
        raise typer.Exit(1)

    console.success("RALF Note health check passed!")


# ... (rest of the file)
