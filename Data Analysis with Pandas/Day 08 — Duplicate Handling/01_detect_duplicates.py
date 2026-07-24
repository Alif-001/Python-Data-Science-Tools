# =========================================
# duplicated() - Find duplicate rows
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 duplicated() মানে: কোন row আগে এসেছে কিনা check করে

print(df.duplicated())

# 👉 True মানে: duplicate row
# 👉 False মানে: unique row

# 👉 কতগুলো duplicate আছে
print("\nTotal duplicates:")
print(df.duplicated().sum())

# 👉 summary:
# duplicated = duplicate detect tool