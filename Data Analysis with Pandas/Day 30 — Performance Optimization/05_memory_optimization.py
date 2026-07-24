# =========================================
# Memory Optimization in Pandas
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 before optimization
print(df.info())

# =========================================
# memory optimization trick
# =========================================

df['Value'] = df['Value'].astype('int32')

# 👉 after optimization
print(df.info())

# 👉 explanation:
# int64 → int32 করলে memory half হয়ে যায়