# Computer Infrastructure – Module Assessments (2025/2026)

**Author:** Edward Cronin  
**Student ID:** g00425645  
**Email:** g00425645@atu.ie  
**GitHub:** [ECronin1973](https://github.com/ECronin1973)

---

## Overview

This repository contains solutions to four practical problems from the ATU Galway Computer Infrastructure module. The primary deliverable is the interactive notebook `notebooks/problems.ipynb`, which fetches hourly FAANG stock data, saves timestamped CSVs, and produces comparison plots.

What's included:

- `notebooks/problems.ipynb` — Interactive notebook with the solutions and step-by-step runner (Steps 0–3)
- `requirements.txt` — Python package dependencies
- `README_SETUP.md` — Setup instructions for Windows PowerShell

This README is a compact companion to the notebook and documents the runtime behaviour and file conventions used by the exercises.

---

## Quick Start (Windows PowerShell)

1. Clone the repository:

```powershell
git clone https://github.com/ECronin1973/computer_infrastructure.git
cd computer_infrastructure
```

2. Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Launch Jupyter and open the notebook:

```powershell
jupyter notebook
```

Open `notebooks/problems.ipynb` and run the cells in order. See `README_SETUP.md` for alternative environment notes.

---

## Key configuration & filename conventions

- DATA folder (default): `data/` (notebooks use `DATA_DIR = Path('../data').resolve()`)
- PLOTS folder (default): `plots/` (notebooks use `PLOTS_DIR = Path('../plots').resolve()`)
- CSV filename pattern (UTC timestamp to seconds): `TICKER_YYYYMMDD-HHmmss.csv` (example: `AAPL_20251030-142530.csv`)
- Plot filename pattern (UTC): `faang_close_YYYYMMDD-HHmmss.png` (the notebook also supports a canonical `faang_close.png` option)

Notes:

- The notebook's Step 1 writes CSVs into `data/` using UTC timestamps (to seconds) and the ticker prefix. This makes filenames lexicographically sortable by time.
- The loader picks the latest timestamped CSV per ticker when loading data for plotting.
- Flags in the notebook control behavior (defaults are set in the Setup cell): `NO_DATE_FILENAMES`, `SAVE_DAILY`, `OVERWRITE`, and `NO_DATE_PLOTS`.

---

## Problem 1 — FAANG Stock Data (summary)

Objective: download hourly data (5-day period, 1-hour interval) for FAANG tickers and save timestamped CSVs.

Important behaviour:

- Filenames: `TICKER_YYYYMMDD-HHmmss.csv` (UTC). Example: `AAPL_20251030-142530.csv`.
- Folder: saved to `data/` relative to the notebook (setup uses `DATA_DIR = Path('../data').resolve()`).
- Each CSV contains hourly OHLCV columns, a `Ticker` column, and an explicit `Date` column (saved as the index label so the loader can parse it using `parse_dates=['Date']`).

Robustness and reproducibility:

- The notebook includes an environment verification helper to check package availability and perform a lightweight `yfinance` request before large downloads.
- File I/O is wrapped in try/except and respects the `OVERWRITE` flag so repeated runs do not clobber files unless requested.

References for Problem 1:

- yfinance: https://pypi.org/project/yfinance/
- pandas.to_csv / read_csv (parse_dates): https://pandas.pydata.org/

---

## Problem 2 — Plotting (summary)

Objective: load the latest saved CSV for each ticker and plot Close prices on one chart.

Behavior:

- The loader finds files matching `TICKER_*.csv` and selects the most recent filename by lexicographic sort (timestamped names are lexicographically sortable when using YYYYMMDD-HHmmss).
- The plot shows all five Close series on a single timeline, with axis labels, legend, and a date-range title.
- Plot files are saved to `plots/` using `faang_close_YYYYMMDD-HHmmss.png` (UTC). The notebook optionally supports a stable `faang_close.png` name for embedding.

References for Problem 2:

- matplotlib: https://matplotlib.org/
- pandas timeseries guide: https://pandas.pydata.org/docs/user_guide/timeseries.html

---

## Scripts & Automation (Problems 3–4)

- Problem 3 suggests packaging the helper functions into a CLI script `faang.py` (root) that performs the same steps as the notebook when run from the terminal.
- Problem 4 suggests a GitHub Actions workflow to run the script weekly (example schedule: every Saturday morning). Place workflows in `.github/workflows/faang.yml`.

---

## Helper functions (notebook)

The notebook contains small, focused helper functions that make the workflow reproducible and testable. Examples:

- `verify_environment()` — checks package availability and tests a sample `yfinance` request
- `install_requirements_if_missing()` — installs packages from `requirements.txt` if missing
- `deduplicate_preserve_order(seq)` — removes duplicates while preserving input order
- `fetch_hourly_history(ticker, period='5d', interval='1h')` — returns hourly stock DataFrame or `None`
- `save_hourly_data(ticker, folder='../data')` — fetches and saves hourly stock data to timestamped CSVs
- `load_latest_csvs(tickers, folder='../data')` — loads the latest CSV per ticker into a dictionary of DataFrames
- `preview_dataframe(df)` — prints shape and head of a DataFrame for inspection

These are described and documented inline in `notebooks/problems.ipynb`.

> 📚 *“Functions help break our program into smaller and modular chunks.”* — [GeeksforGeeks](https://www.geeksforgeeks.org/python-functions/)  
> 🧠 *“Functional decomposition improves clarity and supports reuse.”* — [Python.org](https://docs.python.org/3/howto/functional.html)  
> 🛠️ *“Clean, idiomatic Python code often relies on small, focused helper functions.”* — *Python Cookbook*, 3rd Ed., O’Reilly

---

## References & further reading

- yfinance repository and docs — https://github.com/ranaroussi/yfinance
- pandas documentation (read_csv, to_csv, DateTimeIndex) — https://pandas.pydata.org/
- matplotlib — https://matplotlib.org/
- Jupyter notebook best practices — https://jupyter.org/practices
- The Turing Way (reproducible research) — https://the-turing-way.netlify.app/
- PEP 8 style guide — https://peps.python.org/pep-0008/
- GeeksforGeeks Python functions — https://www.geeksforgeeks.org/python-functions/
- Python.org functional programming HOWTO — https://docs.python.org/3/howto/functional.html
- Real Python — https://realpython.com/
- Python Cookbook, 3rd Ed. — https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/

---

## Quick verification (how to run the notebook)

1. Open `notebooks/problems.ipynb` in Jupyter.
2. Run the Setup cell (imports and flags). Adjust flags if you want canonical filenames or timestamped names.
3. Run the runner cells in order:
   - Step 0 — Smoke test
   - Step 1 — Fetch & save (creates `data/TICKER_YYYYMMDD-HHmmss.csv`)
   - Step 2 — Load (reads latest CSVs)
   - Step 3 — Plot (saves `plots/faang_close_YYYYMMDD-HHmmss.png`)

---

**End of README**