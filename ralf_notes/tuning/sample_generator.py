from typing import List, Dict
from datetime import datetime # Added datetime import

class SampleCodeGenerator:
    """
    Box: Sample Code Generator

    Input: None
    Output: Sample code for testing
    Responsibility: Generate realistic code samples
    """

    # Note: These samples are illustrative and not fully functional. They serve as templates
    # for LLM context and should not be expected to execute as-is.
    SAMPLES: List[str] = [
        # Small sample (~500 chars)
        '''def calculate_total(items):
    """Calculate total with tax."""
    subtotal = sum(item.price for item in items)
    return subtotal * 1.08
''',
        # Medium sample (~2000 chars)
        '''class DataProcessor:
    """Process data with validation."""

    def __init__(self, config):
        self.config = config
        self.cache = {}

    def process(self, data):
        if not self.validate(data):
            raise ValueError("Invalid data")

        result = self.transform(data)
        self.cache[data.id] = result
        return result

    def validate(self, data):
        # Placeholder for data validation logic
        return True 

    def transform(self, data):
        # Placeholder for data transformation logic
        return {
            'id': data.id,
            'value': data.value, # Multiplier is not defined here
            'timestamp': "datetime.now()" # datetime not imported
        }
''',
        # Large sample (~5000 chars)
        '''class ComplexSystem:
    """A complex system with multiple components."""

    def __init__(self):
        # Placeholders for actual dependencies
        self.database = None 
        self.cache = None
        self.validator = None
        self.processor = None
        self.logger = None

    async def process_request(self, request):
        """Process incoming request with full pipeline."""
        try:
            # Validate input
            if not self.validator.validate(request):
                self.logger.warning(f"Invalid request: {request}")
                return {"error": "validation_failed"}

            # Check cache
            cache_key = self._generate_cache_key(request)
            if cached := await self.cache.get(cache_key):
                self.logger.info(f"Cache hit: {cache_key}")
                return cached

            # Process request
            data = await self.database.fetch(request.id)
            processed = self.processor.transform(data)

            # Store in cache
            await self.cache.set(cache_key, processed, ttl=3600)

            self.logger.info(f"Request processed: {request.id}")
            return processed

        except Exception as e:
            self.logger.error(f"Processing failed: {e}")
            raise

    def _generate_cache_key(self, request):
        return f"{request.type}:{request.id}:{request.version}"
'''
    ]

    def generate_sample(self, size: str = "medium") -> str:
        """
        Generate a sample code string.

        Args:
            size: "small", "medium", or "large"

        Returns:
            Sample code string
        """
        size_map: Dict[str, int] = {
            "small": 0,
            "medium": 1,
            "large": 2
        }

        idx: int = size_map.get(size, 1)
        return self.SAMPLES[idx]
