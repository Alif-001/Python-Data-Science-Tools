# =========================================
# FEATURE ENGINEERING
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

df = pd.merge(df, sal, on='EmpID', how='left')
df = pd.merge(df, bonus, on='EmpID', how='left')

# 👉 missing handling
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# 👉 new feature
df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 performance category
df['Performance'] = df['Score'].apply(
    lambda x: 'Excellent' if x >= 90 else ('Good' if x >= 80 else 'Average')
)

print(df)

# 👉 explanation:
# raw data → meaningful features