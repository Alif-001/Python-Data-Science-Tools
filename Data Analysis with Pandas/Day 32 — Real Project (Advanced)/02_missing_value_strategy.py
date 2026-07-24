# =========================================
# SMART MISSING VALUE STRATEGY
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

df = pd.merge(df, sal, on='EmpID', how='left')
df = pd.merge(df, bonus, on='EmpID', how='left')

# =========================================
# STRATEGY 1: Salary → mean fill
# =========================================
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# =========================================
# STRATEGY 2: Bonus → 0 fill
# =========================================
df['Bonus'] = df['Bonus'].fillna(0)

print(df)

# 👉 explanation:
# different column → different strategy