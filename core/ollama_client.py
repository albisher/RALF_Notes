from typing import Optional, Dict, Any
from ollama import Client, ResponseError
from dataclasses import dataclass
import logging
from config import MAX_CTX

logger = logging.getLogger(__name__)

@dataclass
class ModelInfo:
    name: str
    size: int
    family: str
    context_size: int

class OllamaClient:
    """
    Box: Ollama API client wrapper

    Input: host URL
    Output: API responses
    Responsibility: Manage connection to Ollama
    """

    def __init__(self, host: str = 'http://127.0.0.1:11434'):
        self.host = host
        self._client = Client(host=host)

    def generate(
        self,
        model: str,
        prompt: str,
        system: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        stream: bool = True
    ) -> str:
        """
        Generate response from Ollama.

        Input: model name, prompt, options
        Output: generated text
        """
        kwargs = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        if system:
            kwargs["system"] = system
        if options:
            kwargs["options"] = options

        if stream:
            stream_resp = self._client.generate(**kwargs)
            return "".join(chunk['response'] for chunk in stream_resp)
        else:
            return self._client.generate(**kwargs)['response']

    def list_models(self) -> Dict[str, ModelInfo]:
        """
        List available models.

        Input: none
        Output: dict of model name → ModelInfo
        """
        try:
            response = self._client.list()
            models = {}
            for model in response.get('models', []):
                models[model['name']] = ModelInfo(
                    name=model['name'],
                    size=model.get('size', 0),
                    family=model['name'].split(':')[0],
                    context_size=self._detect_context_size(model['name'])
                )
            return models
        except Exception as e:
            logger.error(f"Could not connect to Ollama to list models: {e}")
            return {}


    def model_exists(self, model_name: str) -> bool:
        """Check if model is available."""
        return model_name in self.list_models()

    def _detect_context_size(self, model_name: str) -> int:
        """Detect context size for model."""
        # Logic from Enhancement 2
        try:
            show_response = self._client.show(model_name)
            # Find parameter that indicates context size, e.g., 'parameter.context_size'
            # This is a placeholder, actual Ollama response structure might differ
            params = show_response.get('parameters', '').split('\\n')
            for p in params:
                if 'num_ctx' in p:
                    return int(p.split(' ')[-1])
            return MAX_CTX # Default from config if not found
        except Exception as e:
            logger.warning(f"Could not detect context size for {model_name}: {e}. Using default MAX_CTX.")
            return MAX_CTX
