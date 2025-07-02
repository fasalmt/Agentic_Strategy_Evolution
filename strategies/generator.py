import random

from .moving_average import MovingAverageCrossoverStrategy


def generate_random_strategy() -> MovingAverageCrossoverStrategy:
    """Generate a simple moving average crossover strategy.

    Returns an instance of :class:`MovingAverageCrossoverStrategy` with random
    short and long moving average windows.
    """
    short_window = random.randint(5, 20)
    long_window = random.randint(short_window + 1, 60)
    return MovingAverageCrossoverStrategy(short_window, long_window)
