## 🧪 FAANG Stock Data Lab – Quick Setup (Windows PowerShell)

This lab uses `yfinance` to download hourly FAANG stock data. To keep environments reproducible and lightweight, install only what's needed via `requirements_min.txt`.

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If activation fails due to policy restrictions, run once as Admin:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. Upgrade pip and install minimal requirements
python -m pip install --upgrade pip
python -m pip install -r requirements_min.txt

# 3. (Optional) Register virtualenv with Jupyter
python -m ipykernel install --user --name=faang-lab --display-name "FAANG Lab (.venv)"

# 4. Launch Jupyter and run notebook
jupyter notebook
# Open notebooks/problems.ipynb and run cells in order:
# - Setup (imports + plotting defaults)
# - Verification (smoke test)
# - Download & runner cells (fetch/save CSVs)

# 5. Troubleshooting
# If a package is missing:
python -m pip install <package>
# If yfinance fails, check network and Yahoo Finance access

# 6. Notes
# For full dev setup, use requirements.txt or contact instructor
# For CI/grading:
$env:CI=1
$env:SHOW_PREVIEW="False"
# To freeze environment:
python -m pip freeze > requirements.lock
# On macOS/Linux, activate with:
source .venv/bin/activate
```

# References & best practices

[Jupyter best practices / reproducibility:](https://jupyter.org/practices) https://jupyter.org/practices
[nbval (testing notebooks):](https://nbval.readthedocs.io) https://nbval.readthedocs.io
[PEP 8 for code style:](https://www.python.org/dev/peps/pep-0008/) https://www.python.org/dev/peps/pep-0008/
[Binder / Colab for student convenience:](https://mybinder.org) https://mybinder.org
