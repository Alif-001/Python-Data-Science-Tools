# =========================================
# GROUPBY REVISION
# =========================================

import pandas as pd

df = pd.read_csv("revision_data.csv")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Bonus'] = df['Bonus'].fillna(0)

df['Total_Pay'] = df['Salary'] + df['Bonus']

# 👉 department analysis
group = df.groupby('Department')['Total_Pay'].mean()

print(group)

# 👉 revision:
# groupby = category-wise analysis