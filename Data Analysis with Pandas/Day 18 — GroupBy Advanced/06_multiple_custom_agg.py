# =========================================
# Multiple Custom + Built-in Aggregation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 custom + built-in mix
result = df.groupby('Department')['Salary'].agg([
    'mean',
    'sum',
    lambda x: x.max() - x.min()
])

print(result)

# 👉 explanation:
# lambda দিয়ে quick custom logic