"""
Box: ASCII Art & UI Components

Responsibility: Provide ASCII art banners and structured UI components for RALF Note
"""

from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.columns import Columns
from rich.console import Group
from rich.align import Align


# Main ASCII Art
RALF_ASCII = """
 ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗ ████████╗███████╗
 ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝
 ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║   ██║   █████╗  
 ██╔══██╗██╔══██║██║     ██╔══╝      ██║╚██╗██║██║   ██║   ██║   ██╔══╝  
 ██║  ██║██║  ██║███████╗██║         ██║ ╚████║╚██████╔╝   ██║   ███████╗
 ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝         ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝
"""

# Simple Version
RALF_ASCII_SIMPLE = """
 ██████╗  █████╗ ██╗     ███████╗
 ██╔══██╗██╔══██╗██║     ██╔════╝
 ██████╔╝███████║██║     █████╗  
 ██╔══██╗██╔══██║██║     ██╔══╝  
 ██║  ██║██║  ██║███████╗██║     
 ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     
"""


def get_banner(style: str = 'full') -> str:
    """Get banner string (legacy support)."""
    if style == 'simple':
        return RALF_ASCII_SIMPLE
    return RALF_ASCII


class Banner:
    """
    Structured banner for RALF Note.
    """
    
    @staticmethod
    def get_renderable(style: str = 'full', subtitle: str = ""):
        """Get rich renderable for the banner."""
        ascii_text = RALF_ASCII if style == 'full' else RALF_ASCII_SIMPLE
        
        banner_text = Text(ascii_text, style="bold cyan")
        
        content = [Align.center(banner_text)]
        
        if subtitle:
            content.append(Align.center(Text(subtitle, style="italic dim")))
        else:
            content.append(Align.center(Text("🚀 RECURSIVE AI-POWERED LEARNING FRAMEWORK", style="bold magenta")))
            content.append(Align.center(Text("🧠 OBSIDIAN DOC GENERATOR", style="dim")))

        return Panel(
            Group(*content),
            border_style="bright_blue",
            padding=(1, 2)
        )


def get_dashboard(
    model: str = "N/A",
    target: str = "N/A",
    status: str = "Ready",
    progress: float = 0.0,
    current_file: str = "",
    tuned: bool = False,
    speed: str = ""
):
    """
    Create a dashboard-style panel for real-time progress.
    """
    # Info Table
    info_table = Table.grid(padding=(0, 2))
    info_table.add_column(style="bold cyan")
    info_table.add_column()
    
    tuning_status = "[bold green]Optimized[/bold green]" if tuned else "[bold yellow]Default[/bold yellow]"
    
    info_table.add_row("Model:", f"{model} ({tuning_status})")
    info_table.add_row("Target:", f"[italic]{target}[/italic]")
    info_table.add_row("Status:", f"[bold]{status}[/bold]")
    
    if speed:
        info_table.add_row("Speed:", f"[bold magenta]{speed}[/bold magenta]")
    
    # Progress bar string
    width = 20
    filled = int((progress / 100) * width)
    bar = "█" * filled + "░" * (width - filled)
    progress_str = f"[{bar}] {progress:3.1f}%"
    
    # Bottom columns
    footer = Columns([
        Text(f"📂 {current_file or 'Waiting...'}", style="dim", overflow="ellipsis"),
        Align.right(Text(progress_str, style="bold green"))
    ], expand=True)
    
    return Panel(
        Group(info_table, Text(""), footer),
        title="[bold blue]RALF Dashboard[/bold blue]",
        border_style="cyan",
        padding=(0, 1)
    )