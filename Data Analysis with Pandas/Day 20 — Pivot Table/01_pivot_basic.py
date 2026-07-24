# =========================================
# pivot_table() - Basic Usage
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 department-wise average salary
pivot = pd.pivot_table(
    df,
    values='Salary',     # কোন column calculate হবে
    index='Department',  # row grouping
    aggfunc='mean'       # aggregation function
)

print(pivot)

# 👉 explanation:
# Excel pivot table এর মতো summary তৈরি করে