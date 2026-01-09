#!/usr/bin/env python3
"""
RALF Note v2.0 - AI-Powered Obsidian Documentation Generator

Unified JSON architecture with beautiful TUI
"""

import typer
from pathlib import Path
from typing import Optional, List
from ollama import Client

# V2 imports
from core_v2 import (
    JSONGenerator,
    JSONExtractor,
    JSONValidator,
    MarkdownFormatter,
    DocumentPipeline,
    FileProcessor,
    JSONGeneratorConfig
)
from tui import Console, ProgressManager, get_banner

# Configuration
from config import SOURCE_PATHS, TARGET_DIR, MODEL_NAME, OLLAMA_HOST

# Create Typer app
app = typer.Typer(
    name="ralf",
    help="🚀 RALF Note v2.0 - AI-Powered Obsidian Documentation Generator",
    add_completion=True
)


def build_pipeline(config: JSONGeneratorConfig) -> DocumentPipeline:
    """
    Build the document generation pipeline.

    Args:
        config: Generator configuration

    Returns:
        Configured DocumentPipeline
    """
    # Initialize Ollama client
    client = Client(host=config.ollama_host)

    # Build components
    generator = JSONGenerator(client, config)
    extractor = JSONExtractor()
    validator = JSONValidator()
    formatter = MarkdownFormatter()

    # Build pipeline
    pipeline = DocumentPipeline(generator, extractor, validator, formatter)

    return pipeline


def show_summary(results: dict, console: Console, quiet: bool):
    """
    Display processing summary.

    Args:
        results: Processing results dictionary
        console: Console instance
        quiet: Quiet mode flag
    """
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
def generate(
    path: Optional[Path] = typer.Argument(
        None,
        help="Source path to process (default: config SOURCE_PATHS)"
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Output directory (default: config TARGET_DIR)"
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

    # Build configuration
    source_paths = [path] if path else [Path(p) for p in SOURCE_PATHS]
    target_dir = output if output else Path(TARGET_DIR)
    model_name = model if model else MODEL_NAME

    config = JSONGeneratorConfig(
        model_name=model_name,
        ollama_host=OLLAMA_HOST
    )

    # Show configuration
    if not quiet:
        console.info(f"Model: {config.model_name}")
        console.info(f"Target: {target_dir}")

    # Build pipeline
    try:
        pipeline = build_pipeline(config)
    except Exception as e:
        console.error(f"Failed to initialize pipeline: {e}")
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
    console.banner(get_banner('full'))
    console.print("")

    # Configuration
    console.panel(
        f"""Model: [bold]{MODEL_NAME}[/bold]
Host: {OLLAMA_HOST}
Temperature: 0.1
Context: 10000 tokens""",
        title="⚙️  Configuration",
        style="cyan"
    )

    # Source paths
    console.print("\n📁 Source Paths:")
    for path in SOURCE_PATHS:
        console.print(f"  • {path}")

    console.print(f"\n📂 Target: {TARGET_DIR}\n")


@app.command()
def version():
    """Show version information"""
    console = Console()
    console.banner(get_banner('simple'))
    console.print("")
    console.info("RALF Note v2.0 - Unified JSON Architecture")
    console.info("Built with: Ollama, Rich, Typer")
    console.print("")


@app.command()
def test():
    """Test Ollama connection and model availability"""
    console = Console()
    console.print("")
    console.info("Testing Ollama connection...")

    try:
        client = Client(host=OLLAMA_HOST)

        # Test connection
        response = client.generate(
            model=MODEL_NAME,
            prompt="Hello",
            options={"num_ctx": 100}
        )

        console.success(f"Connected to Ollama at {OLLAMA_HOST}")
        console.success(f"Model '{MODEL_NAME}' is available and responding")
        console.print("")

    except Exception as e:
        console.error(f"Failed to connect to Ollama: {e}")
        console.print("")
        console.warning("Make sure Ollama is running:")
        console.print("  1. Start Ollama: ollama serve")
        console.print(f"  2. Pull model: ollama pull {MODEL_NAME}")
        console.print("")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
