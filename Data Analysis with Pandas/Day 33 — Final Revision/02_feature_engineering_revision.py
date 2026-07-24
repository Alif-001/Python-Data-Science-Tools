# =========================================
# FEATURE ENGINEERING REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

# 👉 new feature
df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 performance category
df['Performance'] = df['Score'].apply(
    lambda x: 'Excellent' if x >= 90 else ('Good' if x >= 80 else 'Average')
)

print(df)

# 👉 revision:
# new column = insight creation