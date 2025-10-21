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

#### 5. **Save CSVs (Runner Cell)**
- Loop through tickers and fetch data using `fetch_hourly_history()`
- Check for existing files to avoid duplication; if files exist, pick the latest by filename
- Generate UTC timestamps: `YYYYMMDDTHHMMSSZ` format for new saves
- Wrap `df.to_csv()` in try/except and collect errors in a list
- Return a `results` dictionary mapping tickers to file paths, plus error summary if any

**Why:** UTC timestamps ensure sortability and reproducibility. Idempotent operations (reusing existing files) and error collection make the workflow robust and informative. ([Jupyter best practices](https://jupyter.org/practices), [Real Python: file I/O](https://realpython.com/python-file-io/))

#### 6. **Preview Saved Data (Optional)**
- Read the latest CSV file for each ticker from `../data/`
- Parse the 'Date' column as a DateTimeIndex during CSV read
- Display shape and head of each DataFrame for verification
- Stores DataFrames in a `data` dictionary for downstream use (e.g., plotting)

**Why:** Reading from saved CSVs avoids redundant network calls and confirms the save operation worked correctly. Parsing dates as DateTimeIndex enables proper time-series operations. ([pandas read_csv docs](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html))

#### 7. **Diagnostics**
- Use `collections.Counter` to detect duplicate tickers
- Report clear feedback on the ticker list state

**Why:** Diagnostics help users debug inputs and understand what the code is doing. ([Python Cookbook](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s02.html))

### Key Learning Resources

1. **[yfinance Documentation](https://pypi.org/project/yfinance/)** — Learn how to use `yf.Ticker()` and `.history()` to fetch stock data, specify time intervals (`interval='1h'`, `period='5d'`), and handle multiple tickers.

2. **[pandas Documentation](https://pandas.pydata.org/)** — Understand DataFrames, `.to_csv()` for saving data, and timestamp handling with pandas datetime functions.

3. **[Python os Module](https://docs.python.org/3/library/os.html)** — Learn `os.makedirs()` for creating directories and `os.path.exists()` for checking file/folder existence.

### Expected Output

After running Problem 1 cells in the notebook:
- CSV files appear in `notebooks/data/` (e.g., `META_20251018T180020Z.csv`)
- Each file contains hourly OHLCV (Open, High, Low, Close, Volume) data plus a 'Ticker' column
- Files are timestamped in UTC and sorted lexicographically
- A `results` dictionary is displayed showing the mapping of ticker → file path
- If any saves fail, an error summary is printed before the results

---

## Problem 2: Plotting Data

### Objective

Create a visualisation that plots the `Close` prices for all five FAANG stocks on a single chart. The plot must:

1. Read the latest CSV files from the `data/` folder
2. Plot all five stocks' Close prices on one chart with a shared timeline
3. Include axis labels, legend, and a date-range title
4. Save the plot to a `plots/` folder with a UTC timestamp: `faang_close_YYYYMMDDTHHMMSSZ.png`

### Requirements

The implementation must:
- Parse the Date column as a DateTimeIndex for proper time-series plotting
- Handle missing or empty data gracefully
- Use matplotlib for plotting with clear labels and legend
- Create the `plots/` folder if it doesn't exist
- Use consistent styling (figure size, grid, colors)

### Implementation Approach

The notebook implements this in three main steps:

#### 1. **Load Data from Saved CSVs**
- Iterate through tickers and find all matching CSV files in `../data/`
- Select the latest file per ticker by sorting filenames (timestamps are [lexicographically](https://docs.python.org/3/library/functions.html#sorted) sortable)
- Read each CSV with `pd.read_csv()`, parsing 'Date' as DateTimeIndex
- Store DataFrames in a dictionary keyed by ticker symbol

**Why:** Reading from saved CSVs avoids redundant network calls and ensures we're plotting the exact data that was saved. Using DateTimeIndex enables proper time-series alignment and formatting. ([pandas datetime docs](https://pandas.pydata.org/docs/user_guide/timeseries.html))

#### 2. **Create the Plot**
- Compute overall date range from all DataFrames for the title
- Create a matplotlib figure with default size (10, 5)
- Loop through the data dictionary and plot each ticker's Close series
- Add labels for x-axis (Date), y-axis (Close Price USD), and a descriptive title
- Include a legend with ticker symbols

**Why:** Plotting all series on one chart enables visual comparison of relative performance and trends. Clear labels and legends make the chart self-documenting. ([matplotlib best practices](https://matplotlib.org/stable/users/index.html))

#### 3. **Save the Plot**
- Ensure `../plots/` directory exists with `os.makedirs(exist_ok=True)`
- Generate UTC timestamp in `YYYYMMDDTHHMMSSZ` format
- Save figure to `../plots/faang_close_{timestamp}.png` using `plt.savefig()`
- Print confirmation message with the saved path

**Why:** UTC timestamps ensure reproducibility and sortability. Saving plots as artifacts enables version control and comparison across runs. ([Jupyter best practices](https://jupyter.org/practices))

### Code Structure

```python
# Load latest CSV per ticker
data = {}
for ticker in tickers:
    files = [p for p in os.listdir('../data') 
             if p.startswith(f"{ticker}_") and p.endswith('.csv')]
    if files:
        latest = sorted(files, reverse=True)[0]
        df = pd.read_csv(f'../data/{latest}', 
                         parse_dates=['Date'], 
                         index_col='Date')
        data[ticker] = df

# Compute date range
min_date = min(df.index.min() for df in data.values())
max_date = max(df.index.max() for df in data.values())

# Plot
plt.figure()
for sym, df in data.items():
    plt.plot(df.index, df['Close'], label=sym)

plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.title(f"FAANG Close Price — {min_date.date()} to {max_date.date()}")
plt.legend(title='Ticker')

# Save
os.makedirs('../plots', exist_ok=True)
ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
plt.savefig(f'../plots/faang_close_{ts}.png')
```

### 📊 Sample Output

The notebook now displays the saved image inline after plotting, and includes a gallery cell that shows all PNGs in `plots/`.

- Browse all plots: [plots/](plots/)
- Example image (one of the generated plots):

![FAANG Close Price Plot](plots/faang_close_20251021T171342Z.png)


The plot shows:
- **META** (blue) — Trading around $710-720
- **AAPL** (orange) — Trading around $245-250
- **AMZN** (green) — Trading around $217-222
- **NFLX** (red) — Trading around $1200-1230 (highest absolute price)
- **GOOG** (purple) — Trading around $240-244

All stocks show relatively stable patterns over the 5-day period (Oct 13-17, 2025), with NFLX dominating the y-axis due to its higher share price.

### Key Learning Resources

1. **[pandas read_csv with datetime](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)** — Learn how to parse date columns during CSV reading using `parse_dates` and `index_col` parameters.

2. **[matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)** — Understand basic plotting functions: `plot()`, `xlabel()`, `ylabel()`, `title()`, `legend()`, and `savefig()`.

3. **[pandas DateTimeIndex](https://pandas.pydata.org/docs/user_guide/timeseries.html)** — Learn how pandas handles time-series data, automatic alignment, and datetime formatting.

### Expected Output

After running Problem 2 cells in the notebook:
- A PNG file appears in `notebooks/plots/` (e.g., `faang_close_20251021T171342Z.png`)
- The plot displays all five stocks on a single chart with proper labels
- The title shows the exact date range of the data
- Console prints: `✅ Plot saved to ../plots/faang_close_YYYYMMDDTHHMMSSZ.png`

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