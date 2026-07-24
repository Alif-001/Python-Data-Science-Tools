# =========================================
# iloc - Position Based Indexing
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 iloc মানে: index POSITION অনুযায়ী data select করা
# (0,1,2... এই position)

# 👉 first row
print(df.iloc[0])

# 👉 second row
print(df.iloc[1])

# 👉 multiple rows
print(df.iloc[0:3])  # 0,1,2

# 👉 specific rows list
print(df.iloc[[0, 3, 5]])

# 👉 summary:
# iloc = position based (0,1,2,...)