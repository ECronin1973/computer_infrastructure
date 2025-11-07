# FAANG Stock Analysis — Winter 25/26 Assessment

📈 FAANG Stock Data — Hourly Analysis
This repository provides a Jupyter notebook and supporting code for fetching, inspecting, and visualising hourly OHLCV stock data for the FAANG companies (Meta, Apple, Amazon, Netflix, and Alphabet). It is based on the [Assessment Problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md) for the [ATU Computer Infrastructure module 2025–2026](https://vlegalwaymayo.atu.ie/course/view.php?id=13109).

---

## Repository Structure

- `problems.ipynb` — Primary notebook, structured into modular steps for setup, data collection, loading, and plotting
- `faang.py` — Standalone CLI script that mirrors the notebook logic
- `data/` — Timestamped CSV outputs (e.g., `20251105-220824.csv`)
- `plots/` — Generated PNG visualisations (e.g., `20251105-220824.png`)
- `requirements.txt` — List of Python packages for environment setup

---

## Download Repository
To download this repository, you can use the following command in your terminal:

```bash
git clone https://github.com/ECronin1973/computer_infrastructure.git
cd computer_infrastructure
```

## 🔧 Environment Setup Instructions

To run the notebook and script successfully, follow these steps to set up your Python environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
1. **Install Python 3.10+**  
   Ensure Python is installed and available in your system path.  
   [📖 Reference: Installing Python](https://realpython.com/installing-python/)

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## To Run the Notebook
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook problems.ipynb
   ```

5. **Run the notebook cells sequentially.**

## To Run the Script faang.py
6. **Make the script executable (if necessary):**
   ```bash
   chmod u+x faang.py
   ```

7. **Execute the script:**
   ```bash
   ./faang.py
   ```

💡 If you're using **GitHub Codespaces**, open the terminal and follow the same script execution steps with file. Use chmod u+x faang.py if the file is not yet executable.

**📖 Reference:** [chmod Command — GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/) — Used to modify file permissions for script execution.

---

### 📚 Background: Accessing Market Data with yfinance

This project uses [`yfinance`](https://github.com/ranaroussi/yfinance) to retrieve hourly OHLCV data from Yahoo Finance.

### Why yfinance?

- No API key required
- Supports hourly and daily intervals
- Returns pandas-compatible DataFrames
- Ideal for exploratory analysis and educational use

**📖 Reference:** [yfinance documentation](https://pypi.org/project/yfinance/) — Used to fetch financial data programmatically via the Yahoo Finance API.

> ⚠️ Note: `yfinance` is not affiliated with or endorsed by Yahoo Inc. Use it only for educational or research purposes.

---

## 🎯 Target Audience
This repository is designed for computing students and professionals with intermediate Python skills. Familiarity with pandas, matplotlib, and basic CLI usage is recommended. The notebook includes environment checks, helper functions, and modular steps to support reproducibility and automation.

**📖 Reference:** [Real Python — CLI Scripts](https://realpython.com/python-command-line-interfaces/) — Used to design and implement command-line flags in faang.py.

---

### 🧪 Problem 1: Fetch Hourly FAANG Data

**Objective:** Fetch hourly OHLCV data for the five FAANG tickers using the yfinance package and save the results as timestamped CSV files.

## Workflow:

- Define and validate the FAANG ticker list
- Use fetch_hourly_history() to retrieve 5 days of hourly data per ticker
- Label and clean each DataFrame
- Save combined data to a timestamped CSV file

**📖 Reference:** [pandas.DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) — Used to export structured data to CSV format for reproducibility.

**📖 Reference:** [datetime Module](https://docs.python.org/3/library/datetime.html) — Used to generate UTC timestamps for filenames and logs.

## Behaviour and File Naming

- Timestamp format (UTC) for CSVs: `YYYYMMDD-HHMMSS` (e.g., `20251105-220824.csv`)

- Default behaviour is conservative (no overwrite); toggle flags are available in the notebook to change this

- Supports both timestamped and non-timestamped filenames via configuration flags

## Output file

Running this notebook code will generate a CSV file in the `data/` folder with a name similar to `20251105-220824.csv`, containing the fetched hourly OHLCV data for the FAANG tickers.  Every time the notebook is run, a new timestamped CSV will be created unless the non-timestamped option is selected.

---

## 📊 Problem 2: Plotting Data

**Objective:** Visualise the closing prices of all FAANG tickers on a single plot using the most recent CSV file.

**Workflow:**

1. Load the latest CSV from the data/ folder

2. Plot the Close prices for each ticker using matplotlib and seaborn

3. Add axis labels, a legend, and a UTC timestamped title

4. Save the plot to the plots/ folder as YYYYMMDD-HHMMSS.png

**📖 Reference:** [matplotlib.pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) — Used to generate line plots of closing prices.

**📖 Reference:** [seaborn.set_style](https://seaborn.pydata.org/generated/seaborn.set_style.html) — Used to apply consistent visual styling across plots.

**Key Concepts:**

- Data filtering by ticker
- Plot styling and layout
- Saving plots programmatically

## Output file

Running this notebook code will generate a png file in the `plots/` folder with a name similar to `20251105-220824.png`, containing the fetched hourly OHLCV data for the FAANG tickers.  Every time the code section is run, a new timestamped plot image of type 'png' will be created.

example of generated plot:

![FAANG Closing Prices](plots/20251107-161049.png)

---

## 🐍 Problem 3: Script

**Objective:** Convert the notebook logic into a standalone Python script (faang.py) that can be run from the command line.

**🧾 Script:** `faang.py`

This script replicates the notebook logic for use in terminal environments or CI pipelines.

**Features:**

- Fetches and saves hourly FAANG data
- Generates and saves comparative plots
- Supports CLI flags for flexible execution

**📖 Reference:** [argparse — CLI Argument Parsing](https://docs.python.org/3/library/argparse.html) — Used to implement command-line flags like --no-download, --outdir, and --no-display.

**CLI Flags:**

--no-download — Use latest CSV without fetching new data

--outdir — Specify custom output directory

--no-display — Suppress plot display (for headless execution)

**Script Features:**

- Fetches and saves hourly data using yfinance

- Generates and saves a comparative plot

### How Script Was Designed

#### Step 1: Copied modular functions from the notebook into faang.py

**Reason:**  It is essential to copy modular functions from the notebook into the script to ensure that the core logic for fetching, processing, and visualising data is preserved. This allows for code reuse and maintains consistency between the notebook and the script.
[Modular Functions in Python](https://realpython.com/python-modules-packages/) — Structuring Python Code with Modules and Packages

#### Step 2: Integrated argument parsing using argparse

**Reason**:  Integrating argument parsing allows users to customize script behaviour via command-line flags, enhancing flexibility and usability in different environments.
[Command-line argument parsing](https://docs.python.org/3/library/argparse.html) — Command-line argument parsing

#### Step 3: Mapped notebook steps to script functions

**Reason**:  Mapping notebook steps to discrete functions in the script improves code organization, readability, and maintainability. Each function encapsulates a specific task, making it easier to test and modify individual components without affecting the overall workflow.
[Mapping Functions in Python](https://realpython.com/python-modules-packages/) — Structuring Python Code with Modules and Packages

#### Step 4: Added CLI flags for flexible execution

**Reason**:  Adding CLI flags allows users to customise the script's behavior without modifying the code. This is particularly useful for adapting the script to different environments or use cases.
[CLI Argument Parsing](https://docs.python.org/3/library/argparse.html) — Command-line argument parsing

#### Step 5: Tested script in terminal and Codespaces environments

**Reason**:  Testing the script in various environments ensures its reliability and helps identify any environment-specific issues.
[Testing Scripts in Different Environments](https://realpython.com/python-modules-packages/) — Structuring Python Code with Modules and Packages

#### Step 6: Documented usage in this README

**Reason**:  Documenting usage instructions helps users understand how to run and utilise the script effectively.
[Documentation Best Practices](https://realpython.com/documenting-python-code/) — Documenting Python Code