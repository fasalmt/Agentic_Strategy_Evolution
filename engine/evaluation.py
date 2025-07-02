import vectorbt as vbt


def evaluate_strategy(strategy, price_data):
    """Run a backtest for a provided strategy object or callable.

    Parameters
    ----------
    strategy : Strategy or Callable
        Object implementing ``generate_signals`` or a callable returning
        ``(entries, exits)`` when passed ``price_data``.
    price_data : pandas.Series
        Series of price data.

    Returns
    -------
    float
        Total return of the strategy.
    """

    if hasattr(strategy, "generate_signals"):
        entries, exits = strategy.generate_signals(price_data)
    elif callable(strategy):
        entries, exits = strategy(price_data)
    else:
        raise TypeError(
            "strategy must be callable or implement generate_signals"
        )

    portfolio = vbt.Portfolio.from_signals(
        price_data,
        entries,
        exits,
        init_cash=1000,
        fees=0.0,
        slippage=0.0,
    )
    return float(portfolio.total_return())
