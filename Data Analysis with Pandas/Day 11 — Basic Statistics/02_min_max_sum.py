# =========================================
# min(), max(), sum()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 minimum value
print("Min Age:", df['Age'].min())

# 👉 maximum value
print("Max Salary:", df['Salary'].max())

# 👉 sum of column
print("Total Salary:", df['Salary'].sum())

# 👉 explanation:
# min → smallest
# max → largest
# sum → total