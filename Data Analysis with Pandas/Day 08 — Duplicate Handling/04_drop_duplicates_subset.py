# =========================================
# drop_duplicates() with subset
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 শুধু Name & City based duplicate remove
clean_df = df.drop_duplicates(subset=['Name', 'City'])

print(clean_df)

# 👉 explanation:
# শুধু Name + City same হলে duplicate ধরা হবে
# Salary difference ignore করবে