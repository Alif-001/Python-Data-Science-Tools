# =========================================
# cut() - Equal Width Binning
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Age কে 3টা group এ ভাগ করা
df['Age_Group'] = pd.cut(df['Age'], bins=3)

print(df)

# 👉 explanation:
# bins=3 → 3টা equal range তৈরি করে
# continuous data → categorical data