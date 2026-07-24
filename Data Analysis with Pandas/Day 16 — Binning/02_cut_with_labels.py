# =========================================
# cut() with labels
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 custom bins + labels
bins = [20, 25, 30, 35]
labels = ['Young', 'Adult', 'Senior']

df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df)

# 👉 explanation:
# 20-25 → Young
# 25-30 → Adult
# 30-35 → Senior