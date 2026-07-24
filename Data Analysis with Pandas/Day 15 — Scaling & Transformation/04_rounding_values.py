# =========================================
# Rounding Values
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 scaling করে rounding করা
df['Salary_scaled'] = (df['Salary'] - df['Salary'].min()) / (df['Salary'].max() - df['Salary'].min())

# 👉 round to 2 decimal places
df['Salary_scaled'] = df['Salary_scaled'].round(2)

print(df)

# 👉 explanation:
# rounding → clean & readable output