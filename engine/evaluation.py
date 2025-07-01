import vectorbt as vbt
import pandas as pd


def evaluate_strategy(strategy, price_data):
    """Run a backtest of a simple moving average crossover strategy.

    Parameters
    ----------
    strategy : dict
        Strategy configuration with ``short_window`` and ``long_window`` keys.
    price_data : pandas.Series
        Series of price data.

    Returns
    -------
    float
        Total return of the strategy.
    """
    short_w = strategy["short_window"]
    long_w = strategy["long_window"]

    fast_ma = vbt.MA.run(price_data, short_w)
    slow_ma = vbt.MA.run(price_data, long_w)

    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)

    portfolio = vbt.Portfolio.from_signals(
        price_data,
        entries,
        exits,
        init_cash=1000,
        fees=0.0,
        slippage=0.0,
    )
    return float(portfolio.total_return())
