# =========================================
# Multiple Feature Creation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Bonus
df['Bonus'] = df['Salary'] * 0.10

# 👉 Tax (5%)
df['Tax'] = df['Salary'] * 0.05

# 👉 Net Salary
df['Net_Salary'] = df['Salary'] - df['Tax']

# 👉 Salary Level
df['Salary_Level'] = df['Salary'].apply(
    lambda x: "High" if x > 35000 else "Low"
)

print(df)

# 👉 explanation:
# multiple features → ML model এর input improve করে