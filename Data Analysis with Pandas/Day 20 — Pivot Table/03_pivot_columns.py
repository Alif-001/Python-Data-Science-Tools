# =========================================
# Pivot Table with Columns
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Department + City pivot
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='City',
    aggfunc='mean'
)

print(pivot)

# 👉 explanation:
# row + column দুই দিকেই grouping