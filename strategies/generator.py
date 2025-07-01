import random


def generate_random_strategy():
    """Generate a simple moving average crossover strategy.

    Returns a dictionary containing short and long moving average windows.
    """
    short_window = random.randint(5, 20)
    long_window = random.randint(short_window + 1, 60)
    return {
        "short_window": short_window,
        "long_window": long_window,
    }
