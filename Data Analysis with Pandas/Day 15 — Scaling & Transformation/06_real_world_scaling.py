# =========================================
# Real-world Scaling Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: scaling
df['Salary_scaled'] = (df['Salary'] - df['Salary'].min()) / (df['Salary'].max() - df['Salary'].min())

# 👉 Step 2: normalization
df['Salary_norm'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()

# 👉 Step 3: rounding
df['Salary_scaled'] = df['Salary_scaled'].round(3)

print(df)

# 👉 summary:
# scaling + normalization = ML ready data