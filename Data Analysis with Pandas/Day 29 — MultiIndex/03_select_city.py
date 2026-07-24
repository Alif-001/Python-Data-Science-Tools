# =========================================
# Multi-level selection
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

df = df.set_index(['Country', 'City', 'Department'])

# 👉 specific city under country
print(df.loc[('India', 'Mumbai')])

# 👉 explanation:
# tuple ব্যবহার করে multi-level access