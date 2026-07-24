# =========================================
# Slicing in Pandas
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 rows slicing (iloc)
print(df.iloc[1:5])
# 1 to 4 rows

# 👉 columns slicing (iloc)
print(df.iloc[:, 0:2])
# সব rows, column 0-1

# 👉 row + column slicing together
print(df.iloc[1:4, 0:3])

# 👉 loc slicing
print(df.loc[1:4, ['Name', 'Salary']])

# 👉 summary:
# slicing = range of data select করা