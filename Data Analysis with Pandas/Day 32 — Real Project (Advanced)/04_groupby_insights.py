# =========================================
# GROUPBY INSIGHTS
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

# 👉 department analysis
group = df.groupby('Department')['Total_Pay'].agg(['mean', 'max', 'min'])

print(group)

# 👉 explanation:
# department wise performance insight