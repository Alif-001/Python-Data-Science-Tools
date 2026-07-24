# =========================================
# drop_duplicates() - remove duplicates
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 duplicate remove করা
clean_df = df.drop_duplicates()

print(clean_df)

# 👉 explanation:
# same row multiple বার থাকলে 1টা রাখে, বাকিগুলো delete করে