# Flowscope

Fear vs. flow. Separates how scary the market looks from whether money is actually leaving, then backtests what each combination meant for BTC (7d and 30d forward returns) and SMH.

## Inputs

| Side | Input | Source (TradingView symbol) |
|---|---|---|
| Fear | Drawdown from 90d high, 14d return, 14d realized vol | `COINBASE:BTCUSD` |
| Fear | Perp vs spot basis (funding proxy) | `BINANCE:BTCUSDT.P` vs `BINANCE:BTCUSDT` |
| Flow | Coinbase premium, 7d avg (US spot / ETF demand) | `COINBASE:BTCUSD` vs `BINANCE:BTCUSDT` |
| Flow | USDT + USDC supply, 30d change (new dollars) | `CRYPTOCAP:USDT`, `CRYPTOCAP:USDC` |
| Positioning | Open interest, 14d change (leverage flush) | `BINANCE:BTCUSDT.P_OI` |
| Snapshot | ETF fund flows 1M / 3M | `fund_flows.1M`, `fund_flows.3M` on IBIT, GBTC, SMH, SOXX, QQQ, XLK, SPY |
| Semis fear | VIX / VIX3M term structure, SMH drawdown | `CBOE:VIX`, `CBOE:VIX3M`, `NASDAQ:SMH` |

Every input is ranked as a percentile of its own trailing 365 days, so there is no lookahead. Thresholds (fear >= 70, flow >= 50 / < 30) were set before the backtest and not tuned.

## Refresh

The container cannot reach TradingView directly, so data comes through the TradingView MCP tools. Ask Claude to "refresh flowscope": it pulls daily bars (columns format, from 2020-01-01) for each symbol above into `data/<NAME>.json` (file names are in `load()` calls in `flowscope.py`), updates `data/etf_snapshot.json`, then runs:

```
python flowscope.py            # today's read + backtest
python flowscope.py --detail   # plus every "FUD, not flight" episode
```

## What the backtest says (data through 2026-10-18)

- The flow proxies here do **not** reliably confirm a buy when fear is high. During high-fear periods, a strong Coinbase premium or rising stablecoin supply came before *worse* 30d returns, not better.
- High fear alone has been a mild positive for BTC (59% of 30d windows up vs 55% for all days) and for SMH.
- Episode counts per regime are around 20, which is too few for any of this to count as proven.

## Blocked sources worth adding

These are the stronger institutional-flow and sentiment series, but the environment's network policy blocks them today: `farside.co.uk` (daily BTC/ETH ETF flows), `api.alternative.me` (Crypto Fear & Greed history), `publicreporting.cftc.gov` (COT: asset manager vs leveraged fund positioning in CME BTC and Nasdaq futures), `stablecoins.llama.fi`.

## TimesFM forecasts (`forecast.py`)

Runs Google's TimesFM 3.0 (`pip install "timesfm[torch]==3.0.2"`, CPU is fine) on log BTC price, alone and with the flow series above as past-only covariates, and scores it on weekly walk-forward origins over the last 2 years against a random walk and a drift baseline.

```
python forecast.py               # next 7d and 30d: median and 80% band
python forecast.py --backtest    # direction hit rate, error, band coverage, long-if-up vs buy and hold
python forecast.py --smoke       # plumbing test with untrained weights
```

Weights come from Hugging Face (`google/timesfm-3.0-pytorch`). This environment blocks `huggingface.co`, so either allow it (plus `cdn-lfs.huggingface.co` and `cas-bridge.xethub.hf.co`) or download the repo elsewhere and pass `--checkpoint /path/to/dir`. Until then the script runs the baselines only.
