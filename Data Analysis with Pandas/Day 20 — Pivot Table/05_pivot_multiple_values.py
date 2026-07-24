# =========================================
# Pivot Table with Multiple Values
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple values
pivot = pd.pivot_table(
    df,
    values=['Salary'],
    index='Department',
    columns='City',
    aggfunc=['mean', 'sum']
)

print(pivot)

# 👉 explanation:
# multiple values + aggregation combine করা যায়