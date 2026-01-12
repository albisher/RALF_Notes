# complex_sample.py
import os
import re
from typing import List, Dict, Optional

class DataProcessor:
    """
    A class to process complex data structures.
    It can load, clean, and analyze data from various sources.
    """
    
    # Class attribute to define supported file types
    SUPPORTED_TYPES = ['csv', 'json']

    def __init__(self, data_source: str):
        """
        Initializes the DataProcessor with a data source.
        
        Args:
            data_source (str): The path to the data source file.
        """
        if not os.path.exists(data_source):
            raise FileNotFoundError(f"Data source not found: {data_source}")
            
        self.source = data_source
        self.data = self._load_data()

    def _load_data(self) -> List[Dict]:
        """
        Private method to load data based on file type.
        """
        _, file_ext = os.path.splitext(self.source)
        ext = file_ext.lower().strip('.')
        
        if ext not in self.SUPPORTED_TYPES:
            raise ValueError(f"Unsupported file type: {ext}")
            
        # In a real scenario, we would load the file here.
        # For this example, we'll return dummy data.
        return [
            {'id': 1, 'name': 'Item A', 'value': 100, 'email': 'test@example.com'},
            {'id': 2, 'name': 'Item B', 'value': 250, 'email': 'user@example.com'},
        ]

    def clean_emails(self) -> int:
        """
        Removes invalid emails from the loaded data.
        
        Returns:
            int: The number of invalid emails removed.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        original_count = len(self.data)
        
        self.data = [
            row for row in self.data 
            if 'email' in row and re.match(email_regex, row['email'])
        ]
        
        return original_count - len(self.data)

def analyze_data(processor: DataProcessor) -> Dict[str, float]:
    """
    Analyzes the data from a DataProcessor instance.
    
    Args:
        processor (DataProcessor): An instance of DataProcessor.
        
    Returns:
        Dict[str, float]: A dictionary with analysis results.
    """
    total_value = sum(row.get('value', 0) for row in processor.data)
    average_value = total_value / len(processor.data) if processor.data else 0
    
    return {
        'total_records': len(self.data),
        'total_value': total_value,
        'average_value': average_value
    }

# Example of how to use the above code
if __name__ == '__main__':
    # This block will not be included in the analysis
    # as it is behind an if __name__ == '__main__': guard.
    processor = DataProcessor('dummy_data.csv')
    removed_count = processor.clean_emails()
    print(f"Removed {removed_count} invalid emails.")
    
    analysis = analyze_data(processor)
    print("Analysis Results:")
    for key, value in analysis.items():
        print(f"- {key}: {value}")