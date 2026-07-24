# =========================================
# PIVOT TABLE REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# 👉 pivot summary
pivot = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='City',
    aggfunc='mean',
    fill_value=0
)

print(pivot)

# 👉 revision:
# pivot = Excel-style summary table