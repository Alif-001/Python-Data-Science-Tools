# =========================================
# OUTER JOIN
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 outer join = সব data combine
merged = pd.merge(emp, sal, on='EmpID', how='outer')

print(merged)

# 👉 explanation:
# সব records থাকবে
# missing জায়গায় NaN