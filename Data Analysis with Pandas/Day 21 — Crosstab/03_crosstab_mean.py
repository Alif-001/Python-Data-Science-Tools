# =========================================
# Crosstab with Mean
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 average salary per group
ct = pd.crosstab(
    df['Department'],
    df['City'],
    values=df['Salary'],
    aggfunc='mean'
)

print(ct)

# 👉 explanation:
# average analysis করা যায়