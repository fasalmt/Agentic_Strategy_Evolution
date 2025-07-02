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

## Source
The data was downloaded from the public Binance API via the `/api/v3/klines` endpoint for the `BTCUSDT` trading pair.
An example request is:
`https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m`.

## Licensing
All candlestick data is © Binance and is provided subject to the
[Binance API Terms of Use](https://www.binance.com/en/terms). The files in this
folder are for personal, non-commercial research and demonstration purposes.
Redistribution or other uses must comply with Binance's terms.

## How the CSV files were generated
A simple Python script queried the Binance API and converted the returned JSON
records into CSV format. Each row in the file corresponds to a one-minute candle.
The script converted Unix timestamps to ISO 8601 strings and wrote the results
with the columns shown above.

## Restrictions and acknowledgments
This repository is not affiliated with Binance. When using these CSVs, please
acknowledge Binance as the data source and ensure your use adheres to the
Binance Terms of Use.

