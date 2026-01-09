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
from .tui import Console, ProgressManager, get_banner

# Create Typer app
app = typer.Typer(
    name="ralf-notes",
    help="🚀 RALF Note v2.0 - AI-Powered Obsidian Documentation Generator",
    add_completion=True
)


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

    # Build config
    gen_config = JSONGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature"),
        chunk_size=config_manager.get("chunk_size"),
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

    summary_text = f"""Total Files: [bold]{total}[/bold]
✅ Success: [success]{success}[/success]
❌ Failed: [error]{failed}[/error]
⏭️  Skipped: [dim]{skipped}[/dim]

Time: {duration:.1f}s
Speed: {fps:.1f} files/s"""

    console.panel(summary_text, title="📊 Results", style="green")

    if failed > 0:
        console.warning(f"Check output for {failed} failed files")


@app.command()
def init(
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite existing configuration"
    )
):
    """
    Initialize RALF Note configuration

    Creates ~/.ralf-notes/config.json with default settings
    """
    console = Console()
    config_manager = ConfigManager()

    if config_manager.config_path.exists() and not force:
        console.warning(f"Configuration already exists at: {config_manager.config_path}")
        console.info("Use --force to overwrite")
        raise typer.Exit(1)

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
        console.warning("No source paths added. You can add them later with 'ralf-notes config'")

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
def config(
    show: bool = typer.Option(False, "--show", help="Show current configuration"),
    add_source: Optional[str] = typer.Option(None, "--add-source", help="Add source path"),
    remove_source: Optional[str] = typer.Option(None, "--remove-source", help="Remove source path"),
    set_target: Optional[str] = typer.Option(None, "--set-target", help="Set target directory"),
    set_model: Optional[str] = typer.Option(None, "--set-model", help="Set Ollama model"),
    reset: bool = typer.Option(False, "--reset", help="Reset to defaults"),
):
    """
    Manage RALF Note configuration

    View and modify configuration settings
    """
    console = Console()
    config_manager = ConfigManager()

    if reset:
        if typer.confirm("Reset configuration to defaults?"):
            config_manager.reset_to_defaults()
            config_manager.save()
            console.success("Configuration reset to defaults")
        return

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

    # Always show config at the end
    console.print("")
    console.panel(config_manager.show(), title="⚙️  Current Configuration", style="cyan")
    console.print("")
    console.info(f"Config file: {config_manager.config_path}")


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
        console.info(f"Target: {target_dir}")

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
def status():
    """Show current configuration and status"""
    console = Console()
    config_manager = ConfigManager()

    console.banner(get_banner('full'))
    console.print("")

    # Configuration
    console.panel(
        f"""Model: [bold]{config_manager.get('model_name')}[/bold]
Host: {config_manager.get('ollama_host')}
Temperature: {config_manager.get('temperature')}
Context: {config_manager.get('num_ctx')} tokens""",
        title="⚙️  Configuration",
        style="cyan"
    )

    # Source paths
    source_paths = config_manager.get("source_paths", [])
    if source_paths:
        console.print("\n📁 Source Paths:")
        for path in source_paths:
            exists = "✅" if Path(path).exists() else "❌"
            console.print(f"  {exists} {path}")
    else:
        console.print("\n📁 Source Paths: [yellow]None configured[/yellow]")
        console.info("Run 'ralf-notes init' to set up")

    console.print(f"\n📂 Target: {config_manager.get('target_dir')}")
    console.print(f"📄 Config file: {config_manager.config_path}\n")


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


@app.command()
def version():
    """Show version information"""
    console = Console()
    console.banner(get_banner('simple'))
    console.print("")
    console.info(f"RALF Note v{VERSION} - Unified JSON Architecture")
    console.info("Built with: Ollama, Rich, Typer")
    console.print("")


@app.command()
def setup():
    """
    Complete setup wizard for first-time users

    Interactive setup that:
    1. Creates configuration
    2. Sets up directories
    3. Tests Ollama connection
    4. Guides through first use
    """
    console = Console()
    console.banner(get_banner('full'))
    console.print("")
    console.info("Welcome to RALF Note Setup Wizard!")
    console.print("")

    # Step 1: Check if already configured
    config_manager = ConfigManager()
    if config_manager.config_path.exists():
        console.warning("Configuration already exists!")
        if not typer.confirm("Do you want to reconfigure?"):
            console.info("Setup cancelled")
            return

    # Step 2: Initialize configuration
    console.rule("Step 1: Configuration")
    console.print("")

    source_paths = []
    console.print("Enter directories to document (press Enter when done):")
    while True:
        path = typer.prompt("  Directory", default="", show_default=False)
        if not path:
            break
        path_obj = Path(path).expanduser().resolve()
        if path_obj.exists():
            source_paths.append(str(path_obj))
            console.success(f"Added: {path_obj}")
        else:
            console.warning(f"Directory not found: {path}")

    target_dir = typer.prompt("\nOutput directory", default=str(Path.home() / "Documents" / "ObsidianVault" / "RALF_Notes"))
    model_name = typer.prompt("Ollama model", default="ministral-3:3b")

    # Save configuration
    config_manager.config["source_paths"] = source_paths
    config_manager.config["target_dir"] = target_dir
    config_manager.config["model_name"] = model_name
    config_manager.save()

    console.print("")
    console.success(f"Configuration saved!")

    # Step 3: Create directories
    console.print("")
    console.rule("Step 2: Creating Directories")
    console.print("")

    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    console.success(f"Created: {target_path}")

    # Step 4: Test Ollama
    console.print("")
    console.rule("Step 3: Testing Ollama")
    console.print("")

    try:
        client = Client(host=config_manager.get("ollama_host"))
        response = client.generate(
            model=model_name,
            prompt="Hello",
            options={"num_ctx": 100}
        )
        console.success("Ollama is working correctly!")
    except Exception as e:
        console.error(f"Cannot connect to Ollama: {e}")
        console.print("")
        console.warning("Please ensure:")
        console.print(f"  1. Ollama is running: ollama serve")
        console.print(f"  2. Model is installed: ollama pull {model_name}")
        console.print("")
        console.info("After fixing, run: ralf-notes test")
        return

    # Step 5: Summary
    console.print("")
    console.rule("Setup Complete!")
    console.print("")

    console.panel(
        f"""✅ Configuration created
✅ Directories ready
✅ Ollama connected

You're all set! 🎉""",
        title="🚀 Ready to Go",
        style="green"
    )

    console.print("")
    console.info("Next steps:")
    console.print("  • Generate docs: ralf-notes generate")
    console.print("  • View config: ralf-notes status")
    console.print("  • Get help: ralf-notes --help")
    console.print("")


if __name__ == "__main__":
    app()
