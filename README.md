# Computer Infrastructure – Module Assessments (2025/2026)

**Author:** Edward Cronin  
**Student ID:** g00425645  
**Email:** g00425645@atu.ie  
**GitHub:** [ECronin1973](https://github.com/ECronin1973)

---

## Overview

This repository contains solutions to four practical problems from the ATU Galway Computer Infrastructure module. The main deliverable is a Jupyter notebook (`notebooks/problems.ipynb`) that demonstrates data retrieval, processing, visualisation, and automation techniques using Python.

**What's included:**
- `notebooks/problems.ipynb` — Interactive notebook with all four problems solved
- `requirements.txt` — Python package dependencies
- `README_SETUP.md` — Detailed setup instructions for Windows PowerShell

**Assessment brief:** [Computer Infrastructure Problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md)

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ECronin1973/computer_infrastructure.git
cd computer_infrastructure
```

### 2. Set Up Python Environment (Windows PowerShell)

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If activation fails due to policy, run once:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Launch Jupyter and Open the Notebook

```powershell
jupyter notebook
```

Then navigate to `notebooks/problems.ipynb` and run the cells in order.

**For detailed setup instructions, see:** [README_SETUP.md](README_SETUP.md)

---

## Dependencies

This project uses the following Python libraries (all listed in `requirements.txt`):

- **pandas** — Data manipulation and analysis
- **numpy** — Numerical computing
- **yfinance** — Financial data from Yahoo Finance
- **matplotlib** — Plotting and visualization
- **seaborn** — Statistical data visualization
- **requests** — HTTP library
- **scikit-learn** — Machine learning tools
- **ipykernel** — Jupyter kernel support

---

## Coding Guidelines and References

This project follows established best practices for coding, documentation, and reproducibility in computational notebooks:

- **Jupyter best practices:** Narrative text should explain the rationale for each step, including references. ([Jupyter.org/practices](https://jupyter.org/practices))
- **The Turing Way:** Document why you made choices, not just what you did. ([The Turing Way](https://the-turing-way.netlify.app/reproducible-research/overview/overview.html))
- **Diátaxis documentation framework:** Conceptual documentation (why) should be close to the code, but detailed background can go in README. ([Diátaxis](https://diataxis.fr/))
- **PEP 8:** Encourages clear, readable code and comments—explanations in markdown cells are the notebook equivalent. ([PEP 8](https://peps.python.org/pep-0008/))

---

## Problem 1: FAANG Stock Data with yfinance

### Objective

Download hourly stock data for the five FAANG companies over the previous 5 days and save to CSV files:

- **META** (Facebook/Meta)
- **AAPL** (Apple)
- **AMZN** (Amazon)
- **NFLX** (Netflix)
- **GOOG** (Google/Alphabet)

### Requirements

The implementation must:
1. Use the [yfinance](https://pypi.org/project/yfinance/) Python package
2. Fetch hourly data for each stock (5-day period, 1-hour intervals)
3. Save data to timestamped CSV files: `TICKER_YYYYMMDDTHHMMSSZ.csv`
4. Create a `data/` folder if it doesn't exist
5. Handle errors gracefully (network issues, missing data)

### Implementation Approach

The notebook implements this in modular steps:

#### 1. **Setup and Imports**
- Import required libraries (`yfinance`, `pandas`, `os`, `datetime`)
- Set plotting defaults for consistency
- Define a `SHOW_PREVIEW` toggle for optional output display

**Why:** Minimal, organized imports improve reproducibility and make dependencies explicit. ([PEP 8](https://peps.python.org/pep-0008/), [Jupyter best practices](https://jupyter.org/practices))

#### 2. **Environment Verification**
- Check that `pandas` and `yfinance` are available
- Perform a lightweight test fetch (1 day of AAPL data)
- Display clear error messages if packages are missing

**Why:** Early verification prevents mid-notebook failures and guides users to install missing dependencies. ([Jupyter best practices](https://jupyter.org/practices), [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/overview/overview.html))

#### 3. **Define Ticker List**
- Create a canonical list of FAANG tickers: `['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']`
- Deduplicate defensively using `dict.fromkeys()` to preserve order
- Validate the list has exactly 5 tickers

**Why:** Centralizing constants avoids duplication and drift across cells. Deduplication ensures clean, predictable data. ([Real Python: constants](https://realpython.com/python-constants/))

#### 4. **Fetch Function**
- Define `fetch_hourly_history(ticker, period='5d', interval='1h')`
- Returns a labeled DataFrame with a 'Ticker' column and 'Date' index
- Returns `None` on failure with a clear error message
- Uses `df.copy()` to avoid pandas SettingWithCopyWarning

**Why:** Encapsulation makes code reusable and testable. Validation and defensive copying prevent subtle bugs. ([pandas docs](https://pandas.pydata.org/docs/))

#### 5. **Save CSVs**
- Loop through tickers and fetch data
- Check for existing files to avoid duplication (idempotent saves)
- Generate UTC timestamps: `YYYYMMDDTHHMMSSZ` format
- Wrap `df.to_csv()` in try/except for robustness

**Why:** UTC timestamps ensure sortability and reproducibility. Idempotent operations and error handling make the workflow robust. ([Jupyter best practices](https://jupyter.org/practices), [Real Python: file I/O](https://realpython.com/python-file-io/))

#### 6. **Diagnostics**
- Use `collections.Counter` to detect duplicate tickers
- Report clear feedback on the ticker list state

**Why:** Diagnostics help users debug inputs and understand what the code is doing. ([Python Cookbook](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s02.html))

### Key Learning Resources

1. **[yfinance Documentation](https://pypi.org/project/yfinance/)** — Learn how to use `yf.Ticker()` and `.history()` to fetch stock data, specify time intervals (`interval='1h'`, `period='5d'`), and handle multiple tickers.

2. **[pandas Documentation](https://pandas.pydata.org/)** — Understand DataFrames, `.to_csv()` for saving data, and timestamp handling with pandas datetime functions.

3. **[Python os Module](https://docs.python.org/3/library/os.html)** — Learn `os.makedirs()` for creating directories and `os.path.exists()` for checking file/folder existence.

### Expected Output

After running Problem 1 cells in the notebook:
- CSV files appear in `notebooks/data/` (e.g., `META_20251018T143052Z.csv`)
- Each file contains hourly OHLCV (Open, High, Low, Close, Volume) data
- Files are timestamped and sorted lexicographically

---

## Problem 2: Plotting Data

### Objective

Write a function called `plot_data()` that opens the latest data file in the `data` folder and, on one plot, plots the `Close` prices for each of the five stocks.
The plot should include axis labels, a legend, and the date as a title.
The function should save the plot into a `plots` folder in the root of your repository using a filename in the format `YYYYMMDD-HHmmss.png`.
Create the `plots` folder if you don't already have one.

(Implementation details to be added as Problem 2 is completed in the notebook...)

---


## Problem 3: Script

### Objective

Create a Python script called `faang.py` in the root of your repository.
Copy the above functions into it and it so that whenever someone at the terminal types `./faang.py`, the script runs, downloading the data and creating the plot.
Note that this will require a shebang line and the script to be marked executable.
Explain the steps you took in your notebook.

(Implementation details to be added as Problem 3 is completed in the notebook...)

---

## Problem 4: Automation

### Objective

Create a [GitHub Actions workflow](https://docs.github.com/en/actions) to run your script every Saturday morning.
The script should be called `faang.yml` in a `.github/workflows/` folder in the root of your repository.
In your notebook, explain each of the individual lines in your workflow.

(Implementation details to be added as Problem 4 is completed in the notebook...)

# END