#!/usr/bin/env python3
"""
📈 FAANG CLI Script

Author: Edward Cronin

This script fetches hourly stock data for FAANG companies (Meta, Apple, Amazon, Netflix, Google),
saves the data as a timestamped CSV file, and generates a plot of closing prices.

It uses Yahoo Finance via the `yfinance` library and supports command-line options
to control downloading, output location, and plot display.

Usage examples:
    ./faang.py
    python faang.py --no-download --outdir ./custom_data --no-display
"""

# 📦 Imports
import argparse
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# ✅ Global configuration
DEFAULT_TICKERS = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 5)

# 🧹 Utility: Deduplicate while preserving order
def deduplicate_preserve_order(items):
    return list(dict.fromkeys(items))

# 📥 Fetch hourly data for a single ticker
def fetch_hourly_history(ticker, period='5d', interval='1h'):
    try:
        df = yf.Ticker(ticker).history(period=period, interval=interval)
        if df.empty:
            print(f"⚠️ No data for {ticker}")
            return None
        df['Ticker'] = ticker
        df.index.name = 'Date'
        return df
    except Exception as e:
        print(f"❌ Error fetching {ticker}: {e}")
        return None

# 💾 Save combined data to timestamped CSV
def save_hourly_data(tickers, output_dir, overwrite=False):
    output_dir.mkdir(parents=True, exist_ok=True)
    dfs = [fetch_hourly_history(t) for t in tickers]
    dfs = [df for df in dfs if df is not None and not df.empty]
    if not dfs:
        print("⚠️ No valid data to save.")
        return None
    final_df = pd.concat(dfs)
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    path = output_dir / f"{ts}.csv"
    if path.exists() and not overwrite:
        print(f"ℹ️ File exists: {path.name}")
        return None
    final_df.to_csv(path, index_label='Date')
    print(f"✅ Data saved to {path}")
    return str(path)

# 📂 Load most recent CSV and split by ticker
def load_latest_data(tickers, folder):
    files = sorted(Path(folder).glob("*.csv"), reverse=True)
    if not files:
        raise FileNotFoundError("No CSV files found.")
    df = pd.read_csv(files[0], parse_dates=["Date"])
    return {t: df[df["Ticker"] == t].copy() for t in tickers}

# 📊 Plot closing prices and save as PNG
def plot_data(data_dict, output_dir, show_plot=True):
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots()
    for sym, df in data_dict.items():
        if 'Close' in df.columns and not df.empty:
            x = df.index if isinstance(df.index, pd.DatetimeIndex) else pd.to_datetime(df['Date'], errors='coerce')
            y = df['Close']
            ax.plot(x, y, label=sym)
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price (USD)')
    ax.legend(title='Ticker')
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f"{ts}.png"
    fig.tight_layout()
    fig.savefig(plot_path, bbox_inches='tight')
    print(f"✅ Plot saved to {plot_path}")
    if show_plot:
        plt.show()

# 🚀 Main CLI entry point
def main():
    parser = argparse.ArgumentParser(description="📈 FAANG Data CLI")
    parser.add_argument('--no-download', action='store_true', help="Skip data download")
    parser.add_argument('--outdir', type=str, default='data', help="Directory to save CSV and plots")
    parser.add_argument('--no-display', action='store_true', help="Suppress plot display")
    args = parser.parse_args()

    tickers = deduplicate_preserve_order(DEFAULT_TICKERS)
    data_dir = Path(args.outdir).resolve()
    plots_dir = Path('plots').resolve()

    if args.no_download:
        try:
            data = load_latest_data(tickers, folder=data_dir)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return
    else:
        csv_path = save_hourly_data(tickers, output_dir=data_dir)
        if not csv_path:
            return
        df = pd.read_csv(csv_path, parse_dates=["Date"])
        data = {t: df[df["Ticker"] == t].copy() for t in tickers}

    plot_data(data, output_dir=plots_dir, show_plot=not args.no_display)

# 🧭 Entry point: run main() when script is executed
if __name__ == '__main__':
    main()
