#!/usr/bin/env python3  # Allows script to be run directly from terminal

# --- Imports ---
import argparse  # For command-line argument parsing
from pathlib import Path  # For cross-platform file and folder handling
from datetime import datetime, timezone  # For timestamped filenames
import pandas as pd  # For data manipulation
import yfinance as yf  # For fetching financial data
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For enhanced plot styling

# --- Configuration ---
DATA_DIR = Path("data").resolve()  # Directory to save CSV files
PLOTS_DIR = Path("plots").resolve()  # Directory to save plot images
TICKERS = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']  # FAANG stock symbols

# Set default plot style
plt.rcParams['figure.figsize'] = (10, 5)
sns.set_style('whitegrid')

# --- Helper Functions ---

def fetch_hourly_history(ticker):
    """
    Fetch 5 days of hourly OHLCV data for a single ticker.
    Adds a 'Ticker' column and sets the index name to 'Date'.
    """
    try:
        df = yf.Ticker(ticker).history(period='5d', interval='1h')
        if df.empty:
            print(f"⚠️ No data for {ticker}")
            return None
        df['Ticker'] = ticker
        df.index.name = 'Date'
        return df
    except Exception as e:
        print(f"❌ Error fetching {ticker}: {e}")
        return None

def save_hourly_data(tickers, output_dir, overwrite=False):
    """
    Fetch data for multiple tickers and save to a timestamped CSV file.
    Creates output directory if needed. Skips saving if no valid data.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Saving to directory: {output_dir}")

    dfs = []
    for t in tickers:
        df = fetch_hourly_history(t)
        if df is not None and not df.empty:
            print(f"✅ {t}: {len(df)} rows")
            dfs.append(df)
        else:
            print(f"⚠️ {t}: No valid data")

    if not dfs:
        print("🚫 No valid data to save.")
        return None

    final_df = pd.concat(dfs)
    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    path = output_dir / f"{ts}.csv"

    # Handle overwrite logic
    if path.exists() and not overwrite:
        print(f"🛑 File already exists and overwrite=False: {path.name}")
        return None

    try:
        final_df.to_csv(path, index_label='Date')
        print(f"✅ Data saved to {path}")
        return str(path)
    except Exception as e:
        print(f"❌ Failed to save file: {e}")
        return None

def load_latest_data(tickers, folder='data'):
    """
    Load the most recent CSV file from the given folder.
    Splits the data into separate DataFrames per ticker.
    """
    files = sorted(Path(folder).glob("*.csv"), reverse=True)
    if not files:
        print("🚫 No CSV files found.")
        return {}

    df = pd.read_csv(files[0], parse_dates=["Date"])
    data = {t: df[df["Ticker"] == t].copy() for t in tickers}

    # Print status for each ticker
    print("📋 Ticker load status:")
    for t in tickers:
        if t not in data:
            print(f"{t}: ⚠️ Missing")
        elif data[t].empty:
            print(f"{t}: ⚠️ Empty")
        else:
            print(f"{t}: ✅ Loaded")

    return data

def plot_close_prices(data, output_dir, show=False):
    """
    Generate and save a line plot of Close prices for each ticker.
    Saves the plot to a timestamped PNG file. Optionally displays it.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 6))

    for sym, df in data.items():
        if 'Close' in df.columns and not df.empty:
            x = pd.to_datetime(df['Date'], errors='coerce')
            y = df['Close']
            ax.plot(x, y, label=sym)

    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price (USD)")
    ax.legend(title="Ticker")

    ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    plot_path = output_dir / f"{ts}.png"
    fig.tight_layout()
    fig.savefig(plot_path, bbox_inches='tight')
    print(f"✅ Plot saved to {plot_path}")

    if show:
        plt.show()

# --- Main CLI Entry Point ---

def main():
    """
    Parse command-line arguments and run the script logic.
    Supports flags for plotting, overwriting, and displaying the plot.
    """
    parser = argparse.ArgumentParser(description="Fetch and plot FAANG stock data.")
    parser.add_argument("--plot", action="store_true", help="Generate and save plot after fetching data.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing CSV if timestamp matches.")
    parser.add_argument("--show", action="store_true", help="Display plot after saving.")
    args = parser.parse_args()

    # Fetch and save data
    saved_file = save_hourly_data(TICKERS, DATA_DIR, overwrite=args.overwrite)
    if not saved_file:
        print("🚫 No data file saved. Exiting.")
        return

    # Load and optionally plot data
    data = load_latest_data(TICKERS, folder=str(DATA_DIR))
    if args.plot:
        plot_close_prices(data, PLOTS_DIR, show=args.show)

# --- Script Execution Trigger ---
if __name__ == "__main__":
    main()
