"""TimesFM forecasts for BTC, with an honest walk-forward backtest.

Forecasts log(BTC price) with Google's TimesFM 3.0, alone and with the
flowscope flow series as past-only covariates, and scores both against
simple baselines on rolling origins the model never saw.

    python forecast.py                    # forecast the next 7 and 30 days
    python forecast.py --backtest         # walk-forward backtest vs baselines
    python forecast.py --smoke            # plumbing test with untrained weights

Weights: by default pulled from Hugging Face (google/timesfm-3.0-pytorch).
If huggingface.co is blocked, download that repo elsewhere and pass
--checkpoint /path/to/dir (with config.json + model.safetensors) or set
TIMESFM_CHECKPOINT.
"""
import argparse
import os

import numpy as np
import pandas as pd

import flowscope

HORIZONS = (7, 30)
COVARIATES = ["cb_premium", "stable_30d", "oi_14d", "basis", "vol14"]


def load_series():
    df, _, _ = flowscope.build_btc()
    df = df[df.px.notna()].copy()
    df["logp"] = np.log(df.px)
    df[COVARIATES] = df[COVARIATES].ffill().bfill()
    return df


# ---------------------------------------------------------------- forecasters
# Each forecaster takes a list of context frames and returns, per context,
# an array of shape (max_horizon, 3): q10, median, q90 of log price.

def random_walk(contexts, h):
    out = []
    for c in contexts:
        lp = c.logp.values
        rets = lp[h:] - lp[:-h]
        last = lp[-1]
        q = [np.quantile(rets[-365:], p) for p in (0.1, 0.9)] if len(rets) > 30 else [0, 0]
        steps = np.arange(1, h + 1) / h
        out.append(np.column_stack([last + q[0] * np.sqrt(steps), np.full(h, last), last + q[1] * np.sqrt(steps)]))
    return out


def drift(contexts, h):
    out = []
    for c, rw in zip(contexts, random_walk(contexts, h)):
        mu = np.diff(c.logp.values[-366:]).mean()
        out.append(rw + (mu * np.arange(1, h + 1))[:, None])
    return out


class TimesFM:
    def __init__(self, checkpoint, context_len, covariates, smoke=False):
        import torch
        from timesfm3.torch import timesfm3_forecaster as tf

        torch.set_num_threads(os.cpu_count() or 4)
        if smoke:
            cfg = tf.ModelConfig(checkpoint_path="untrained", device="cpu")
            m = tf.TimesFM3Forecaster.__new__(tf.TimesFM3Forecaster)
            m.config, m.device = cfg, torch.device("cpu")
            m.model = tf._make_torch_model(cfg).to(m.device).eval()
            self.model = m
        else:
            self.model = tf.TimesFM3Forecaster.from_pretrained(checkpoint, device="cpu")
        self.context_len = context_len
        self.covariates = covariates
        qs = list(self.model.config.quantiles)
        self.qidx = [qs.index(0.1), qs.index(0.5), qs.index(0.9)]

    def __call__(self, contexts, h):
        ctx = [c.logp.values[-self.context_len:] for c in contexts]
        cov = [c[self.covariates].values[-self.context_len:].T for c in contexts] if self.covariates else None
        out = []
        for i in range(0, len(ctx), 16):
            res = self.model.predict_batch(
                contexts=ctx[i:i + 16], horizon=h,
                past_only_covariates=cov[i:i + 16] if cov else None,
                return_quantiles=True)
            for r in res:
                q = np.asarray(r.quantiles).reshape(-1, len(self.model.config.quantiles))[:h]
                out.append(q[:, self.qidx])
        return out


# ------------------------------------------------------------------ backtest

def backtest(df, models, years=2.0, step=7):
    hmax = max(HORIZONS)
    end = len(df) - hmax - 1
    start = end - int(365 * years)
    origins = list(range(start, end + 1, step))
    contexts = [df.iloc[:i + 1] for i in origins]
    actual = np.array([[df.logp.iloc[i + h] - df.logp.iloc[i] for h in HORIZONS] for i in origins])
    rows = []
    for name, fn in models.items():
        preds = fn(contexts, hmax)
        for j, h in enumerate(HORIZONS):
            last = np.array([c.logp.iloc[-1] for c in contexts])
            q10, med, q90 = (np.array([p[h - 1, k] for p in preds]) - last for k in range(3))
            a = actual[:, j]
            # long when the median says up, flat otherwise; non-overlapping trades only
            take = np.arange(0, len(a), -(-h // step))
            strat = np.exp(np.where(med[take] > 0, a[take], 0).sum()) - 1
            rows.append({
                "model": name, "horizon": f"{h}d", "n": len(a),
                "direction_hit": np.mean(np.sign(med) == np.sign(a)) if np.any(med != 0) else np.nan,
                "mae_pct": np.mean(np.abs(np.exp(med) - np.exp(a))) * 100,
                "band80_coverage": np.mean((a >= q10) & (a <= q90)),
                "long_if_up": strat,
                "buy_hold": np.exp(a[take].sum()) - 1,
            })
    period = (df.index[origins[0]].date(), df.index[origins[-1]].date())
    return pd.DataFrame(rows), period, actual


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backtest", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="untrained weights, plumbing test only")
    ap.add_argument("--checkpoint", default=os.environ.get("TIMESFM_CHECKPOINT", "google/timesfm-3.0-pytorch"))
    ap.add_argument("--context", type=int, default=1024)
    ap.add_argument("--years", type=float, default=2.0)
    args = ap.parse_args()

    df = load_series()
    models = {"random_walk": random_walk, "drift": drift}
    try:
        models["timesfm"] = TimesFM(args.checkpoint, args.context, None, args.smoke)
        models["timesfm+flows"] = TimesFM(args.checkpoint, args.context, COVARIATES, args.smoke)
        models["timesfm+flows"].model = models["timesfm"].model      # share weights
    except Exception as e:                                             # weights unreachable
        print(f"TimesFM unavailable ({type(e).__name__}: {str(e)[:160]}). Running baselines only.\n")
    if args.smoke:
        print("SMOKE TEST: TimesFM weights are random. Numbers below are meaningless.\n")

    if args.backtest:
        res, period, _ = backtest(df, models, args.years)
        print(f"Walk-forward backtest, weekly origins {period[0]} to {period[1]}\n")
        pd.set_option("display.width", 200)
        print(res.to_string(index=False, formatters={
            "direction_hit": "{:.0%}".format, "mae_pct": "{:.1f}%".format,
            "band80_coverage": "{:.0%}".format, "long_if_up": "{:+.0%}".format, "buy_hold": "{:+.0%}".format}))
        return

    last = df.logp.iloc[-1]
    print(f"BTC {df.px.iloc[-1]:,.0f} on {df.index[-1].date()}\n")
    for name, fn in models.items():
        p = fn([df], max(HORIZONS))[0]
        cells = [f"{h}d: {np.exp(p[h - 1, 1]):,.0f} (80% band {np.exp(p[h - 1, 0]):,.0f} to {np.exp(p[h - 1, 2]):,.0f}, "
                 f"median {np.exp(p[h - 1, 1] - last) - 1:+.1%})" for h in HORIZONS]
        print(f"{name:<14} " + "  |  ".join(cells))


if __name__ == "__main__":
    main()
