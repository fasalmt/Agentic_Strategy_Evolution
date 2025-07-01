import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from strategy import generate_strategy, evaluate_strategy

def test_generate_strategy_default_length():
    strategy = generate_strategy()
    assert len(strategy) == 5
    assert all(isinstance(x, int) for x in strategy)

def test_generate_strategy_custom_length():
    strategy = generate_strategy(length=3)
    assert len(strategy) == 3

def test_evaluate_strategy_sums_elements():
    strategy = [1, 2, 3]
    assert evaluate_strategy(strategy) == 6

def test_evaluate_strategy_invalid_type():
    with pytest.raises(TypeError):
        evaluate_strategy('not a list')

def test_evaluate_strategy_non_int_elements():
    with pytest.raises(ValueError):
        evaluate_strategy([1, 'a', 3])
