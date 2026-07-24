# =========================================
# isnull() & notnull()
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 isnull() → missing value খুঁজে বের করে
print(df.isnull())

# 👉 notnull() → data আছে কিনা দেখায়
print(df.notnull())

# 👉 column-wise missing count
print(df.isnull().sum())

# 👉 summary:
# isnull = missing detect
# notnull = data exists check