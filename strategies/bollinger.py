from dataclasses import dataclass
import pandas as pd
import vectorbt as vbt

from .base import Strategy


@dataclass
class BollingerBandStrategy(Strategy):
    """Bollinger Bands breakout strategy."""

    window: int
    std_mul: float = 2.0

    def generate_signals(self, price_data: pd.Series):
        bb = vbt.BBANDS.run(price_data, window=self.window, alpha=self.std_mul)
        entries = bb.close_crossed_above(bb.lower)
        exits = bb.close_crossed_below(bb.upper)
        return entries, exits
