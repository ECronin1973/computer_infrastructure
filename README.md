
# FAANG Stock Data — Hourly Analysis

This repository provides a Jupyter notebook and supporting code for fetching, inspecting, and plotting hourly OHLCV stock data for the FAANG companies (Meta, Apple, Amazon, Netflix, and Alphabet). This README summarises the notebook (`notebooks/problems.ipynb`), explains environment setup, and lists references for further study.

---

## 🎯 Target Audience

This lab is intended for computing students and professionals with some experience in Python (familiarity with pandas and matplotlib is recommended). The material is self-contained, with helper functions, environment checks, and usage notes provided in the notebook, enabling users to follow along in a local environment or CI pipeline.

---

## 🧩 Assignment Structure

The notebook addresses the following problems, as outlined in the [Assessment Problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md) for the ATU [Computer Infrastructure module 2025–2026](https://vlegalwaymayo.atu.ie/course/view.php?id=13109):

- **Problem 1:** Fetch and save hourly FAANG data
- **Problem 2:** Load and visualise the latest dataset
- **Problems 3–4:** Reserved for future extensions (e.g., anomaly detection, forecasting)

---

## Project Overview

- Retrieve hourly stock data using `yfinance`
- Clean and prepare OHLCV time series in pandas
- Visualise comparative close-price series for FAANG tickers
- Practical tips for reproducible notebook work (centralised imports, plotting defaults, timestamped outputs)

---

## Learning Outcomes

After completing the notebook, users will be able to:

- Fetch hourly historical data for multiple tickers and save combined CSVs
- Load the most recent timestamped CSV into pandas for analysis
- Produce and save timestamped plots comparing close prices
- Apply defensive programming patterns in notebooks to enhance reproducibility and debuggability

---

## 📚 Background: Accessing Market Data with yfinance

This project uses [`yfinance`](https://github.com/ranaroussi/yfinance) to retrieve hourly OHLCV data from Yahoo Finance.

### Why yfinance?

- No API key required
- Supports hourly and daily intervals
- Returns pandas-compatible DataFrames
- Ideal for exploratory analysis and educational use

> ⚠️ Note: `yfinance` is not affiliated with or endorsed by Yahoo Inc. Use it only for educational or research purposes.

---

## Repository Structure

- `notebooks/problems.ipynb` — Primary notebook, organised into modular steps (environment verification, fetch & save, load, plot)
- `data/` — Timestamped CSV outputs (e.g., `20251105-220824.csv`)
- `plots/` — Generated PNG visualisations (e.g., FAANG close-price chart)
- `requirements.txt` — List of Python packages for environment setup

---

## Quick Start

1. **Create and activate a virtual environment (recommended):**
   - Windows PowerShell:
     ```powershell
     python -m venv .venv; .\.venv\Scripts\Activate.ps1
     ```
2. **Install requirements:**
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. **Open the notebook in JupyterLab or Jupyter Notebook and run the cells in order.** Alternatively, run the smoke tests described in the notebook.

**Notes:**
- Prefer `%pip install` inside a notebook cell only for ad-hoc installs; for reproducibility, use the environment and `requirements.txt`.
- Network access is required for `yfinance` requests.

---

## Notebook Structure

The notebook is designed to be read and executed sequentially. Key sections:

- **Setup and centralised imports:** All imports are in one cell for readability and to reduce duplication.
- **Global configuration:** Plotting defaults, data and plots directories, and toggles (preview, filename style, overwrite behaviour).
- **Environment verification:** Checks for required packages and performs a lightweight `yfinance` request (AAPL) as a smoke test.
- **Utility functions:** Well-documented helpers for deduplication, fetching hourly history, saving combined CSVs, and loading the latest CSV.

- **Runner steps (0–3):**
  - Step 0 — Smoke test: quick single-ticker fetch to validate helper functions and connectivity.
  - Step 1 — Fetch & Save: download hourly data for FAANG tickers and save a timestamped CSV in `data/`.
  - Step 2 — Load: read the most recent combined CSV into a dictionary of pandas DataFrames (indexed by Date).
  - Step 3 — Plot: generate and save a comparative close-price chart to `plots/`.

Each step is modular, allowing users to rerun parts of the workflow without unnecessary network calls.

---

## Behaviour and File Naming

- Timestamp format (UTC) for CSVs and plots: `YYYYMMDD-HHMMSS` (e.g., `20251105-220824.csv`)
- Default behaviour is conservative (no overwrite); toggle flags are available in the notebook to change this
- Supports both timestamped and non-timestamped filenames via configuration flags

---

## Checks and Good Practice

- Run the environment verification cell first to confirm package availability and API/network access
- If packages are missing, install them with `pip` or use `install_requirements_if_missing()` provided in the notebook
- Keep code cells small, well-commented, and idempotent where possible
- Centralise imports and configuration to reduce errors
- Use UTC timestamps for machine-sortable and reproducible outputs
- Wrap file I/O in try/except blocks for actionable diagnostics

---

## References and Further Reading

- [yfinance documentation](https://github.com/ranaroussi/yfinance)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [seaborn documentation](https://seaborn.pydata.org/)
- [PEP 8 (code style)](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/) — articles on imports, file I/O, and constants

---

## Next Steps / Suggestions

- Convert the notebook's core logic into a CLI script (`faang.py`) for non-interactive use (documented as Problem 3)
- Add a small automated test to validate the `verify_environment()` behaviour in CI (mocking network calls where appropriate)

---

_Last updated: see commit history. For specific questions about the notebook, open `notebooks/problems.ipynb` and inspect the annotated cells._

**Licence:** See repository `LICENSE` file.
