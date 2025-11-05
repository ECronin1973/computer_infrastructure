# 🏗️ FAANG Stock Data Lab – Infrastructure & Setup

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

