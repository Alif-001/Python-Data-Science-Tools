# =========================================
# Index vs Position Concept
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 POSITION (iloc)
# - 0,1,2,3...
# - computer order

print("iloc position based:")
print(df.iloc[0])  # first row

# 👉 INDEX / LABEL (loc)
# - row label (default 0,1,2 but can change)

print("\nloc label based:")
print(df.loc[0])

# 👉 index change example
df2 = df.copy()
df2.index = ['a','b','c','d','e','f','g']

print("\nCustom index:")
print(df2.loc['a'])  # label based

# 👉 summary:
# position = iloc
# label = loc