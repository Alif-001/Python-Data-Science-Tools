# =========================================
# drop_duplicates() keep options
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 keep='first' (default)
df1 = df.drop_duplicates(keep='first')

print("Keep First:")
print(df1)

# 👉 keep='last'
df2 = df.drop_duplicates(keep='last')

print("\nKeep Last:")
print(df2)

# 👉 keep=False (সব duplicate delete)
df3 = df.drop_duplicates(keep=False)

print("\nRemove All Duplicates:")
print(df3)

# 👉 summary:
# first = প্রথমটা রাখে
# last = শেষটা রাখে
# False = সব duplicate delete