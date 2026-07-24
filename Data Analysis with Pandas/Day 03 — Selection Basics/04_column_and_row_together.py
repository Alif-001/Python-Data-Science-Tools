# =========================================
# Row + Column Selection Together
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 specific row + column
# syntax: df.iloc[row_index, column_index]

print(df.iloc[0, 0])  # first row, first column

# 👉 multiple rows + columns
print(df.iloc[0:3, 0:2])
# rows: 0-2
# columns: 0-1

# 👉 summary:
# iloc[row, col]