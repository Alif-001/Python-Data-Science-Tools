# =========================================
# apply() vs Vectorization
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# =========================================
# ❌ SLOW WAY (apply)
# =========================================

df['Square_apply'] = df['Value'].apply(lambda x: x * x)

# =========================================
# ✅ FAST WAY (Vectorization)
# =========================================

df['Square_vector'] = df['Value'] * df['Value']

print(df)

# 👉 explanation:
# apply → row by row (slow)
# vectorization → full column operation (fast)