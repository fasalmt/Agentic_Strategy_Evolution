import random

from .moving_average import MovingAverageCrossoverStrategy
from .rsi import RSIStrategy
from .bollinger import BollingerBandStrategy


def generate_random_strategy(allowed_types=None):
    """Generate a random trading strategy instance.

    Parameters
    ----------
    allowed_types : list[str] or None, optional
        Restrict the strategy types that can be generated. When ``None`` all
        available strategy types are considered.
    """

    choices = ["ma", "rsi", "bb"] if allowed_types is None else allowed_types
    choice = random.choice(choices)

    if choice == "ma":
        short_window = random.randint(5, 20)
        long_window = random.randint(short_window + 1, 60)
        return MovingAverageCrossoverStrategy(short_window, long_window)

    if choice == "rsi":
        window = random.randint(5, 30)
        overbought = random.randint(60, 80)
        oversold = random.randint(20, 40)
        return RSIStrategy(window=window, overbought=overbought, oversold=oversold)

    window = random.randint(10, 30)
    std_mul = round(random.uniform(1.5, 3.0), 1)
    return BollingerBandStrategy(window=window, std_mul=std_mul)
