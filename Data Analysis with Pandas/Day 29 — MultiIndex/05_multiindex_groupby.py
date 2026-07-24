# =========================================
# MultiIndex with GroupBy
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 group by multiple columns
grouped = df.groupby(['Country', 'City'])['Salary'].mean()

print(grouped)

# 👉 explanation:
# MultiIndex automatically তৈরি হয়