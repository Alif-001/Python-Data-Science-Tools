# =========================================
# Crosstab Normalization
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 row-wise normalization (percentage)
ct = pd.crosstab(
    df['Department'],
    df['City'],
    normalize='index'
)

print(ct)

# 👉 explanation:
# প্রতিটি row এর percentage distribution