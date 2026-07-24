# =========================================
# stack() - Column to Row stacking
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 stack requires index
df = df.set_index('Name')

stacked = df.stack()

print(stacked)

# 👉 explanation:
# columns → single column format
# hierarchical index তৈরি হয়