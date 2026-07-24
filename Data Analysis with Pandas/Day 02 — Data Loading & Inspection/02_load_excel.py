# =========================================
# Load Excel File in Pandas
# =========================================

import pandas as pd

# 👉 Excel file (.xlsx) load করা
# NOTE: Excel read করতে openpyxl লাগতে পারে
# install: pip install openpyxl

df = pd.read_excel("data.xlsx")

print(df)

# 👉 specific sheet load করা
# df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# 👉 summary:
# read_excel() = Excel file load করার function