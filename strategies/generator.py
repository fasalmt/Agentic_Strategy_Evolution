import random

from .moving_average import MovingAverageCrossoverStrategy
from .rsi import RSIStrategy
from .bollinger import BollingerBandStrategy


def generate_random_strategy():
    """Generate a random trading strategy instance."""

    choice = random.choice(["ma", "rsi", "bb"])

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
