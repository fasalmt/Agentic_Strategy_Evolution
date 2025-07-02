The CSV files in this folder provide sample one-minute candlestick data for
BTC/USDT. Columns follow the standard Binance export format:

```
timestamp,open,high,low,close,volume,close_time,quote_asset_volume,
number_of_trades,taker_buy_base_asset_volume,taker_buy_quote_asset_volume,ignore
```

`timestamp` is in UTC and can be parsed with `pandas.read_csv` using
`parse_dates=True`. Example:

```python
import pandas as pd
price_series = pd.read_csv("BTCUSDT_1m_data.csv", index_col="timestamp", parse_dates=True)["close"]
```
