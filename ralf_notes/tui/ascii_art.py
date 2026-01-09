"""
Box: ASCII Art

Responsibility: Provide ASCII art banners for RALF Note
"""

# Main banner (full) - with dynamic status lines
RALF_BANNER = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║  ███████  ████   █      █████     ███  ██  ████  ████████ ████████  ║
║  ██   ██ ██  ██  ██     ██       ██ ██ ██ ██  ██    ██    ██       ║
║  ███████ ██████  ██     █████    ██ ████  ██  ██    ██    ██████   ║
║  ██   ██ ██  ██  ██     ██       ██  ███  ██  ██    ██    ██       ║
║  ██   ██ ██  ██  █████  ██       ██   ██  ████      ██    ████████ ║
║                                                                      ║
║              🚀 RECURSIVE AI-POWERED LEARNING FRAMEWORK              ║
║                       🧠 OBSIDIAN DOC GENERATOR                      ║
║                             ✨ VERSION 2.1                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# Simple banner
RALF_SIMPLE = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                            ┃
┃  ███████  ████   █      █████     ███  ██  ████  ████████ ┃
┃  ██   ██ ██  ██  ██     ██       ██ ██ ██ ██  ██    ██   ┃
┃  ███████ ██████  ██     █████    ██ ████  ██  ██    ██   ┃
┃  ██   ██ ██  ██  █████  ██       ██   ██  ████      ██   ┃
┃                                                            ┃
┃  🚀 AI-Powered Documentation Generator  ✨ v2.1            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

# Compact banner
RALF_COMPACT = """
╭─────────────────────────────────────╮
│  🚀 RALF Note v2.1 - Doc Generator  │
╰─────────────────────────────────────╯
"""


def get_banner(style: str = 'full') -> str:
    """
    Get banner based on style.

    Args:
        style: Banner style ('full', 'simple', 'compact')

    Returns:
        ASCII banner string
    """
    banners = {
        'full': RALF_BANNER,
        'simple': RALF_SIMPLE,
        'compact': RALF_COMPACT
    }
    return banners.get(style, RALF_COMPACT)


def create_progress_bar(percent: float, width: int = 10) -> str:
    """
    Create a progress bar with filled blocks.

    Args:
        percent: Progress percentage (0-100)
        width: Width of progress bar in characters

    Returns:
        Progress bar string
    """
    filled = int((percent / 100) * width)
    bar = '▓' * filled + '░' * (width - filled)
    return bar


def get_banner_with_status(
    style: str = 'full',
    model: str = 'ministral-3:3b',
    target: str = 'to_obsidian',
    source: str = '',
    files: int = 0,
    progress: float = 0.0,
    status: str = 'ready'
) -> str:
    """
    Get banner with dynamic status lines.

    Args:
        style: Banner style ('full', 'simple', 'compact')
        model: Model name
        target: Target directory
        source: Source directory
        files: Number of files
        progress: Progress percentage (0-100)
        status: Status message

    Returns:
        ASCII banner with status lines
    """
    base_banner = get_banner(style)

    # Only add status for full banner
    if style != 'full':
        return base_banner

    # Create progress bars
    status_bar = create_progress_bar(progress if status == 'processing' else 100, 7)
    file_progress = create_progress_bar(progress, 10)

    # Build status lines
    status_lines = f"""║  [status]  {status_bar} {int(progress):3d}%  [model] {model:<20s} ║
║  [target]  {target:<56s} ║"""

    if source:
        status_lines += f"""
║  [source]  {source:<20s}  [files] {files:<4d}  [progress] {file_progress} {int(progress):3d}%   ║"""

    # Insert status lines before the closing border
    banner_lines = base_banner.strip().split('\n')
    banner_lines.insert(-1, status_lines)

    return '\n'.join(banner_lines)
