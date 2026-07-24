# =========================================
# Crosstab Full Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 frequency + normalization together
ct = pd.crosstab(df['Department'], df['City'])

print("Frequency Table:\n", ct)

print("\nRow-wise Percentage:")
print(pd.crosstab(df['Department'], df['City'], normalize='index'))

print("\nColumn-wise Percentage:")
print(pd.crosstab(df['Department'], df['City'], normalize='columns'))

# 👉 explanation:
# normalize = data কে percentage এ convert করে