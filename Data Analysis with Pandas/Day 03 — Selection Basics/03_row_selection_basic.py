# =========================================
# Row Selection (Basic)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 প্রথম row select করা
print(df.iloc[0])
# iloc = index based (position)
# 0 = first row

# 👉 2nd row
print(df.iloc[1])

# 👉 multiple rows select
print(df.iloc[0:3])
# 0 to 2 (3 not included)

# 👉 specific rows
print(df.iloc[[0, 2, 4]])

# 👉 summary:
# iloc = row selection by position