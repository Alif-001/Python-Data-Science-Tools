# =========================================
# Real-world Merge Example
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 Step 1: merge data
df = pd.merge(emp, sal, on='EmpID', how='left')

# 👉 Step 2: fill missing salary
df['Salary'] = df['Salary'].fillna(0)

# 👉 Step 3: total payroll
total_salary = df['Salary'].sum()

print(df)
print("\nTotal Payroll:", total_salary)

# 👉 explanation:
# merge = real database join concept