# Agentic Strategy Evolution

This repository contains tools and experiments for evolving trading strategies.

## Installation

First, create and activate a Python environment. Then install the dependencies
using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

The main dependencies are:

- `vectorbt`
- `numpy`
- `pandas`
- `matplotlib`
- `deap`

## Sample data

The `data/` directory contains minute level candlestick data for BTC/USDT.
CSV files use the following columns:

```
timestamp,open,high,low,close,volume,close_time,quote_asset_volume,
number_of_trades,taker_buy_base_asset_volume,taker_buy_quote_asset_volume,ignore
```

Load a file with pandas and parse the timestamp column to a `datetime` index:

```python
import pandas as pd
df = pd.read_csv("data/BTCUSDT_1m_data.csv", index_col="timestamp", parse_dates=True)
```

This DataFrame can then be used as `price_data` when evaluating strategies.

## Evolving strategies

Run the evolution driver to create and evolve a population of moving average
strategies:

```bash
python engine/evolution.py
```

By default the script generates random price series. To evolve against your own
data, load it using pandas as shown above and modify `engine/evolution.py`
accordingly.

## Running tests

After installing dependencies, execute the test suite with:

```bash
pytest -q
```

Tests cover the strategy generator and evaluation helper to ensure they produce
valid strategies and numeric performance results.

## Style checks

Use `flake8` to ensure code style compliance:

```bash
flake8 .
```

