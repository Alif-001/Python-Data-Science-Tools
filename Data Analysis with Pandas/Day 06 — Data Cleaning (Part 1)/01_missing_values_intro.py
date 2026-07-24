# =========================================
# Missing Values (NaN) Introduction
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 NaN মানে: Not a Number / missing data
# 👉 real-world dataset এ প্রায় সবসময় missing value থাকে

print(df)

# 👉 missing values দেখার জন্য:
print(df.isnull())

# 👉 True মানে missing data
# 👉 False মানে data আছে