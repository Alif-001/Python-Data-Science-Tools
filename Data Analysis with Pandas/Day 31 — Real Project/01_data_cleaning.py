# =========================================
# DATA CLEANING STEP
# =========================================

import pandas as pd

df = pd.read_csv("employees.csv")

# 👉 missing values check
print("Missing values:\n", df.isnull().sum())

# 👉 fill missing Salary with mean
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# 👉 fill missing Bonus with 0
df['Bonus'] = df['Bonus'].fillna(0)

print("\nCleaned Data:\n", df)

# 👉 explanation:
# real data = always messy → cleaning required