from dataclasses import dataclass
import pandas as pd
import vectorbt as vbt

from .base import Strategy


@dataclass
class RSIStrategy(Strategy):
    """Relative Strength Index strategy."""

    window: int
    overbought: float = 70.0
    oversold: float = 30.0

    def generate_signals(self, price_data: pd.Series):
        rsi = vbt.RSI.run(price_data, window=self.window)
        entries = rsi.rsi_below(self.oversold)
        exits = rsi.rsi_above(self.overbought)
        return entries, exits
