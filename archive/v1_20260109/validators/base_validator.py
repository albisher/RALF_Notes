from abc import ABC, abstractmethod
from typing import Tuple

class BaseValidator(ABC):
    """
    Box: Validator interface

    Input: text to validate
    Output: (is_valid, error_message)
    Responsibility: Define validation contract
    """

    @abstractmethod
    def validate(self, text: str) -> Tuple[bool, str]:
        """
        Validate text.

        Returns:
            (True, "") if valid
            (False, "error message") if invalid
        """
        pass

    def __call__(self, text: str) -> bool:
        """Allow validator(text) syntax"""
        is_valid, _ = self.validate(text)
        return is_valid
