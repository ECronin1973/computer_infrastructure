#!/usr/bin/env python3
"""
📈 FAANG CLI Script

This script fetches hourly stock data for FAANG companies (Meta, Apple, Amazon, Netflix, Google),
saves the data as a timestamped CSV file, and generates a plot of closing prices.

It uses Yahoo Finance via the `yfinance` library and supports command-line options
to control downloading, output location, and plot display.

Usage examples:
    ./faang.py
    python faang.py --no-download --outdir ./custom_data --no-display
"""

# 📦 Import required libraries
import argparse                      # For parsing command-line arguments
from pathlib import Path             # For handling file paths
from datetime import datetime, timezone  # For timestamping and UTC time
import pandas as pd                  # For data manipulation
import matplotlib.pyplot as plt      # For plotting
import seaborn as sns                # For styling plots
import yfinance as yf                # For fetching stock data from Yahoo Finance

# ✅ Define the canonical list of FAANG tickers
# These represent Meta, Apple, Amazon, Netflix, and Alphabet (Google)
tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

# 🧹 Utility function to remove duplicates while preserving order
# This ensures the ticker list is clean and consistent
def deduplicate_preserve_order(items):
    return list(dict.fromkeys(items))

# Apply deduplication to the ticker list
tickers = deduplicate_preserve_order(tickers)

# 🔍 Sanity check: Confirm we have exactly 5 unique tickers
if len(tickers) != 5:
    print('⚠️ Warning: unexpected tickers list (duplicates removed):', tickers)

# 📥 Fetch hourly historical data for a single ticker
def fetch_hourly_history(ticker, period='5d', interval='1h'):
    try:
        print(f"🔄 Fetching data for {ticker}...")
        t = yf.Ticker(ticker)                        # Create a ticker object
        df = t.history(period=period, interval=interval)  # Fetch historical data

        # Handle case where no data is returned
        if df is None or df.empty:
            print(f"⚠️ No data returned for {ticker}")
            return None

        # Add ticker column and set index name for clarity
        df = df.copy()
        df['Ticker'] = ticker
        df.index.name = 'Date'

        print(f"✅ Fetched {len(df)} rows for {ticker}")
        return df
    except Exception as e:
        print(f"❌ Error fetching {ticker}: {e}")
        return None

# 💾 Save combined data for all tickers to a timestamped CSV file
def save_hourly_data(tickers, output_dir, overwrite=False):
    output_dir.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists
    combined_df = []

    # Fetch data for each ticker and collect results
    for sym in tickers:
        print(f'🔄 Fetching {sym}...')
        df = fetch_hourly_history(sym)
        if df is None or df.empty:
            print(f'⚠️ No data returned for {sym}; skipping')
            continue
        combined_df.append(df)

    # Exit early if no data was collected
    if not combined_df:
        print("⚠️ No data to save.")
        return None

    # Combine all dataframes into one
    final_df = pd.concat(combined_df)

    # 🕒 Generate timestamp for filenames and logs
    now = datetime.now(timezone.utc)
    ts_filename = now.strftime('%Y%m%d-%H%M%S')       # For filename
    ts_human = now.strftime('%Y-%m-%d %H:%M:%S UTC')  # For display

    print("Current date and time:", now)
    print("Formatted date and time:", ts_human)

    filename = f'{ts_filename}.csv'
    path = output_dir / filename

    print(f"🗓️ Save timestamp: {ts_human}")

    # Avoid overwriting existing file unless explicitly allowed
    if path.exists() and not overwrite:
        print(f'ℹ️ File already exists ({filename}); skipping save (OVERWRITE=False)')
        return None

    # Save the combined data to CSV
    try:
        final_df.to_csv(path, index_label='Date')
        print(f'✅ Saved combined data -> {path}')
        return str(path)
    except Exception as e:
        print(f'❌ Failed to save data: {e}')
        return None

# 📊 Generate and save a plot of closing prices for each ticker
def plot_data(csv_path, output_dir, tickers, show_plot=True):
    # Load the CSV data
    df = pd.read_csv(csv_path, parse_dates=['Date'])

    # Ensure the 'Ticker' column exists
    if 'Ticker' not in df.columns:
        print("❌ Missing 'Ticker' column in CSV.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)  # Ensure plot directory exists
    plt.figure(figsize=(10, 5))                    # Set plot size
    sns.set_style('whitegrid')                     # Use clean plot style

    # Plot each ticker's closing prices
    for ticker in tickers:
        subdf = df[df['Ticker'] == ticker]
        if subdf.empty:
            print(f"⚠️ No data to plot for {ticker}")
            continue
        plt.plot(subdf['Date'], subdf['Close'], label=ticker)

    plt.xlabel('Date')
    plt.ylabel('Close Price')

    # 🕒 Add timestamp to plot title
    ts_human = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    plt.title(f'FAANG Hourly Prices — {ts_human}')
    plt.legend()

    # Save plot with timestamped filename
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f'{ts}.png'
    plt.savefig(plot_path)
    print(f'📊 Plot saved to {plot_path}')

    # Optionally display the plot
    if show_plot:
        plt.show()

# 🚀 Main function: handles CLI arguments and orchestrates workflow
def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="📈 FAANG Data CLI")
    parser.add_argument('--no-download', action='store_true', help="Skip data download")
    parser.add_argument('--outdir', type=str, default='data', help="Directory to save CSV and plots")
    parser.add_argument('--no-display', action='store_true', help="Suppress plot display")

    args = parser.parse_args()
    outdir = Path(args.outdir).resolve()           # Resolve output path
    plots_dir = outdir.parent / 'plots'            # Plot directory is sibling to data

    # If --no-download is used, load the most recent CSV file
    if args.no_download:
        csv_files = sorted(outdir.glob("*.csv"), reverse=True)
        if not csv_files:
            print("❌ No CSV files found.")
            return
        csv_path = csv_files[0]
    else:
        # Otherwise, fetch new data and save it
        csv_path = save_hourly_data(tickers, outdir)
        if csv_path is None:
            return

    # Generate plot from the selected or downloaded CSV
    plot_data(csv_path, plots_dir, tickers, show_plot=not args.no_display)

# 🧭 Entry point: run main() when script is executed
if __name__ == '__main__':
    main()
