# FAANG Stock Data — hourly analysis

This repository contains a Jupyter notebook and supporting code to fetch, inspect and plot hourly OHLCV stock data for the FAANG companies (Meta, Apple, Amazon, Netflix and Alphabet). The README summarises the notebook `notebooks/problems.ipynb`, explains how to set up the environment, and lists references for independent study.

## What this project covers
- Retrieving hourly stock data using `yfinance`.
- Cleaning and preparing OHLCV time series in pandas.
- Visualising comparative close-price series for FAANG tickers.
- Practical tips for reproducible notebook work (centralised imports, plotting defaults, timestamped outputs).

## Learning outcomes
After working through the notebook you should be able to:
- Fetch hourly historical data for multiple tickers and save combined CSVs.
- Load the most recent timestamped CSV into pandas for analysis.
- Produce and save timestamped plots comparing close prices.
- Apply defensive programming patterns in notebooks to increase reproducibility and debuggability.

## Intended audience
This lab is aimed at computing students and professionals with some Python experience (pandas / matplotlib familiar). The material is self-contained: helper functions, environment checks and usage notes are provided in the notebook so you can follow along in a local environment or CI.

## Files of interest
- `notebooks/problems.ipynb` — primary notebook. It is organised into modular steps (environment verification, fetch & save, load, plot).
- `data/` — timestamped CSV outputs created by the notebook (one combined CSV containing all tickers; filename example: `20251105-220824.csv`).
- `plots/` — generated PNG visualisations (faang close-price chart).
- `requirements.txt` — list of Python packages used by the notebook. Use this to create an isolated environment.

## Quick start (recommended)
1. Create and activate a virtual environment (recommended):

   - Windows PowerShell:

     ```powershell
     python -m venv .venv; .\.venv\Scripts\Activate.ps1
     ```

2. Install the project's requirements:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Open the notebook in JupyterLab / Jupyter Notebook and run the cells in order. Alternatively, run the smoke tests described in the notebook.

Notes:
- Prefer `%pip install` inside a notebook cell only for ad-hoc installs; for reproducibility use the environment and `requirements.txt` above.
- Network access is required for `yfinance` requests.

## Notebook structure (summary)
The notebook is organised to be read and executed sequentially. Key sections:

- Setup and centralised imports — imports are kept in one cell to aid readability and reduce duplication.
- Global configuration — plotting defaults, data and plots directories, and toggles (preview, filename style, overwrite behaviour).
- Environment verification — checks presence of required packages and performs a lightweight `yfinance` request (AAPL) as a smoke test.
- Utility functions — small, well-documented helpers for deduplication, fetching hourly history, saving combined CSVs, and loading the latest CSV.
- Runner steps (0–3):
  - Step 0 — Smoke test: quick single-ticker fetch to validate helper functions and connectivity.
  - Step 1 — Fetch & Save: download hourly data for FAANG tickers and save a timestamped CSV in `data/`.
  - Step 2 — Load: read the most recent combined CSV into a dictionary of pandas DataFrames (indexed by Date).
  - Step 3 — Plot: generate and save a comparative close-price chart to `plots/`.

Each step is intentionally modular so you can re-run portions of the workflow without repeating network calls unnecessarily.

## Behaviour and file naming
- Timestamp format (UTC) for CSVs and plots: `YYYYMMDD-HHMMSS` (e.g. `20251105-220824.csv`).
- Default behaviour is conservative (no overwrite) — toggle flags are available in the notebook to change this.
- The notebook supports both timestamped and non-timestamped filenames via configuration flags.

## How to run the important checks
- Run the environment verification cell first. It will report which packages are available and execute a small `yfinance` call to confirm API/network access.
- If packages are missing, install them with `pip` (or use `install_requirements_if_missing()` provided in the notebook).

## Pedagogy and good practice (what to watch for)
- Keep code cells small, well-commented and idempotent where possible.
- Centralise imports and configuration to make notebook execution order less error-prone.
- Use UTC timestamps to make saved outputs machine-sortable and reproducible.
- Wrap file I/O in try/except to provide actionable diagnostics rather than failing silently.

## References and further reading
- yfinance — https://github.com/ranaroussi/yfinance (Ticker.history for fetching data)
- pandas documentation — https://pandas.pydata.org/docs/
- matplotlib documentation — https://matplotlib.org/stable/contents.html
- seaborn documentation — https://seaborn.pydata.org/
- PEP 8 (code style) — https://peps.python.org/pep-0008/
- Real Python — articles on imports, file I/O and constants: https://realpython.com/

## Next steps / suggestions
- Convert the notebook's core logic into a CLI script (`faang.py`) for non-interactive use (the notebook already documents this as Problem 3).
- Add a small automated test that validates the `verify_environment()` behaviour in CI (mocking network calls where appropriate).

---
Last updated: see commit history. For specific questions about the notebook, open `notebooks/problems.ipynb` and inspect the annotated cells.

License: See repository `LICENSE` file.