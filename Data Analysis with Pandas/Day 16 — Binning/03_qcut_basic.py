# =========================================
# qcut() - Equal Frequency Binning
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Salary কে 3 equal groups (same count)
df['Salary_Group'] = pd.qcut(df['Salary'], q=3)

print(df)

# 👉 explanation:
# qcut → equal number of data in each bin