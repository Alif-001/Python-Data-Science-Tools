# =========================================
# Real-world Reshaping Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: melt for analysis
long_df = pd.melt(
    df,
    id_vars=['Name'],
    var_name='Subject',
    value_name='Marks'
)

# 👉 Step 2: average marks per subject
avg_marks = long_df.groupby('Subject')['Marks'].mean()

print("Long Format Data:\n", long_df)
print("\nAverage Marks:\n", avg_marks)

# 👉 explanation:
# melt = ML + analytics friendly format