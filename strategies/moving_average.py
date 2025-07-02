from dataclasses import dataclass
import pandas as pd
import vectorbt as vbt
from .base import Strategy


@dataclass
class MovingAverageCrossoverStrategy(Strategy):
    """Simple moving average crossover strategy."""

    short_window: int
    long_window: int

    def generate_signals(self, price_data: pd.Series):
        fast_ma = vbt.MA.run(price_data, self.short_window)
        slow_ma = vbt.MA.run(price_data, self.long_window)
        entries = fast_ma.ma_crossed_above(slow_ma)
        exits = fast_ma.ma_crossed_below(slow_ma)
        return entries, exits
