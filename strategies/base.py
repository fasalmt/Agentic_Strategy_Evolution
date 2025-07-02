from abc import ABC, abstractmethod
import pandas as pd


class Strategy(ABC):
    """Abstract base class for trading strategies."""

    @abstractmethod
    def generate_signals(self, price_data: pd.Series):
        """Return entry and exit signal series."""
        pass
