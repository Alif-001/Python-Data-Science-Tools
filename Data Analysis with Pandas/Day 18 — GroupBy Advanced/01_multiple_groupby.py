# =========================================
# Multiple Column Grouping
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Department + City অনুযায়ী group
grouped = df.groupby(['Department', 'City'])

# 👉 average salary
result = grouped['Salary'].mean()

print(result)

# 👉 explanation:
# multi-level grouping তৈরি হয়