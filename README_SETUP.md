Setup instructions (Windows PowerShell)

This project contains a Jupyter notebook that demonstrates downloading hourly stock data using `yfinance`. To keep student environments reproducible and small, a minimal requirements file is provided in `requirements.txt`.

1) Create and activate a virtual environment (PowerShell)

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

If your shell blocks running scripts, run (as Administrator) once:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

2) Upgrade pip and install the minimal requirements

    python -m pip install --upgrade pip
    python -m pip install -r requirements_min.txt

3) (Optional) Install a kernel so the virtualenv is available to Jupyter

    python -m ipykernel install --user --name=computer_infra_venv --display-name "ComputerInfra (.venv)"

4) Open the notebook

- Start Jupyter in the repository root with:

    jupyter notebook

- Open `notebooks/problems.ipynb` and run cells in order.

5) Verifying installation

- Run the import cell at the top of the notebook and then the verification cell. If any package is missing, the notebook prints instructions to install it manually. Use the following command in PowerShell to install an individual package:

    python -m pip install yfinance

Notes and tips
- For reproducible grading, you can create a frozen lock file after installing dependencies with:

    python -m pip freeze > requirements.lock

- If students are on macOS/Linux, the venv activation command is `source .venv/bin/activate`.
- Avoid installing large packages (TensorFlow) in student environments unless explicitly required.
