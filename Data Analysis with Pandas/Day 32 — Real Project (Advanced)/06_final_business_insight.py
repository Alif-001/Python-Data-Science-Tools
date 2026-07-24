# =========================================
# FINAL BUSINESS INSIGHT
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

df = pd.merge(emp, sal, on='EmpID', how='left')
df = pd.merge(df, bonus, on='EmpID', how='left')

# 👉 cleaning strategy
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# 👉 feature engineering
df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 insights
best_emp = df.loc[df['Total_Pay'].idxmax()]
best_dept = df.groupby('Department')['Total_Pay'].mean().idxmax()

print("Best Employee:\n", best_emp)
print("\nBest Department:", best_dept)

# 👉 explanation:
# real decision making from data