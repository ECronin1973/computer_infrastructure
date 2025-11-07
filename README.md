
📈 FAANG Stock Data — Hourly Analysis
This repository provides a Jupyter notebook and supporting code for fetching, inspecting, and plotting hourly OHLCV stock data for the FAANG companies (Meta, Apple, Amazon, Netflix, and Alphabet). It is based on the [Assessment Problems](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md) for the [ATU Computer Infrastructure module 2025–2026](https://vlegalwaymayo.atu.ie/course/view.php?id=13109).

---

## Repository Structure

- `notebooks/problems.ipynb` — Primary notebook, organised into modular steps (environment verification, fetch & save, load, plot)
- `scripts/faang.py` — Standalone script for fetching and plotting FAANG data
- `data/` — Timestamped CSV outputs (e.g., `20251105-220824.csv`)
- `plots/` — Generated PNG visualisations (e.g., `20251105-220824.png`)
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

### 📚 Background: Accessing Market Data with yfinance

This project uses [`yfinance`](https://github.com/ranaroussi/yfinance) to retrieve hourly OHLCV data from Yahoo Finance.

### Why yfinance?

- No API key required
- Supports hourly and daily intervals
- Returns pandas-compatible DataFrames
- Ideal for exploratory analysis and educational use

> ⚠️ Note: `yfinance` is not affiliated with or endorsed by Yahoo Inc. Use it only for educational or research purposes.

---

## 🎯 Target Audience

This repository is intended for computing students and professionals with some experience in Python (familiarity with pandas and matplotlib is recommended). The material is self-contained, with helper functions, environment checks, and usage notes provided in the notebook, enabling users to follow along in a local environment or CI pipeline.

---
##  Problem-Based Structure

### 🧪 Problem 1: Data from yfinance

**Objective:** Fetch hourly OHLCV data for the five FAANG tickers using the yfinance package and save the results as timestamped CSV files.

**Steps:**

1. Define a canonical list of FAANG tickers (META, AAPL, AMZN, NFLX, GOOG)

2. Use fetch_hourly_history() to retrieve 5 days of hourly data per ticker

3. Validate and label each DataFrame

4. Save combined data to the data/ folder with filenames formatted as YYYYMMDD-HHMMSS.csv

**Key Concepts:**

- Defensive programming (e.g. fallback tickers, empty DataFrame checks)

- UTC timestamping for reproducibility

- Use of pandas and yfinance for data handling

## Behaviour and File Naming

- Timestamp format (UTC) for CSVs: `YYYYMMDD-HHMMSS` (e.g., `20251105-220824.csv`)

- Default behaviour is conservative (no overwrite); toggle flags are available in the notebook to change this

- Supports both timestamped and non-timestamped filenames via configuration flags

## Output file

Running this notebook code will generate a CSV file in the `data/` folder with a name similar to `20251105-220824.csv`, containing the fetched hourly OHLCV data for the FAANG tickers.  Every time the notebook is run, a new timestamped CSV will be created unless the non-timestamped option is selected.

---

## 📊 Problem 2: Plotting Data

**Objective:** Visualise the closing prices of all FAANG tickers on a single plot using the most recent CSV file.

**Steps:**

1. Load the latest CSV from the data/ folder

2. Plot the Close prices for each ticker using matplotlib and seaborn

3. Add axis labels, a legend, and a UTC timestamped title

4. Save the plot to the plots/ folder as YYYYMMDD-HHMMSS.png

**Key Concepts:**

- Data filtering by ticker

- Plot styling and layout

- Saving plots programmatically

## Output file

Running this notebook code will generate a png file in the `plots/` folder with a name similar to `20251105-220824.png`, containing the fetched hourly OHLCV data for the FAANG tickers.  Every time the code section is run, a new timestamped plot image of type 'png' will be created.

---

## 🐍 Problem 3: Script

**Objective:** Convert the notebook logic into a standalone Python script (faang.py) that can be run from the command line.

## 🧾 Script : `faang.py`

This script automates the process of downloading and visualising hourly stock data for FAANG companies (Meta, Apple, Amazon, Netflix, Google). It mirrors the logic developed in the notebook and is designed for command-line use.

**Script Features:**

- Fetches and saves hourly data using yfinance

- Generates and saves a comparative plot

- Supports CLI flags:

--no-download: Use latest CSV without fetching new data

--outdir: Specify custom output directory

--no-display: Suppress plot display (for automation)

### 🧱 Steps Taken in the Script

1. **Define Canonical Tickers**
   - A default list of FAANG tickers is defined and deduplicated.
   - If a custom list is provided globally, it is validated and used instead.

2. **Fetch Hourly Data**
   - The `fetch_hourly_history()` function retrieves 5 days of hourly OHLCV data for each ticker using the `yfinance` API.
   - Each DataFrame is labelled with its ticker and validated to ensure it's not empty.

3. **Save Data to CSV**
   - Valid data is combined and saved to a timestamped CSV file in the `data/` folder.
   - UTC timestamps are used for reproducibility and logging.

4. **Generate Plot**
   - The `plot_data()` function reads the latest CSV and plots the closing prices for all tickers.
   - The plot includes axis labels, a legend, and a UTC timestamped title.
   - The image is saved to the `plots/` folder.

5. **Support CLI Flags**
   - `--no-download`: Skips data fetching and uses the latest CSV
   - `--outdir`: Specifies a custom output directory
   - `--no-display`: Suppresses plot display (useful for automation)

6. **Run as Executable**
   - The script includes a shebang line and can be run directly from the terminal.
   - Example usage:
     ```bash
     ./faang.py
     python faang.py --no-download --outdir ./custom_data --no-display
     ```

### Run file in Codespaces

As file **faang.py** is already in the repository, simply open the Codespaces terminal and view repository structure to confirm file is present.  Change permission to make executable if required using the steps below:

https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/

1. Check file permissions for **faang.py** using command

```bash
ls -l
```
Output should show something like:
*-rw-rw-rw-  1 codespace root 5333 Nov 6 11:26 faang.py*
**This indicates the file is not executable.**


2. If not executable, run command to add execute permissions:
```bash
chmod u+x faang.py
```

repeat step 1 to confirm permissions changed in **faang.py**:
```bash
ls -l
```
Output should now show something like:
*-rw-rwx-rw-  1 codespace root 5333 Nov  6 11:26 faang.py*
**This indicates the file is now executable.**

3. Run the script:
```bash
./faang.py
```

## 🤖 Problem 4: Automation

**Objective:** Automate the script using GitHub Actions to run every Saturday morning.

**Steps:**

1. Create a workflow file: .github/workflows/faang.yml

2. Schedule the job using a cron expression (0 6 * * 6)

3. Install dependencies and run faang.py with appropriate flags

4. Save outputs to the repository or configured storage

**Key Concepts:**

- CI/CD with GitHub Actions

- Scheduled automation using cron syntax

- Headless execution of CLI scripts

---

## References and Further Reading

- [yfinance documentation](https://github.com/ranaroussi/yfinance)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [seaborn documentation](https://seaborn.pydata.org/)
- [PEP 8 (code style)](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/) — articles on imports, file I/O, and constants

---
**Licence:** See repository `LICENSE` file.