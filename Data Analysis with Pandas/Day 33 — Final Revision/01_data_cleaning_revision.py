# =========================================
# DATA CLEANING REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

# 👉 missing value check
print(df.isnull().sum())

# 👉 fill missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

print(df)

# 👉 revision:
# isnull → detect
# fillna → fix