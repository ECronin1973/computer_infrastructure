# 📘 Computer Infrastructure – FAANG Stock Analysis

This repository contains solutions to the four assessment problems for the ATU Galway Computer Infrastructure module. It provides a transparent, reproducible pipeline to fetch hourly FAANG stock data for the last 5 trading days, save timestamped CSVs, and produce reviewer‑friendly plots that clearly state the last available trading date. Automation via GitHub Actions is supported to keep outputs fresh and reproducible.

**Author:** Edward Cronin  
**Student ID:** g00425645  
**Email:** g00425645@atu.ie  
**GitHub:** [ECronin1973](https://github.com/ECronin1973/computer_infrastructure/tree/main)  
**Module:** Higher Diploma in Data Analytics, ATU Galway (Winter 2025–2026)  

---

## 📑 Table of Contents
1. [Background](#background)
2. [Download repository](#download-repository)
3. [Target audience](#target-audience)
4. [Environment setup](#environment-setup)
5. [Included files](#included-files)
6. [Functions used in this project](#functions-used-in-this-project)
7. [Helper Functions and Modular Design](#helper-functions-and-modular-design)
8. [Problem 1: Fetch Hourly FAANG Data](#problem-1-fetch-hourly-faang-data)
9. [Problem 2: Plotting Data](#problem-2-plotting-data)
10. [Problem 3: Script Creation (`faang.py`)](#problem-3-script-creation-faangpy)
11. [Problem 4: Automation with GitHub Actions (To Be Completed)](#problem-4-automation-with-github-actions-to-be-completed)
12. [Analysis (optional)](#analysis-optional)
13. [Acknowledgements](#acknowledgements)
14. [Personal reflection](#personal-reflection)

---

### Background
This notebook supports the ATU Winter 2025–2026 Computer Infrastructure module assessment (see [assessment problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md)) and implements a reproducible pipeline to collect, persist, and visualise hourly FAANG stock data. It focuses on the following tickers: Meta (META), Apple (AAPL), Amazon (AMZN), Netflix (NFLX), and Alphabet (GOOG), using Python tooling: yfinance (data retrieval), pandas (data handling), matplotlib and seaborn (visualisation).

The work maps directly to the module assessment tasks:

#### Problem 1 — Fetch and save hourly data
- Download hourly OHLCV for each FAANG ticker covering the last 5 trading days (trading days, not calendar days).
- Persist raw outputs as timestamped CSV files in data/ for reproducibility.

#### Problem 2 — Plot closing prices
- Load the latest CSV per ticker and plot hourly Close series on a single comparison chart.
- Save reviewer‑friendly, timestamped PNGs to plots/. Chart titles explicitly display the last available trading session to avoid weekend/holiday ambiguity.

#### Problem 3 — Convert logic into a CLI script
- Encapsulate notebook logic into faang.py with flags such as --plot, --overwrite, and --show for repeatable, scriptable execution.

#### Problem 4 — Automate execution using GitHub Actions
- Provide a scheduled workflow (.github/workflows/faang.yml) that runs the script on a fixed cadence (for example, weekly) and commits updated CSVs and plots to the repository to produce a clear, auditable commit history.

**Notes and assumptions**

- “5 days” always refers to the last 5 trading sessions; running the notebook or script on weekends or market holidays will return data up to the most recent trading day because exchanges are closed.
- Filenames are UTC timestamped and lexicographically sortable (format: TICKER_YYYYMMDD-HHmmss.csv) to allow deterministic “latest file” selection.
- Helper functions and short Markdown explanation blocks are included throughout the notebook to document design choices, runtime flags, and reviewer considerations.

---

### Download Repository

To download and explore the repository:

```bash
git clone https://github.com/ECronin1973/computer_infrastructure.git
cd computer_infrastructure
```

After cloning, you can either:
- Run the notebook (problems.ipynb) step by step in Jupyter.
- Execute the script directly with ./faang.py to fetch data and generate plots automatically.
- outputs are automatically saved logically into data/ and plots/ folders.

### Included Files

- [problems.ipynb](https://github.com/ECronin1973/computer_infrastructure/blob/main/problems.ipynb) — Interactive notebook with modular steps for each problem
- [faang.py](https://github.com/ECronin1973/computer_infrastructure/blob/main/faang.py) — CLI script with mirrored logic from the notebook
- data/ — Folder for saved timestamped CSV files
- plots/ — Folder for saved timestamped PNG plots
- [requirements.txt](https://github.com/ECronin1973/computer_infrastructure/blob/main/requirements.txt) — Python dependencies

---

## Environment Setup

To run the notebook and script successfully, choose one of the following setup options:

### Option 1: GitHub Codespaces (Recommended)
1. Open the repository in Codespaces → GitHub → Code dropdown → Codespaces → Create codespace on main

2. Install required packages

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

**note:** the script automatically saves CSV's and plots appropriately into data/ and plots/ folders.

📖 Reference: [GitHub Codespaces Overview](https://docs.github.com/en/codespaces/quickstart)

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
📖 References:

[Python Virtual Environments — Real Python](https://realpython.com/python-virtual-environments-a-primer/).  
*This shows how to create and manage virtual environments for Python projects.*

[chmod Command — GeeksforGeeks](https://www.geeksforgeeks.org/chmod-command-in-linux-with-examples/).  *This explains how to use the chmod command to change file permissions in Unix-like operating systems.*

---

## Target Audience

This repository is designed for computing students and professionals with intermediate Python skills ([Real Python](https://realpython.com/intermediate-python/)). Familiarity with pandas ([docs](https://pandas.pydata.org/docs/)), matplotlib ([docs](https://matplotlib.org/stable/users/index.html)), and basic CLI usage ([Real Python CLI Guide](https://realpython.com/ref/stdlib/argparse/)) is recommended. The notebook includes environment checks, helper functions, and modular steps ([Real Python Modules](https://realpython.com/python-modules-packages/)) to support reproducibility and automation.

**note** the notebook is designed to be **reviewer-friendly**, with clear sections, comments, and references to facilitate understanding and assessment.

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

These functions are designed for **reusability, readability, and transparency**. Their modular structure ensures reproducibility across both notebook and script, while making it easy for reviewers to see how each step fulfils the assessment requirements. Inline documentation and clear responsibilities mean the workflow can be maintained or scaled later without breaking consistency.


#### References  
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/)  
- [GeeksforGeeks – Python Helper Functions](https://www.geeksforgeeks.org/python-helper-functions/)  
- [Wikipedia – DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)  
- [pandas Documentation](https://pandas.pydata.org/docs/)  
- [matplotlib Documentation](https://matplotlib.org/stable/api/pyplot_summary.html)  
- [seaborn Documentation](https://seaborn.pydata.org)  

---

## Problem 1: Fetch Hourly FAANG Data

### Objective
Use the `yfinance` package to fetch **5 days of hourly OHLCV data** for the FAANG tickers and save the results to a timestamped CSV file.  
This fulfils the **Problem 1 requirement** of the assessment.

### Workflow
- Define and validate the FAANG ticker list (`META`, `AAPL`, `AMZN`, `NFLX`, `GOOG`).  
- Use `fetch_hourly_history()` to retrieve hourly OHLCV data via `yfinance.Ticker.history`.  
- Label each DataFrame with a `Ticker` column and clean the index (`Date`).  
- Concatenate all ticker DataFrames into one combined dataset.  
- Save the dataset to `data/YYYYMMDD-HHMMSS.csv` using `pandas.DataFrame.to_csv`.  

### 📤 Output File
- **Format:** `data/YYYYMMDD-HHMMSS.csv`  
- **Example:** `data/20251122-162358.csv`  
- A single combined CSV is saved per run, containing rows for all FAANG tickers.  
- Each row includes OHLCV values plus a `Ticker` label for clarity.  
- Filenames are timestamped for reproducibility and version control.

📖 References:  
- [yfinance.Ticker.history](https://github.com/ranaroussi/yfinance)  
- [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)  
- [datetime Module](https://docs.python.org/3/library/datetime.html)  

---

## 📊 Problem 2: Plotting Data

### 🎯 Objective
Visualise the **hourly closing prices** of all FAANG tickers using the most recent CSV file.  
This fulfils the **Problem 2 requirement** of the assessment.

### ⚙️ Workflow
1. Load the latest combined CSV from the `data/` folder using `pandas.read_csv`.  
2. Split rows by ticker and plot the `Close` prices for each using `matplotlib`.  
3. Add axis labels (`Date`, `Close Price (USD)`), a legend for tickers, and a title showing the **current system date** at runtime.  
4. Save the plot to `plots/YYYYMMDD-HHMMSS.png` with a UTC timestamped filename.  

### 📤 Output File
- **Format:** `plots/YYYYMMDD-HHMMSS.png`  
- **Example:** `plots/20251122-162358.png`  
- Each plot provides a clear visual comparison of FAANG hourly closes over the last five trading days.  

![Example Plot](plots/20251122-162358.png)

📖 References:  
- [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
- [matplotlib.pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)  

---

### Analysis (optional)
These visuals extend beyond the assessment and are displayed inline in the notebook (not saved as PNGs). They build on the derived columns added in Step 6a (Return and RollingMean).

### Step 8 visualisations (8a–8e)

#### 8a: Per‑ticker return distribution (histogram + KDE):

 For each ticker, hourly returns are computed with pct_change(), converted to numeric, and plotted using seaborn.histplot with a seaborn.kdeplot overlay. This highlights the distribution shape and volatility for each stock.

#### 8b: Return distribution (remaining tickers):
  The histogram + KDE workflow repeats across all FAANG tickers, ensuring consistent comparison of hourly return behaviour and tail risk profiles across symbols.

#### 8c: Cross‑ticker returns boxplot: 

  Returns for all tickers are assembled into a single DataFrame and plotted via seaborn.boxplot, summarising spread and outliers to compare volatility at a glance.

#### 8d: Rolling average overlays (per ticker): 

  Each ticker’s raw Close series is plotted alongside a 30‑period rolling mean (rolling(window=30).mean()), using matplotlib line plots to reveal smoothed trends versus hourly noise.

#### 8e: Notes on plotting style and previews: 

  Plots use a consistent white‑grid style (seaborn.set_style('whitegrid')), and the notebook includes previews and summaries before plotting to validate data integrity and shape.
---

## Problem 3: Script Creation (`faang.py`)

### Objective
Convert the notebook logic into a standalone Python script that can be executed from the terminal.  
This fulfils the **Problem 3 requirement** of the assessment.

### Script: `faang.py`
The script replicates the notebook logic and supports flexible execution via command‑line flags.  
It automatically saves outputs into the `data/` and `plots/` folders with timestamped filenames.

### Features
- Fetches and saves hourly FAANG data (`save_hourly_data()`)  
- Generates and saves comparative plots (`plot_close_prices()`)  
- Supports CLI flags for flexible execution  
- Titles plots with the **last available trading date** for consistency  

### CLI Flags
- `--plot` — Generate and save a plot after fetching data  
- `--overwrite` — Allow overwriting an existing CSV file  
- `--show` — Display the plot after saving  

📖 Reference: [argparse — CLI Argument Parsing](https://docs.python.org/3/library/argparse.html)

### Script Design Process
- ✅ Copied modular functions from the notebook into `faang.py`  
  📖 [Modular Functions in Python](https://realpython.com/python-modules-packages/)  

- ✅ Implemented `plot_close_prices()` in the script to package plotting logic  
  📖 [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html), [seaborn](https://seaborn.pydata.org)  

- ✅ Integrated `argparse` to support CLI flags  
  📖 [argparse Documentation](https://docs.python.org/3/library/argparse.html)  

- ✅ Mapped notebook steps to discrete functions for clarity and reuse  
  📖 [Python Modules and Packages](https://realpython.com/python-modules-packages/)  

- ✅ Added CLI flags for flexible execution in different environments  

- ✅ Tested the script in both terminal and GitHub Codespaces environments  

- ✅ Documented usage and functionality in this README  
  📖 [Documenting Python Code](https://realpython.com/documenting-python-code/)  

---

## Problem 4: Automation with GitHub Actions ( To Be Completed )

---

### Acknowledgements

Copilot was used to assist with code generation and suggestions throughout this project.

### Personal Reflection

They say less is more and that is certainly true when it comes to writing code.  I used copilot to help me with this assignment and found that it often produced code that was too verbose and complicated for the task at hand.  By simplifying the code and focusing on the core functionality, I was able to create a more efficient and maintainable solution.  By reviewing weekly lectures, I was able to see what was being asked in a notebook, not cells full of extremely complicated code.  I was conscious of my audience. This experience has reinforced the importance of writing clean and concise code, and I will strive to apply this principle in my future coding endeavors.  I found the feedback very useful in helping me to identify areas where I could improve my code and I set out to ensure that my final submission reflected these improvements. I spent time refining my code to enhance its clarity and efficiency, ultimately leading to I hope, a more polished final submission.

