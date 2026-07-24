# =========================================
# Real-world Cleaning Strategy
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: check missing
print(df.isnull().sum())

# 👉 Step 2: fill numeric missing with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 👉 Step 3: fill categorical missing
df['City'] = df['City'].fillna("Unknown")

# 👉 Step 4: fill salary with median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nCleaned Data:")
print(df)

# 👉 summary:
# real dataset = mix of fillna + logic