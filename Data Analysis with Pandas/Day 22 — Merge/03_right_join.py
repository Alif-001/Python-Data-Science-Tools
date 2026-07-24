# =========================================
# RIGHT JOIN
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 right join = salary table full থাকবে
merged = pd.merge(emp, sal, on='EmpID', how='right')

print(merged)

# 👉 explanation:
# EmpID=6 থাকবে (employees নাই → NaN)