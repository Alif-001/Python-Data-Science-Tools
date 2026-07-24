# =========================================
# Real-world Type Cleaning Strategy
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: check types
print(df.dtypes)

# 👉 Step 2: convert numeric columns
df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

# 👉 Step 3: convert date column
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 👉 Step 4: verify
print("\nAfter conversion:")
print(df.dtypes)

# 👉 Step 5: preview data
print(df.head())

# 👉 summary:
# real dataset = string → numeric → datetime conversion