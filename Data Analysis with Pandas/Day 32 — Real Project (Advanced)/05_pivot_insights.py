# =========================================
# PIVOT TABLE INSIGHTS
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

df = pd.merge(df, sal, on='EmpID', how='left')
df = pd.merge(df, bonus, on='EmpID', how='left')

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 pivot analysis
pivot = pd.pivot_table(
    df,
    values='Total_Pay',
    index='Department',
    columns='City',
    aggfunc='mean',
    fill_value=0
)

print(pivot)

# 👉 explanation:
# business reporting view