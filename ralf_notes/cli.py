#!/usr/bin/env python3
"""
RALF Note v2.0 - CLI Application

Main command-line interface
"""

import typer
from pathlib import Path
from typing import Optional, List
from ollama import Client

from .version import VERSION
from .config_manager import ConfigManager
from .core import (
    JSONGenerator,
    JSONExtractor,
    JSONValidator,
    MarkdownFormatter,
    DocumentPipeline,
    FileProcessor,
    JSONGeneratorConfig
)
from rich.table import Table
from .tui import Console, ProgressManager, get_banner


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
                # Use a bulleted list for paths and check existence
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


# Create Typer app
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
        console.info(f"RALF Note v{VERSION} - Unified JSON Architecture")
        console.info("Built with: Ollama, Rich, Typer")
        console.print("")
        raise typer.Exit()


@app.callback()
def callback(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help="Show version information.",
        callback=version_callback,
        is_eager=True,
    )
):
    """
    RALF Note v2.0 - AI-Powered Obsidian Documentation Generator
    """
    pass


def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    """
    Build the document generation pipeline.

    Args:
        config_manager: Configuration manager

    Returns:
        Configured DocumentPipeline
    """
    # Initialize Ollama client
    client = Client(host=config_manager.get("ollama_host"))

    # Build config from configuration file (no hardcoded values)
    gen_config = JSONGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature"),
        chunk_size=config_manager.get("chunk_size"),
        max_content_length=config_manager.get("max_content_length"),
        max_chunk_summary_length=config_manager.get("max_chunk_summary_length"),
        ollama_host=config_manager.get("ollama_host")
    )

    # Build components
    generator = JSONGenerator(client, gen_config)
    extractor = JSONExtractor()
    validator = JSONValidator()
    formatter = MarkdownFormatter()

    # Build pipeline
    pipeline = DocumentPipeline(generator, extractor, validator, formatter)

    return pipeline


def show_summary(results: dict, console: Console, quiet: bool):
    """Display processing summary."""
    if quiet:
        return

    console.rule("Summary")

    total = results.get('total', 0)
    success = results.get('success', 0)
    failed = results.get('failed', 0)
    skipped = results.get('skipped', 0)
    duration = results.get('duration', 0)
    fps = results.get('files_per_second', 0)
    is_dry_run = results.get('dry_run', False)

    summary_text = f"""Total Files: [bold]{total}[/bold]
✅ Success: [success]{success}[/success]
❌ Failed: [error]{failed}[/error]
⏭️  Skipped: [dim]{skipped}[/dim]

Time: {duration:.1f}s
Speed: {fps:.1f} files/s"""

    if is_dry_run:
        title = "📊 Results (Dry Run)"
        summary_text += "\n\n[info]No files were written.[/info]"
    else:
        title = "📊 Results"

    console.panel(summary_text, title=title, style="green")

    if failed > 0:
        console.warning(f"Check output for {failed} failed files")


@app.command()
def init(
    show: bool = typer.Option(False, "--show", help="Show current configuration."),
    add_source: Optional[str] = typer.Option(None, "--add-source", help="Add a source path to the configuration."),
    remove_source: Optional[str] = typer.Option(None, "--remove-source", help="Remove a source path from the configuration."),
    set_target: Optional[str] = typer.Option(None, "--set-target", help="Set the target directory for generated docs."),
    set_model: Optional[str] = typer.Option(None, "--set-model", help="Set the Ollama model name."),
    reset: bool = typer.Option(False, "--reset", help="Reset configuration to defaults."),
):
    """
    Initialize or manage RALF Note configuration.

    - Run without options for interactive setup.
    - Use options to view or modify settings directly.
    """
    console = Console()
    config_manager = ConfigManager()

    # --- Flag-based actions (from old 'config' command) ---
    action_taken = False
    if reset:
        action_taken = True
        if typer.confirm("Reset configuration to defaults?"):
            config_manager.reset_to_defaults()
            config_manager.save()
            console.success("Configuration reset to defaults")
        else:
            console.info("Reset cancelled.")
    if add_source:
        action_taken = True
        if not Path(add_source).exists():
            console.error(f"Path does not exist: {add_source}")
            raise typer.Exit(1)
        config_manager.add_source_path(add_source)
        config_manager.save()
        console.success(f"Added source path: {add_source}")
    if remove_source:
        action_taken = True
        config_manager.remove_source_path(remove_source)
        config_manager.save()
        console.success(f"Removed source path: {remove_source}")
    if set_target:
        action_taken = True
        config_manager.set_target_dir(set_target)
        config_manager.save()
        console.success(f"Target directory set to: {set_target}")
    if set_model:
        action_taken = True
        config_manager.set_model(set_model)
        config_manager.save()
        console.success(f"Model set to: {set_model}")

    # If any flag-based action was taken, or if --show is used, show config and exit.
    if action_taken or show:
        display_config_table(console, config_manager)
        return

    # --- Interactive Setup (if no flags were passed) ---

    if config_manager.config_path.exists():
        console.warning(f"Configuration already exists at: {config_manager.config_path}")
        display_config_table(console, config_manager)
        if not typer.confirm("Do you want to overwrite it?"):
            console.info("Initialization cancelled.")
            raise typer.Exit()

    # Interactive setup
    console.banner(get_banner('simple'))
    console.print("")
    console.info("Setting up RALF Note configuration...")
    console.print("")

    # Get source paths
    console.print("📁 [bold]Source Paths[/bold] (directories to document)")
    console.print("Enter paths one by one (press Enter with empty line when done):")
    source_paths = []
    while True:
        path = typer.prompt("  Source path", default="", show_default=False)
        if not path:
            break
        if Path(path).exists():
            source_paths.append(path)
            console.success(f"Added: {path}")
        else:
            console.warning(f"Path does not exist: {path}")

    if not source_paths:
        console.warning("No source paths added. You can add them later with 'ralf-notes init --add-source ...'")

    # Get target directory
    console.print("")
    target_dir = typer.prompt("📂 Target directory for generated docs", default="./to_obsidian")

    # Get model name
    console.print("")
    model_name = typer.prompt("🤖 Ollama model name", default="ministral-3:3b")

    # Save configuration
    config_manager.config["source_paths"] = source_paths
    config_manager.config["target_dir"] = target_dir
    config_manager.config["model_name"] = model_name
    config_manager.save()

    console.print("")
    console.success(f"Configuration saved to: {config_manager.config_path}")
    console.print("")
    console.info("Next steps:")
    console.print("  1. Make sure Ollama is running: ollama serve")
    console.print(f"  2. Pull the model: ollama pull {model_name}")
    console.print("  3. Test connection: ralf-notes test")
    console.print("  4. Generate docs: ralf-notes generate")
    console.print("")


@app.command()
def generate(
    path: Optional[Path] = typer.Argument(
        None,
        help="Source path to process (overrides config)"
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Output directory (overrides config)"
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Preview without writing files"
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        help="Overwrite existing documents"
    ),
    quiet: bool = typer.Option(
        False,
        "--quiet", "-q",
        help="Minimal output"
    ),
    model: Optional[str] = typer.Option(
        None,
        "--model", "-m",
        help="Override model name"
    ),
):
    """
    Generate Obsidian documentation from source files
    """
    # Setup console
    console = Console(quiet=quiet)

    if not quiet:
        console.banner(get_banner('full'))
        console.print("")

    # Load configuration
    config_manager = ConfigManager()

    # Build paths
    if path:
        source_paths = [path]
    else:
        source_paths = [Path(p) for p in config_manager.get("source_paths", [])]

    if not source_paths:
        console.error("No source paths configured!")
        console.info("Run 'ralf-notes init' to set up configuration")
        raise typer.Exit(1)

    target_dir = output if output else Path(config_manager.get("target_dir"))

    if model:
        config_manager.set_model(model)

    # Show configuration
    if not quiet:
        console.info(f"Model: {config_manager.get('model_name')}")
        console.info(f"Target folder as assigned by user: {target_dir}")
        console.info("Source folders as assigned by user:")
        if source_paths:
            for sp in source_paths:
                console.info(f"  - {sp}")
        else:
            console.info("  - None configured.")

    # Build pipeline
    try:
        pipeline = build_pipeline(config_manager)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
        console.info("Make sure Ollama is running: ollama serve")
        raise typer.Exit(1)

    # Create file processor
    processor = FileProcessor(pipeline)

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    # Process files with progress
    with ProgressManager(console) as progress:
        results = processor.process_paths(
            source_paths,
            target_dir,
            dry_run=dry_run,
            overwrite=overwrite,
            console=console,
            progress=progress
        )

    # Show summary
    show_summary(results, console, quiet)

    # Exit with error if failures
    if results.get('failed', 0) > 0:
        raise typer.Exit(1)


@app.command()
def test():
    """Test Ollama connection and model availability"""
    console = Console()
    config_manager = ConfigManager()

    console.print("")
    console.info("Testing Ollama connection...")

    try:
        client = Client(host=config_manager.get("ollama_host"))
        model_name = config_manager.get("model_name")

        # Test connection
        response = client.generate(
            model=model_name,
            prompt="Hello",
            options={"num_ctx": 100}
        )

        console.success(f"Connected to Ollama at {config_manager.get('ollama_host')}")
        console.success(f"Model '{model_name}' is available and responding")
        console.print("")

    except Exception as e:
        console.error(f"Failed to connect to Ollama: {e}")
        console.print("")
        console.warning("Make sure Ollama is running:")
        console.print("  1. Start Ollama: ollama serve")
        console.print(f"  2. Pull model: ollama pull {config_manager.get('model_name')}")
        console.print("")
        raise typer.Exit(1)




if __name__ == "__main__":
    app()
