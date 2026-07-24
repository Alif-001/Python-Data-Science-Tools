# =========================================
# Real-world MultiIndex Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: group by hierarchy
grouped = df.groupby(['Country', 'City'])['Salary'].agg(['mean', 'max'])

print("Hierarchical Salary Analysis:\n", grouped)

# 👉 Step 2: convert to table view
table = grouped.unstack()

print("\nTable View:\n", table)

# 👉 insight
print("\nHighest Salary Group:")
print(grouped['mean'].idxmax())

# 👉 explanation:
# MultiIndex = enterprise-level data analysis