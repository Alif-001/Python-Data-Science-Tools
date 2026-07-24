# =========================================
# Show only duplicate rows
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 শুধু duplicate rows দেখানো
duplicates = df[df.duplicated()]

print(duplicates)

# 👉 explanation:
# duplicated() → True/False mask তৈরি করে
# df[condition] → filtering করে