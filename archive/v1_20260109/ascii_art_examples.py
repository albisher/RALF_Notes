#!/usr/bin/env python3
"""
Python ASCII Art and Terminal Color Examples (2026)
Comprehensive demonstration of modern libraries for creating colored ASCII art banners.
"""

# ============================================================================
# 1. BASIC ASCII ART WITH PYFIGLET
# ============================================================================

def example_basic_pyfiglet():
    """Basic pyfiglet usage with different fonts."""
    try:
        import pyfiglet

        print("\n" + "="*80)
        print("EXAMPLE 1: Basic PyFiglet")
        print("="*80)

        # Simple text with default font
        result = pyfiglet.figlet_format("Hello World")
        print(result)

        # Using slant font
        result = pyfiglet.figlet_format("Documentation", font='slant')
        print(result)

        # Using banner3 font
        result = pyfiglet.figlet_format("RALF", font='banner3')
        print(result)

        # List available fonts (commented out - too many)
        # fonts = pyfiglet.FigletFont.getFonts()
        # print(f"\nTotal fonts available: {len(fonts)}")

    except ImportError:
        print("Install with: pip install pyfiglet")


# ============================================================================
# 2. COLORED TEXT WITH TERMCOLOR
# ============================================================================

def example_termcolor():
    """Using termcolor for colored text."""
    try:
        from termcolor import colored, cprint

        print("\n" + "="*80)
        print("EXAMPLE 2: Termcolor Basic Usage")
        print("="*80)

        # Basic colors
        print(colored('Hello, World!', 'red'))
        print(colored('Hello, World!', 'green'))
        print(colored('Hello, World!', 'yellow'))
        print(colored('Hello, World!', 'blue'))
        print(colored('Hello, World!', 'magenta'))
        print(colored('Hello, World!', 'cyan'))
        print(colored('Hello, World!', 'white'))

        # With attributes
        print(colored('Bold text', 'red', attrs=['bold']))
        print(colored('Underlined text', 'green', attrs=['underline']))
        print(colored('Bold + Underlined', 'yellow', attrs=['bold', 'underline']))

        # Background colors
        print(colored('Text with background', 'white', 'on_red'))
        print(colored('Green on grey', 'green', 'on_grey'))

    except ImportError:
        print("Install with: pip install termcolor")


# ============================================================================
# 3. PYFIGLET + TERMCOLOR COMBINATION
# ============================================================================

def example_pyfiglet_termcolor():
    """Combining pyfiglet with termcolor for colored ASCII art."""
    try:
        import pyfiglet
        from termcolor import colored

        print("\n" + "="*80)
        print("EXAMPLE 3: PyFiglet + Termcolor")
        print("="*80)

        # Create ASCII art and color it
        ascii_art = pyfiglet.figlet_format("RALF Notes", font='slant')
        colored_art = colored(ascii_art, 'cyan', attrs=['bold'])
        print(colored_art)

        # Different colors for different text
        title = pyfiglet.figlet_format("Documentation", font='banner')
        print(colored(title, 'yellow'))

        subtitle = pyfiglet.figlet_format("Tool", font='banner')
        print(colored(subtitle, 'green'))

    except ImportError as e:
        print(f"Install with: pip install pyfiglet termcolor\nError: {e}")


# ============================================================================
# 4. RICH LIBRARY - MODERN TERMINAL FORMATTING
# ============================================================================

def example_rich_basic():
    """Using Rich for modern terminal output."""
    try:
        from rich.console import Console
        from rich.panel import Panel
        from rich.text import Text
        from rich import box

        console = Console()

        print("\n" + "="*80)
        print("EXAMPLE 4: Rich Library Basics")
        print("="*80)

        # Basic colored text
        console.print("Hello, World!", style="bold magenta")
        console.print("This is [bold red]bold red[/] and [italic green]italic green[/]")

        # RGB colors (true color)
        console.print("RGB Color", style="rgb(255,0,255)")
        console.print("Another RGB", style="on rgb(50,50,100) white")

        # Hex colors
        console.print("Hex color", style="#FF00FF")

        # Panel with border
        console.print(Panel("Documentation Tool",
                           title="RALF Notes",
                           border_style="cyan",
                           box=box.DOUBLE))

        # Text with gradient (requires rich)
        text = Text("Gradient Text")
        text.stylize("bold magenta", 0, 8)
        text.stylize("bold cyan", 8, 12)
        console.print(text)

    except ImportError:
        print("Install with: pip install rich")


# ============================================================================
# 5. RICH-PYFIGLET - COMBINING RICH AND PYFIGLET
# ============================================================================

def example_rich_pyfiglet():
    """Using rich-pyfiglet for advanced colored ASCII art banners."""
    try:
        from rich_pyfiglet import RichFiglet
        from rich.console import Console

        console = Console()

        print("\n" + "="*80)
        print("EXAMPLE 5: Rich-PyFiglet (Advanced)")
        print("="*80)

        # Basic usage
        banner = RichFiglet("RALF Notes", font="slant", colors="cyan")
        console.print(banner)

        # With gradient
        banner_gradient = RichFiglet(
            "Documentation",
            font="banner3",
            colors=["#FF0000", "#00FF00", "#0000FF"],  # RGB gradient
            direction="horizontal"
        )
        console.print(banner_gradient)

        # With border
        banner_border = RichFiglet(
            "Welcome",
            font="standard",
            colors=["magenta", "cyan"],
            border=True,
            border_color="yellow"
        )
        console.print(banner_border)

    except ImportError:
        print("Install with: pip install rich-pyfiglet")


# ============================================================================
# 6. ASCII-MAGIC - IMAGE TO ASCII ART
# ============================================================================

def example_ascii_magic():
    """Convert images to colored ASCII art."""
    try:
        from ascii_magic import AsciiArt
        import colorama

        print("\n" + "="*80)
        print("EXAMPLE 6: ascii-magic (Image to ASCII)")
        print("="*80)

        # Note: This requires an actual image file
        # Uncomment if you have an image:
        # colorama.init()
        # my_art = AsciiArt.from_image('path/to/image.jpg')
        # my_art.to_terminal(columns=80)

        print("ascii-magic converts images to colored ASCII art")
        print("Supports 24-bit color (16 million colors)")
        print("\nBasic usage:")
        print("  from ascii_magic import AsciiArt")
        print("  import colorama")
        print("  colorama.init()  # For Windows")
        print("  art = AsciiArt.from_image('image.jpg')")
        print("  art.to_terminal(columns=120)")

    except ImportError:
        print("Install with: pip install ascii-magic")


# ============================================================================
# 7. COLORAMA - CROSS-PLATFORM COLOR SUPPORT
# ============================================================================

def example_colorama():
    """Using colorama for cross-platform ANSI color support."""
    try:
        from colorama import init, Fore, Back, Style

        # Initialize colorama (especially important on Windows)
        init(autoreset=True)

        print("\n" + "="*80)
        print("EXAMPLE 7: Colorama (Cross-platform)")
        print("="*80)

        # Foreground colors
        print(Fore.RED + 'Red text')
        print(Fore.GREEN + 'Green text')
        print(Fore.YELLOW + 'Yellow text')
        print(Fore.BLUE + 'Blue text')
        print(Fore.MAGENTA + 'Magenta text')
        print(Fore.CYAN + 'Cyan text')

        # Background colors
        print(Back.RED + 'Red background')
        print(Back.GREEN + 'Green background')

        # Styles
        print(Style.DIM + 'Dim text')
        print(Style.BRIGHT + 'Bright text')

        # Combining styles
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT + 'Bright cyan on black')

        # Reset (autoreset=True does this automatically)
        print(Style.RESET_ALL + 'Normal text')

    except ImportError:
        print("Install with: pip install colorama")


# ============================================================================
# 8. BLESSED - ADVANCED TERMINAL CONTROL
# ============================================================================

def example_blessed():
    """Using blessed for advanced terminal capabilities."""
    try:
        from blessed import Terminal

        term = Terminal()

        print("\n" + "="*80)
        print("EXAMPLE 8: Blessed (Advanced Terminal Control)")
        print("="*80)

        # Colors
        print(term.red('Red text'))
        print(term.green('Green text'))
        print(term.yellow('Yellow text'))
        print(term.blue('Blue text'))

        # RGB colors (true color)
        print(term.color_rgb(255, 0, 255)('RGB Magenta'))
        print(term.on_color_rgb(50, 50, 150)('RGB Background'))

        # Styles
        print(term.bold('Bold text'))
        print(term.underline('Underlined text'))
        print(term.reverse('Reversed text'))

        # Terminal info
        print(f"\nTerminal width: {term.width}")
        print(f"Terminal height: {term.height}")
        print(f"Number of colors: {term.number_of_colors}")

        # Named colors (X11 colors)
        print(term.cornflowerblue('Cornflower Blue'))
        print(term.orangered('Orange Red'))

    except ImportError:
        print("Install with: pip install blessed")


# ============================================================================
# 9. COMPLETE DOCUMENTATION TOOL BANNER EXAMPLE
# ============================================================================

def create_documentation_banner():
    """
    Complete example: Creating a catchy banner for a documentation tool.
    Uses multiple techniques for maximum visual impact.
    """
    try:
        import pyfiglet
        from rich.console import Console
        from rich.panel import Panel
        from rich.text import Text
        from rich import box
        from termcolor import colored

        console = Console()

        print("\n" + "="*80)
        print("EXAMPLE 9: Complete Documentation Tool Banner")
        print("="*80)

        # Method 1: PyFiglet + Termcolor (simple, cross-platform)
        print("\n--- Method 1: PyFiglet + Termcolor ---")
        banner_text = pyfiglet.figlet_format("RALF Notes", font='slant')
        print(colored(banner_text, 'cyan', attrs=['bold']))
        print(colored("  Your AI-Powered Documentation Assistant", 'yellow'))
        print(colored("  Version 2.0.0 | 2026 Edition\n", 'green'))

        # Method 2: Rich Panel (modern, feature-rich)
        print("\n--- Method 2: Rich Panel ---")
        title_text = Text("RALF Notes", style="bold magenta")
        subtitle = Text("\nYour AI-Powered Documentation Assistant", style="italic cyan")
        version = Text("\nVersion 2.0.0 | 2026 Edition", style="dim green")

        panel_content = Text()
        panel_content.append("🚀 ", style="bold yellow")
        panel_content.append("RALF Notes", style="bold magenta on black")
        panel_content.append(" 🚀\n", style="bold yellow")
        panel_content.append("\nYour AI-Powered Documentation Assistant", style="italic cyan")
        panel_content.append("\nVersion 2.0.0 | 2026 Edition", style="dim green")

        console.print(Panel(
            panel_content,
            title="[bold yellow]Welcome[/]",
            border_style="cyan",
            box=box.DOUBLE,
            padding=(1, 2)
        ))

        # Method 3: Custom with RGB colors
        print("\n--- Method 3: Rich with True Color (RGB) ---")
        console.print("╔═══════════════════════════════════════════╗", style="rgb(0,255,255)")
        console.print("║  [bold rgb(255,0,255)]RALF Notes[/]                            ║", style="rgb(0,255,255)")
        console.print("║  [italic rgb(0,255,255)]AI-Powered Documentation Tool[/]       ║", style="rgb(0,255,255)")
        console.print("║  [dim rgb(0,255,0)]Version 2.0.0 - 2026[/]                  ║", style="rgb(0,255,255)")
        console.print("╚═══════════════════════════════════════════╝", style="rgb(0,255,255)")

    except ImportError as e:
        print(f"Install required packages: pip install pyfiglet rich termcolor\nError: {e}")


# ============================================================================
# 10. RICH-PYFIGLET ADVANCED BANNER
# ============================================================================

def create_advanced_banner():
    """
    Advanced banner using rich-pyfiglet with gradients and animations.
    """
    try:
        from rich_pyfiglet import RichFiglet
        from rich.console import Console
        from rich.panel import Panel

        console = Console()

        print("\n" + "="*80)
        print("EXAMPLE 10: Advanced Rich-PyFiglet Banner")
        print("="*80)

        # Horizontal gradient banner
        banner = RichFiglet(
            "RALF Notes",
            font="slant",
            colors=["#FF0080", "#FF8000", "#FFFF00", "#00FF00", "#00FFFF"],
            direction="horizontal",
            border=True,
            border_color="white",
            padding=(0, 2)
        )
        console.print(banner)

        # Vertical gradient
        subtitle = RichFiglet(
            "Documentation",
            font="banner",
            colors=["cyan", "blue", "magenta"],
            direction="vertical"
        )
        console.print(subtitle)

        # Simple colored banner
        tagline = RichFiglet(
            "AI Powered",
            font="digital",
            colors="green",
            border=True,
            border_color="yellow"
        )
        console.print(tagline)

    except ImportError:
        print("Install with: pip install rich-pyfiglet")


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

def performance_comparison():
    """
    Compare performance of different libraries.
    """
    import time

    print("\n" + "="*80)
    print("PERFORMANCE COMPARISON")
    print("="*80)

    iterations = 1000

    # Test pyfiglet
    try:
        import pyfiglet
        start = time.time()
        for _ in range(iterations):
            _ = pyfiglet.figlet_format("Test")
        pyfiglet_time = time.time() - start
        print(f"PyFiglet: {pyfiglet_time:.4f}s for {iterations} iterations")
    except ImportError:
        print("PyFiglet not installed")

    # Test termcolor
    try:
        from termcolor import colored
        start = time.time()
        for _ in range(iterations):
            _ = colored("Test", 'red')
        termcolor_time = time.time() - start
        print(f"Termcolor: {termcolor_time:.4f}s for {iterations} iterations")
    except ImportError:
        print("Termcolor not installed")

    # Test Rich
    try:
        from rich.console import Console
        from io import StringIO
        console = Console(file=StringIO())  # Don't actually print
        start = time.time()
        for _ in range(iterations):
            console.print("Test", style="bold red")
        rich_time = time.time() - start
        print(f"Rich: {rich_time:.4f}s for {iterations} iterations")
    except ImportError:
        print("Rich not installed")

    # Test colorama
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
        start = time.time()
        for _ in range(iterations):
            _ = Fore.RED + "Test" + Style.RESET_ALL
        colorama_time = time.time() - start
        print(f"Colorama: {colorama_time:.4f}s for {iterations} iterations")
    except ImportError:
        print("Colorama not installed")


# ============================================================================
# CROSS-PLATFORM SUPPORT INFORMATION
# ============================================================================

def print_compatibility_info():
    """Print cross-platform compatibility information."""
    print("\n" + "="*80)
    print("CROSS-PLATFORM COMPATIBILITY")
    print("="*80)

    compatibility = {
        "PyFiglet": {
            "Windows": "✓ Full support",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "Requires color library (termcolor, Rich, etc.)"
        },
        "Termcolor": {
            "Windows": "✓ With colorama.init()",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "8 basic colors + attributes"
        },
        "Colorama": {
            "Windows": "✓ Full support (primary use case)",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "8 basic colors, ANSI codes"
        },
        "Rich": {
            "Windows": "✓ Windows Terminal (true color), ⚠ CMD (16 colors)",
            "macOS": "✓ Full support (true color)",
            "Linux": "✓ Full support (true color)",
            "Colors": "True color (16M colors), 256 colors, 8 colors"
        },
        "Blessed": {
            "Windows": "✓ Full support (Python 3.7+)",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "True color (24-bit RGB), 256 colors"
        },
        "Rich-PyFiglet": {
            "Windows": "✓ Same as Rich",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "True color + gradients"
        },
        "ascii-magic": {
            "Windows": "✓ With colorama.init()",
            "macOS": "✓ Full support",
            "Linux": "✓ Full support",
            "Colors": "24-bit color (16M colors)"
        }
    }

    for lib, support in compatibility.items():
        print(f"\n{lib}:")
        for platform, status in support.items():
            print(f"  {platform:15}: {status}")


# ============================================================================
# INSTALLATION GUIDE
# ============================================================================

def print_installation_guide():
    """Print installation guide for all libraries."""
    print("\n" + "="*80)
    print("INSTALLATION GUIDE")
    print("="*80)

    packages = {
        "ASCII Art Generation": [
            ("pyfiglet", "pip install pyfiglet"),
            ("art", "pip install art"),
        ],
        "Color Support": [
            ("colorama", "pip install colorama"),
            ("termcolor", "pip install termcolor"),
            ("Rich", "pip install rich"),
            ("blessed", "pip install blessed"),
        ],
        "Combined Solutions": [
            ("rich-pyfiglet", "pip install rich-pyfiglet"),
            ("ascii-magic", "pip install ascii-magic"),
        ],
        "TUI Frameworks": [
            ("asciimatics", "pip install asciimatics"),
            ("textual", "pip install textual"),
            ("textual-pyfiglet", "pip install textual-pyfiglet"),
        ]
    }

    for category, libs in packages.items():
        print(f"\n{category}:")
        for name, command in libs:
            print(f"  {name:20} → {command}")

    print("\n" + "-"*80)
    print("Install all at once:")
    print("  pip install pyfiglet art colorama termcolor rich blessed rich-pyfiglet ascii-magic asciimatics")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print(" Python ASCII Art & Terminal Colors - Comprehensive Examples (2026)")
    print("="*80)

    # Run all examples
    examples = [
        ("Basic PyFiglet", example_basic_pyfiglet),
        ("Termcolor", example_termcolor),
        ("PyFiglet + Termcolor", example_pyfiglet_termcolor),
        ("Rich Library", example_rich_basic),
        ("Rich-PyFiglet", example_rich_pyfiglet),
        ("ascii-magic", example_ascii_magic),
        ("Colorama", example_colorama),
        ("Blessed", example_blessed),
        ("Documentation Banner", create_documentation_banner),
        ("Advanced Banner", create_advanced_banner),
    ]

    for name, func in examples:
        try:
            func()
        except Exception as e:
            print(f"\nError in {name}: {e}")

    # Additional info
    performance_comparison()
    print_compatibility_info()
    print_installation_guide()

    print("\n" + "="*80)
    print(" Examples Complete!")
    print("="*80)
