# =========================================
# Real-world Optimization Example
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 fast calculation (vectorized)
df['Square'] = df['Value'] * df['Value']

# 👉 conditional logic
df['Label'] = df['Value'].apply(
    lambda x: 'Even' if x % 2 == 0 else 'Odd'
)

# 👉 memory optimization
df['Value'] = df['Value'].astype('int32')

print(df)

# 👉 explanation:
# performance + memory + logic balance