# =========================================
# Real-world Group Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: group average salary
df['Dept_Avg'] = df.groupby('Department')['Salary'].transform('mean')

# 👉 Step 2: high earners (above dept avg)
df['High_Earner'] = df['Salary'] > df['Dept_Avg']

# 👉 Step 3: filter departments with high avg salary
high_dept = df.groupby('Department').filter(
    lambda x: x['Salary'].mean() > 30000
)

print("Full Data with Flags:")
print(df)

print("\nHigh Salary Departments:")
print(high_dept)

# 👉 summary:
# transform + filter = powerful combo