# =========================================
# head() & tail()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 head() কী?
# - প্রথম 5টা row দেখায় (default)
print(df.head())

# 👉 custom number
print(df.head(3))   # first 3 rows

# 👉 tail() কী?
# - শেষের 5টা row দেখায়
print(df.tail())

# 👉 custom number
print(df.tail(2))   # last 2 rows

# 👉 summary:
# head() = top data
# tail() = bottom data