# =========================================
# INNER JOIN
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 inner join = common data only
merged = pd.merge(emp, sal, on='EmpID', how='inner')

print(merged)

# 👉 explanation:
# শুধু যাদের EmpID দুই table এ আছে তারা থাকবে
# (1,2,3,4 only)