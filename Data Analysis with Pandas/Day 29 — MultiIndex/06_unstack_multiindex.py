# =========================================
# Unstack MultiIndex
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

grouped = df.groupby(['Country', 'City'])['Salary'].mean()

# 👉 hierarchical → table format
unstacked = grouped.unstack()

print(unstacked)

# 👉 explanation:
# MultiIndex → pivot table style