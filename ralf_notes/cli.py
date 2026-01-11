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
        console.print("  2. Run [bold green]ralf-notes generate[/bold green] to generate documentation.")
        console.print("  3. Use [bold green]ralf-notes check-health[/bold green] to verify your Ollama setup.")
        console.print("")
        console.print("For more information, run [bold green]ralf-notes --help[/bold green].")
        raise typer.Exit()


@app.command()
def init(
    show: bool = typer.Option(False, "--show", help="Show current configuration."),
    add_source: Optional[str] = typer.Option(None, "--add-source", help="Add a source path to the configuration."),
    remove_source: Optional[str] = typer.Option(None, "--remove-source", help="Remove a source path."),
    set_target: Optional[str] = typer.Option(None, "--set-target", help="Set the target directory."),
    set_model: Optional[str] = typer.Option(None, "--set-model", help="Set the Ollama model name."),
    set_max_files: Optional[int] = typer.Option(None, "--set-max-files", help="Set the max number of files to process (0 for no limit)."),
    reset: bool = typer.Option(False, "--reset", help="Reset configuration to defaults."),
):
    """Initialize or manage RALF Note configuration."""
    console = Console()
    config_manager = ConfigManager()
    action_taken = False
    if any([reset, add_source, remove_source, set_target, set_model, set_max_files is not None, show]):
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
        if set_model:
            config_manager.set_model(set_model)
            config_manager.save()
            console.success(f"Model set to: {set_model}")
        if set_max_files is not None:
            config_manager.set("max_files_to_process", set_max_files)
            config_manager.save()
            console.success(f"Max files to process set to: {set_max_files}")
        
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
    
    target_dir = typer.prompt("Target directory for generated docs", default="./to_obsidian")
    model_name = typer.prompt("Ollama model name", default="ministral-3:3b")
    
    config_manager.config["source_paths"] = source_paths
    config_manager.config["target_dir"] = target_dir
    config_manager.config["model_name"] = model_name
    config_manager.save()
    
    console.success(f"\nConfiguration saved to: {config_manager.config_path}")
    console.info("\nNext steps:\n  1. Ensure Ollama is running: ollama serve\n  2. Pull the model: ollama pull {model_name}\n  3. Test connection: ralf-notes check-health\n  4. Generate docs: ralf-notes generate\n")

@app.command()
def generate(
    path: Optional[Path] = typer.Argument(None, help="Source path to process (overrides config)"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output directory (overrides config)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without writing files"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing documents"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override model name"),
):
    """Generate Obsidian documentation from source files"""
    console = Console(quiet=quiet)
    config_manager = ConfigManager()
    
    source_paths = [path] if path else [Path(p) for p in config_manager.get("source_paths", [])]
    if not source_paths:
        console.error("No source paths configured!")
        console.info("Run 'ralf-notes init' to set up configuration")
        raise typer.Exit(1)

    target_dir = output if output else Path(config_manager.get("target_dir"))
    if model: config_manager.set_model(model)
    
    if not quiet:
        console.info(f"Model: {config_manager.get('model_name')}")
        console.info(f"Target folder: {target_dir}")
        console.info("Source folders:")
        for sp in source_paths: console.info(f"  - {sp}")
        console.print("")

    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        raise typer.Exit(1)
        
    processor = FileProcessor(pipeline, config_manager)
    target_dir.mkdir(parents=True, exist_ok=True)

    with ProgressManager(console) as progress:
        results = processor.process_paths(source_paths, target_dir, dry_run, overwrite, console, progress)
    
    show_summary(results, console, quiet)
    if results.get('failed', 0) > 0: raise typer.Exit(1)

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
