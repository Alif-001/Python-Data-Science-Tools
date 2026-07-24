# =========================================
# stack + unstack with grouping style
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df = df.set_index('Name')

# 👉 stack
stacked = df.stack()

# 👉 reset structure
print("Stacked Data:\n", stacked)

# 👉 unstack first level
unstacked = stacked.unstack()

print("\nUnstacked Data:\n", unstacked)

# 👉 explanation:
# reshape = data format change