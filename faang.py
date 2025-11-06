#!/usr/bin/env python3
"""
📈 FAANG CLI Script

This script fetches hourly stock data for FAANG companies (Meta, Apple, Amazon, Netflix, Google),
saves the data as a timestamped CSV file, and generates a plot of closing prices.

Features:
- Downloads data using Yahoo Finance API via yfinance
- Saves CSV files in the data/ folder
- Generates plots in the plots/ folder
- Supports command-line flags:
    --no-download   → use latest CSV without fetching new data
    --outdir        → specify custom output directory
    --no-display    → suppress plot display (useful for automation)

Usage:
    ./faang.py
    python faang.py --no-download --outdir ./custom_data --no-display
"""

import argparse
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# ✅ Canonical FAANG tickers
DEFAULT_TICKERS = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

# 🧹 Remove duplicates while preserving order
def deduplicate_preserve_order(items):
    return list(dict.fromkeys(items))

# 📥 Fetch hourly data for a single ticker
def fetch_hourly_history(ticker, period='5d', interval='1h'):
    try:
        print(f"🔄 Fetching data for {ticker}...")
        t = yf.Ticker(ticker)
        df = t.history(period=period, interval=interval)

        if df is None or df.empty:
            print(f"⚠️ No data returned for {ticker}")
            return None

        df = df.copy()
        df['Ticker'] = ticker
        df.index.name = 'Date'

        print(f"✅ Fetched {len(df)} rows for {ticker}")
        return df
    except Exception as e:
        print(f"❌ Error fetching {ticker}: {e}")
        return None

# 💾 Save combined data to CSV
def save_hourly_data(tickers, output_dir, overwrite=False):
    output_dir.mkdir(parents=True, exist_ok=True)
    combined_df = []

    for sym in tickers:
        print(f'🔄 Fetching {sym}...')
        df = fetch_hourly_history(sym)
        if df is None or df.empty:
            print(f'⚠️ No data returned for {sym}; skipping')
            continue
        combined_df.append(df)

    if not combined_df:
        print("⚠️ No data to save.")
        return None

    final_df = pd.concat(combined_df)

    # 🕒 Get current UTC time and format timestamps
    now = datetime.now(timezone.utc)
    ts_filename = now.strftime('%Y%m%d-%H%M%S')       # For filename
    ts_human = now.strftime('%Y-%m-%d %H:%M:%S UTC')  # For logging

    # 🖨️ Display both formats
    print("Current date and time:", now)
    print("Formatted date and time:", ts_human)

    filename = f'{ts_filename}.csv'
    path = output_dir / filename

    print(f"🗓️ Save timestamp: {ts_human}")

    if path.exists() and not overwrite:
        print(f'ℹ️ File already exists ({filename}); skipping save (OVERWRITE=False)')
        return None

    try:
        final_df.to_csv(path, index_label='Date')
        print(f'✅ Saved combined data -> {path}')
        return str(path)
    except Exception as e:
        print(f'❌ Failed to save data: {e}')
        return None

# 📊 Generate and save plot
def plot_data(csv_path, output_dir, show_plot=True):
    df = pd.read_csv(csv_path, parse_dates=['Date'])
    if 'Ticker' not in df.columns:
        print("❌ Missing 'Ticker' column in CSV.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    sns.set_style('whitegrid')

    for ticker in DEFAULT_TICKERS:
        subdf = df[df['Ticker'] == ticker]
        plt.plot(subdf['Date'], subdf['Close'], label=ticker)

    plt.xlabel('Date')
    plt.ylabel('Close Price')

    # 🕒 Use UTC timestamp for plot title
    ts_human = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    plt.title(f'FAANG Hourly Prices — {ts_human}')
    plt.legend()

    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f'{ts}.png'
    plt.savefig(plot_path)
    print(f'📊 Plot saved to {plot_path}')

    if show_plot:
        plt.show()

# 🚀 Main CLI entry point
def main():
    parser = argparse.ArgumentParser(description="📈 FAANG Data CLI")
    parser.add_argument('--no-download', action='store_true', help="Skip data download")
    parser.add_argument('--outdir', type=str, default='data', help="Directory to save CSV and plots")
    parser.add_argument('--no-display', action='store_true', help="Suppress plot display")

    args = parser.parse_args()
    outdir = Path(args.outdir).resolve()
    plots_dir = outdir.parent / 'plots'

    tickers = globals().get('tickers')
    if not isinstance(tickers, list) or not all(isinstance(t, str) for t in tickers) or not tickers:
        tickers = DEFAULT_TICKERS
        print("⚠️ 'tickers' not found or invalid; using default FAANG list:", tickers)

    tickers = deduplicate_preserve_order(tickers)

    if args.no_download:
        csv_files = sorted(outdir.glob("*.csv"), reverse=True)
        if not csv_files:
            print("❌ No CSV files found.")
            return
        csv_path = csv_files[0]
    else:
        csv_path = save_hourly_data(tickers, outdir)
        if csv_path is None:
            return

    plot_data(csv_path, plots_dir, show_plot=not args.no_display)

if __name__ == '__main__':
    main()
