# =========================================
# Multiple Column Selection
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple column select করতে double bracket লাগে
# syntax: df[['col1', 'col2']]

subset = df[['Name', 'Salary']]

print(subset)

# 👉 type check
print(type(subset))
# output: pandas DataFrame (2D data)

# 👉 different combination
print(df[['Name', 'Age', 'City']])

# 👉 summary:
# multiple columns = DataFrame