# =========================================
# GROUPBY ANALYSIS
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# 👉 department wise analysis
group = df.groupby('Department')

print("Average Salary:\n", group['Salary'].mean())
print("\nMax Score:\n", group['Score'].max())

# 👉 explanation:
# department-wise insight বের করা