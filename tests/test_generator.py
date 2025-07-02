from strategies import generate_random_strategy


def test_generate_random_strategy_keys():
    strat = generate_random_strategy()
    assert hasattr(strat, "short_window") and hasattr(strat, "long_window")
    assert strat.short_window < strat.long_window
    assert hasattr(strat, "generate_signals")
