"""
Box: Console Manager

Responsibility: Centralized console output with consistent styling and high-level UI components
"""

from rich.console import Console as RichConsole
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.status import Status
from typing import Optional, Dict, Any, List
from contextlib import contextmanager


# Custom theme
RALF_THEME = Theme({
    "info": "cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "dim": "dim",
    "highlight": "bold magenta",
    "code": "bold blue",
    "path": "italic cyan",
    "step": "bold underline white",
    "substep": "dim italic white"
})


class Console:
    """
    Box: Console Manager

    Responsibility: Centralized console output with consistent styling
    """

    def __init__(self, quiet: bool = False):
        """
        Initialize console.

        Args:
            quiet: If True, suppress output
        """
        self.console = RichConsole(theme=RALF_THEME)
        self.quiet = quiet

    def print(self, message: Any, style: Optional[str] = None):
        """Print message with optional style."""
        if not self.quiet:
            self.console.print(message, style=style)

    def info(self, message: str, icon: str = "ℹ️"):
        """Info message."""
        self.print(f"{icon}  {message}", style="info")

    def success(self, message: str, icon: str = "✅"):
        """Success message."""
        self.print(f"{icon}  {message}", style="success")

    def warning(self, message: str, icon: str = "⚠️"):
        """Warning message."""
        self.print(f"{icon}  {message}", style="warning")

    def error(self, message: str, icon: str = "❌"):
        """Error message."""
        self.print(f"{icon}  {message}", style="error")

    def step(self, message: str, step_num: Optional[int] = None):
        """Step message."""
        prefix = f"Step {step_num}: " if step_num else "→ "
        self.print(f"\n{prefix}{message}", style="step")

    def substep(self, message: str):
        """Substep message."""
        self.print(f"  • {message}", style="substep")

    def processing(self, message: str, icon: str = "⚙️"):
        """Processing message."""
        self.print(f"{icon}  {message}", style="dim")

    def file(self, action: str, filename: str):
        """File operation message."""
        self.print(f"📄  {action}: [path]{filename}[/path]")

    def panel(self, content: Any, title: str = "", style: str = "info"):
        """Display content in a panel."""
        if not self.quiet:
            self.console.print(Panel(content, title=title, border_style=style))

    def banner(self, banner_obj: Any):
        """Display banner (can be string or renderable)."""
        if not self.quiet:
            self.console.print(banner_obj)

    def rule(self, title: str = "", style: str = "dim"):
        """Display horizontal rule."""
        if not self.quiet:
            self.console.rule(title, style=style)

    @contextmanager
    def status(self, message: str, spinner: str = "dots"):
        """Context manager for showing status with a spinner."""
        if self.quiet:
            yield
        else:
            with self.console.status(message, spinner=spinner) as status:
                yield status

    @staticmethod
    def format_speed(fps: float) -> str:
        """Format speed into a human-readable string without confusing fractions."""
        if fps <= 0:
            return "0 files/s"
        if fps >= 1000:
            return f"{int(fps/1000)}K files/s"
        if fps >= 1.0:
            return f"{int(fps)} files/s"
        
        # Slow speed (< 1 file/sec)
        fpm = fps * 60
        if fpm >= 1.0:
            return f"{int(fpm)} files/min"
        
        # Very slow speed (< 1 file/min)
        spf = 1.0 / fps
        return f"1 file / {int(spf)}s"

    def table_from_dict(self, data: Dict[str, Any], title: str = "", columns: List[str] = None):
        """Display key-value pairs as table."""
        if self.quiet:
            return

        table = Table(title=title, show_header=columns is not None)
        if columns:
            for col in columns:
                table.add_column(col, style="cyan" if "Key" in col or "Setting" in col else "white")
        else:
            table.add_column("Key", style="cyan")
            table.add_column("Value", style="white")

        for key, value in data.items():
            table.add_row(str(key), str(value))

        self.console.print(table)