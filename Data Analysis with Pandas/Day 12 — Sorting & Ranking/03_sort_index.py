# =========================================
# sort_index() - Index Based Sorting
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 index shuffle করার জন্য
df_shuffled = df.sample(frac=1)

print("Before sorting index:")
print(df_shuffled)

# 👉 index অনুযায়ী sort
sorted_index_df = df_shuffled.sort_index()

print("\nAfter sorting index:")
print(sorted_index_df)

# 👉 explanation:
# sort_index() = row order fix করে