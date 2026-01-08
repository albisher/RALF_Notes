class TokenEstimator:
    """
    Box: Token Estimator
    
    Input: text
    Output: estimated number of tokens
    Responsibility: Estimate the number of tokens in a given text.
    """
    @staticmethod
    def estimate(text: str) -> float:
        """Rough token estimator: words * 1.3 + overhead."""
        return len(text.split()) * 1.3 + 100
