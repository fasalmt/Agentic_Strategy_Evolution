import random
from typing import List

def generate_strategy(length: int = 5) -> List[int]:
    """Generate a simple strategy consisting of a list of integers."""
    return [random.randint(0, 10) for _ in range(length)]


def evaluate_strategy(strategy: List[int]) -> int:
    """Evaluate a strategy by summing its elements."""
    if not isinstance(strategy, list):
        raise TypeError("Strategy must be a list")
    if not all(isinstance(x, int) for x in strategy):
        raise ValueError("All elements in strategy must be integers")
    return sum(strategy)
