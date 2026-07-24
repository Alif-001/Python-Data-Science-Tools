# =========================================
# Sum per Group
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 total salary per department
total_salary = df.groupby('Department')['Salary'].sum()

print(total_salary)

# 👉 explanation:
# department wise total calculation