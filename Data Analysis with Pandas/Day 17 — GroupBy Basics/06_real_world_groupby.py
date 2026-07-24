# =========================================
# Real-world GroupBy Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 department-wise analysis

group = df.groupby('Department')

# 👉 avg age
avg_age = group['Age'].mean()

# 👉 max salary
max_salary = group['Salary'].max()

print("Average Age:\n", avg_age)
print("\nMax Salary:\n", max_salary)

# 👉 insight
print("\nHighest Paid Department:")
print(max_salary.idxmax())