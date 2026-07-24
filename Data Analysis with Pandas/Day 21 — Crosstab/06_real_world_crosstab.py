# =========================================
# Real-world Crosstab Analysis
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 Step 1: frequency table
freq = pd.crosstab(df['Department'], df['City'])

# 👉 Step 2: percentage distribution
percent = pd.crosstab(df['Department'], df['City'], normalize='index')

print("Frequency:\n", freq)

print("\nPercentage Distribution:\n", percent)

# 👉 insight
print("\nMost active department-city combination:")
print(freq.stack().idxmax())

# 👉 explanation:
# crosstab = survey + business reporting tool