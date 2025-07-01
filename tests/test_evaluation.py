import numpy as np
import pandas as pd

from strategies.generator import generate_random_strategy
from engine.evaluation import evaluate_strategy


def test_evaluate_strategy_returns_float():
    price = pd.Series(
        np.cumprod(1 + np.random.normal(0, 0.01, 100)), name="price"
    )
    strat = generate_random_strategy()
    result = evaluate_strategy(strat, price)
    assert isinstance(result, float)
