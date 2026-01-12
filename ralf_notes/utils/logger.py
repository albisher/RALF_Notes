import logging
from pathlib import Path
from typing import Optional

def setup_logging(log_level: str = "INFO", log_file: Optional[Path] = None):
    """Set up logging for RALF Notes."""
    if log_file is None:
        log_file = Path.home() / ".ralf-notes" / "ralf-notes.log"

    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Remove all handlers associated with the root logger to avoid duplicate messages
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
