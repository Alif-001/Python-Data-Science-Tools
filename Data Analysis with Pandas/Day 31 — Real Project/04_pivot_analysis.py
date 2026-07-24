# =========================================
# PIVOT TABLE ANALYSIS
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# 👉 pivot table
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
# Excel-style reporting