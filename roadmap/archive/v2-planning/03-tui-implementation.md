# TUI Implementation Plan

**Date:** 2026-01-09
**Goal:** Create a beautiful, professional terminal interface with ASCII art and colored output

---

## Design Philosophy

> "Make the terminal experience delightful"

**Principles:**
1. **Visual Clarity** - Color-coded status, clear hierarchy
2. **Real-time Feedback** - Progress bars, spinners, live updates
3. **Professional Aesthetic** - ASCII art banner, clean panels
4. **Informative** - Show what's happening at all times
5. **Non-intrusive** - Can be quieted for scripting

---

## Technology Stack

### Rich Library (Comprehensive TUI)

**Features we'll use:**
- ✅ **Console** - Colored output, markup
- ✅ **Panel** - Bordered boxes for sections
- ✅ **Progress** - Progress bars with ETA
- ✅ **Table** - Formatted data display
- ✅ **Tree** - File hierarchy visualization
- ✅ **Syntax** - Code highlighting
- ✅ **Live** - Auto-updating displays
- ✅ **Spinner** - Loading animations

### Typer (CLI Framework)

**Features we'll use:**
- ✅ **Commands** - Multiple subcommands
- ✅ **Arguments** - Positional parameters
- ✅ **Options** - Flags and named parameters
- ✅ **Help** - Auto-generated documentation
- ✅ **Completion** - Shell completion support

---

## ASCII Art Banner

### Main Banner (Startup)

```python
# tui/ascii_art.py

RALF_BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗  ║
║   ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║  ║
║   ██╔══██╗██╔══██║██║     ██╔══╝      ██║╚██╗██║██║   ██║  ║
║   ██║  ██║██║  ██║███████╗██║         ██║ ╚████║╚██████╔╝  ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝         ╚═╝  ╚═══╝ ╚═════╝   ║
║                                                              ║
║        Recursive AI-powered Learning Framework               ║
║           Obsidian Documentation Generator                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

# Alternative: Simpler banner
RALF_SIMPLE = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ███████╗ ███████╗ ██╗     ███████╗                    ┃
┃  ██╔════╝ ██╔══██╗ ██║     ██╔════╝                    ┃
┃  █████╗   ███████║ ██║     █████╗     Notes            ┃
┃  ██╔══╝   ██╔══██║ ██║     ██╔══╝                      ┃
┃  ███████╗ ██║  ██║ ███████╗██║                         ┃
┃  ╚══════╝ ╚═╝  ╚═╝ ╚══════╝╚═╝                         ┃
┃                                                         ┃
┃  📚 AI-Powered Documentation Generator                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

# Compact banner for subsequent runs
RALF_COMPACT = """
╭─────────────────────────────────────╮
│  🚀 RALF Note - Documentation Gen  │
╰─────────────────────────────────────╯
"""

def get_banner(style: str = 'full') -> str:
    """Get banner based on context"""
    banners = {
        'full': RALF_BANNER,
        'simple': RALF_SIMPLE,
        'compact': RALF_COMPACT
    }
    return banners.get(style, RALF_COMPACT)
```

### Catchy Name Ideas

Based on the acronym **RALF** (Recursive AI-powered Learning Framework):

1. **RALF Note** ✅ (Current - Good!)
2. **RALF Docs** - Documentation focus
3. **RALF Vault** - Obsidian vault connection
4. **DocRALF** - Document + RALF
5. **RALFie** - Friendly, approachable
6. **RALF.ai** - AI emphasis
7. **ObsiRALF** - Obsidian + RALF
8. **CodeRALF** - Code documentation focus

**Recommendation:** Stick with **"RALF Note"** - it's catchy, memorable, and clearly describes purpose.

---

## Console Manager

```python
# tui/console.py

from rich.console import Console as RichConsole
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from typing import Optional

# Custom theme
RALF_THEME = Theme({
    "info": "cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "dim": "dim",
    "highlight": "bold magenta",
    "code": "bold blue",
    "path": "italic cyan"
})

class Console:
    """
    Box: Console Manager

    Responsibility: Centralized console output with consistent styling
    """

    def __init__(self, quiet: bool = False):
        self.console = RichConsole(theme=RALF_THEME)
        self.quiet = quiet

    def print(self, message: str, style: Optional[str] = None):
        """Print message with optional style"""
        if not self.quiet:
            self.console.print(message, style=style)

    def info(self, message: str, icon: str = "ℹ️"):
        """Info message"""
        self.print(f"{icon}  {message}", style="info")

    def success(self, message: str, icon: str = "✅"):
        """Success message"""
        self.print(f"{icon}  {message}", style="success")

    def warning(self, message: str, icon: str = "⚠️"):
        """Warning message"""
        self.print(f"{icon}  {message}", style="warning")

    def error(self, message: str, icon: str = "❌"):
        """Error message"""
        self.print(f"{icon}  {message}", style="error")

    def processing(self, message: str, icon: str = "⚙️"):
        """Processing message"""
        self.print(f"{icon}  {message}", style="dim")

    def file(self, action: str, filename: str):
        """File operation message"""
        self.print(f"📄  {action}: [path]{filename}[/path]")

    def panel(self, content: str, title: str = "", style: str = "info"):
        """Display content in a panel"""
        if not self.quiet:
            self.console.print(Panel(content, title=title, border_style=style))

    def banner(self, banner_text: str):
        """Display ASCII banner"""
        if not self.quiet:
            self.console.print(Text(banner_text, style="bold cyan"))

    def rule(self, title: str = ""):
        """Display horizontal rule"""
        if not self.quiet:
            self.console.rule(title, style="dim")

    def table_from_dict(self, data: dict, title: str = ""):
        """Display key-value pairs as table"""
        from rich.table import Table

        if self.quiet:
            return

        table = Table(title=title, show_header=False)
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="white")

        for key, value in data.items():
            table.add_row(str(key), str(value))

        self.console.print(table)
```

---

## Progress Display

```python
# tui/progress.py

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    TimeElapsedColumn
)
from typing import Optional
from pathlib import Path

class ProgressManager:
    """
    Box: Progress Manager

    Responsibility: Show progress during file processing
    """

    def __init__(self, console):
        self.console = console
        self.progress: Optional[Progress] = None

    def __enter__(self):
        """Start progress display"""
        if not self.console.quiet:
            self.progress = Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                "•",
                TimeElapsedColumn(),
                "•",
                TimeRemainingColumn(),
                console=self.console.console
            )
            self.progress.__enter__()
        return self

    def __exit__(self, *args):
        """Stop progress display"""
        if self.progress:
            self.progress.__exit__(*args)

    def add_task(self, description: str, total: int):
        """Add a progress task"""
        if self.progress:
            return self.progress.add_task(description, total=total)
        return None

    def update(self, task_id, advance: int = 1, description: str = None):
        """Update progress"""
        if self.progress and task_id is not None:
            if description:
                self.progress.update(task_id, advance=advance, description=description)
            else:
                self.progress.advance(task_id, advance)

    def complete(self, task_id):
        """Mark task as complete"""
        if self.progress and task_id is not None:
            self.progress.update(task_id, completed=True)


class SimpleProgressReporter:
    """
    Box: Simple Progress Reporter

    Responsibility: Simple progress without progress bar (for quiet mode)
    """

    def __init__(self, console):
        self.console = console
        self.current = 0
        self.total = 0

    def start(self, total: int, description: str = "Processing"):
        """Start tracking"""
        self.total = total
        self.current = 0
        self.console.info(f"{description} ({total} files)")

    def update(self, filename: str):
        """Update progress"""
        self.current += 1
        pct = (self.current / self.total * 100) if self.total > 0 else 0
        self.console.processing(
            f"[{self.current}/{self.total}] ({pct:.0f}%) {filename}"
        )

    def complete(self):
        """Finish"""
        self.console.success(f"Processed {self.current} files")
```

---

## Main CLI Interface

```python
# main.py

import typer
from pathlib import Path
from typing import Optional, List
from rich.table import Table

from tui.console import Console
from tui.progress import ProgressManager
from tui.ascii_art import get_banner
from core.document_pipeline import DocumentPipeline
from core.file_processor import FileProcessor
from config import Config

app = typer.Typer(
    name="ralf",
    help="🚀 RALF Note - AI-Powered Obsidian Documentation Generator",
    add_completion=True
)

console = Console()

def show_banner():
    """Display startup banner"""
    console.banner(get_banner('full'))
    console.print("")

@app.command()
def generate(
    path: Optional[Path] = typer.Argument(
        None,
        help="Source path to process (default: config SOURCE_PATHS)",
        exists=True
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
    no_cache: bool = typer.Option(
        False,
        "--no-cache",
        help="Disable caching"
    ),
):
    """
    Generate Obsidian documentation from source files
    """
    if not quiet:
        show_banner()

    # Build configuration
    config = Config()
    if path:
        config.source_paths = [path]
    if output:
        config.target_dir = output

    # Setup pipeline
    pipeline = build_pipeline(config, use_cache=not no_cache)
    processor = FileProcessor(pipeline, console)

    # Process files
    with ProgressManager(console) as progress:
        results = processor.process_paths(
            config.source_paths,
            config.target_dir,
            dry_run=dry_run,
            overwrite=overwrite,
            progress=progress
        )

    # Show summary
    show_summary(results, console, quiet)


@app.command()
def status():
    """Show current configuration and status"""
    show_banner()

    config = Config()

    console.panel(
        f"""Model: [bold]{config.model_name}[/bold]
Temperature: {config.temperature}
Context: {config.num_ctx} tokens
Cache: {'Enabled' if config.use_cache else 'Disabled'}""",
        title="⚙️  Configuration",
        style="cyan"
    )

    # Source paths
    table = Table(title="📁 Source Paths", show_header=False)
    table.add_column("Path", style="cyan")
    for path in config.source_paths:
        table.add_row(str(path))
    console.console.print(table)

    console.info(f"Target: {config.target_dir}")


@app.command()
def cache_stats():
    """Show cache statistics"""
    from core.cache_manager import CacheManager

    show_banner()
    console.rule("Cache Statistics")

    cache = CacheManager()
    stats = cache.get_stats()

    console.table_from_dict(stats, title="📊 Cache Stats")


@app.command()
def clear_cache(
    confirm: bool = typer.Option(
        False,
        "--yes", "-y",
        help="Skip confirmation"
    )
):
    """Clear the cache"""
    from core.cache_manager import CacheManager

    if not confirm:
        confirm = typer.confirm("Clear all cached documents?")

    if confirm:
        cache = CacheManager()
        count = cache.clear_all()
        console.success(f"Cleared {count} cached documents")
    else:
        console.info("Cache clear cancelled")


@app.command()
def validate(
    file: Path = typer.Argument(..., help="Markdown file to validate", exists=True),
):
    """Validate an existing Obsidian document"""
    show_banner()

    console.info(f"Validating: {file.name}")

    # Parse existing markdown
    # Validate structure
    # Show report

    console.success("Validation complete!")


@app.command()
def watch(
    path: Path = typer.Argument(..., help="Path to watch", exists=True),
):
    """Watch directory and auto-generate on changes"""
    show_banner()

    console.info(f"Watching: {path}")
    console.warning("Press Ctrl+C to stop")

    # Use watchdog to monitor file changes
    # Auto-generate when files change

    console.info("Watching stopped")


def show_summary(results: dict, console: Console, quiet: bool):
    """Display processing summary"""
    if quiet:
        return

    console.rule("Summary")

    total = results.get('total', 0)
    success = results.get('success', 0)
    failed = results.get('failed', 0)
    cached = results.get('cached', 0)
    skipped = results.get('skipped', 0)

    summary_text = f"""Total Files: [bold]{total}[/bold]
✅ Success: [success]{success}[/success]
❌ Failed: [error]{failed}[/error]
📦 Cached: [info]{cached}[/info]
⏭️  Skipped: [dim]{skipped}[/dim]

Time: {results.get('duration', 0):.1f}s
Speed: {results.get('files_per_second', 0):.1f} files/s"""

    console.panel(summary_text, title="📊 Results", style="green")

    if failed > 0:
        console.warning(f"Check logs for {failed} failed files")


if __name__ == "__main__":
    app()
```

---

## Usage Examples

### Basic Usage

```bash
# Generate docs with full banner
ralf generate

# Generate for specific path
ralf generate /path/to/code

# Dry run (preview)
ralf generate --dry-run

# Quiet mode (minimal output)
ralf generate --quiet

# Overwrite existing docs
ralf generate --overwrite
```

### Configuration

```bash
# Show current configuration
ralf status

# Check cache stats
ralf cache-stats

# Clear cache
ralf clear-cache --yes
```

### Advanced

```bash
# Custom output directory
ralf generate --output /custom/output

# Disable caching
ralf generate --no-cache

# Watch mode (auto-generate on changes)
ralf watch /path/to/code
```

---

## Visual Output Examples

### Startup Banner
```
╔══════════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗  ║
║   ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║  ║
║   ██╔══██╗██╔══██║██║     ██╔══╝      ██║╚██╗██║██║   ██║  ║
║   ██║  ██║██║  ██║███████╗██║         ██║ ╚████║╚██████╔╝  ║
║                                                              ║
║        Recursive AI-powered Learning Framework               ║
╚══════════════════════════════════════════════════════════════╝
```

### Progress Display
```
⚙️  Processing files...
◐ Processing: main.py     ████████████████░░░░  75/100 • 00:45 • 00:15
```

### File Processing
```
📄  Analyzing: main.py
✅  Generated doc for main.py
📄  Analyzing: config.py
⚠️   JSON parsing failed for config.py (using fallback)
✅  Saved: config.md
```

### Summary Panel
```
╭─────────── 📊 Results ───────────╮
│ Total Files: 100                 │
│ ✅ Success: 95                   │
│ ❌ Failed: 3                     │
│ 📦 Cached: 2                     │
│ ⏭️  Skipped: 0                   │
│                                  │
│ Time: 125.4s                     │
│ Speed: 0.8 files/s               │
╰──────────────────────────────────╯
```

---

## Color Scheme

```python
# Color palette
COLORS = {
    'primary': 'cyan',          # Info, paths
    'success': 'green',         # Success messages
    'warning': 'yellow',        # Warnings
    'error': 'red',             # Errors
    'processing': 'blue',       # Processing status
    'dim': 'dim white',         # Secondary info
    'highlight': 'magenta',     # Important highlights
    'banner': 'bold cyan',      # ASCII art
}

# Status icons
ICONS = {
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    'processing': '⚙️',
    'cached': '📦',
    'skipped': '⏭️',
    'file': '📄',
    'folder': '📁',
    'rocket': '🚀',
}
```

---

## Next Steps

1. **Error handling** → See `04-error-handling-strategy.md`
2. **Testing plan** → See `05-testing-strategy.md`
3. **Performance optimization** → See `06-performance-optimization.md`
4. **Complete roadmap** → See `07-implementation-roadmap.md`

---

## Summary

The TUI implementation provides:

- ✅ **Beautiful ASCII banner** - Professional appearance
- ✅ **Colored console output** - Easy status identification
- ✅ **Progress indicators** - Real-time feedback
- ✅ **Rich panels** - Organized information display
- ✅ **Professional CLI** - Typer-powered commands
- ✅ **Flexible output** - Quiet mode for scripting

**User experience upgrade:** From plain text to delightful terminal interface!
