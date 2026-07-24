# =========================================
# apply() - Basic Usage
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 apply() = function apply করা column/row এ

# 👉 example: Age + 1 (increment)
df['Age_plus_1'] = df['Age'].apply(lambda x: x + 1)

print(df)

# 👉 explanation:
# lambda x: x + 1 → ছোট function
# x = প্রতিটি value