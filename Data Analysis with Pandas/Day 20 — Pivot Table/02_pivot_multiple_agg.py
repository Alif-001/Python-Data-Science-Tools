# =========================================
# Multiple Aggregation in Pivot Table
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple aggregation
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    aggfunc=['mean', 'sum', 'max']
)

print(pivot)

# 👉 explanation:
# একসাথে অনেক stats পাওয়া যায়