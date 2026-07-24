# =========================================
# Normalization (Z-score)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 formula:
# (x - mean) / std

mean_val = df['Salary'].mean()
std_val = df['Salary'].std()

df['Salary_normalized'] = (df['Salary'] - mean_val) / std_val

print(df)

# 👉 explanation:
# normalization → centered data (mean=0)