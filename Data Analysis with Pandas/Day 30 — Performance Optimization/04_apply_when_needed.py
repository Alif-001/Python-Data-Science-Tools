# =========================================
# When apply() is useful
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 condition-based logic (apply needed)
df['Category'] = df['Value'].apply(
    lambda x: 'High' if x > 50 else 'Low'
)

print(df)

# 👉 explanation:
# complex logic → apply useful
# simple math → avoid apply