# =========================================
# lower() & upper() string operations
# =========================================

import pandas as pd

df = pd.read_csv("data.csv")

# 👉 সব email কে lowercase করা (cleaning step)
df['Email_lower'] = df['Email'].str.lower()

# 👉 সব email কে uppercase করা
df['Email_upper'] = df['Email'].str.upper()

print(df)

# 👉 explanation:
# str.lower() → সব letter ছোট করে
# str.upper() → সব letter বড় করে