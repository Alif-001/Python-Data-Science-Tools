# =========================================
# Check Data Types
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 data types check করা খুব গুরুত্বপূর্ণ
print(df.dtypes)

# 👉 explanation:
# object = string type
# int/float = numeric type