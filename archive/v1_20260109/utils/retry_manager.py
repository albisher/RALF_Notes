import time
import logging
from typing import Callable, Any

class RetryManager:
    """
    Box: Retry Manager
    
    Input: a function to execute, number of attempts
    Output: the result of the function
    Responsibility: Wrap a function call with retry logic.
    """

    def __init__(self, attempts: int = 3, delay: int = 2):
        self.attempts = attempts
        self.delay = delay
        self.logger = logging.getLogger(__name__)

    def execute(self, func: Callable, *args, **kwargs) -> Any:
        for attempt in range(self.attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt == self.attempts - 1:
                    self.logger.error(f"All retries failed: {e}")
                    raise
                time.sleep(self.delay ** attempt)
        return None
