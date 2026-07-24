# =========================================
# FINAL INSIGHTS (REAL PROJECT OUTPUT)
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

# 👉 cleaning
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# 👉 feature engineering
df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 group analysis
group = df.groupby('Department')['Total_Pay'].mean()

print("Average Total Pay:\n", group)

# 👉 best department
print("\nTop Department:")
print(group.idxmax())

# 👉 explanation:
# real business decision making