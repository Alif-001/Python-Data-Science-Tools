# =========================================
# rank() methods (handling ties)
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 method = average (default)
df['Rank_avg'] = df['Marks'].rank(method='average')

# 👉 method = min
df['Rank_min'] = df['Marks'].rank(method='min')

# 👉 method = max
df['Rank_max'] = df['Marks'].rank(method='max')

# 👉 method = first
df['Rank_first'] = df['Marks'].rank(method='first')

print(df)

# 👉 explanation:
# tie হলে rank কিভাবে assign হবে তা control করা যায়