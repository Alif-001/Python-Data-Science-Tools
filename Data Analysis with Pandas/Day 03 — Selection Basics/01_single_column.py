# =========================================
# Single Column Selection
# =========================================

import pandas as pd

# 👉 CSV file load করা
df = pd.read_csv("data.csv")

# 👉 একটি column select করা
# syntax: df['column_name']
name_column = df['Name']

print(name_column)

# 👉 type check
print(type(name_column))
# output: pandas Series (1D data)

# 👉 specific column print
print(df['Age'])

# 👉 summary:
# single column = Series