# 📘 Computer Infrastructure – FAANG Stock Analysis

This repository demonstrates reproducible workflows for FAANG stock analysis, aligned with the ATU Galway Computer Infrastructure module assessment. It provides transparent pipelines for fetching, validating, and visualising hourly FAANG data, with clear documentation and reviewer guidance.

**Author:** Edward Cronin  
**Student ID:** g00425645  
**Email:** g00425645@atu.ie  
**GitHub:** [ECronin1973](https://github.com/ECronin1973/computer_infrastructure/tree/main)  
**Module:** Higher Diploma in Data Analytics, ATU Galway (Winter 2025–2026)  

---

![FAANG Automation Workflow](https://github.com/ECronin1973/computer_infrastructure/actions/workflows/faang.yml/badge.svg)

---

## 📑 Table of Contents
1. [Background](#background)
2. [Target Audience](#target-audience)
3. [Environment Setup](#environment-setup)
4. [Included Files](#included-files)
5. [Helper Functions and Modular Design](#helper-functions-and-modular-design)
6. [Problem 1: Fetch Hourly FAANG Data](#problem-1--fetch-hourly-faang-data)
7. [Problem 2: Plot Closing Prices](#problem-2--plot-closing-prices)
8. [Problem 3: CLI Script (`faang.py`)](#problem-3--cli-script-faangpy)
9. [Problem 4: Automation with GitHub Actions](#problem-4--automation-with-github-actions)
10. [Extended Visualisations (Steps 8a to 8e)](#extended-visualisations-steps8a-to-8e)
11. [Workflow Documentation (Step 9)](#step-9--workflow-documentation)
12. [Requirements Compliance Checklist](#-requirements-compliance-checklist)
13. [Personal Reflection](#personal-reflection)
14. [Acknowledgements](#acknowledgements)

---

### Background

This notebook supports the ATU Winter 2025–2026 Computer Infrastructure module assessment (see [assessment problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md)).  
It implements a reproducible pipeline to collect, persist, and visualise hourly FAANG stock data for Meta (META), Apple (AAPL), Amazon (AMZN), Netflix (NFLX), and Alphabet (GOOG).

The workflow maps directly to the module’s assessment tasks:
- **Problem 1** — Fetch and save hourly FAANG data  
- **Problem 2** — Plot closing prices  
- **Problem 3** — Convert notebook logic into a CLI script  
- **Problem 4** — Automate execution with GitHub Actions  

**Notes and assumptions**  
- “5 days” refers to the last 5 trading sessions; weekends/holidays return data up to the most recent trading day.  
- Filenames are UTC timestamped and sortable (`YYYYMMDD-HHmmss.csv`) for deterministic “latest file” selection.  
- Helper functions and Markdown explanation blocks document design choices, runtime flags, and reviewer considerations.  

---

## Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/ECronin1973/computer_infrastructure.git
cd computer_infrastructure
```

After cloning, you can either:
- Run the notebook (problems.ipynb) step by step in Jupyter.
- Execute the script directly with ./faang.py to fetch data and generate plots automatically.
- outputs are automatically saved into data/ and plots/ folders with UTC‑timestamped filenames.

---

## Included Files

- `problems.ipynb` — main notebook implementing assessment tasks  
- `faang.py` — CLI script version of notebook logic  
- `data/` — folder for timestamped CSVs (raw downloads)  
- `plots/` — folder for saved PNGs (visualisations)  
- `.github/workflows/faang.yml` — GitHub Actions workflow for automation (committed and active)

---

## Environment Setup

To run the notebook and script successfully, choose one of the following setup options:

### Option 1: GitHub Codespaces (Recommended)

1. **Open the repository in Codespaces**  
   GitHub → Code dropdown → Codespaces → Create codespace on `main`

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
  ```

3. Check file permissions

```bash
ls -l
```

4. Make scripts executable (if needed)

```bash
chmod +x faang.py
```

5. Run the notebook or script

```bash
jupyter notebook problems.ipynb
./faang.py
```

Note: The script automatically saves CSVs and plots into data/ and plots/ folders with UTC‑timestamped filenames.

### Reference 
- [GitHub Codespaces Overview](https://docs.github.com/en/codespaces/quickstart)

### Option 2: Local Python Environment

1. Install Python 3.10+ 

📖 [Installing Python — Real Python](https://realpython.com/installing-python/)

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Make scripts executable (if needed)

```bash
chmod +x faang.py
```

5. Run the notebook or script

```bash
jupyter notebook problems.ipynb
./faang.py
```

### References
- [Python Virtual Environments — Real Python](https://realpython.com/python-virtual-environments-a-primer/).  
*This shows how to create and manage virtual environments for Python projects.*
- [chmod Command — GeeksforGeeks](https://www.geeksforgeeks.org/chmod-command-in-linux-with-examples/).  *This explains how to use the chmod command to change file permissions in Unix-like operating systems.*

---

## Target Audience

This repository is designed for:
- **Module reviewers** — to verify reproducibility and transparency of workflows  
- **Students** — to learn reproducible data analysis practices  
- **Collaborators** — to extend or adapt FAANG analysis pipelines for related projects  

---

## Helper Functions and Modular Design

This project uses a set of modular helper functions defined directly within the notebook (`problems.ipynb`) and script (`faang.py`). While these functions are not stored in a separate helper file (like `utils.py`), they are structured and reused in a way that mirrors the benefits of a modular helper module.

By adapting the logic into reusable functions within the main files, the project maintains clean separation of concerns, avoids code duplication, and supports both interactive and automated workflows — all without requiring external imports.

### Functions Used in This Project

The following helper functions are defined in the notebook (`problems.ipynb`).  
Additional functions, such as `plot_close_prices(data, output_dir)`, are implemented in the script (`faang.py`) to package the plotting logic for automation.

| Function | Purpose | Benefit | Reference |
|----------|---------|---------|-----------|
| `verify_environment(show_preview=True)` | Runs a quick connectivity check with yfinance and previews sample data. | Ensures dependencies and data access work before executing the full workflow. | [yfinance Quickstart](https://pypi.org/project/yfinance/) |
| `fetch_hourly_history(ticker)` | Retrieves 5 days of hourly OHLCV data for a single ticker. | Provides clean, labeled data for each FAANG stock. | [yfinance.Ticker.history](https://github.com/ranaroussi/yfinance) |
| `save_hourly_data(tickers, output_dir, overwrite=False)` | Fetches all tickers, concatenates them into one DataFrame, and saves a single timestamped CSV. | Guarantees reproducibility with versioned combined data files. | [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) |
| `load_latest_data(tickers, folder='data', show_preview=True)` | Reads the newest combined CSV and splits rows into separate DataFrames per ticker. | Supports targeted analysis and plotting by company. | [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) |
| `plot_data()` | Loads the latest combined CSV and plots hourly closing prices for all tickers. | Produces reviewer‑friendly PNGs saved in plots/ with timestamped filenames. | [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot) |
| `preview_dataframe(df)` | Prints shape, dtypes, and head of a DataFrame. | Quick inspection of structure and values for reviewers. | [pandas.DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) |
| `check_missing_values(df)` | Reports missing values per column. | Confirms dataset integrity before plotting or analysis. | [pandas.DataFrame.isnull](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html) |
| `describe_data(df)` | Generates summary statistics for numeric columns. | Provides quick insight into ranges, averages, and volatility. | [pandas.DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) |
| `add_returns_and_rolling(df)` | Adds derived columns: percentage returns and 30‑period rolling mean. | Supports optional analysis (return histograms, boxplots, rolling averages). | [pandas.DataFrame.pct_change](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html) |

> ℹ️ Note: In the notebook, plotting is handled by 'plot_data()' (Step 7). In the script (faang.py), plotting is modularised into plot_close_prices(data, output_dir) for automation. Optional enrichments (returns, rolling mean, correlation heatmap) are demonstrated in later notebook steps but are not required for the core assessment tasks.

---

### Why this matters
This project demonstrates reproducible workflows for FAANG stock analysis, aligning with module assessment requirements. By documenting inputs, alignment choices, and diagnostics, it ensures transparency for reviewers and provides a clear learning resource for students.”

### References  
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/)  
- [GeeksforGeeks – Python Helper Functions](https://www.geeksforgeeks.org/python-helper-functions/)  
- [Wikipedia – DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)  
- [pandas Documentation](https://pandas.pydata.org/docs/)  
- [matplotlib Documentation](https://matplotlib.org/stable/api/pyplot_summary.html)  
- [seaborn Documentation](https://seaborn.pydata.org)  

---

## Problem 1 — Fetch Hourly FAANG Data

### Objective  
Download hourly OHLCV data for META, AAPL, AMZN, NFLX, and GOOG covering the last 5 trading sessions, and save timestamped CSVs.

### What it does  
- Uses `yfinance` to fetch hourly data.  
- Aligns each ticker’s data with `Date` as datetime index.  
- Saves outputs into `data/` folder with filenames `TICKER_YYYYMMDD-HHmmss.csv` (UTC).  

### Why it’s useful  
*Provides reproducible, timestamped datasets for analysis and comparison.*  
- Guarantees reviewers can trace plots and statistics back to exact input files.  
- Prevents ambiguity around weekends or market holidays by explicitly saving the last available trading session.  

### Reviewer guidance  
- Diagnostics print shape and time range before saving.  
- Filenames are lexicographically sortable for deterministic “latest file” selection.  
- If no overlapping timestamps are found, consider outer joins with documented NaN handling.  

### References  
- [yfinance documentation](https://pypi.org/project/yfinance/)  
- [pandas read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
- [datetime module](https://docs.python.org/3/library/datetime.html)  

---

## Problem 2 — Plot Closing Prices

### Objective  
Load the latest saved CSV for each ticker and plot hourly Close prices on a single chart.

### What it does  
- Uses `load_latest_csvs()` helper to select the most recent file per ticker.  
- Plots all five Close price series on a shared timeline with axis labels, legend, and date‑range title.  
- Saves plots to `plots/` with filenames `faang_close_YYYYMMDD-HHmmss.png` (UTC).  
- Supports a stable filename `faang_close.png` when `NO_DATE_PLOTS=True` (useful for README embedding).  

### Why it’s useful  
*Provides a clear visual comparison of FAANG hourly closes over the last five trading days.*  

### Reviewer guidance  
- Titles explicitly display the last available trading session to avoid weekend/holiday ambiguity.  
- Saved plots are timestamped for reproducibility.

### Output File
![Example Plot](plots/20251122-162358.png)

### References  
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)  
- [pandas timeseries guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)  

---

## Problem 3 — CLI Script (`faang.py`)

### Objective  
Encapsulate notebook logic into a standalone script for repeatable execution.

### What it does  
- Replicates notebook functions in `faang.py`.  
- Supports CLI flags (`--plot`, `--overwrite`, `--show`).  
- Saves outputs into `data/` and `plots/` folders with timestamped filenames.  

### Why it’s useful  
*Enables reproducible automation outside Jupyter, with flexible command‑line execution.*  

### Reviewer guidance  
- Documented usage and functionality in README.  
- Tested in both terminal and GitHub Codespaces environments.  

### References  
- [argparse documentation](https://docs.python.org/3/library/argparse.html)  

---

## Problem 4: Automation with GitHub Actions

### Objective 
Automate execution of faang.py on a fixed cadence.

### What it does
- Provides scheduled workflow (.github/workflows/faang.yml).
- Commits updated CSVs and plots to repository.
- Produces clear, auditable commit history.

### GitHub Actions Workflow
- The automation pipeline is defined in `.github/workflows/faang.yml`.  
- This file documents triggers, environment setup, dependency installation, diagnostics, script execution, and commit/push steps.

### Workflow Logs
- Each automated run produces detailed logs in the GitHub Actions dashboard.  
- Reviewers can verify environment diagnostics, script execution, and commit history directly from these logs.
- Logs can be accessed via the Actions tab in GitHub, under the FAANG Automation Workflow runs.

### Automated Outputs
- New CSVs are saved into `data/` with UTC‑timestamped filenames.  
- Plots are saved into `plots/` with UTC‑timestamped filenames.  
- Both are committed weekly by the GitHub Actions workflow, ensuring reproducibility and transparency.

### Why it’s useful 
Ensures outputs remain fresh and reproducible without manual intervention.

### Reviewer guidance
- Workflow is conservative; runs weekly by default.
- Commit history documents updates transparently.

### References
- [GitHub Actions documentation](https://docs.github.com/en/actions)

---

## Local Repository Sync
Before making local changes, run `git status` and `git pull` to ensure your branch is up to date.  
This prevents conflicts with automated commits pushed by the workflow and maintains a clean audit trail.

---

### 📌 Requirements Compliance Checklist

This section confirms that the notebook and repository meet the assessment requirements for **Problem 1 (Data Collection)**, **Problem 2 (Visualisation)**, **Problem 3 (CLI Script)**, and **Problem 4 (Automation)**.

---

**Problem 1: Data from yfinance**
- ✔ Function `get_data()` defined  
- ✔ Downloads **hourly OHLCV data** for the last 5 trading days  
- ✔ Covers FAANG tickers: META, AAPL, AMZN, NFLX, GOOG  
- ✔ Saves data into `data/` folder  
- ✔ Filenames follow format `TICKER_YYYYMMDD-HHmmss.csv` (UTC)  
- ✔ Creates `data/` folder automatically if missing  

---

**Problem 2: Plotting Data**
- ✔ Function `plot_data()` defined  
- ✔ Opens latest CSV file in `data/`  
- ✔ Plots hourly `Close` prices for all FAANG tickers on one chart  
- ✔ Adds axis labels, legend, and title with last available trading date  
- ✔ Saves plot into `plots/` folder with timestamped filename `faang_close_YYYYMMDD-HHmmss.png`  
- ✔ Creates `plots/` folder automatically if missing  
- ✔ Displays plot inline in the notebook  

**Clarification:**  
All plotted values are **hourly closes**, not daily closes. Each point reflects the end of a one‑hour trading interval, exactly as required by the assignment.

---

**Problem 3: CLI Script (`faang.py`)**
- ✔ Script `faang.py` created replicating notebook logic  
- ✔ Supports flags: `--plot`, `--overwrite`, `--show`  
- ✔ Saves timestamped CSVs into `data/` and plots into `plots/`  
- ✔ Provides deterministic “latest file” selection via lexicographic sort  
- ✔ Includes inline documentation and usage notes for reviewers  
- ✔ Tested in terminal and Codespaces environments  

---

**Problem 4: Automation with GitHub Actions**
- ✔ Workflow file `.github/workflows/faang.yml` defined  
- ✔ Automates execution of `faang.py` on a fixed cadence (weekly by default)  
- ✔ Commits updated CSVs and plots to repository  
- ✔ Produces clear, auditable commit history for reproducibility  
- ✔ Workflow conservatively scheduled to avoid rate‑limit issues  

---

**Overall Compliance Notes**
- ✔ All problems (1–4) implemented with reproducibility and transparency in mind  
- ✔ Diagnostics (shapes, ranges, co‑observation counts) printed before key computations  
- ✔ Helper functions and Markdown explanation blocks document design choices and reviewer considerations  

---

## Extended Visualisations (Steps 8a to 8e)

These optional, display‑only cells build on the Problem 1–4 workflow to provide deeper analysis and exploratory plots.

---

### Step 8a — Return Distributions

**Objective**  
Plot histograms and kernel density estimates (KDEs) of hourly returns for each ticker.

**What it does**  
- Computes synchronous hourly returns from aligned Close prices.  
- Plots histograms with overlaid KDE curves.  

**Why it’s useful**  
*Highlights distribution shape, skewness, and volatility across FAANG tickers.*  

**Reviewer guidance**  
- Ensure returns are computed after alignment to avoid spurious distributions.  

**References**  
- [seaborn histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)  

---

### Step 8b — Pairwise Scatterplot Matrix

**Objective**  
Visualise pairwise relationships between synchronous returns.

**What it does**  
- Uses `seaborn.pairplot` to plot scatterplots for each ticker pair.  
- Diagonal plots show KDEs of individual return distributions.  

**Why it’s useful**  
*Reveals linear/non‑linear relationships and potential outliers.*  

**Reviewer guidance**  
- Confirm alignment diagnostics before plotting.  

**References**  
- [seaborn pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)  

---

### Step 8c — Correlation Analysis

**Objective**  
Compute and visualise Pearson correlations on synchronous returns.

**What it does**  
- Aligns tickers with inner join.  
- Computes correlation matrix with `returns.corr()`.  
- Displays annotated heatmap.  

**Why it’s useful**  
*Shows strength and direction of co‑movement between FAANG tickers.*  

**Reviewer guidance**  
- Diagnostics print sample size and time range.  
- Inner join ensures correlations reflect truly co‑observed hours.  

**References**  
- [Pearson correlation coefficient overview](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)  
- [seaborn heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)  

---

### Step 8d — Cumulative Returns vs Benchmark

**Objective**  
Plot cumulative returns for each ticker against an equal‑weight FAANG benchmark.

**What it does**  
- Builds aligned price matrix.  
- Computes synchronous returns and equal‑weight benchmark.  
- Plots cumulative returns `(1 + r).cumprod() - 1`.  

**Why it’s useful**  
*Highlights relative outperformance vs a simple portfolio proxy.*  

**Reviewer guidance**  
- Diagnostics print aligned shape and time range.  
- Optional log scale can be enabled for growth rate comparison.  

**References**  
- [Cumulative return overview](https://www.investopedia.com/terms/c/cumulative-return.asp)  
- [Matplotlib plotting](https://matplotlib.org/stable/contents.html)  

---

### Step 8e — Rolling Average Plots

**Objective**  
Plot hourly Close prices alongside a 30‑period rolling average.

**What it does**  
- Reads each ticker’s DataFrame from Step 1.  
- Uses existing `RollingMean` column or computes in‑memory 30‑period SMA.  
- Plots Close vs rolling average.  

**Why it’s useful**  
*Smooths short‑term fluctuations to reveal longer‑term trends.*  

**Reviewer guidance**  
- Plots are exploratory only; they do not modify saved CSVs.  
- Adjust rolling window if needed for different smoothing levels.  

**References**  
- [pandas rolling](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)  
- [Moving averages overview (Investopedia)](https://www.investopedia.com/terms/m/movingaverage.asp)  

---

## Step 9 — Workflow Documentation

### Objective  
Summarise the notebook’s workflow and reproducibility practices.

### Workflow demonstrated  
1. Fetch hourly FAANG data  
2. Load and validate downloads  
3. Preview and summarise datasets  
4. Plot closing prices  
5. Extended visualisations (returns, rolling means, histograms, boxplots, pairplots)  
6. Correlation analysis on synchronous returns  
7. Comparative performance vs benchmark  
8. Notebook‑level documentation and references  

### Why it’s useful  
*Provides a clear roadmap of the analysis pipeline and ensures transparency for reviewers.*  

### Reviewer guidance  
- Each step documents inputs, alignment choices, and imputation.  
- Diagnostics (shapes, time ranges, co‑observation counts) are printed before key computations.  

### References  
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)  
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)  
- [Seaborn documentation](https://seaborn.pydata.org/)  

---

### Acknowledgements

Copilot was used to assist with code generation and suggestions throughout this project.

---

### Personal Reflection

This project reinforced the importance of writing clean, concise, and reproducible code. Copilot assisted with code generation, but outputs were simplified and refined for clarity. By focusing on transparency, diagnostics, and reviewer guidance, the final workflow is both efficient and easy to understand.

### END