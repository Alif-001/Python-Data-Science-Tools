# =========================================
# MultiIndex Creation
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 multiple column কে index বানানো
df = df.set_index(['Country', 'City', 'Department'])

print(df)

# 👉 explanation:
# এখন data tree structure এর মতো হয়ে গেছে
# Country → City → Department