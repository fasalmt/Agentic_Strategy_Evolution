from strategies.generator import generate_random_strategy


def test_generate_random_strategy_keys():
    strat = generate_random_strategy()
    assert "short_window" in strat and "long_window" in strat
    assert strat["short_window"] < strat["long_window"]
