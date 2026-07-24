# =========================================
# Real-world Binning Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Age grouping
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[20, 25, 30, 40],
    labels=['Young', 'Adult', 'Senior']
)

# 👉 Salary level
df['Salary_Level'] = pd.qcut(
    df['Salary'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

# 👉 Marks grade
df['Grade'] = pd.cut(
    df['Marks'],
    bins=[70, 80, 90, 100],
    labels=['C', 'B', 'A']
)

print(df)

# 👉 summary:
# binning = continuous → categorical