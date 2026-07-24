# =========================================
# Mean per Group
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 average salary per department
mean_salary = df.groupby('Department')['Salary'].mean()

print(mean_salary)

# 👉 explanation:
# department অনুযায়ী average বের হয়