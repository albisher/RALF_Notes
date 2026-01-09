import os
import logging
from datetime import datetime

class LoggerFactory:
    """
    Box: Logger Factory
    
    Input: log directory, log level
    Output: a configured logger instance
    Responsibility: Create and configure logger instances.
    """

    @staticmethod
    def get_logger(log_dir: str = './logs', level: int = logging.INFO):
        ensure_dir(log_dir)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file_path = os.path.join(log_dir, f'obsidian_generator_{timestamp}.log')

        logger = logging.getLogger(__name__)
        logger.setLevel(level)

        # Clear existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # File handler
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(level)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(console_formatter)

        class ConsoleFilter(logging.Filter):
            def filter(self, record):
                return not hasattr(record, 'detailed')

        console_handler.addFilter(ConsoleFilter())
        logger.addHandler(console_handler)
        
        return logger

def ensure_dir(directory: str):
    os.makedirs(directory, exist_ok=True)
