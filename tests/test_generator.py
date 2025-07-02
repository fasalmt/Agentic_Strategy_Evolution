from unittest.mock import patch

from strategies import (
    generate_random_strategy,
    MovingAverageCrossoverStrategy,
    RSIStrategy,
    BollingerBandStrategy,
)


def test_generate_random_strategy_keys():
    strat = generate_random_strategy()
    assert hasattr(strat, "generate_signals")


def test_generator_returns_each_strategy_type():
    with patch("strategies.generator.random.choice", side_effect=["ma", "rsi", "bb"]):
        strat1 = generate_random_strategy()
        strat2 = generate_random_strategy()
        strat3 = generate_random_strategy()

    assert isinstance(strat1, MovingAverageCrossoverStrategy)
    assert isinstance(strat2, RSIStrategy)
    assert isinstance(strat3, BollingerBandStrategy)
