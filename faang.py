#!/usr/bin/env python3
"""
faang.py — Assessment Script for FAANG Stock Analysis — Winter 25/26 Assessment

Author: Edward Cronin

Implements:
- Problem 1: Fetch FAANG hourly data (last 5 days) and save to CSV.
- Problem 2: Plot FAANG hourly closing prices from latest CSV and save to PNG.
- Problem 3: Executable script that runs both steps when called from terminal.

Notes:
- 'Close' refers to the price at the end of each hourly interval, not the final daily close.
- The yfinance API only provides hourly data up to the most recent trading day.
  • On weekdays when markets are open, the script captures hourly closes intraday.
  • On weekends or holidays, no new hourly data is available, so the latest file stops
    at the final close of the last trading session (e.g., Friday’s market close).
- The chart title has been updated to reflect the last available trading date in the dataset,
  ensuring consistency between the plot and the underlying data.
- This aligns with the assignment requirement to fetch 5 days of hourly data.
"""

from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

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
    """Fetch hourly FAANG data for the last 5 days."""
    df = yf.Ticker(ticker).history(period='5d', interval='1h')
    if df.empty:
        print(f"⚠️ No data for {ticker}")
        return None
    df['Ticker'] = ticker
    df.index.name = 'Date'
    return df

def save_hourly_data(tickers, output_dir):
    """Save combined FAANG data into data/ folder with timestamped filename."""
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

    final_df = pd.concat(dfs)
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    path = output_dir / f"{ts}.csv"
    final_df.to_csv(path, index_label='Date')
    print(f"✅ Data saved to {path}")
    return str(path)

def load_latest_data(tickers, folder='data'):
    """Load the most recent CSV from data/ folder and split into ticker DataFrames."""
    files = sorted(Path(folder).glob("*.csv"), reverse=True)
    if not files:
        print("🚫 No CSV files found.")
        return {}

    df = pd.read_csv(files[0], parse_dates=["Date"])
    data = {t: df[df["Ticker"] == t].copy() for t in tickers}
    return data

def plot_close_prices(data, output_dir):
    """Plot hourly closing prices for FAANG tickers and save to plots/ folder."""
    fig, ax = plt.subplots()
    plotted = False
    last_date = None

    for sym, df in data.items():
        if 'Close' in df.columns and not df.empty:
            x = pd.to_datetime(df['Date'], errors='coerce')
            y = df['Close']
            ax.plot(x, y, label=sym)
            plotted = True
            # Track the latest date across tickers
            if last_date is None or df['Date'].max() > last_date:
                last_date = df['Date'].max()

    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price (USD)")

    if plotted:
        ax.legend(title="Ticker", loc="best")

    # ✅ Use the last available date from the dataset for the title
    if last_date is not None:
        title_date = pd.to_datetime(last_date).strftime("%Y-%m-%d")
        ax.set_title(f"FAANG Hourly Closing Prices — up to {title_date}")
    else:
        ax.set_title("FAANG Hourly Closing Prices — No Data")

    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f"{ts}.png"
    fig.tight_layout()
    fig.savefig(plot_path, bbox_inches='tight')
    plt.close(fig)
    print(f"✅ Plot saved to {plot_path}")

# --- Script Execution ---
def main():
    """Run data download and plotting in sequence (Problems 1–3)."""
    saved_file = save_hourly_data(TICKERS, DATA_DIR)
    if not saved_file:
        print("🚫 No data file saved. Exiting.")
        return
    data = load_latest_data(TICKERS, folder=str(DATA_DIR))
    plot_close_prices(data, PLOTS_DIR)

if __name__ == "__main__":
    main()
