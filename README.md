# Computer-Infrastructure-Assessments
Submissions for the Computer Infrastructure Module 2025/2026

Welcome to Edward Cronin’s repository for the Computer Infrastructure module at ATU Galway. This repository contains completed assessments, including individual tasks and a comprehensive final project (to be added later), demonstrating practical applications of key infrastructure concepts.

### Overview
This repository is organised into two main sections:

**Section 1: Tasks (2025/2026)**  
This section contains four problems assigned throughout the module, showcasing practical implementations of core Computer Infrastructure techniques.

**Section 2: Final Project (2025/2026)**  
This section will present a capstone project that integrates the skills and knowledge acquired during the course. (Coming Soon)

Feedback and collaboration are welcome!

### Repository Contents

- **problems.ipynb**: This file contains four completed tasks as outlined in the [2025 Computer Infrastructure Module Assessment document](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md).

- **project.ipynb**: This file includes the completed project work as detailed in the Project Section of the [2025 Computer Infrastructure Module README document](#) (to be completed later).

- **requirements.txt**: This file lists the Python packages required to run the code in this repository.


### Author Information
- **Name:** Edward Cronin  
- **Student ID:** g00425645  
- **Email:** g00425645@atu.ie  
- **GitHub Profile:** [ECronin1973](https://github.com/ECronin1973)  

## Cloning the Repository

1. Visit the GitHub repository at [My Computer Infrastructure Repository](https://github.com/ECronin1973/computer_infrastructure.git).
2. Click the "Code" button, then copy the URL provided for cloning.
3. Open a terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/ECronin1973/computer_infrastructure.git
   ```
4. To run the code, ensure that Python and Jupyter are installed on your system.

## Code of Conduct

This repository is governed by a code of conduct, which is available for reference within the repository.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the Jupyter notebooks, navigate to the directory containing the files and execute the following command:

```bash
jupyter notebook
```

## Dependencies

This project relies on several Python libraries, which are listed in the `requirements.txt` file. These include:

- yfinance
- pandas
- matplotlib
- datetime
- os
- glob
- TO BE UPDATED AS NECESSARY

Ensure that you install these dependencies to guarantee smooth execution of the code.

## AI Assistance

Some of the code in this repository was generated with the assistance of AI tools to facilitate learning and expedite development.

# Tasks for the 2025/2026 Computer Infrastructure Module

## Course Objective

Create a notebook named `problems.ipynb` in the root of the repository. Complete all tasks outlined in `problems.md` within this notebook.

## Problem 1: FAANG Stock Data with yfinance

### Objective
Using the [yfinance](https://github.com/ranaroussi/yfinance) Python package, write a function called `get_data()` that downloads hourly data for the five FAANG stocks over the previous five days:

- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The function should save the data in a folder named `data` within the root of your repository. The filenames should follow the format `YYYYMMDD-HHmmss.csv`, where `YYYYMMDD` represents the four-digit year (e.g., 2025), followed by the two-digit month (e.g., 09 for September), the two-digit day, and `HHmmss` represents hours, minutes, and seconds. If the `data` folder does not already exist, the function should create it.

### Implementation Summary

The `get_data()` function should:

- Download hourly data for each of the specified stocks
- Save the data into the `data/` folder using the filename format `YYYYMMDD-HHmmss.csv`
- Create the `data` folder if it does not exist


**Further Reading Completed**

1. [yfinance Documentation](https://pypi.org/project/yfinance/): This documentation provided the foundation for interacting with Yahoo Finance’s API using Python. It helped me to:

   - Understand the API structure: I learned how to use `yf.Ticker()` and `ticker.history()` to retrieve hourly data for FAANG stocks.
   - Specify time intervals: The documentation clarified how to set `interval='1h'` and `period='5d'` to obtain the exact data range required.
   - Handle multiple tickers: I found examples showing how to loop through multiple stock symbols efficiently.
   - Export data: I received guidance on converting the data to a DataFrame and saving it as a .csv file, which was essential for meeting the task’s output format requirements.

2. [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/): This documentation was crucial for data manipulation and storage. It helped me to:

   - Work with DataFrames: I learned how to create, manipulate, and export DataFrames, which is key for handling stock data.
   - Save to CSV: The documentation provided methods such as `DataFrame.to_csv()` to save the data in the required format.
   - Manage dates and times: I utilized Pandas functions to handle timestamps and format filenames correctly.

3. [Python os Module Documentation](https://docs.python.org/3/library/os.html): This documentation was essential for file and directory management. It helped me to:

   - Create directories: I learned how to use `os.makedirs()` to create the 'data/' folder if it doesn’t already exist.
   - Check for existence: The documentation provided methods like `os.path.exists()` to verify if the folder already exists before creating it.

All documents relevant to this task have been added to the references section at the end of this README.md file.

# END

## Problem 2: Plotting Data

Write a function called `plot_data()` that opens the latest data file in the `data` folder and, on one plot, plots the `Close` prices for each of the five stocks.
The plot should include axis labels, a legend, and the date as a title.
The function should save the plot into a `plots` folder in the root of your repository using a filename in the format `YYYYMMDD-HHmmss.png`.
Create the `plots` folder if you don't already have one.

TO BE UPDATED

# END

## Problem 3: Script

Create a Python script called `faang.py` in the root of your repository.
Copy the above functions into it and it so that whenever someone at the terminal types `./faang.py`, the script runs, downloading the data and creating the plot.
Note that this will require a shebang line and the script to be marked executable.
Explain the steps you took in your notebook.

TO BE UPDATED

# END

## Problem 4: Automation

Create a [GitHub Actions workflow](https://docs.github.com/en/actions) to run your script every Saturday morning.
The script should be called `faang.yml` in a `.github/workflows/` folder in the root of your repository.
In your notebook, explain each of the individual lines in your workflow.

TO BE UPDATED

# END

## References

The following online resources were used to complete tasks in this repository and to create this README.md file:

1. [ATU Lectures - Applied Statistics, Dr Ian McLoughlin](https://vlegalwaymayo.atu.ie/course/view.php?id=13109)
2. [Writing README.md files on GitHub](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
3. [Creating tables in Markdown](https://www.makeuseof.com/tag/create-markdown-table/)
4. [GitHub Docs - Creating a repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
5. [GitHub Docs - Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
6. [GitHub Docs - Creating a .gitignore file](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
7. [yfinance Documentation](https://pypi.org/project/yfinance/)
8. [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
9. [Python os Module Documentation](https://docs.python.org/3/library/os.html)
10. [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
