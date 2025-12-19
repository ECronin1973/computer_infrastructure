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

This project implements modular helper functions directly within the notebook (problems.ipynb) and script (faang.py). Although these functions are not placed in a separate helper file such as utils.py, their structure and reuse provide the advantages typically associated with a modular helper module.

Adapting logic into reusable functions within the main files ensures a clear separation of concerns, minimizes code duplication, and supports both interactive and automated workflows without the need for external imports.

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

In the notebook, plotting is managed by the plot_data() function (Step 7). In the script (faang.py), plotting is modularized into plot_close_prices(data, output_dir) to facilitate automation. Optional enhancements, such as returns, rolling mean, and correlation heatmap, are demonstrated in subsequent notebook steps but are not required for the core assessment tasks.

---

### Why this matters
This project demonstrates reproducible workflows for FAANG stock analysis in accordance with module assessment requirements. Documenting inputs, alignment choices, and diagnostics ensures transparency for reviewers and offers a clear learning resource for students.

### References  
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/)  
- [GeeksforGeeks – Python Helper Functions](https://www.geeksforgeeks.org/python-helper-functions/)  
- [Wikipedia – DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)  
- [pandas Documentation](https://pandas.pydata.org/docs/)  
- [matplotlib Documentation](https://matplotlib.org/stable/api/pyplot_summary.html)  
- [seaborn Documentation](https://seaborn.pydata.org)  

---

## Problem 1: Retrieval of Hourly FAANG Data

### Objective
Obtain hourly OHLCV data for META, AAPL, AMZN, NFLX, and GOOG for the five most recent trading sessions, and store the results as timestamped CSV files

### Purpose
- Utilises the yfinance library to retrieve hourly OHLCV data for each ticker independently.
- Stores all tickers together in a single CSV file, with a Ticker column identifying each series.
- Saves output files in the data/ directory using the format YYYYMMDD-HHmmss.csv (UTC)

### Function
Enables reproducible and timestamped datasets suitable for subsequent analysis and comparison.
- Ensures that reviewers can trace plots and statistical results directly to the corresponding input files.
- Eliminates ambiguity related to weekends or market holidays by explicitly saving data from the most recent available trading session

### Reviewer Note
- Diagnostic outputs display the data shape and time range prior to saving.
- Filenames are lexicographically sortable, ensuring deterministic selection of the most recent dataset.
- Alignment of timestamps (inner/outer joins) is performed in later analysis steps, not during data retrieval.

### References  
- [yfinance documentation](https://pypi.org/project/yfinance/)  
- [pandas read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
- [datetime module](https://docs.python.org/3/library/datetime.html)  

---

## Problem 2 — Plot Closing Prices

### Objective
Load the most recent CSV file containing all FAANG tickers and plot the hourly closing prices on a single chart.

### Purpose
- Utilise the load_latest_data() helper function to select and load the most recent timestamped CSV file from the data/ directory.
- Plot all five closing price series on a shared timeline, including axis labels, a legend, and a title showing the last available trading date.
- Save plots in the plots/ directory using filenames formatted as YYYYMMDD-HHmmss.png (UTC).
- Support a stable filename, faang_close.png, when NO_DATE_PLOTS is set to True (useful for embedding in README files).

### Function
Enable clear visual comparison of FAANG hourly closing prices over the most recent five trading days.

### Reviewer Note
- Ensure that titles explicitly display the last available trading session to avoid ambiguity around weekends or holidays.
- Timestamp saved plots to support reproducibility and traceability.

### References  
- [matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [Pandas - timeseries guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)

---

## Problem 3 — CLI Script (faang.py)

### Objective
Encapsulates notebook logic within a standalone script to enable repeatable execution.

### Function
- Implements the notebook's functions within faang.py.
- Supports command-line interface (CLI) flags, including --plot, --overwrite, and --show.
- Saves outputs to the data and plots directories, appending timestamped filenames.
- The script mirrors the notebook’s behaviour but does not require a Jupyter environment, making it suitable for batch execution or integration into automated workflows.

### Purpose
- Facilitates reproducible automation outside of Jupyter environments and allows flexible command-line execution.

### Reviewer Note
- Usage instructions and functionality are documented in the README file.
- The script has been tested in both terminal and GitHub Codespaces environments.

### References  
- [argparse documentation](https://docs.python.org/3/library/argparse.html)  

---

# Problem 4: Automation with GitHub Actions

## Objective
The execution of 'faang.py' is automated on a fixed schedule to ensure reproducibility, transparency, and outputs that facilitate reviewer assessment. The workflow is scheduled for 08:08 UTC every Saturday to avoid market open and close times and to minimize rate-limit issues.

## Workflows

### FAANG Automation Workflow
- **File:** `.github/workflows/faang.yml`
- **Purpose:** Executes  `faang.py` on a weekly basis to generate updated datasets and plots.
- **Process:**  
  - Triggered on a scheduled cadence.  
  - Sets up the environment, installs dependencies, and runs diagnostics.  
  - Executes `faang.py` and commits the resulting outputs to the repository.  
- **Outputs:**  
  - New CSVs saved in `data/` with UTC‑timestamped filenames.  
  - New plots saved in `plots/` with UTC‑timestamped filenames.  
  - Weekly commits support reproducibility and provide a transparent audit trail.  
- **Logs:**  
  - Each run produces detailed logs in the **Actions** tab.  
  - Reviewers are able to verify the environment setup, script execution, and commit history directly.

### Practice Workflow
- **File:** `.github/workflows/github-actions-practice.yml`
- **Purpose:** Provides a lightweight sandbox for testing GitHub Actions functionality prior to deploying the full FAANG pipeline.
- **Process:**  
  - Triggered on **push events**.  
  - Executes a basic job to list repository files. 
- **Benefits:**  
  - Safe experimentation without affecting the FAANG workflow.  
  - Confirms workflow triggers and syntax correctness.  
  - Serves as a reference for future workflow development.  
- **Reviewer Note:** : This workflow is not included in formal assessment tasks; however, its runs are available for review in the **Actions** tab.

## Verification
Following the scheduled FAANG workflow execution:
- Checked the **Actions** tab for successful execution.  
- Reviewed logs for errors or warnings.  
- Confirmed the presence of new CSV files and plots with UTC-timestamped filenames in the data and plots directories.  
- Verified commits were pushed to the repository.  
- Ran `git status` and `git pull` locally to sync with remote changes.

## Local Repository Sync
Before making local changes, always run:
```bash
git status
git pull
```
---

### 📌 Requirements Compliance Checklist

This section confirms that the notebook and repository meet the assessment requirements for **Problem 1 (Data Collection)**, **Problem 2 (Visualisation)**, **Problem 3 (CLI Script)**, and **Problem 4 (Automation)**.

---

#### Problem 1: Data from yfinance
- ✔ Function `get_data()` defined  
- ✔ Downloads **hourly OHLCV data** for the last 5 trading days  
- ✔ Covers FAANG tickers: META, AAPL, AMZN, NFLX, GOOG  
- ✔ Saves data into `data/` folder  
- ✔ Filenames follow format YYYYMMDD-HHmmss.csv (UTC), containing all tickers in one file.
- ✔ Creates `data/` folder automatically if missing  

---

#### Problem 2: Plotting Data
- ✔ Function `plot_data()` defined  
- ✔ Opens latest CSV file in `data/`  
- ✔ Plots hourly `Close` prices for all FAANG tickers on one chart  
- ✔ Adds axis labels, legend, and title with last available trading date  
- ✔ Saves plot into plots/ with timestamped filename YYYYMMDD-HHmmss.png
- ✔ Creates plots/ folder automatically if missing  
- ✔ Displays plot inline in the notebook  

---

#### Problem 3: CLI Script (`faang.py`) 
- ✔ Script `faang.py` created replicating notebook logic  
- ✔ Supports flags: `--plot`, `--overwrite`, `--show`  
- ✔ Saves timestamped CSVs into `data/` and plots into `plots/`
- ✔ Supports stable filename faang_close.png when NO_DATE_PLOTS=True 
- ✔ Provides deterministic “latest file” selection via lexicographic sort  
- ✔ Includes inline documentation and usage notes for reviewers  
- ✔ Tested in terminal and Codespaces environments  

---

#### Problem 4: Automation with GitHub Actions
- ✔ Workflow file `.github/workflows/faang.yml` defined  
- ✔ Automates execution of `faang.py` on a fixed cadence (weekly by default)  
- ✔ Commits updated CSVs and plots to repository  
- ✔ Produces clear, auditable commit history for reproducibility  
- ✔ Workflow conservatively scheduled to avoid rate‑limit issues  

---

#### Summary of Compliance
- All problems (1–4) have been implemented with a focus on reproducibility and transparency.
- Diagnostics, including shapes, ranges, and co-observation counts, are printed before key computations.
- Helper functions and Markdown explanation blocks are provided to document design choices and considerations for reviewers.

---

## Extended Visualisations (Steps 8a to 8e)

These optional, display-only cells extend the Problem 1–4 workflow by offering deeper analysis and additional exploratory visualizations.

---

## Step 8a — Return Distributions

### Objective
Generate histograms and kernel density estimates (KDEs) of hourly returns for each ticker.

### Purpose
-  Calculates synchronous hourly returns using aligned Close prices.
-  Displays histograms with overlaid KDE curves.

### Function
- Illustrates the distribution shape, skewness, and volatility for each FAANG ticker.

### Reviewer Note
- Verify that returns are calculated after alignment to prevent inaccurate distributions.

### References

- [seaborn histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)

---

## Step 8b — Pairwise Scatterplot Matrix

### Objective
Visualise pairwise relationships among synchronous returns.

### Purpose
-  Utilises 'seaborn.pairplot' to generate scatterplots for each ticker pair.
- Diagonal plots display KDEs for individual return distributions.

### Function
Identifies linear and non-linear relationships as well as potential outliers.

### Reviewer Note
- Confirm that alignment diagnostics are complete before generating plots.

### References

- [seaborn pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)

---

## Step 8c — Correlation Analysis

### Objective
Compute and visualise Pearson correlations for synchronous returns.

### Purpose
- Aligns tickers using an inner join.
- Calculates the correlation matrix using returns.corr().
- Displays an annotated heatmap of the results.

### Function
Indicates the strength and direction of co-movement among FAANG tickers.

### Reviewer Note
- Diagnostics display the sample size and time range.
- The inner join ensures that correlations reflect only truly co-observed hours.

### References

- [Pearson correlation coefficient overview](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
- [seaborn heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

---

## Step 8d — Cumulative Returns vs Benchmark

### Objective
Plot cumulative returns for each ticker compared to an equal-weight FAANG benchmark.

### Purpose
- Constructs an aligned price matrix.
- Calculates synchronous returns and the equal-weight benchmark.
- Plots cumulative returns using (1 + r).cumprod() - 1.

### Function
Highlights relative outperformance compared to a simple portfolio proxy.

### Reviewer Note
- Diagnostics display the aligned shape and time range.
- You can enable an optional log scale to compare growth rates.

### References
- [Cumulative return overview](https://www.investopedia.com/terms/c/cumulative_return.asp)
- [Matplotlib plotting](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

---

## Step 8e — Rolling Average Plots

### Objective
Plot hourly Close prices together with a 30-period rolling average.

### Purpose
- Retrieves each ticker’s DataFrame from Step 1.
- Uses the existing RollingMean column or computes a 30-period simple moving average in memory.
- Plots Close prices against the rolling average.

### Function
Reduces short-term fluctuations to reveal longer-term trends.

### Reviewer Note
- These plots are for exploratory purposes only and do not modify saved CSV files.
- Adjust the rolling window as needed to achieve different levels of smoothing.

### References
- [pandas rolling](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html)
- [Moving averages overview (Investopedia)](https://www.investopedia.com/terms/m/movingaverage.asp)

---

## Step 9: Workflow Documentation

### Objective
Summarise the workflow and reproducibility practices implemented within the notebook.

### Workflow demonstrated

1. Fetch hourly FAANG data
2. Load and validate downloads
3. Preview and summarise datasets
4. Plot closing prices
5. Generate extended visualizations, including returns, rolling means, histograms, boxplots, and pairplots.
6. Correlation analysis on synchronous returns
7. Comparative performance vs benchmark
8. Notebook‑level documentation and references

### Purpose
This documentation offers a clear overview of the analysis pipeline and promotes transparency for reviewers.

### Reviewer guidance
- Each step details the inputs, alignment decisions, and imputation methods applied.
- Diagnostics, such as data shapes, time ranges, and co-observation counts, are displayed prior to key computations.

### References  
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)  
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)  
- [Seaborn documentation](https://seaborn.pydata.org/)  

---

### Acknowledgements

- **AI Assistance:**  
  Microsoft Copilot was used throughout the project to refine documentation, structure sections, and ensure clarity in presenting results and limitations. Copilot’s support helped strengthen transparency and alignment with assessment criteria.

  - **Grammarily Editor** was used to proofread and enhance the readability of documentation sections.

---

## Personal Reflection

Working on this project deepened my appreciation for writing code that is not just functional, but also clean, concise, and reproducible. While Copilot offered helpful code suggestions, I took care to distil and polish the results for maximum clarity. Prioritising transparency, thorough diagnostics, and clear guidance for reviewers transformed the workflow into a streamlined process that anyone can follow with ease.

The automation section proved to be a real puzzle at first, since the workflow stubbornly kept files in memory instead of committing them to the repository. To crack this, I returned to basics with the GitHub Actions Practice Workflow, a simpler playground for testing triggers and outputs. As I got this practice flow humming, I layered on new features one at a time, diving into GitHub Actions documentation and experimenting until the full automation pipeline finally clicked. This hands-on, stepwise process underscored just how powerful experimentation, steady learning, and persistence can be when facing unfamiliar infrastructure challenges.

During early runs of the automation workflow, I repeatedly encountered the following error messages:

```lang
Run python faang.py 
Failed to get ticker 'META' reason: Expecting value: line 1 column 1 (char 0) 
$META: possibly delisted; no price data found (period=5d) 
Failed to get ticker 'AAPL' reason: Expecting value: line 1 column 1 (char 0) 
$AAPL: possibly delisted; no price data found (period=5d) ... 
🚫 No valid data to save. 
🚫 No data file saved. Exiting.
```

These errors stemmed from a misconfigured workflow environment that could not fetch live ticker data, leaving yfinance with nothing to return. Digging into the .yml setup and exploring how GitHub Actions manages Python environments and dependencies, I methodically fixed the issues: installing the right requirements, guaranteeing internet access during the job, and pinning versions for consistency. With these tweaks in place, the workflow finally pulled in and saved FAANG data, generating real CSVs and plots.

This experience drove home the importance of troubleshooting environment-specific quirks in CI/CD pipelines. It also reinforced how vital clear logging, step-by-step testing, and fallback practice workflows are for building confidence before taking on more advanced automation.

### END