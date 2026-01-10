"""
Box: Console Manager

Responsibility: Centralized console output with consistent styling
"""

from rich.console import Console as RichConsole
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from typing import Optional, Dict, Any


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
        """
        Initialize console.

        Args:
            quiet: If True, suppress output
        """
        self.console = RichConsole(theme=RALF_THEME)
        self.quiet = quiet

    def print(self, message: str, style: Optional[str] = None):
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

    def processing(self, message: str, icon: str = "⚙️"):
        """Processing message."""
        self.print(f"{icon}  {message}", style="dim")

    def file(self, action: str, filename: str):
        """File operation message."""
        self.print(f"📄  {action}: [path]{filename}[/path]")

    def panel(self, content: str, title: str = "", style: str = "info"):
        """Display content in a panel."""
        if not self.quiet:
            self.console.print(Panel(content, title=title, border_style=style))

    def banner(self, banner_text: str):
        """Display ASCII banner."""
        if not self.quiet:
            self.console.print(Text(banner_text, style="bold cyan"))

    def rule(self, title: str = "", style: str = "dim"):
        """Display horizontal rule."""
        if not self.quiet:
            self.console.rule(title, style=style)

    def table_from_dict(self, data: Dict[str, Any], title: str = ""):
        """Display key-value pairs as table."""
        if self.quiet:
            return

        table = Table(title=title, show_header=False)
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="white")

        for key, value in data.items():
            table.add_row(str(key), str(value))

        self.console.print(table)
