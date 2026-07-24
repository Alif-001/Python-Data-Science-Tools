# =========================================
# shape & columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 shape কী?
# - (rows, columns) return করে
print(df.shape)

# 👉 number of rows
print(df.shape[0])

# 👉 number of columns
print(df.shape[1])

# 👉 columns কী?
# - column name list দেয়
print(df.columns)

# 👉 column list convert করা
print(list(df.columns))

# 👉 summary:
# shape = size of dataset
# columns = column names