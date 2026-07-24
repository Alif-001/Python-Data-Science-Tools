# =========================================
# Real-world Combine (Join + Concat)
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

# 👉 Step 1: join salary
df = pd.merge(emp, sal, on='EmpID', how='left')

# 👉 Step 2: concat bonus
df = pd.merge(df, bonus, on='EmpID', how='left')

# 👉 Step 3: total compensation
df['Total_Pay'] = df['Salary'] + df['Bonus']

print(df)

# 👉 explanation:
# join + concat = real data pipeline