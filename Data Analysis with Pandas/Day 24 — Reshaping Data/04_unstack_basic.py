# =========================================
# unstack() - Row to Column
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df = df.set_index('Name')

# 👉 stack → unstack
stacked = df.stack()
unstacked = stacked.unstack()

print(unstacked)

# 👉 explanation:
# original format ফিরে আসে