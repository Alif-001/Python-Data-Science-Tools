# =========================================
# Direct Vectorized Operations
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 direct math operations
df['Add'] = df['Value'] + 5
df['Multiply'] = df['Value'] * 2
df['Divide'] = df['Value'] / 2

print(df)

# 👉 explanation:
# pandas internally optimized C-level operations ব্যবহার করে