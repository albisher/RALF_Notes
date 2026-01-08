from dataclasses import dataclass
from typing import Optional

@dataclass
class GenerationOptions:
    """Represents the options for the Ollama client."""
    num_ctx: Optional[int] = None
    temperature: Optional[float] = None
    keep_alive: Optional[str] = None
    num_predict: Optional[int] = None
