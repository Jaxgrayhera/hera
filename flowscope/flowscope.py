"""Flowscope: fear vs. flow.

Separates loud fear (price stress, derivatives stress) from actual money
movement (US spot demand, stablecoin inflows, leverage flushes), and
backtests what each combination has meant for forward returns.

Data is pulled from TradingView (see README) into ./data as JSON files.

    python flowscope.py            # today's read + backtest summary
    python flowscope.py --detail   # also print per-episode table
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data"
PCT_WINDOW = 365      # trailing window for percentile ranks (no lookahead)
FEAR_HI = 70          # thresholds chosen up front, not tuned
FLOW_OK = 50
FLOW_BAD = 30
COOLDOWN = 7          # days between counted episodes
HORIZONS = {"7d": 7, "30d": 30}


def load(name):
    raw = json.load(open(DATA / f"{name}.json"))["bars"]
    df = pd.DataFrame({k: raw[k] for k in "ohlc"},
                      index=pd.to_datetime(raw["t"], unit="s").normalize())
    return df[~df.index.duplicated(keep="last")]


def trailing_pct(s, window=PCT_WINDOW):
    """Percentile (0-100) of today's value within the trailing window."""
    return s.rolling(window, min_periods=120).apply(
        lambda w: (w[:-1] < w[-1]).mean() * 100 if len(w) > 1 else np.nan, raw=True)


def build_btc():
    cb, bn = load("CB_BTCUSD").c, load("BN_BTCUSDT").c
    perp, oi = load("BN_BTCUSDT_PERP").c, load("BN_BTC_OI").c
    stables = load("USDT_MCAP").c.add(load("USDC_MCAP").c, fill_value=0)
    df = pd.DataFrame({"px": cb, "bn": bn, "perp": perp, "oi": oi, "stables": stables}).dropna(subset=["px", "bn", "perp"])

    # Fear side: how scary the tape looks
    df["drawdown"] = df.px / df.px.rolling(90, min_periods=1).max() - 1
    df["ret14"] = df.px.pct_change(14)
    df["basis"] = (df.perp / df.bn - 1).rolling(3).mean()           # perp vs spot, funding proxy
    df["vol14"] = np.log(df.px).diff().rolling(14).std() * np.sqrt(365)
    fear_parts = pd.DataFrame({
        "drawdown": 100 - trailing_pct(df.drawdown),
        "ret14": 100 - trailing_pct(df.ret14),
        "basis": 100 - trailing_pct(df.basis),
        "vol14": trailing_pct(df.vol14),
    })
    df["fear"] = fear_parts.mean(axis=1)

    # Flow side: is real money leaving or arriving
    df["cb_premium"] = (df.px / df.bn - 1).rolling(7).mean()        # US spot / ETF demand
    df["stable_30d"] = df.stables.pct_change(30)                    # new dollars entering crypto
    df["oi_14d"] = df.oi.pct_change(14)                             # leverage build or flush
    flow_parts = pd.DataFrame({
        "cb_premium": trailing_pct(df.cb_premium),
        "stable_30d": trailing_pct(df.stable_30d),
    })
    df["flow"] = flow_parts.mean(axis=1)
    df["flush"] = 100 - trailing_pct(df.oi_14d)                     # high = leverage washed out

    for k, n in HORIZONS.items():
        df[f"fwd_{k}"] = df.px.shift(-n) / df.px - 1
    df["regime"] = classify(df.fear, df.flow)
    return df, fear_parts, flow_parts


def classify(fear, flow):
    r = pd.Series("neutral", index=fear.index)
    r[(fear >= FEAR_HI) & (flow >= FLOW_OK)] = "FUD, not flight"
    r[(fear >= FEAR_HI) & (flow < FLOW_BAD)] = "real selling"
    r[(fear >= FEAR_HI) & (flow >= FLOW_BAD) & (flow < FLOW_OK)] = "fear, mixed flow"
    r[(fear < 40) & (flow < FLOW_BAD)] = "calm distribution"
    r[fear.isna() | flow.isna()] = np.nan
    return r


def episodes(df, regime):
    """First day of each run of a regime, at least COOLDOWN days apart."""
    days = df.index[df.regime == regime]
    picked, last = [], None
    for d in days:
        if last is None or (d - last).days > COOLDOWN:
            picked.append(d)
        last = d
    return df.loc[picked]


def summarize(df, start=None, end=None):
    d = df.loc[start:end].dropna(subset=["regime", "fwd_30d"])
    rows = []
    for name in ["FUD, not flight", "fear, mixed flow", "real selling", "calm distribution", "neutral", "ALL DAYS"]:
        g = d if name == "ALL DAYS" else d[d.regime == name]
        ep = d if name == "ALL DAYS" else episodes(d, name)
        if len(g) == 0:
            continue
        row = {"regime": name, "days": len(g), "episodes": len(ep) if name != "ALL DAYS" else np.nan}
        for k in HORIZONS:
            row[f"avg_{k}"] = g[f"fwd_{k}"].mean()
            row[f"win_{k}"] = (g[f"fwd_{k}"] > 0).mean()
            row[f"ep_avg_{k}"] = ep[f"fwd_{k}"].mean() if name != "ALL DAYS" else np.nan
        rows.append(row)
    return pd.DataFrame(rows).set_index("regime")


def build_semis():
    smh, vix, vix3m = load("SMH").c, load("VIX").c, load("VIX3M").c
    df = pd.DataFrame({"px": smh, "vix": vix, "vix3m": vix3m}).dropna()
    df["term"] = df.vix / df.vix3m                       # > 1 = panic (backwardation)
    df["drawdown"] = df.px / df.px.rolling(63, min_periods=1).max() - 1
    df["fear"] = (trailing_pct(df.term, 252) + 100 - trailing_pct(df.drawdown, 252)) / 2
    for k, n in {"1w": 5, "1m": 21}.items():
        df[f"fwd_{k}"] = df.px.shift(-n) / df.px - 1
    return df


def pct(x):
    return "n/a" if pd.isna(x) else f"{x * 100:+.1f}%"


def main():
    detail = "--detail" in sys.argv
    btc, fear_parts, flow_parts = build_btc()
    t = btc.dropna(subset=["fear", "flow"]).index[-1]
    now = btc.loc[t]

    print(f"# Flowscope read for {t.date()}\n")
    print(f"BTC {now.px:,.0f}  |  FEAR {now.fear:.0f}/100  |  FLOW {now.flow:.0f}/100  |  leverage flush {now.flush:.0f}/100")
    print(f"Regime: **{now.regime}**")
    hist = summarize(btc).loc[[now.regime, "ALL DAYS"]]
    print(f"  history of this regime: 30d avg {pct(hist.avg_30d.iloc[0])} ({hist.win_30d.iloc[0]:.0%} up) "
          f"vs all days {pct(hist.avg_30d.iloc[1])} ({hist.win_30d.iloc[1]:.0%} up)\n")
    print("Fear inputs (percentile vs last year, high = scarier):")
    for k, v in fear_parts.loc[t].items():
        print(f"  {k:<10} {v:5.0f}")
    print(f"  raw: drawdown {pct(now.drawdown)}, 14d return {pct(now.ret14)}, perp basis {now.basis * 1e4:+.1f} bps, vol {now.vol14 * 100:.0f}%")
    print("Flow inputs (percentile vs last year, high = money arriving):")
    for k, v in flow_parts.loc[t].items():
        print(f"  {k:<10} {v:5.0f}")
    print(f"  raw: Coinbase premium {now.cb_premium * 1e4:+.1f} bps, stablecoin supply 30d {pct(now.stable_30d)}, OI 14d {pct(now.oi_14d)}")

    snap = DATA / "etf_snapshot.json"
    if snap.exists():
        s = json.load(open(snap))
        print(f"\nETF fund flows (TradingView snapshot {s['as_of']}, $M):")
        for sym, f in s["funds"].items():
            print(f"  {sym:<6} 1M {f['1M'] / 1e6:+9,.0f}   3M {f['3M'] / 1e6:+9,.0f}")

    pd.set_option("display.width", 200)
    fmt = {c: pct for c in ["avg_7d", "avg_30d", "ep_avg_7d", "ep_avg_30d"]} | {c: "{:.0%}".format for c in ["win_7d", "win_30d"]}
    for label, a, b in [("FULL HISTORY", None, None), ("2020-2023 (in-sample)", None, "2023-12-31"), ("2024-2026 (out-of-sample)", "2024-01-01", None)]:
        s = summarize(btc, a, b)
        print(f"\n## BTC backtest, {label}\n")
        print(s.to_string(formatters=fmt))

    if detail:
        ep = episodes(btc.dropna(subset=["regime"]), "FUD, not flight")
        print("\n## 'FUD, not flight' episodes\n")
        print(ep[["px", "fear", "flow", "drawdown", "fwd_7d", "fwd_30d"]].to_string(
            formatters={"px": "{:,.0f}".format, "fear": "{:.0f}".format, "flow": "{:.0f}".format,
                        "drawdown": pct, "fwd_7d": pct, "fwd_30d": pct}))

    semis = build_semis()
    u = semis.index[-1]
    print(f"\n# Semis (SMH) {u.date()}: VIX/VIX3M {semis.term.iloc[-1]:.2f}, drawdown {pct(semis.drawdown.iloc[-1])}, fear {semis.fear.iloc[-1]:.0f}/100\n")
    d = semis.dropna(subset=["fear", "fwd_1m"])
    for name, mask in [("fear >= 80", d.fear >= 80), ("VIX backwardation (term > 1)", d.term > 1), ("all days", d.fear.notna())]:
        g = d[mask]
        print(f"  {name:<30} days {len(g):4}  SMH 1w {pct(g.fwd_1w.mean())} ({(g.fwd_1w > 0).mean():.0%} up)  1m {pct(g.fwd_1m.mean())} ({(g.fwd_1m > 0).mean():.0%} up)")


if __name__ == "__main__":
    main()
