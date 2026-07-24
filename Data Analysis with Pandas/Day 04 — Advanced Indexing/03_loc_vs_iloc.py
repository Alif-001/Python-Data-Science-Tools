# =========================================
# loc vs iloc difference
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 iloc = position based
print(df.iloc[0])   # first row

# 👉 loc = label based
print(df.loc[0])    # row label 0

# 👉 main difference:
# iloc → index number (0,1,2)
# loc → label (row name / index value)

# 👉 example difference in slicing:
print(df.iloc[0:3])  # 0,1,2
print(df.loc[0:3])    # 0,1,2,3 (inclusive)

# 👉 summary:
# iloc = Python style slicing
# loc = pandas label slicing