# =========================================
# rank() - Ranking Data
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Salary ranking (ascending)
df['Salary_Rank'] = df['Salary'].rank()

print(df)

# 👉 descending rank (highest = 1)
df['Salary_Rank_Desc'] = df['Salary'].rank(ascending=False)

print("\nDescending Rank:")
print(df)

# 👉 explanation:
# rank() = position assign করে