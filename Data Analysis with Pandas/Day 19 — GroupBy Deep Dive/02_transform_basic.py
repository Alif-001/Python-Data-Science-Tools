# =========================================
# transform() - Same size output
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 department-wise average salary
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')

print(df)

# 👉 explanation:
# transform → result original size এর মতো থাকে
# group info → row level এ নিয়ে আসে