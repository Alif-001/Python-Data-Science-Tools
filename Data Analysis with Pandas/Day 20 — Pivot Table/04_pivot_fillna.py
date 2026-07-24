# =========================================
# Pivot Table with fill_value
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 missing value fill করা
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='City',
    aggfunc='mean',
    fill_value=0
)

print(pivot)

# 👉 explanation:
# NaN → 0 করা যায়