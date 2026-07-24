# =========================================
# Column Transformation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Salary কে হাজারে convert করা
df['Salary_K'] = df['Salary'] / 1000

# 👉 Age group তৈরি করা
df['Age_Group'] = df['Age'].apply(
    lambda x: "Young" if x < 25 else "Adult"
)

print(df)

# 👉 explanation:
# transformation = existing data modify করা