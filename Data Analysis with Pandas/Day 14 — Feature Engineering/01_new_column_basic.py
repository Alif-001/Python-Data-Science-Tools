# =========================================
# Create New Column
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 নতুন column তৈরি করা
# example: Bonus (Salary এর 10%)

df['Bonus'] = df['Salary'] * 0.10

print(df)

# 👉 explanation:
# নতুন feature তৈরি করা = feature engineering