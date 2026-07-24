# =========================================
# describe() - Full Statistical Summary
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 describe() সব stats একসাথে দেয়
print(df.describe())

# 👉 include all columns
print(df.describe(include='all'))

# 👉 explanation:
# count, mean, std, min, 25%, 50%, 75%, max