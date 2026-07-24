# =========================================
# Forward Fill & Backward Fill
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 forward fill (ffill)
# আগের value দিয়ে fill করে

df_ffill = df.fillna(method='ffill')

print("Forward Fill:")
print(df_ffill)

# 👉 backward fill (bfill)
# পরের value দিয়ে fill করে

df_bfill = df.fillna(method='bfill')

print("\nBackward Fill:")
print(df_bfill)

# 👉 explanation:
# ffill = previous row value copy
# bfill = next row value copy