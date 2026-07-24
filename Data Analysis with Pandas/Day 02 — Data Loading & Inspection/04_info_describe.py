# =========================================
# info() & describe()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 info() কী?
# - dataset এর full summary দেয়
# - column name, data type, null count

print(df.info())

# 👉 describe() কী?
# - numeric data এর statistics দেয়
# - mean, min, max, std

print(df.describe())

# 👉 summary:
# info() = structure info
# describe() = statistical summary