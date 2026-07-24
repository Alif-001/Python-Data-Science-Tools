# =========================================
# agg() with multiple statistics
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple stats একসাথে
result = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max', 'min'])

print(result)

# 👉 explanation:
# agg() = aggregation powerful tool