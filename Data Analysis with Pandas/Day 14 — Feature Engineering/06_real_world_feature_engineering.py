# =========================================
# Real-world Feature Engineering Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: Bonus + Tax
df['Bonus'] = df['Salary'] * 0.10
df['Tax'] = df['Salary'] * 0.05

# 👉 Step 2: Net Salary
df['Net_Salary'] = df['Salary'] - df['Tax'] + df['Bonus']

# 👉 Step 3: Salary Category
df['Salary_Category'] = df['Salary'].apply(
    lambda x: "High" if x > 40000 else (
        "Medium" if x > 25000 else "Low"
    )
)

# 👉 Step 4: Marks Grade
df['Grade'] = df['Marks'].apply(
    lambda x: "A" if x >= 90 else (
        "B" if x >= 80 else "C"
    )
)

print(df)

# 👉 summary:
# feature engineering = raw data → meaningful data