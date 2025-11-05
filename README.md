# 🏗️ FAANG Stock Data

This project explores hourly stock data for the FAANG companies—**Facebook (Meta), Apple, Amazon, Netflix, and Google (Alphabet)**—using Python. It is designed for computing professionals and data enthusiasts interested in financial data analysis.

## 📌 What You'll Learn
- 📥 How to retrieve stock data using `yfinance`
- 🧹 Techniques for cleaning and preparing datasets
- 📊 Visualizing trends with Python plotting libraries
- 📈 Performing basic statistical analysis

## 🎯 Target Audience
This lab is intended for informed computing professionals (e.g., prospective employers or colleagues). It assumes a strong technical background but no prior familiarity with the specific Python packages used. Comments and concise explanations are provided to support clarity.

## 🧩 Assignment Structure
This notebook corresponds to the module **Problems**:
- **Problem 1**: Data download
- **Problem 2**: Plotting the latest dataset
- **Problems 3–4**: Outlined here and will be implemented in future notebook updates

## 🧠 Key Concepts
- Follow [PEP 8](https://peps.python.org/pep-0008/) for readable, consistent code
- Set plotting defaults for reproducible visuals (Jupyter best practices)
- Keep imports minimal to reduce environment friction ([Real Python: imports](https://realpython.com/python-import/))

## 📚 Background: Accessing Market Data with yfinance
This project uses the [`yfinance`](https://github.com/ranaroussi/yfinance) library to retrieve hourly stock data. `yfinance` is a popular tool for accessing historical and real-time financial data from Yahoo Finance.

### 🔍 Why yfinance?
- No API key required
- Supports hourly and daily intervals
- Compatible with pandas DataFrames
- Ideal for exploratory analysis and educational use

> ⚠️ Note: `yfinance` is not affiliated with or endorsed by Yahoo Inc. Use it only for educational or research purposes.

## ⚙️ Installation
To install `yfinance`, run the following command in your notebook environment:

```python
%pip install yfinance
```

## 📊 Problem 1 — FAANG Stock Data with yfinance

In this task, you'll download **hourly stock data** for the FAANG companies:

- `META` (Facebook)
- `AAPL` (Apple)
- `AMZN` (Amazon)
- `NFLX` (Netflix)
- `GOOG` (Google)

You'll retrieve data for the **past 5 days** using the `yfinance` library and save timestamped CSVs to the `data/` folder.

### 🧼 Notebook Guidelines
- Keep code cells small, well-commented, and reproducible
- Use centralized imports and configuration for clarity
- Avoid re-importing modules in helper cells

### 📥 Inputs
- No user input required: data is fetched live from Yahoo Finance via `yfinance`
- Network access must be available for `yfinance` requests

### 📤 Outputs
- Timestamped CSV file saved to the `data/` folder, all tickers in one file
- Filename pattern (UTC): `YYYYMMDD-HHmmss.csv`  
  Example: `20251030-142530.csv`
- CSV contains hourly OHLCV columns with a `Date` column suitable for parsing as a `DatetimeIndex`
- These files are used by downstream cells (preview, plotting, and the `faang.py` script)

### ⚙️ Notebook Setup
The notebook includes a minimal setup cell that:
- Imports core libraries for data analysis and visualisation
- Sets default plot styles for consistency
- Defines a toggle (`SHOW_PREVIEW`) to control whether large DataFrames are displayed inline

### 📁 Directory & Save Behavior
- `DATA_DIR` and `PLOTS_DIR` are resolved using `Path` objects
- `NO_DATE_FILENAMES`: when `True`, saves as `<TICKER>.csv` (no date)
- `SAVE_DAILY`: when `True`, saves as `YYYYMMDD.csv`
- If both flags are `False`, filenames include full timestamps
- `OVERWRITE`: when `True`, replaces existing files
- `NO_DATE_PLOTS`: when `True`, saves plots as `faang_close.png`; otherwise includes timestamp

### 🎨 Plotting Defaults
- Default figure size: `(10, 5)`
- Style: `whitegrid` via `seaborn`

> ✅ Centralized imports loaded. If you need to install packages, see `README_SETUP.md`.

> 💡 Tip: Use `%pip install` in notebooks only if needed. Prefer project virtual environments and `requirements.txt` for reproducibility.