# =========================================
# Categorical Optimization
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 category type (memory saving)
df['Value_cat'] = df['Value'].astype('category')

print(df.info())

# 👉 explanation:
# repeated values থাকলে category অনেক efficient