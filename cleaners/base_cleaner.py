from abc import ABC, abstractmethod

class BaseCleaner(ABC):
    """
    Box: Cleaner interface

    Input: text to clean
    Output: cleaned text
    Responsibility: Define cleaning contract
    """

    @abstractmethod
    def clean(self, text: str) -> str:
        """Clean text."""
        pass

    def __call__(self, text: str) -> str:
        """Allow cleaner(text) syntax"""
        return self.clean(text)
