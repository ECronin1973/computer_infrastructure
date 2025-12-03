#!/usr/bin/env python3
"""
faang.py — Assessment Script for FAANG Stock Analysis — Winter 25/26

Author: Edward Cronin

Implements:
- Problem 1: Fetch FAANG hourly data (last 5 trading days) and save to a single timestamped CSV.
- Problem 2: Load the latest combined CSV and plot FAANG hourly closing prices, saving a timestamped PNG.
- Problem 3: Script entry point to run the above steps.

Notes:
- The CSV saved per run is a single combined file containing all tickers with a Ticker column.
- The plot title is derived from the last available Date in the dataset to avoid weekend/holiday confusion.
"""

from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Execution controls
# -----------------------
# Set both to True when you want the script to fetch/save a new CSV or produce a plot.
# Set either to False to skip that particular step
RUN_PROBLEM_1 = True   # Fetch and save a new combined CSV when True
RUN_PROBLEM_2 = True   # Load latest CSV and produce plot when True

# --- Configuration ---
DATA_DIR = Path("data").resolve()
PLOTS_DIR = Path("plots").resolve()
TICKERS = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

DATA_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Apply notebook-style aesthetics for consistency
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['font.size'] = 12

# --- Helper Functions ---
def fetch_hourly_history(ticker):
    """Fetch hourly data (last 5 trading days) for a single ticker and return a DataFrame."""
    df = yf.Ticker(ticker).history(period='5d', interval='1h')
    if df is None or df.empty:
        print(f"⚠️ No data for {ticker}")
        return None
    df = df.copy()
    df['Ticker'] = ticker
    df.index.name = 'Date'
    df.reset_index(inplace=True)
    return df

def save_hourly_data(tickers, output_dir: Path):
    """Fetch all tickers, concatenate into one DataFrame and save a single timestamped CSV."""
    dfs = []
    for t in tickers:
        df = fetch_hourly_history(t)
        if df is not None and not df.empty:
            dfs.append(df)
            print(f"✅ {t}: {len(df)} rows")
        else:
            print(f"⚠️ {t}: No valid data")

    if not dfs:
        print("🚫 No valid data to save.")
        return None

    final_df = pd.concat(dfs, ignore_index=True)
    # Ensure Date column is datetime and sorted
    final_df['Date'] = pd.to_datetime(final_df['Date'])
    final_df.sort_values(['Ticker', 'Date'], inplace=True)

    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    path = output_dir / f"{ts}.csv"
    # Atomic-ish write: write to temp then rename
    tmp = path.with_suffix('.tmp')
    final_df.to_csv(tmp, index=False)
    tmp.replace(path)
    print(f"✅ Data saved to {path}")
    return path

def load_latest_data(tickers, folder: str = 'data'):
    """Load the most recent combined CSV (lexicographic newest) and return dict of ticker DataFrames."""
    folder_path = Path(folder)
    files = sorted(folder_path.glob("*.csv"))
    if not files:
        print("🚫 No CSV files found in", folder)
        return {}

    latest = files[-1]  # lexicographic newest (assumes timestamped filenames)
    df = pd.read_csv(latest, parse_dates=["Date"])
    data = {t: df[df["Ticker"] == t].copy().reset_index(drop=True) for t in tickers}
    print(f"✅ Loaded {latest}")
    return data

def plot_close_prices(data: dict, output_dir: Path, show: bool = False):
    """Plot hourly Close series for each ticker and save to a timestamped PNG."""
    fig, ax = plt.subplots()
    plotted = False
    last_date = None

    for sym, df in data.items():
        if df is None or df.empty:
            continue
        if 'Close' not in df.columns:
            continue
        x = pd.to_datetime(df['Date'], errors='coerce')
        y = pd.to_numeric(df['Close'], errors='coerce')
        if x.isna().all() or y.isna().all():
            continue
        ax.plot(x, y, label=sym)
        plotted = True
        this_max = x.max()
        if pd.isna(last_date) or (this_max is not pd.NaT and (last_date is None or this_max > last_date)):
            last_date = this_max

    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price (USD)")
    if plotted:
        ax.legend(title="Ticker", loc="best")

    if last_date is not None:
        title_date = pd.to_datetime(last_date).strftime("%Y-%m-%d")
        ax.set_title(f"FAANG Hourly Closing Prices — up to {title_date}")
    else:
        ax.set_title("FAANG Hourly Closing Prices — No Data")

    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f"{ts}.png"
    fig.tight_layout()
    fig.savefig(str(plot_path), bbox_inches='tight')
    print(f"✅ Plot saved to {plot_path}")

    if show:
        plt.show()
    plt.close(fig)

# --- Main flow ---
def main():
    saved_path = None

    # Problem 1 — Fetch and save CSV (optional)
    if RUN_PROBLEM_1:
        saved_path = save_hourly_data(TICKERS, DATA_DIR)
        if not saved_path:
            print("🚫 No data file saved. Exiting.")
            return
    else:
        print("ℹ️ Problem 1 skipped — CSV not generated (RUN_PROBLEM_1 = False).")

    # Problem 2 — Load latest CSV and plot (optional)
    if RUN_PROBLEM_2:
        data = load_latest_data(TICKERS, folder=str(DATA_DIR))
        if not data:
            print("🚫 No CSV available to load for plotting. Enable RUN_PROBLEM_1 or ensure a CSV exists.")
            return
        plot_close_prices(data, PLOTS_DIR, show=True)
    else:
        print("ℹ️ Problem 2 skipped — set RUN_PROBLEM_2 = True to generate and display the plot.")

if __name__ == "__main__":
    main()
