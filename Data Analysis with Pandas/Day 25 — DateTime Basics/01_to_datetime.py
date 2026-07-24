# =========================================
# to_datetime() - Convert to Date type
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 string → datetime conversion
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df)

# 👉 explanation:
# আগে এটা string ছিল
# এখন real date object