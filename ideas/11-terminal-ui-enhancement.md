# Enhancement 11: Terminal UI (TUI) with ASCII Art

## Priority: ⭐⭐⭐ HIGH VALUE / MEDIUM EFFORT

## Problem

Current terminal output is basic logging:
```
2026-01-09 00:18:33,338 - INFO - ============================================================
2026-01-09 00:18:33,338 - INFO - RALF Notes - Ollama Documentation Generator
2026-01-09 00:18:33,338 - INFO - ============================================================
2026-01-09 00:18:33,338 - INFO - Cache: 2 entries, 0.00 MB
```

**Issues:**
- No visual feedback during long processing
- No progress indication
- Boring, plain text output
- Hard to see what's happening
- No live statistics
- No interactive elements

## Solution

Transform RALF Notes into a beautiful Terminal UI app with:
- 🎨 ASCII art banner
- 📊 Real-time progress bars
- 🌈 Colorful output
- 📈 Live statistics dashboard
- 🎯 Interactive file selection
- 💫 Animated spinners
- 🎭 Rich formatting

---

## Implementation Options

### Option 1: Rich Library (Recommended) ⭐⭐⭐⭐⭐

**Best for:** Beautiful output, progress bars, live displays
**Install:** `pip install rich`

**Pros:**
- ✅ Easy to use
- ✅ Beautiful by default
- ✅ Great documentation
- ✅ Progress bars, tables, panels, syntax highlighting
- ✅ Works with existing logging
- ✅ No event loop needed

**Cons:**
- ❌ Not fully interactive (no keyboard input handling)

**Perfect for RALF Notes because:**
- We mostly just need progress display
- Works with existing architecture
- Non-intrusive (can add gradually)

### Option 2: Textual (Advanced) ⭐⭐⭐⭐

**Best for:** Full TUI apps with widgets, forms, menus
**Install:** `pip install textual`

**Pros:**
- ✅ Full TUI framework
- ✅ React-like component model
- ✅ Keyboard/mouse input
- ✅ Built on Rich
- ✅ Widgets: buttons, input fields, trees

**Cons:**
- ❌ More complex (requires event loop)
- ❌ Architecture changes needed
- ❌ Steeper learning curve

**Use case:** If you want fully interactive mode (file selection, config editing)

### Option 3: Curses (Classic) ⭐⭐⭐

**Best for:** Maximum control, low-level TUI
**Install:** Built-in (Python stdlib)

**Pros:**
- ✅ No dependencies
- ✅ Full control
- ✅ Works everywhere

**Cons:**
- ❌ Low-level API
- ❌ More code to write
- ❌ Not as pretty by default

---

## Recommended: Rich Implementation

### Installation

```bash
pip install rich pyfiglet
```

### Phase 1: Beautiful Startup Banner

**File:** Create `ui/banner.py`

```python
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from pyfiglet import Figlet

console = Console()

def show_banner():
    """Display RALF Notes ASCII art banner"""

    # Generate ASCII art
    f = Figlet(font='slant')
    ascii_art = f.renderText('RALF Notes')

    # Create styled text
    banner = Text()
    banner.append(ascii_art, style="bold cyan")
    banner.append("\n")
    banner.append("Repository Analysis, Linkage & Formatting\n", style="dim")
    banner.append("Powered by Ollama • Version 2.0\n", style="green")

    # Wrap in panel
    panel = Panel(
        banner,
        border_style="cyan",
        padding=(1, 2)
    )

    console.print(panel)
    console.print()

def show_summary(stats):
    """Show processing summary with stats"""
    from rich.table import Table

    table = Table(title="Processing Summary", border_style="green")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green", justify="right")

    table.add_row("Files Processed", str(stats['processed']))
    table.add_row("Files Failed", str(stats['failed']))
    table.add_row("Files Skipped", str(stats['skipped']))
    table.add_row("Cache Hits", str(stats.get('cache_hits', 0)))
    table.add_row("Cache Misses", str(stats.get('cache_misses', 0)))
    table.add_row("Total Time", f"{stats['elapsed']:.1f}s")
    table.add_row("Speed", f"{stats['files_per_minute']:.1f} files/min")

    console.print(table)
```

### Phase 2: Progress Bars

**File:** `ui/progress.py`

```python
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    TimeElapsedColumn
)
from rich.console import Console

console = Console()

def create_progress():
    """Create beautiful progress bar"""
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(complete_style="green", finished_style="bold green"),
        TaskProgressColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
        TextColumn("•"),
        TimeRemainingColumn(),
        console=console
    )

def process_files_with_ui(files_to_process, generator):
    """Process files with beautiful progress display"""
    from rich.live import Live
    from rich.table import Table

    stats = {
        'processed': 0,
        'failed': 0,
        'skipped': 0,
        'cache_hits': 0,
        'cache_misses': 0,
        'current_file': '',
        'start_time': time.time()
    }

    def make_status_table():
        """Generate live status table"""
        table = Table.grid(padding=(0, 2))
        table.add_column(style="cyan")
        table.add_column(style="green")

        table.add_row("📁 Current File:", stats['current_file'])
        table.add_row("✅ Processed:", str(stats['processed']))
        table.add_row("❌ Failed:", str(stats['failed']))
        table.add_row("⏭️  Skipped:", str(stats['skipped']))
        table.add_row("💾 Cache Hits:", str(stats['cache_hits']))

        elapsed = time.time() - stats['start_time']
        if elapsed > 0:
            speed = stats['processed'] / (elapsed / 60)
            table.add_row("⚡ Speed:", f"{speed:.1f} files/min")

        return Panel(table, title="[bold cyan]Status", border_style="cyan")

    with create_progress() as progress:
        task = progress.add_task(
            "[cyan]Processing files...",
            total=len(files_to_process)
        )

        with Live(make_status_table(), refresh_per_second=4) as live:
            for file_path in files_to_process:
                stats['current_file'] = os.path.basename(file_path)
                live.update(make_status_table())

                try:
                    # Check cache first
                    # ... processing logic
                    stats['processed'] += 1

                except Exception as e:
                    stats['failed'] += 1
                    console.print(f"[red]✗ Failed: {file_path} - {e}")

                progress.update(task, advance=1)

    return stats
```

### Phase 3: Rich Logging

**File:** Update `utils/logger_factory.py`

```python
import logging
from rich.logging import RichHandler
from rich.console import Console

console = Console()

class LoggerFactory:
    """Factory for creating rich loggers"""

    @staticmethod
    def get_logger(name='ralf_notes'):
        """Get a rich logger instance"""
        logger = logging.getLogger(name)

        if not logger.handlers:
            # Rich handler for console
            rich_handler = RichHandler(
                console=console,
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                markup=True
            )
            rich_handler.setLevel(logging.INFO)

            # File handler for detailed logs
            file_handler = logging.FileHandler('logs/ralf.log')
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_formatter)

            logger.addHandler(rich_handler)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)

        return logger
```

### Phase 4: Update main.py

```python
from ui.banner import show_banner, show_summary
from ui.progress import process_files_with_ui
from rich.console import Console

console = Console()

def main():
    """Enhanced main with TUI"""

    # Show beautiful banner
    show_banner()

    # Validate model
    console.print("[cyan]🔍 Checking Ollama connection...[/cyan]")
    if not validate_model_availability():
        console.print("[red]❌ Ollama not available[/red]")
        return
    console.print("[green]✓ Ollama connected[/green]")

    # Warm up model
    console.print("[cyan]🔥 Warming up model...[/cyan]")
    warmup_model()
    console.print("[green]✓ Model ready[/green]")

    # Get files
    console.print(f"[cyan]📂 Scanning {len(SOURCE_PATHS)} directories...[/cyan]")
    all_files = get_all_files(SOURCE_PATHS)
    console.print(f"[green]✓ Found {len(all_files)} files[/green]\n")

    if not all_files:
        console.print("[yellow]⚠️  No files to process[/yellow]")
        return

    # Cache stats
    if ENABLE_CACHING:
        cache_stats = get_cache_stats()
        console.print(f"[cyan]💾 Cache: {cache_stats['entry_count']} entries, "
                     f"{cache_stats['total_size_mb']:.2f} MB[/cyan]\n")

    # Build generator
    console.print("[cyan]⚙️  Building document generator...[/cyan]")
    generator = build_document_generator()
    console.print("[green]✓ Generator ready[/green]\n")

    # Process with beautiful UI
    stats = process_files_with_ui(all_files, generator)

    # Show summary
    console.print()
    show_summary(stats)

    console.print("\n[bold green]✨ All done![/bold green]\n")
```

---

## Visual Examples

### Example 1: Startup Banner

```
╭────────────────────────────────────────────────────────────╮
│                                                            │
│      ____   ___    __   ______   _   __      __           │
│     / __ \ / _ |  / /  / ____/  / | / /___  / /____  _____│
│    / /_/ // __ | / /  / /_     /  |/ // _ \/ __/ _ \/ ___/│
│   / _, _// /_/ // /__/ __/    / /|  //  __/ /_/  __(__  ) │
│  /_/ |_|/_/ |_//____/_/      /_/ |_/ \___/\__/\___/____/  │
│                                                            │
│  Repository Analysis, Linkage & Formatting                │
│  Powered by Ollama • Version 2.0                          │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### Example 2: Progress Display

```
🔄 Processing files... ━━━━━━━━━━━━━━━━━╸━━━━━━ 45% • 1:23 • 0:42 remaining

╭─────────── Status ───────────╮
│ 📁 Current File: main.py     │
│ ✅ Processed:    45          │
│ ❌ Failed:       2           │
│ ⏭️  Skipped:     8           │
│ 💾 Cache Hits:   12          │
│ ⚡ Speed:        32.5 files/m│
╰──────────────────────────────╯
```

### Example 3: Summary Table

```
╭─────────── Processing Summary ───────────╮
│ Metric           │              Value    │
├──────────────────┼───────────────────────┤
│ Files Processed  │                   95  │
│ Files Failed     │                    2  │
│ Files Skipped    │                    3  │
│ Cache Hits       │                   47  │
│ Cache Misses     │                   48  │
│ Total Time       │               245.3s  │
│ Speed            │         23.2 files/min│
╰──────────────────┴───────────────────────╯
```

### Example 4: Live Section Generation

```
Generating document for config.py...

  Summary     ━━━━━━━━━━━━━━━━━━━━━━ 100% ✓
  Details     ━━━━━━━━━━━━━━━━━━━━━━ 100% ✓
  Tags        ━━━━━━━━━━━━━━━━━━━━━━ 100% ✓
  Functions   ━━━━━━━━━━╸━━━━━━━━━━━  55% ...
  Usage       ━━━━━━━━━━━━━━━━━━━━━━   0%
  Related     ━━━━━━━━━━━━━━━━━━━━━━   0%
  Dep Graph   ━━━━━━━━━━━━━━━━━━━━━━   0%
  Security    ━━━━━━━━━━━━━━━━━━━━━━   0%
```

---

## Advanced: Full Interactive Mode (Textual)

For completely interactive experience:

### Installation

```bash
pip install textual textual-dev
```

### Interactive File Browser

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DirectoryTree, DataTable, Static
from textual.containers import Horizontal, Vertical

class RALFNotesApp(App):
    """RALF Notes Interactive TUI"""

    CSS = """
    Screen {
        background: $surface;
    }

    DirectoryTree {
        width: 40;
        border: solid $primary;
    }

    #stats {
        height: 10;
        border: solid $success;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("p", "process", "Process Selected"),
        ("c", "clear_cache", "Clear Cache"),
    ]

    def compose(self) -> ComposeResult:
        """Create UI layout"""
        yield Header()

        with Horizontal():
            # File tree on left
            yield DirectoryTree("/path/to/source")

            # Stats on right
            with Vertical():
                yield Static("Statistics", id="stats")
                yield DataTable()

        yield Footer()

    def action_process(self):
        """Process selected files"""
        selected = self.query_one(DirectoryTree).selected
        # Process files...

    def action_clear_cache(self):
        """Clear cache"""
        clear_cache()
        self.notify("Cache cleared!")

# Run the app
if __name__ == "__main__":
    app = RALFNotesApp()
    app.run()
```

---

## Implementation Plan

### Week 1: Basic Rich Integration (4 hours)

1. **Install dependencies:**
   ```bash
   pip install rich pyfiglet
   ```

2. **Create ui/ module:**
   ```bash
   mkdir ui
   touch ui/__init__.py
   touch ui/banner.py
   touch ui/progress.py
   ```

3. **Add banner to main.py**
4. **Replace basic logging with Rich logging**
5. **Test with existing code**

### Week 2: Progress Bars (4 hours)

1. **Create progress.py module**
2. **Update main.py to use progress bars**
3. **Add live status display**
4. **Test with file processing**

### Week 3: Advanced Features (8 hours)

1. **Live section generation progress**
2. **Cache statistics display**
3. **Error highlighting**
4. **Summary tables**
5. **Color themes**

### Week 4: Interactive Mode (Optional, 16 hours)

1. **Install Textual**
2. **Create interactive app**
3. **File browser widget**
4. **Configuration editor**
5. **Real-time log viewer**

---

## Configuration

Add to `config.py`:

```python
# --- UI Configuration ---
ENABLE_RICH_UI = True              # Use Rich for beautiful output
SHOW_ASCII_BANNER = True           # Show ASCII art banner
SHOW_PROGRESS_BARS = True          # Show progress bars
SHOW_LIVE_STATUS = True            # Show live status updates
ENABLE_COLORS = True               # Use colors in output
THEME = "cyan"                     # Color theme: cyan, green, magenta, blue

# ASCII Art Settings
BANNER_FONT = "slant"              # pyfiglet font: slant, banner, big, etc.
BANNER_COLOR = "cyan"              # Banner color

# Progress Settings
PROGRESS_STYLE = "bar"             # bar, dots, spinner
SHOW_TIME_REMAINING = True         # Show ETA
SHOW_SPEED = True                  # Show files/min
```

---

## Benefits

### User Experience:
- ✅ Know what's happening at all times
- ✅ See progress clearly
- ✅ Beautiful, professional output
- ✅ Catch errors easily (highlighted in red)
- ✅ Understand performance (speed metrics)

### Developer Experience:
- ✅ Easy to debug (rich tracebacks)
- ✅ Better logging (formatted)
- ✅ Testing feedback (visual)

### Performance:
- ✅ No performance impact (Rich is fast)
- ✅ Can disable for CI/CD (`ENABLE_RICH_UI=False`)
- ✅ Works in all terminals

---

## Compatibility

### Terminal Support:
- ✅ macOS Terminal
- ✅ iTerm2
- ✅ Windows Terminal
- ✅ Linux terminals (xterm, gnome-terminal)
- ✅ VS Code integrated terminal
- ✅ SSH sessions

### Fallback:
```python
# Detect terminal capabilities
from rich.console import Console

console = Console()

if not console.is_terminal:
    # Running in CI/CD or piped output
    # Fall back to basic logging
    USE_RICH = False
```

---

## Testing

### Manual Testing:
```bash
# Test with rich
python main.py

# Test without rich (fallback)
ENABLE_RICH_UI=false python main.py

# Test piped output
python main.py > output.txt
```

### Unit Tests:
```python
def test_banner():
    """Test banner generation"""
    from ui.banner import show_banner
    show_banner()  # Visual inspection

def test_progress():
    """Test progress bars"""
    from ui.progress import create_progress
    progress = create_progress()
    assert progress is not None
```

---

## Examples from Other Projects

### Similar TUI Apps:
- **Poetry** - Uses Rich for beautiful output
- **Black** - Rich progress bars
- **Pytest** - Rich assertion output
- **Typer** - CLI framework with Rich integration
- **HTTPie** - Beautiful API client

### Inspiration:
- Docker CLI (progress for pulls)
- npm/yarn (dependency installation)
- Git (colored diffs)
- Kubernetes CLI (table outputs)

---

## Dependencies

```bash
# Minimal (Rich only)
pip install rich pyfiglet

# Full (with Textual)
pip install rich pyfiglet textual textual-dev

# Optional (more ASCII art)
pip install art colorama
```

### requirements.txt addition:
```
rich>=13.0.0
pyfiglet>=0.8.0
textual>=0.50.0  # Optional, for interactive mode
```

---

## Rollback Plan

If TUI has issues, easy to disable:

### Option 1: Config flag
```python
# config.py
ENABLE_RICH_UI = False
```

### Option 2: Environment variable
```bash
export RALF_RICH_UI=false
python main.py
```

### Option 3: Command line flag
```bash
python main.py --no-rich
```

---

## Summary

**Transform RALF Notes into a beautiful TUI app with:**
- 🎨 ASCII art banner
- 📊 Real-time progress bars
- 🌈 Colorful output
- 📈 Live statistics
- ⚡ Professional appearance

**Recommended approach:**
1. Start with Rich (easy, beautiful)
2. Add progress bars (immediate value)
3. Enhance gradually (banner, stats, colors)
4. Consider Textual for full interactivity (optional)

**Effort:** 4-16 hours depending on features
**Impact:** Major UX improvement, professional appearance

**Next:** See implementation examples above and `ideas/11-terminal-ui-enhancement.md` for full guide.
