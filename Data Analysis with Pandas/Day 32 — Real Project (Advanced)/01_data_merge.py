# =========================================
# MULTIPLE DATASET MERGE
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")
bonus = pd.read_csv("bonus.csv")

# 👉 Step 1: merge salary
df = pd.merge(emp, sal, on='EmpID', how='left')

# 👉 Step 2: merge bonus
df = pd.merge(df, bonus, on='EmpID', how='left')

print(df)

# 👉 explanation:
# multiple dataset combine = real database style