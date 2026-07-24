# =========================================
# Multiple Statistics per Group
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple stats একসাথে
stats = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max', 'min'])

print(stats)

# 👉 explanation:
# agg() = multiple aggregation apply করা যায়