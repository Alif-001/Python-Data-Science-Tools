# =========================================
# LEFT JOIN
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 left join = left table (employees) full থাকবে
merged = pd.merge(emp, sal, on='EmpID', how='left')

print(merged)

# 👉 explanation:
# সব employee থাকবে
# missing salary → NaN