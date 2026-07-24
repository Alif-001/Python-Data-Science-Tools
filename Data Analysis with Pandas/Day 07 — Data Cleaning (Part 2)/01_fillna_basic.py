# =========================================
# fillna() - Replace Missing Values
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 fillna() মানে: NaN এর জায়গায় value বসানো

# 👉 সব NaN কে 0 দিয়ে replace
filled_df = df.fillna(0)

print(filled_df)

# 👉 explanation:
# missing value থাকলে analysis ভুল হতে পারে
# তাই fill করে data complete করা হয়