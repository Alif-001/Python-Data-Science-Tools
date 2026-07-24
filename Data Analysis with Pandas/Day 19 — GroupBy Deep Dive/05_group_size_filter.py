# =========================================
# Filter by group size
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 যেসব department এ 2 জনের বেশি আছে

filtered = df.groupby('Department').filter(
    lambda x: len(x) > 2
)

print(filtered)

# 👉 explanation:
# group size check করা যায়